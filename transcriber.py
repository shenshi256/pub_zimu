#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Time    : 2025/6/19 17:24
# @Author  : WXY
# @File    : transcriber.py
# @PROJECT_NAME: whisper_gui
# @PRODUCT_NAME: PyCharm
# -------------------------------------------------------------------------------
import os , sys, io
import json
import whisper
from LoggerManager import logger_manager  # ✅ 导入全局日志管理器
from utils import setup_ffmpeg#, setup_ffprobe  # ✅ 导入 ffmpeg 设置函数
import gc
import time
import subprocess
# ✅ 设置 ffmpeg 路径
ffmpeg_path = setup_ffmpeg()
if ffmpeg_path:
    logger_manager.info(f"✅ 使用 ffmpeg 路径: {ffmpeg_path}")
else:
    logger_manager.warning("⚠️ 未找到 ffmpeg.exe，将使用系统 PATH 中的 ffmpeg, 如果系统没有ffmpeg，请自行安装, 并配置环境变量PATH")

# ffprobe_path = setup_ffprobe()
# if ffprobe_path:
#     logger_manager.info(f"✅ 使用 ffprobe 路径: {ffprobe_path}")
# else:
#     logger_manager.warning("⚠️ 未找到 ffprobe.exe，将使用系统 PATH 中的 ffprobe, 如果系统没有ffprobe，请自行安装, 并配置环境变量PATH")

import moviepy.editor as mp
from opencc import OpenCC
from PySide6.QtCore import QObject, Signal, Slot, QTimer

# 在文件开头添加
try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False
    logger_manager.warning("psutil未安装，无法进行进程清理", "transcriber")



class Transcriber(QObject):
    log_signal = Signal(str)
    progress_signal = Signal(int)
    transcription_started = Signal()
    transcription_finished = Signal()
    # ✅ 添加音频时长信号
    audio_duration_signal = Signal(float)
    # ✅ 添加无效文件格式信号
    invalid_file_format_signal = Signal()
    # ✅ 添加批量处理信号
    batch_file_started = Signal(str)  # 文件开始处理信号
    batch_file_finished = Signal(str, bool)  # 文件路径, 是否成功
    batch_all_finished = Signal()
    def __init__(self, model_path, debug_mode=False, log_file_path=None, export_format='srt', convert_to_simple=False):
        super().__init__()
        self.model_path = model_path
        self.export_format = export_format
        self.cc = OpenCC('t2s')
        self.debug_mode = debug_mode
        self.log_file_path = log_file_path
        # ✅ 添加简体转换控制参数
        self.convert_to_simple = convert_to_simple

        self.audio_duration = 0
        # ✅ 批量处理相关变量
        self.cached_model = None  # 缓存的模型
        self.batch_files = []     # 批量文件队列
        self.current_batch_index = 0  # 当前处理的文件索引

        # ✅ 如果启用调试模式，设置文件日志
        if self.debug_mode and self.log_file_path:
            logger_manager.setup_file_logging(self.log_file_path, True)

    def convert_text_if_needed(self, text):
        """根据设置决定是否转换为简体中文"""
        if self.convert_to_simple:
            return self.cc.convert(text)
        else:
            return text

    def write_to_log_file(self, message):
        # if self.debug_mode and self.log_file_path:
        #     try:
        #         with open(self.log_file_path, 'a', encoding='utf-8') as f:
        #             timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #             f.write(f"[{timestamp}] {message}\n")
        #     except Exception as e:
        #         print(f"写入日志文件失败: {str(e)}")
        """兼容原有方法，内部使用全局日志管理器"""
        logger_manager.debug(message, "transcriber")

    def emit_log(self, message):
        # self.log_signal.emit(message)
        # self.write_to_log_file(message)
        """发出日志信号并记录到日志系统"""
        # 发出信号给UI
        self.log_signal.emit(message)
        # 记录到日志系统
        logger_manager.info(message, "transcriber")

    @Slot(str)
    def transcribe(self, file_path):
        try:
            logger_manager.info(f"🔍 开始转录任务，文件路径: {file_path}", "transcriber", show_in_ui=True)
            logger_manager.info(f"🎯 使用模型: {os.path.basename(self.model_path)}", "transcriber", show_in_ui=True)
            logger_manager.info(f"📋 系统信息检查开始", "transcriber", show_in_ui=True)

            # 文件存在性检查
            if not os.path.exists(file_path):
                logger_manager.error(f"❌ 文件不存在: {file_path}", "transcriber", show_in_ui=True)
                return
            logger_manager.info(f"✅ 文件存在检查通过", "transcriber", show_in_ui=True)

            if not os.path.exists(self.model_path):
                logger_manager.error(f"❌ 模型文件不存在: {self.model_path}", "transcriber", show_in_ui=True)
                return
            logger_manager.info(f"✅ 模型文件存在检查通过", "transcriber", show_in_ui=True)

            # 文件格式检查
            ext = os.path.splitext(file_path)[1].lower()
            is_video = ext in [".mp4", ".mov", ".mkv", ".avi", ".flv"]
            is_audio = ext in [".wav", ".mp3", ".ogg", ".flac"]
            video_text = "是" if is_video else "不是"
            audio_text = "是" if is_audio else "不是"
            logger_manager.info(f"📁 文件类型: {ext}, 是视频: {video_text}, 是音频: {audio_text}", "transcriber", show_in_ui=True)

            if not is_video and not is_audio:
                logger_manager.error(
                    f"❌ 不支持的文件格式: {ext}。请选择视频文件(.mp4, .mov, .mkv, .avi, .flv)或音频文件(.wav, .mp3, .ogg, .flac)",
                    "transcriber", show_in_ui=True)
                self.invalid_file_format_signal.emit()
                return
            logger_manager.info(f"✅ 文件格式验证通过", "transcriber", show_in_ui=True)

            # 初始化变量
            audio_path = None
            temp_audio_created = False
            model = None
            audio_duration = 0
            video_clip = None
            audio_clip = None

            # 获取音频时长（使用 MoviePy）
            try:
                logger_manager.info(f"📊 使用 MoviePy 获取音频时长...", "transcriber", show_in_ui=True)

                if is_video:
                    video_clip = mp.VideoFileClip(file_path)
                    audio_duration = video_clip.duration if video_clip.duration else 0
                    logger_manager.info(f"📊 视频时长: {audio_duration:.2f}秒", "transcriber", show_in_ui=True)
                else:
                    audio_clip = mp.AudioFileClip(file_path)
                    audio_duration = audio_clip.duration if audio_clip.duration else 0
                    logger_manager.info(f"📊 音频时长: {audio_duration:.2f}秒", "transcriber", show_in_ui=True)

            except Exception as e:
                logger_manager.warning(f"⚠️ 获取音频时长失败: {e}，设置为0", "transcriber", show_in_ui=True)
                audio_duration = 0
            finally:
                # 及时释放 MoviePy 资源
                if video_clip:
                    video_clip.close()
                    video_clip = None
                if audio_clip:
                    audio_clip.close()
                    audio_clip = None

            # 处理视频文件 - 提取音频
            if is_video:
                logger_manager.info(f"🎬 识别到视频文件，使用 ffmpeg 提取音频...", "transcriber", show_in_ui=True)
                time.sleep(1.0)

                import tempfile
                import uuid

                temp_dir = tempfile.gettempdir()
                temp_filename = f"whisper_temp_{uuid.uuid4().hex[:8]}.wav"
                audio_path = os.path.join(temp_dir, temp_filename)
                temp_audio_created = True
                logger_manager.info(f"📁 临时音频文件路径: {audio_path}", "transcriber", show_in_ui=True)

                try:
                    # 使用 ffmpeg 提取音频
                    ffmpeg_cmd = [
                        ffmpeg_path,
                        "-i", file_path,
                        "-vn",  # 不处理视频
                        "-acodec", "pcm_s16le",  # 使用 PCM 16位编码
                        "-ar", "16000",  # 采样率 16kHz（Whisper 推荐）
                        "-ac", "1",  # 单声道
                        "-y",  # 覆盖输出文件
                        audio_path
                    ]

                    logger_manager.info(f"🔧 执行 ffmpeg 命令: {' '.join(ffmpeg_cmd)}", "transcriber", show_in_ui=True)
                    # 在 Windows 下隐藏控制台窗口
                    startupinfo = None
                    if os.name == 'nt':  # Windows
                        startupinfo = subprocess.STARTUPINFO()
                        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                        startupinfo.wShowWindow = subprocess.SW_HIDE

                    result = subprocess.run(
                        ffmpeg_cmd,
                        capture_output=True,
                        text=True,
                        timeout=300,  # 5分钟超时
                        encoding='utf-8',
                        errors='ignore',
                        startupinfo=startupinfo  # 隐藏控制台黑窗口的闪出
                    )

                    if result.returncode != 0:
                        logger_manager.error(f"❌ ffmpeg 提取音频失败: {result.stderr}", "transcriber", show_in_ui=True)
                        return

                    logger_manager.info(f"✅ ffmpeg 音频提取完成", "transcriber", show_in_ui=True)

                except subprocess.TimeoutExpired:
                    logger_manager.error(f"❌ ffmpeg 提取音频超时（5分钟）", "transcriber", show_in_ui=True)
                    return
                except Exception as ffmpeg_error:
                    logger_manager.error(f"❌ ffmpeg 提取音频失败: {str(ffmpeg_error)}", "transcriber", show_in_ui=True)
                    return
            else:
                audio_path = file_path
                logger_manager.info(f"🎧 识别到音频文件，直接处理: {audio_path}", "transcriber", show_in_ui=True)

            # 音频文件检查
            if not os.path.exists(audio_path):
                logger_manager.error(f"❌ 音频文件不存在: {audio_path}", "transcriber", show_in_ui=True)
                return

            file_size = os.path.getsize(audio_path)
            logger_manager.info(f"✅ 音频文件检查通过，大小: {file_size} 字节", "transcriber", show_in_ui=True)

            # 垃圾回收和资源清理
            gc.collect()
            time.sleep(1)
            logger_manager.info(f"🧹 垃圾回收完成", "transcriber", show_in_ui=True)

            # 加载 Whisper 模型
            logger_manager.info(f"🤖 准备加载Whisper模型: {self.model_path}", "transcriber", show_in_ui=True)
            time.sleep(1.0)

            try:
                model = whisper.load_model(self.model_path)
                time.sleep(1.0)
                logger_manager.info(f"✅ 模型加载成功", "transcriber", show_in_ui=True)
            except Exception as model_error:
                logger_manager.error(f"❌ 模型加载失败: {str(model_error)}", "transcriber", show_in_ui=True)
                raise

            # 设置音频时长并发送信号
            self.audio_duration = audio_duration
            # logger_manager.info(f"📡 发送进度信号", "transcriber", show_in_ui=True)
            self.progress_signal.emit(0)
            self.audio_duration_signal.emit(self.audio_duration)
            self.transcription_started.emit()

            # 开始转录
            logger_manager.info("⏳ 正在转录，请耐心等待……", "transcriber", show_in_ui=True)
            # 在转录调用前设置环境变量禁用 tqdm
             # 设置全局环境变量隐藏所有subprocess窗口（包括whisper内部的ffmpeg调用）
            if os.name == 'nt':  # Windows系统
                # 设置CREATE_NO_WINDOW标志，隐藏所有子进程窗口
                original_popen = subprocess.Popen
                def patched_popen(*args, **kwargs):
                    if 'creationflags' not in kwargs:
                        kwargs['creationflags'] = subprocess.CREATE_NO_WINDOW
                    else:
                        kwargs['creationflags'] |= subprocess.CREATE_NO_WINDOW
                    return original_popen(*args, **kwargs)
                subprocess.Popen = patched_popen
            
            # 保存原始的 stdout 和 stderr
            original_stdout = sys.stdout
            original_stderr = sys.stderr
            try:
                # 重定向标准输出到 devnull，防止 tqdm 输出
                sys.stdout = io.StringIO()
                sys.stderr = io.StringIO()

                logger_manager.info(f"🔄 开始转录处理...", "transcriber", show_in_ui=True)
                result = model.transcribe(
                    audio_path,
                    verbose=False
                )
                logger_manager.info(f"✅ 转录完成", "transcriber", show_in_ui=True)
            except Exception as transcribe_error:
                logger_manager.error(f"❌ 转录失败: {str(transcribe_error)}", "transcriber", show_in_ui=True)
                import traceback
                logger_manager.debug(f"转录错误堆栈: {traceback.format_exc()}", "transcriber")
                raise
            finally:
                # 恢复原始的 stdout 和 stderr
                sys.stdout = original_stdout
                sys.stderr = original_stderr

                # 恢复 tqdm 设置（如果需要）
                if 'TQDM_DISABLE' in os.environ:
                    del os.environ['TQDM_DISABLE']

            # 保存转录结果
            logger_manager.info(f"💾 正在保存转录结果...", "transcriber", show_in_ui=True)
            if self.export_format == 'srt':
                self.save_as_srt(result, file_path, self.audio_duration)
            elif self.export_format == 'txt':
                self.save_as_txt(result, file_path)
            elif self.export_format == 'json':
                self.save_as_json(result, file_path)
            elif self.export_format == 'vtt':
                self.save_as_vtt(result, file_path)

            self.progress_signal.emit(100)
            logger_manager.info(f"🎉 转录任务完成", "transcriber", show_in_ui=True)

        except Exception as e:
            logger_manager.error(f"❌ 转录过程中发生错误: {str(e)}", "transcriber", show_in_ui=True)
            import traceback
            logger_manager.debug(f"详细错误信息: {traceback.format_exc()}", "transcriber")
        finally:
            try:
                # 清理临时文件
                if temp_audio_created and audio_path and os.path.exists(audio_path):
                    os.remove(audio_path)
                    logger_manager.info(f"🧹 已删除临时音频文件: {audio_path}", "transcriber")

                # 显式释放模型和结果对象
                model = None
                result = None

                # 确保 MoviePy 资源完全释放
                if 'video_clip' in locals() and video_clip:
                    video_clip.close()
                if 'audio_clip' in locals() and audio_clip:
                    audio_clip.close()

                # 多次垃圾回收
                for _ in range(3):
                    gc.collect()

            except Exception as cleanup_error:
                logger_manager.warning(f"⚠️ 清理资源失败: {cleanup_error}", "transcriber")

            self.transcription_finished.emit()


    def format_timestamp(self, seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millis = int((seconds - int(seconds)) * 1000)
        return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

    def log(self, text):
        # print(text)
        # self.log_signal.emit(text)
        """兼容原有方法"""
        logger_manager.info(text, "transcriber", show_in_ui=True)


    def _validate_result(self, result, file_format):
        """验证转录结果的有效性"""
        if not result or not isinstance(result, dict):
            logger_manager.error(f"❌ {file_format}保存失败：转录结果为空或格式错误", "transcriber", show_in_ui=True)
            return False
        return True

    def _validate_segments(self, result, file_format):
        """验证segments数据的有效性"""
        if "segments" not in result or not result["segments"]:
            logger_manager.error(f"❌ {file_format}保存失败：没有可用的语音段落", "transcriber", show_in_ui=True)
            return False
        return True

    def _update_progress_with_log(self, progress, message):
        """更新进度并记录日志"""
        self.progress_signal.emit(progress)
        logger_manager.info(message, "transcriber", show_in_ui=True)

    def _safe_file_write(self, file_path, write_func, file_format):
        """安全的文件写入操作"""
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                write_func(f)
            logger_manager.info(f"🎉 已保存{file_format}文件: {file_path}", "transcriber", show_in_ui=True)
        except Exception as e:
            logger_manager.error(f"❌ {file_format}文件写入失败: {str(e)}", "transcriber", show_in_ui=True)
            raise




    def save_as_srt(self, result, file_path, duration=None):
        """保存为SRT格式"""
        if not self._validate_result(result, "SRT") or not self._validate_segments(result, "SRT"):
            return

        srt_file = os.path.splitext(file_path)[0] + ".srt"
        total_segments = len(result["segments"])

        self._update_progress_with_log(90, "✅ [90%] 开始保存 SRT 文件...")

        def write_srt(f):
            for i, segment in enumerate(result["segments"]):
                # 验证每个段落的完整性
                required_keys = ["start", "end", "text"]
                if not isinstance(segment, dict) or not all(key in segment for key in required_keys):
                    logger_manager.warning(f"⚠️ 跳过格式异常的语音段落 {i + 1}", "transcriber")
                    continue

                start = self.format_timestamp(segment["start"])
                end = self.format_timestamp(segment["end"])
                text = self.convert_text_if_needed(segment['text'].strip())
                f.write(f"{i + 1}\n{start} --> {end}\n{text}\n\n")

                # 更新进度（90-95%）
                if total_segments > 0:
                    progress = 90 + int((i + 1) / total_segments * 5)
                    self.progress_signal.emit(progress)

        self._safe_file_write(srt_file, write_srt, "SRT")

    def save_as_txt(self, result, file_path):
        """保存为TXT格式"""
        if not self._validate_result(result, "TXT"):
            return

        if "text" not in result:
            logger_manager.error("❌ TXT保存失败：转录结果中没有文本内容", "transcriber", show_in_ui=True)
            return

        txt_file = os.path.splitext(file_path)[0] + ".txt"

        self._update_progress_with_log(90, "✅ [90%] 开始保存文本文件...")

        def write_txt(f):
            f.write(self.convert_text_if_needed(result["text"]))

        self._safe_file_write(txt_file, write_txt, "TXT")
        self.progress_signal.emit(95)

    def save_as_json(self, result, file_path):
        """保存为JSON格式"""
        if not self._validate_result(result, "JSON"):
            return

        json_file = os.path.splitext(file_path)[0] + ".json"

        self._update_progress_with_log(90, "✅ [90%] 开始保存 JSON 文件...")

        def write_json(f):
            if self.convert_to_simple:
                # 深拷贝结果以避免修改原始数据
                import copy
                result_copy = copy.deepcopy(result)

                # 转换主文本
                if "text" in result_copy:
                    result_copy["text"] = self.convert_text_if_needed(result_copy["text"])

                # 转换每个段落的文本
                if "segments" in result_copy and result_copy["segments"]:
                    for segment in result_copy["segments"]:
                        if isinstance(segment, dict) and "text" in segment:
                            segment["text"] = self.convert_text_if_needed(segment["text"])

                json.dump(result_copy, f, ensure_ascii=False, indent=2)
            else:
                json.dump(result, f, ensure_ascii=False, indent=2)

        self._safe_file_write(json_file, write_json, "JSON")
        self.progress_signal.emit(95)

    def save_as_vtt(self, result, file_path):
        """保存为VTT格式"""
        if not self._validate_result(result, "VTT") or not self._validate_segments(result, "VTT"):
            return

        vtt_file = os.path.splitext(file_path)[0] + ".vtt"
        total_segments = len(result["segments"])

        self._update_progress_with_log(90, "✅ [90%] 开始保存 VTT 文件...")

        def write_vtt(f):
            f.write("WEBVTT\n\n")
            for i, segment in enumerate(result["segments"]):
                # 验证段落完整性
                required_keys = ["start", "end", "text"]
                if not isinstance(segment, dict) or not all(key in segment for key in required_keys):
                    logger_manager.warning(f"⚠️ 跳过格式异常的语音段落 {i + 1}", "transcriber")
                    continue

                start = self.format_timestamp(segment["start"]).replace(",", ".")
                end = self.format_timestamp(segment["end"]).replace(",", ".")
                text = self.convert_text_if_needed(segment['text'].strip())
                f.write(f"{start} --> {end}\n{text}\n\n")

                # 更新进度（90-95%）
                if total_segments > 0:
                    progress = 90 + int((i + 1) / total_segments * 5)
                    self.progress_signal.emit(progress)

        self._safe_file_write(vtt_file, write_vtt, "VTT")

    # ✅ 批量处理相关方法
    @Slot(list)
    def transcribe_batch(self, file_paths):
        """批量转录文件，只加载一次模型"""
        try:
            self.batch_files = file_paths
            self.current_batch_index = 0

            if not self.batch_files:
                logger_manager.warning("❌ 批量文件列表为空", "transcriber", show_in_ui=True)
                self.batch_all_finished.emit()
                return

            logger_manager.info(f"🚀 开始批量转录，共 {len(self.batch_files)} 个文件", "transcriber", show_in_ui=True)

            # 只加载一次模型
            self._load_model_once()

            # 开始处理第一个文件
            self._process_next_batch_file()

        except Exception as e:
            logger_manager.error(f"❌ 批量转录初始化失败: {str(e)}", "transcriber", show_in_ui=True)
            self.batch_all_finished.emit()

    @Slot()
    def transcribe_batch_from_stored(self):
        """从存储的文件列表开始批量转录（解决Qt信号槽参数传递问题）"""
        try:
            if not hasattr(self, 'batch_files') or not self.batch_files:
                logger_manager.warning("❌ 批量文件列表为空", "transcriber", show_in_ui=True)
                self.batch_all_finished.emit()
                return

            self.current_batch_index = 0
            logger_manager.info(f"🚀 开始批量转录，共 {len(self.batch_files)} 个文件", "transcriber", show_in_ui=True)

            # 只加载一次模型
            self._load_model_once()

            # 开始处理第一个文件
            self._process_next_batch_file()

        except Exception as e:
            logger_manager.error(f"❌ 批量转录初始化失败: {str(e)}", "transcriber", show_in_ui=True)
            self.batch_all_finished.emit()

    def _load_model_once(self):
        """只加载一次模型并缓存"""
        if self.cached_model is None:
            logger_manager.info(f"🤖 批量模式：加载Whisper模型: {self.model_path}", "transcriber", show_in_ui=True)
            try:
                self.cached_model = whisper.load_model(self.model_path)
                logger_manager.info(f"✅ 批量模式：模型加载成功，将复用于所有文件", "transcriber", show_in_ui=True)
            except Exception as e:
                logger_manager.error(f"❌ 批量模式：模型加载失败: {str(e)}", "transcriber", show_in_ui=True)
                raise

    def _process_next_batch_file(self):
        """处理下一个批量文件"""
        if self.current_batch_index >= len(self.batch_files):
            # 所有文件处理完成
            self._cleanup_batch_model()
            logger_manager.info(f"🎉 批量转录全部完成！", "transcriber", show_in_ui=True)
            self.batch_all_finished.emit()
            return

        current_file = self.batch_files[self.current_batch_index]
        # logger_manager.info(f"📁 批量处理 ({self.current_batch_index + 1}/{len(self.batch_files)}): {current_file}",
        #                     "transcriber", show_in_ui=True)
        # 发送文件开始处理信号，让主窗口标记为"处理中"
        self.batch_file_started.emit(current_file)
        # 计算整体批量进度
        overall_progress = int((self.current_batch_index / len(self.batch_files)) * 100)
        logger_manager.info(
            f"📁 批量处理 ({self.current_batch_index + 1}/{len(self.batch_files)}) [整体进度: {overall_progress}%]: {os.path.basename(current_file)}",
            "transcriber", show_in_ui=True)
        try:
            # 使用缓存的模型处理单个文件
            success = self._transcribe_single_file_with_cached_model(current_file)
            self.batch_file_finished.emit(current_file, success)

        except Exception as e:
            logger_manager.error(f"❌ 批量处理文件失败: {current_file}, 错误: {str(e)}", "transcriber", show_in_ui=True)
            self.batch_file_finished.emit(current_file, False)

        # 处理下一个文件
        self.current_batch_index += 1
        self._process_next_batch_file()

    def _transcribe_single_file_with_cached_model(self, file_path):
        """使用缓存的模型转录单个文件"""
        try:
            # 发送转录开始信号，启动进度条模拟
            self.transcription_started.emit()

            # 文件检查逻辑（复用原有逻辑）
            if not os.path.exists(file_path):
                logger_manager.error(f"❌ 文件不存在: {file_path}", "transcriber", show_in_ui=True)
                return False

            # 文件格式检查
            ext = os.path.splitext(file_path)[1].lower()
            is_video = ext in [".mp4", ".mov", ".mkv", ".avi", ".flv"]
            is_audio = ext in [".wav", ".mp3", ".ogg", ".flac"]

            if not is_video and not is_audio:
                logger_manager.error(f"❌ 不支持的文件格式: {ext}", "transcriber", show_in_ui=True)
                return False
            # 初始进度
            self.progress_signal.emit(5)
            logger_manager.info(f"🔄 [5%] 开始处理文件: {os.path.basename(file_path)}", "transcriber", show_in_ui=True)

            # 音频提取逻辑（复用原有逻辑）
            audio_path = None
            temp_audio_created = False

            if is_video:
                # 提取音频到临时文件
                import tempfile
                import uuid
                temp_dir = tempfile.gettempdir()
                temp_filename = f"whisper_batch_{uuid.uuid4().hex[:8]}.wav"
                audio_path = os.path.join(temp_dir, temp_filename)
                temp_audio_created = True


                self.progress_signal.emit(10)
                logger_manager.info(f"🔄 [10%] 提取音频: {os.path.basename(file_path)}", "transcriber", show_in_ui=True)

                # 使用ffmpeg提取音频（复用原有逻辑）
                ffmpeg_cmd = [
                    ffmpeg_path, "-i", file_path, "-vn", "-acodec", "pcm_s16le",
                    "-ar", "16000", "-ac", "1", "-y", audio_path
                ]

                startupinfo = None
                if os.name == 'nt':
                    startupinfo = subprocess.STARTUPINFO()
                    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                    startupinfo.wShowWindow = subprocess.SW_HIDE

                result = subprocess.run(ffmpeg_cmd, capture_output=True, text=True,
                                        timeout=300, encoding='utf-8', errors='ignore',
                                        startupinfo=startupinfo)

                if result.returncode != 0:
                    logger_manager.error(f"❌ ffmpeg 提取音频失败: {result.stderr}", "transcriber", show_in_ui=True)
                    return False

                self.progress_signal.emit(20)
                logger_manager.info(f"✅ [20%] 音频提取完成", "transcriber", show_in_ui=True)
            else:
                audio_path = file_path
                self.progress_signal.emit(15)
                logger_manager.info(f"🔄 [15%] 直接使用音频文件", "transcriber", show_in_ui=True)

                # 获取音频时长并发送信号
            try:
                audio_clip = mp.AudioFileClip(audio_path)
                duration = audio_clip.duration
                audio_clip.close()
                self.audio_duration_signal.emit(duration)
                logger_manager.info(f"📊 音频时长: {duration:.2f}秒", "transcriber", show_in_ui=True)
            except Exception as e:
                logger_manager.warning(f"⚠️ 无法获取音频时长: {str(e)}", "transcriber", show_in_ui=True)
                duration = 0

            # 使用缓存的模型进行转录
            # logger_manager.info(f"⏳ 使用缓存模型转录: {os.path.basename(file_path)}", "transcriber", show_in_ui=True)
            self.progress_signal.emit(30)
            logger_manager.info(f"⏳ [30%] 使用缓存模型转录: {os.path.basename(file_path)}", "transcriber", show_in_ui=True)

            # 保存原始的 stdout 和 stderr
            original_stdout = sys.stdout
            original_stderr = sys.stderr
            try:
                sys.stdout = io.StringIO()
                sys.stderr = io.StringIO()

                result = self.cached_model.transcribe(audio_path, verbose=False)
                # logger_manager.info(f"✅ 转录完成: {os.path.basename(file_path)}", "transcriber", show_in_ui=True)
                self.progress_signal.emit(85)
                logger_manager.info(f"✅ [85%] 转录完成: {os.path.basename(file_path)}", "transcriber", show_in_ui=True)

            finally:
                sys.stdout = original_stdout
                sys.stderr = original_stderr

            # 保存结果
            # logger_manager.info(f"💾 保存转录结果: {os.path.basename(file_path)}", "transcriber", show_in_ui=True)
            self.progress_signal.emit(90)
            logger_manager.info(f"💾 [90%] 保存转录结果: {os.path.basename(file_path)}", "transcriber", show_in_ui=True)
            if self.export_format == 'srt':
                self.save_as_srt(result, file_path)
            elif self.export_format == 'txt':
                self.save_as_txt(result, file_path)
            elif self.export_format == 'json':
                self.save_as_json(result, file_path)
            elif self.export_format == 'vtt':
                self.save_as_vtt(result, file_path)

            # 清理临时文件
            if temp_audio_created and audio_path and os.path.exists(audio_path):
                os.remove(audio_path)
            # 完成进度
            self.progress_signal.emit(100)
            logger_manager.info(f"🎉 [100%] 文件处理完成: {os.path.basename(file_path)}", "transcriber", show_in_ui=True)

            # 发送转录完成信号
            self.transcription_finished.emit()

            return True

        except Exception as e:
            logger_manager.error(f"❌ 转录文件失败: {file_path}, 错误: {str(e)}", "transcriber", show_in_ui=True)
            # 发送转录完成信号，即使失败也要停止进度条
            self.transcription_finished.emit()
            return False

    def _cleanup_batch_model(self):
        """清理批量处理的缓存模型"""
        if self.cached_model is not None:
            logger_manager.info(f"🧹 批量处理完成，清理缓存模型", "transcriber", show_in_ui=True)
            self.cached_model = None
            # 多次垃圾回收
            for _ in range(3):
                gc.collect()
            logger_manager.info(f"✅ 模型资源清理完成", "transcriber", show_in_ui=True)

    # def save_as_srt(self, result, file_path, duration):
    #     # ✅ 验证结果参数
    #     if not result or not isinstance(result, dict):
    #         logger_manager.error("❌ SRT保存失败：转录结果为空或格式错误", "transcriber", show_in_ui=True)
    #         return
    #
    #     if "segments" not in result or not result["segments"]:
    #         logger_manager.error("❌ SRT保存失败：没有可用的语音段落", "transcriber", show_in_ui=True)
    #         return
    #
    #     srt_file = os.path.splitext(file_path)[0] + ".srt"
    #     total_segments = len(result["segments"])
    #
    #     # ✅ 开始进度更新
    #     self.progress_signal.emit(90)
    #     logger_manager.info("✅ [90%] 开始保存 SRT 文件...", "transcriber", show_in_ui=True)
    #
    #     try:
    #         with open(srt_file, "w", encoding="utf-8") as f:
    #             for i, segment in enumerate(result["segments"]):
    #                 # ✅ 验证每个段落的完整性
    #                 if not isinstance(segment,
    #                                   dict) or "start" not in segment or "end" not in segment or "text" not in segment:
    #                     logger_manager.warning(f"⚠️ 跳过格式异常的语音段落 {i + 1}", "transcriber")
    #                     continue
    #
    #                 start = self.format_timestamp(segment["start"])
    #                 end = self.format_timestamp(segment["end"])
    #                 text = self.convert_text_if_needed(segment['text'].strip())
    #                 f.write(f"{i + 1}\n{start} --> {end}\n{text}\n\n")
    #
    #                 # ✅ 基于处理的段落数量计算进度（90-95%）
    #                 if total_segments > 0:
    #                     progress = 90 + int((i + 1) / total_segments * 5)
    #                     self.progress_signal.emit(progress)
    #
    #         logger_manager.info(f"🎉 已保存字幕文件: {srt_file}", "transcriber", show_in_ui=True)
    #     except Exception as e:
    #         logger_manager.error(f"❌ SRT文件写入失败: {str(e)}", "transcriber", show_in_ui=True)
    #         raise
    #     # srt_file = os.path.splitext(file_path)[0] + ".srt"
    #     # total_segments = len(result["segments"])
    #     #
    #     # # ✅ 开始进度更新
    #     # self.progress_signal.emit(90)
    #     # #self.emit_log("✅ [90%] 开始保存 SRT 文件...")
    #     # logger_manager.info("✅ [90%] 开始保存 SRT 文件...", "transcriber", show_in_ui=True)
    #     #
    #     # with open(srt_file, "w", encoding="utf-8") as f:
    #     #     for i, segment in enumerate(result["segments"]):
    #     #         start = self.format_timestamp(segment["start"])
    #     #         end = self.format_timestamp(segment["end"])
    #     #         # text = self.cc.convert(segment['text'].strip())
    #     #         # f.write(f"{i + 1}\n{start} --> {end}\n{text}\n\n")
    #     #         # ✅ 使用新的转换方法
    #     #         text = self.convert_text_if_needed(segment['text'].strip())
    #     #         f.write(f"{i + 1}\n{start} --> {end}\n{text}\n\n")
    #     #         # ✅ 基于处理的段落数量计算进度（90-95%）
    #     #         if total_segments > 0:
    #     #             progress = 90 + int((i + 1) / total_segments * 5)
    #     #             self.progress_signal.emit(progress)
    #     #             #self.emit_log(f"✅ [{progress}%] {start} → {end}")
    #     #             #logger_manager.debug(f"✅ [{progress}%] {start} → {end}", "transcriber")
    #     # #self.emit_log(f"🎉 已保存字幕文件: {srt_file}")
    #     # logger_manager.info(f"🎉 已保存字幕文件: {srt_file}", "transcriber", show_in_ui=True)
    # def save_as_txt(self, result, file_path):
    #     txt_file = os.path.splitext(file_path)[0] + ".txt"
    #
    #     # ✅ 添加进度更新（90-95%）
    #     self.progress_signal.emit(90)
    #     #self.emit_log("✅ [90%] 开始保存文本文件...")
    #     logger_manager.info("✅ [90%] 开始保存文本文件...", "transcriber", show_in_ui=True)
    #     with open(txt_file, "w", encoding="utf-8") as f:
    #         # f.write(self.cc.convert(result["text"]))
    #         # ✅ 使用新的转换方法
    #         f.write(self.convert_text_if_needed(result["text"]))
    #     # ✅ 完成进度更新
    #     self.progress_signal.emit(95)
    #     #self.emit_log(f"🎉 已保存文本文件: {txt_file}")
    #     logger_manager.info(f"🎉 已保存文本文件: {txt_file}", "transcriber", show_in_ui=True)
    # def save_as_json(self, result, file_path):
    #     json_file = os.path.splitext(file_path)[0] + ".json"
    #
    #     # ✅ 添加进度更新（90-95%）
    #     self.progress_signal.emit(90)
    #     logger_manager.info("✅ [90%] 开始保存 JSON 文件...", "transcriber", show_in_ui=True)
    #
    #     # ✅ 如果需要转换为简体，处理JSON中的文本内容
    #     if self.convert_to_simple:
    #         # 深拷贝结果以避免修改原始数据
    #         import copy
    #         result_copy = copy.deepcopy(result)
    #         # 转换主文本
    #         result_copy["text"] = self.convert_text_if_needed(result_copy["text"])
    #         # 转换每个段落的文本
    #         for segment in result_copy["segments"]:
    #             segment["text"] = self.convert_text_if_needed(segment["text"])
    #
    #         with open(json_file, "w", encoding="utf-8") as f:
    #             json.dump(result_copy, f, ensure_ascii=False, indent=2)
    #     else:
    #         with open(json_file, "w", encoding="utf-8") as f:
    #             json.dump(result, f, ensure_ascii=False, indent=2)
    #     # ✅ 完成进度更新
    #     self.progress_signal.emit(95)
    #     logger_manager.info(f"🎉 已保存 JSON 文件: {json_file}", "transcriber", show_in_ui=True)
    #
    # def save_as_vtt(self, result, file_path):
    #     vtt_file = os.path.splitext(file_path)[0] + ".vtt"
    #     total_segments = len(result["segments"])
    #
    #     # ✅ 开始进度更新
    #     self.progress_signal.emit(90)
    #     logger_manager.info("✅ [90%] 开始保存 VTT 文件...", "transcriber", show_in_ui=True)
    #
    #     with open(vtt_file, "w", encoding="utf-8") as f:
    #         f.write("WEBVTT\n\n")
    #         for i, segment in enumerate(result["segments"]):
    #             start = self.format_timestamp(segment["start"]).replace(",", ".")
    #             end = self.format_timestamp(segment["end"]).replace(",", ".")
    #             # text = self.cc.convert(segment['text'].strip())
    #             # f.write(f"{start} --> {end}\n{text}\n\n")
    #             # ✅ 使用新的转换方法
    #             text = self.convert_text_if_needed(segment['text'].strip())
    #             f.write(f"{start} --> {end}\n{text}\n\n")
    #             # ✅ 基于处理的段落数量计算进度（90-95%）
    #             if total_segments > 0:
    #                 progress = 90 + int((i + 1) / total_segments * 5)
    #                 self.progress_signal.emit(progress)
    #                 #logger_manager.debug(f"VTT进度: {progress}%", "transcriber")
    #
    #     logger_manager.info(f"🎉 已保存 VTT 文件: {vtt_file}", "transcriber", show_in_ui=True)


