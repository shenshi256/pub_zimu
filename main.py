#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Time    : 2025/6/19 16:19
# @Author  : WXY
# @File    : main.py
# @PROJECT_NAME: whisper_gui
# @PRODUCT_NAME: PyCharm
# -------------------------------------------------------------------------------
import os
import random
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from HelpDialog import HelpDialog
from SystemMonitorWorker import SystemMonitorWorker
from ui_main import Ui_MainWindow
from transcriber import Transcriber
from PySide6.QtCore import QThread,  QMetaObject, Qt, Q_ARG, QTimer ,QSettings
from PySide6.QtGui import QTextCursor  # 添加这行导入
from auth_window import AuthWindow  # 授权窗口
from settings_manager import settings_manager
from AESEncrypt import aes_decrypt
from datetime import datetime, timedelta
from LoggerManager import logger_manager
from utils import show_info, show_warning, show_error, setup_window_icon, get_system_monitor_info, VERSION
from disclaimers import DisclaimersHelpDialog
from SingleInstanceManager import SingleInstanceManager
from SplashScreen import SplashScreen
# 导入全局异常处理器

from GlobalExceptionHandler import GlobalExceptionHandler

def ensure_model_directory():
    """确保model目录存在"""
    model_dir = os.path.join(os.getcwd(), "model")
    if not os.path.exists(model_dir):
        try:
            os.makedirs(model_dir)
            print(f"已创建model目录: {model_dir}")
        except Exception as e:
            print(f"创建model目录失败: {e}")
    return model_dir



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        setup_window_icon(self)
        # ✅ 使用全局设置管理器
        self.settings = settings_manager.settings

        # ✅ 确保model目录存在
        self.model_dir = ensure_model_directory()

        # ✅ 加载UI设置并应用到控件
        self.load_ui_settings()
        # ✅ 添加日志文件管理
        self.log_file_path = None
        self.log_file = None

        self.worker_thread = None
        self.transcriber = None
        self.ui.progressBar.setValue(0)
        self.ui.memoryRate.setText("")
        # # ✅ 添加系统监控定时器
        # self.system_monitor_timer = QTimer()
        # self.system_monitor_timer.timeout.connect(self.update_system_monitor)
        # self.system_monitor_timer.start(5000)  # 每5秒更新一次

        # 创建系统监控工作线程
        self.monitor_worker = SystemMonitorWorker()
        self.monitor_worker.monitor_updated.connect(self.update_system_monitor_display)
        self.monitor_worker.start()

        # ✅ 在主线程中创建定时器
        self.working_timer = QTimer()
        # ✅ 设置初始间隔（3-5秒随机）
        initial_interval = random.randint(3000, 5000)
        self.working_timer.setInterval(initial_interval)
        self.working_timer.timeout.connect(self.send_working_message)


        # ✅ 添加进度模拟定时器
        self.progress_timer = QTimer()
        self.progress_timer.timeout.connect(self.update_progress)
        self.sim_progress = 0
        # ✅ 添加音频时长变量
        self.audio_duration = 0
        self.progress_interval = 300  # 默认300ms

        # ✅ 设置 textEdit 的初始 tip
        self.update_textEdit_tip()

        # ✅ 监听 textEdit 文本变化
        self.ui.textEdit.textChanged.connect(self.update_textEdit_tip)



        # ✅ 动态加载模型文件名
        self.model_dir = os.path.join(os.getcwd(), "model")
        self.load_model_list()

        # 绑定按钮
        self.ui.pushButton.clicked.connect(self.select_file)
        self.ui.pushButton_2.clicked.connect(self.start_transcribe)
        # 调起帮助窗口
        self.ui.pushButton_3.clicked.connect(self.open_help_dialog)
        # 初始化帮助窗口为None
        self.help_dialog = None

        # 调起免责声明窗口
        self.ui.pushButton_4.clicked.connect(self.open_disclaimers_dialog)
        # 初始化免责声明窗口为None
        self.disclaimers_dialog = None

        # ✅ 添加comboBox选择变化的信号连接
        self.ui.comboBox.currentTextChanged.connect(self.on_model_selection_changed)

        # ✅ 新增：为comboBox添加下拉展开事件监听
        # 方法1：重写comboBox的showPopup方法
        original_show_popup = self.ui.comboBox.showPopup

        def custom_show_popup():
            self.refresh_model_list()  # 展开前刷新模型列表
            original_show_popup()  # 调用原始的showPopup方法

        self.ui.comboBox.showPopup = custom_show_popup

        # ✅ 设置UI文本框引用
        logger_manager.set_ui_text_edit(self.ui.textEdit_2)
        logger_manager.info("主窗口初始化完成", "main")

        # 连接日志管理器的UI更新信号
        logger_manager.ui_update_signal.connect(self.update_ui_log)
        logger_manager.batch_update_signal.connect(self.batch_update_ui_log)  # 新增批量更新信号

    def update_ui_log(self, message):
        """线程安全的UI日志更新"""
        self.ui.textEdit_2.append(message)

    def batch_update_ui_log(self, messages):
        """批量消息更新（子线程使用）"""
        if not messages:
            return

        # 暂停重绘以提高性能
        self.ui.textEdit_2.setUpdatesEnabled(False)

        try:
            # 批量添加消息
            for message in messages:
                self.ui.textEdit_2.append(message)

            # 限制最大行数（可选）
            self._limit_text_edit_lines()

        finally:
            # 恢复重绘
            self.ui.textEdit_2.setUpdatesEnabled(True)
            # 确保滚动到底部
            self.ui.textEdit_2.ensureCursorVisible()

    def _limit_text_edit_lines(self, max_lines=1000):
        """限制文本框最大行数，防止内存占用过大"""
        document = self.ui.textEdit_2.document()
        current_lines = document.blockCount()

        if current_lines > max_lines:
            # 删除前面的行
            cursor = self.ui.textEdit_2.textCursor()
            cursor.movePosition(cursor.Start)

            lines_to_remove = current_lines - max_lines + 50  # 多删除50行，避免频繁删除
            for _ in range(lines_to_remove):
                cursor.select(cursor.BlockUnderCursor)
                cursor.removeSelectedText()
                if not cursor.atEnd():
                    cursor.deleteChar()  # 删除换行符

    def load_ui_settings(self):
        """加载UI设置并应用到控件"""
        try:
            output_type, debug_enabled, simple_enabled = settings_manager.get_ui_settings()

            # 设置输出类型
            if output_type == "txt":
                self.ui.txtType.setChecked(True)
            elif output_type == "vtt":
                self.ui.vttType.setChecked(True)
            elif output_type == "json":
                self.ui.jsonType.setChecked(True)
            else:  # 默认srt
                self.ui.srtType.setChecked(True)

            # 设置调试模式
            if debug_enabled:
                self.ui.yesDebug.setChecked(True)
            else:
                self.ui.noDebug.setChecked(True)

            # 设置简体转换
            if simple_enabled:
                self.ui.yesSimple.setChecked(True)
            else:
                self.ui.noSimple.setChecked(True)

            logger_manager.info(f"UI设置已加载: 输出类型={output_type}, 调试={debug_enabled}, 简体={simple_enabled}",
                                "main")

        except Exception as e:
            logger_manager.error(f"加载UI设置失败: {str(e)}，使用默认值", "main")
            # 设置默认值
            self.ui.srtType.setChecked(True)
            self.ui.noDebug.setChecked(True)
            self.ui.noSimple.setChecked(True)

    def save_ui_settings(self):
        """保存当前UI设置"""
        try:
            # 获取输出类型
            if self.ui.txtType.isChecked():
                output_type = "txt"
            elif self.ui.vttType.isChecked():
                output_type = "vtt"
            elif self.ui.jsonType.isChecked():
                output_type = "json"
            else:
                output_type = "srt"

            # 获取调试模式
            debug_enabled = self.ui.yesDebug.isChecked()

            # 获取简体转换
            simple_enabled = self.ui.yesSimple.isChecked()

            # 保存设置
            settings_manager.save_ui_settings(output_type, debug_enabled, simple_enabled)
            logger_manager.info(f"UI设置已保存: 输出类型={output_type}, 调试={debug_enabled}, 简体={simple_enabled}",
                                "main")

        except Exception as e:
            logger_manager.error(f"保存UI设置失败: {str(e)}", "main")
            
    def update_textEdit_tip(self):
        """动态更新 textEdit 的 tip"""
        current_text = self.ui.textEdit.toPlainText().strip()

        if not current_text:
            # 文本为空时显示提示
            self.ui.textEdit.setToolTip("请选择音视频文件")
        else:
            # 文本不为空时显示完整路径
            self.ui.textEdit.setToolTip(current_text)
    def load_model_list(self):
        # self.ui.comboBox.clear()
        # # 确保model目录存在
        # if not os.path.exists(self.model_dir):
        #     os.makedirs(self.model_dir)
        #
        # try:
        #     model_files = [f for f in os.listdir(self.model_dir) if f.endswith(".pt")]
        # except Exception as e:
        #     logger_manager.error(f"读取model目录失败: {str(e)}", "main")
        #     model_files = []
        #
        # if not model_files:
        #     self.ui.comboBox.addItem("请先下载模型文件到model目录")
        #     # QMessageBox.information(self, "提示",
        #     #                         f"未在 model 目录下发现任何模型文件。\n\n请下载Whisper模型文件(.pt格式)并放置到：\n{self.model_dir}")
        #     show_info(self, "提示", f"未在 model 目录下发现任何模型文件。\n\n请下载Whisper模型文件(.pt格式)并放置到：\n{self.model_dir}")
        #     return
        #
        # self.ui.comboBox.addItem("请选择模型")
        # for model in model_files:
        #     self.ui.comboBox.addItem(model)
        #
        # self.ui.comboBox.setCurrentIndex(1)  # 默认选第一个模型

        self.ui.comboBox.clear()

        # 确保model目录存在
        if not os.path.exists(self.model_dir):
            os.makedirs(self.model_dir)

        try:
            model_files = [f for f in os.listdir(self.model_dir) if f.endswith(".pt")]
        except Exception as e:
            logger_manager.error(f"读取model目录失败: {str(e)}", "main")
            model_files = []

        if not model_files:
            self.ui.comboBox.addItem("请先下载模型文件到model目录")
            show_info(self, "提示",
                      f"未在 model 目录下发现任何模型文件。\n\n请下载模型文件(.pt格式)并放置到：\n{self.model_dir} 。\n\n详情请点击【使用帮助】")
            return

        self.ui.comboBox.addItem("请选择模型")
        for model in model_files:
            self.ui.comboBox.addItem(model)

        # ✅ 回填上次选择的模型
        last_selected_model = settings_manager.get_selected_model()
        if last_selected_model and last_selected_model in model_files:
            # 找到上次选择的模型，设置为当前选择
            model_index = model_files.index(last_selected_model) + 1  # +1是因为第0项是"请选择模型"
            self.ui.comboBox.setCurrentIndex(model_index)
            logger_manager.info(f"已回填上次选择的模型: {last_selected_model}", "main")
        else:
            # 没有上次选择或上次选择的模型不存在，默认选第一个模型
            self.ui.comboBox.setCurrentIndex(1)  # 默认选第一个模型
            # ✅ 使用comboBox当前选中的文本，确保一致性
            current_text = self.ui.comboBox.currentText()
            self.on_model_selection_changed(current_text)

    def update_system_monitor(self):
        """更新系统监控信息到memoryRate控件"""
        monitor_info = get_system_monitor_info()

        if 'error' in monitor_info:
            self.ui.memoryRate.setText(f"监控错误: {monitor_info['error']}")
            logger_manager.error(f"系统监控更新失败: {monitor_info['error']}", "main")
            return

        # 格式化显示文本（两行格式）
        monitor_text = (
            f"进程: 内存 {monitor_info['process_memory_text']}, CPU: {monitor_info['process_cpu']:.0f}%\n"
            f"系统: 内存 {monitor_info['system_memory_percent']:.0f}%, CPU: {monitor_info['system_cpu']:.0f}%"
        )

        # 更新UI控件
        self.ui.memoryRate.setText(monitor_text)
    def refresh_model_list(self):
        """刷新模型列表（保持当前选择）"""
        try:
            # 保存当前选择
            current_selection = self.ui.comboBox.currentText()

            # 重新加载模型列表
            self.ui.comboBox.clear()

            # 确保model目录存在
            if not os.path.exists(self.model_dir):
                os.makedirs(self.model_dir)

            try:
                model_files = [f for f in os.listdir(self.model_dir) if f.endswith(".pt")]
            except Exception as e:
                logger_manager.error(f"读取model目录失败: {str(e)}", "main")
                model_files = []

            if not model_files:
                self.ui.comboBox.addItem("请先下载模型文件到model目录")
                logger_manager.info("刷新模型列表：未发现模型文件", "main")
                return

            self.ui.comboBox.addItem("请选择模型")
            for model in model_files:
                self.ui.comboBox.addItem(model)

            # 尝试恢复之前的选择
            if current_selection and current_selection in model_files:
                model_index = model_files.index(current_selection) + 1  # +1是因为第0项是"请选择模型"
                self.ui.comboBox.setCurrentIndex(model_index)
                logger_manager.info(f"刷新模型列表：恢复选择 {current_selection}", "main")
            elif current_selection == "请选择模型":
                self.ui.comboBox.setCurrentIndex(0)
            else:
                # 如果之前选择的模型不存在了，选择第一个可用模型
                if len(model_files) > 0:
                    self.ui.comboBox.setCurrentIndex(1)
                    logger_manager.info(f"刷新模型列表：之前选择的模型不存在，自动选择 {model_files[0]}", "main")
                else:
                    self.ui.comboBox.setCurrentIndex(0)

            logger_manager.info(f"刷新模型列表完成：发现 {len(model_files)} 个模型文件", "main")

        except Exception as e:
            logger_manager.error(f"刷新模型列表失败: {str(e)}", "main")
    def on_model_selection_changed(self, selected_text):
        """当comboBox选择发生变化时调用"""
        # 无论选择什么都保存，让save_selected_model方法内部判断
        settings_manager.save_selected_model(selected_text)

        if selected_text and selected_text.endswith(".pt"):
            logger_manager.info(f"已保存模型选择: {selected_text}", "main")
        else:
            logger_manager.info(f"已清空模型选择（当前选择: {selected_text}）", "main")
    def select_file(self):
        # settings = QSettings("MyCompany", "WhisperApp")  # ✅ App名和组织名可自定义
        # last_dir = settings.value("last_directory", "")  # 读取上次目录，默认为空
        # ✅ 读取上次保存的目录，如果没有则使用当前目录
        last_dir = self.settings.value("last_directory", os.getcwd())
        file_path, _ = QFileDialog.getOpenFileName(
            # 请选择视频文件(*.mp4  *.mov  *.mkv  *.avi  *.flv)或音频文件(.wav, .mp3, .ogg, .flac)
            self, "选择音视频文件",   last_dir, "音视频文件 (*.mp4  *.mov  *.mkv  *.avi  *.flv *.wav *.mp3 *.ogg *.flac);;所有文件 (*.*)"
        )
        if file_path:
            self.ui.textEdit.setText(file_path)
            # ✅ 修正：使用正确的 PySide6 语法
            self.ui.textEdit.moveCursor(QTextCursor.MoveOperation.End)
            # ✅ 保存当前目录作为下次默认目录, 这个文件存储在:
            self.settings.setValue("last_directory", os.path.dirname(file_path))
            # ✅ 手动更新 tip（虽然 textChanged 信号也会触发，但这样更及时）
            self.update_textEdit_tip()
        """
        ✅ QSettings 文件保存位置
        系统	存储位置	示例
        Windows	注册表路径：HKEY_CURRENT_USER\Software\MyCompany\WhisperApp	使用 regedit 查看
        macOS	~/Library/Preferences/com.MyCompany.WhisperApp.plist	
        Linux	~/.config/MyCompany/WhisperApp.conf
        """

    def start_transcribe(self):
        file_path = self.ui.textEdit.toPlainText().strip()
        model_file = self.ui.comboBox.currentText()

        if not file_path or not os.path.exists(file_path):
            # QMessageBox.warning(self, "错误", "请选择一个有效的音频或视频文件")
            show_warning(self, "提示", "请选择一个有效的音频或视频文件")
            return

        if model_file == "请选择模型":
            show_warning(self, "提示", "请先下载模型文件到model目录")
            #QMessageBox.warning(self, "错误", "请选择一个模型文件")
            return
        # ✅ 检查调试模式并初始化日志文件
        self.setup_debug_logging()
        full_model_path = os.path.join(self.model_dir, model_file)

        # 清空之前的日志和重置进度条
        self.ui.textEdit_2.clear()
        self.ui.progressBar.setValue(0)

        # 获取格式类型
        if self.ui.txtType.isChecked():
            format_type = 'txt'
        elif self.ui.vttType.isChecked():
            format_type = 'vtt'
        elif self.ui.jsonType.isChecked():
            format_type = 'json'
        else:
            format_type = 'srt'  # 默认

        # 创建转录器和工作线程
        self.transcriber = Transcriber(model_path=full_model_path,
                                       debug_mode=self.ui.yesDebug.isChecked(),# 是否启用调试模式
                                       log_file_path=self.log_file_path,
                                       export_format=format_type,
                                       convert_to_simple=self.ui.yesSimple.isChecked() )  # 简体转换参数
        self.worker_thread = QThread()
        self.transcriber.moveToThread(self.worker_thread)

        # try:
        #     self.transcriber.progress_signal.disconnect()
        # except:
        #     pass
        # 连接信号槽
        self.transcriber.log_signal.connect(self.ui.textEdit_2.append)
        self.transcriber.progress_signal.connect(self.ui.progressBar.setValue)
        # ✅ 添加调试连接，确认信号是否发出
        # self.transcriber.progress_signal.connect(lambda val: print(f"[MAIN] Received progress: {val}"))

        # ✅ 转录开始时启动进度模拟
        self.transcriber.transcription_started.connect(self.start_progress_simulation)
        # ✅ 接收音频时长信号
        self.transcriber.audio_duration_signal.connect(self.set_audio_duration)
        # ✅ 转录完成时停止所有定时器
        self.transcriber.transcription_finished.connect(self.stop_all_timers)
        self.transcriber.transcription_finished.connect(lambda: self.ui.pushButton_2.setEnabled(True))
        # ✅ 连接文件格式错误信号
        self.transcriber.invalid_file_format_signal.connect(self.handle_invalid_file_format)

        # 线程启动时调用transcribe方法
        # self.worker_thread.started.connect(lambda: self.transcriber.transcribe(file_path))
        self.worker_thread.started.connect(
            lambda: QMetaObject.invokeMethod(
                self.transcriber,
                "transcribe",
                Qt.QueuedConnection,
                Q_ARG(str, file_path)
            )
        )
        # 转录完成后的处理
        self.transcriber.progress_signal.connect(self.check_finish)

        # 线程清理
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(lambda: setattr(self, 'transcriber', None))

        # 启动线程
        self.worker_thread.start()

        # 禁用开始按钮防止重复点击
        self.ui.pushButton_2.setEnabled(False)

    def set_audio_duration(self, duration):
        """设置音频时长并计算进度间隔"""
        self.audio_duration = duration
        # 计算每1%需要的时间（秒）
        time_per_percent = duration / 100
        # 转换为毫秒
        self.progress_interval = int(time_per_percent * 1000)
        self.write_debug_log(f"📊 音频时长: {duration:.2f}秒，每1%进度需要: {time_per_percent:.2f}秒")
    def setup_debug_logging(self):
        """设置调试日志文件"""
        if self.ui.yesDebug.isChecked():
            today = datetime.now().strftime("%Y%m%d")
            self.log_file_path = os.path.join(os.getcwd(), f"{today}_log.log")
            logger_manager.setup_file_logging(self.log_file_path, True)
        else:
            logger_manager.info("调试模式已关闭，不记录日志文件", "main")
            self.log_file_path = None
    def check_finish(self, val):
        if val >= 100:
            # ✅ 停止定时器
            self.working_timer.stop()
            # 重新启用开始按钮
            self.ui.pushButton_2.setEnabled(True)
            # 安全地退出线程
            if self.worker_thread and self.worker_thread.isRunning():
                self.worker_thread.quit()
                self.worker_thread.wait()


    def cleanup_worker_thread(self):
        """强制清理工作线程"""
        try:
            if self.worker_thread and self.worker_thread.isRunning():
                # 给线程一些时间自然结束
                self.worker_thread.quit()
                if not self.worker_thread.wait(3000):  # 等待3秒
                    # 如果3秒内没有结束，强制终止
                    logger_manager.warning("⚠️ 线程未能正常退出，强制终止", "main")
                    self.worker_thread.terminate()
                    self.worker_thread.wait(1000)  # 再等待1秒

            # 清理转录器引用
            if hasattr(self, 'transcriber') and self.transcriber:
                self.transcriber = None

            # 强制垃圾回收
            import gc
            gc.collect()

        except Exception as e:
            logger_manager.error(f"❌ 清理工作线程时发生错误: {e}", "main")

    def write_debug_log(self, message, show_in_ui=False):
        """写入调试日志到文件

        Args:
            message (str): 要写入的日志消息
            show_in_ui (bool): 是否同时在UI中显示消息
        """
        logger_manager.debug(message, "main", show_in_ui)
    def send_working_message(self):
        """在主线程中发送工作提示消息"""
        current_time = datetime.now().strftime("%Y年%m月%d日%H:%M:%S")
        str_temp = f"🕐 {current_time}  正在努力转换中，请稍候..."

        # ✅ 使用新的UI消息方法
        logger_manager.ui_message(str_temp, also_log=True, log_level='info', module_name='main')

        # 设置下一次的随机间隔（3-5秒）
        next_interval = random.randint(3000, 5000)
        self.working_timer.setInterval(next_interval)

    def update_system_monitor_display(self, monitor_info):
        """在主线程中更新UI显示"""
        if 'error' in monitor_info:
            self.ui.memoryRate.setText(f"监控错误: {monitor_info['error']}")
            return

        monitor_text = (
            f"进程: 内存 {monitor_info['process_memory_text']}, CPU: {monitor_info['process_cpu']:.0f}%\n"
            f"系统: 内存 {monitor_info['system_memory_percent']:.0f}%, CPU: {monitor_info['system_cpu']:.0f}%"
        )
        self.ui.memoryRate.setText(monitor_text)

    def closeEvent(self, event):
        """程序关闭时的处理"""
        """窗口关闭时的清理工作"""
        try:
            # 停止系统监控定时器
            if hasattr(self, 'system_monitor_timer'):
                self.system_monitor_timer.stop()

            # 停止其他定时器
            if hasattr(self, 'working_timer'):
                self.working_timer.stop()
            if hasattr(self, 'progress_timer'):
                self.progress_timer.stop()

            # 保存UI设置
            self.save_ui_settings()

        except Exception as e:
            logger_manager.error(f"窗口关闭清理失败: {str(e)}", "main")

        if hasattr(self, 'monitor_worker'):
            self.monitor_worker.stop()
        super().closeEvent(event)
        # 调用父类的closeEvent
        super().closeEvent(event)

    def cleanup_temp_files(self):
        """清理可能残留的临时文件"""
        try:
            current_dir = os.getcwd()
            for file in os.listdir(current_dir):
                if file.endswith('_extracted.wav'):
                    temp_file_path = os.path.join(current_dir, file)
                    try:
                        os.remove(temp_file_path)
                        logger_manager.info(f"🗑️ 已清理残留临时文件: {file}", "main")
                    except:
                        pass
        except Exception as e:
            logger_manager.debug(f"清理临时文件时发生错误: {e}", "main")

    def open_help_dialog(self):
        """打开帮助窗体"""
        try:
            # 如果帮助窗口已经存在且可见，则将其置于前台
            if self.help_dialog and self.help_dialog.isVisible():
                self.help_dialog.raise_()
                self.help_dialog.activateWindow()
                return

            # 创建新的帮助窗口
            self.help_dialog = HelpDialog()
            self.help_dialog.show()
            logger_manager.info("帮助窗口已打开", "auth_window")

        except Exception as e:
            logger_manager.error(f"打开帮助窗口时发生错误: {str(e)}", "auth_window")
            # QMessageBox.warning(self, "错误", f"无法打开帮助窗口: {str(e)}")
            show_error(self, "错误", f"无法打开帮助窗口: {str(e)}")

    def open_disclaimers_dialog(self):
        """打开免责声明窗体"""
        try:
            # 如果免责声明窗口已经存在且可见，则将其置于前台
            if self.disclaimers_dialog and self.disclaimers_dialog.isVisible():
                self.disclaimers_dialog.raise_()
                self.disclaimers_dialog.activateWindow()
                return

            # 创建新的免责声明窗口
            self.disclaimers_dialog = DisclaimersHelpDialog()
            self.disclaimers_dialog.show()
            logger_manager.info("使用说明窗口已打开", "main")

        except Exception as e:
            logger_manager.error(f"打开使用说明窗口失败: {str(e)}", "main")
            show_error(self, "错误", f"无法打开使用说明窗口: {str(e)}")

    def start_working_timer(self):
        #self.working_timer.start()
        """启动工作提示定时器"""
        # ✅ 设置初始随机间隔
        initial_interval = random.randint(3000, 5000)
        self.working_timer.setInterval(initial_interval)
        self.working_timer.start()

    def stop_working_timer(self):
        self.working_timer.stop()

    def start_progress_simulation(self):
        """启动进度模拟"""
        self.sim_progress = 0
        self.progress_timer.start(300)  # 前10%仍使用300ms
        # print("[DEBUG] Progress simulation started in main thread")

        # 同时启动工作提示
        self.start_working_timer()

    def update_progress(self):
        """在主线程中更新模拟进度"""
        if self.sim_progress < 10:
            # 前10%保持当前速度：每300ms增加0.5%
            self.sim_progress += 0.5
            progress_value = int(self.sim_progress)

            self.ui.progressBar.setValue(progress_value)

            # 当达到10%时，切换到基于音频时长的间隔
            if progress_value >= 10:
                self.progress_timer.stop()
                self.progress_timer.start(self.progress_interval)  # 使用计算出的间隔
                #self.write_debug_log(f"🔄 切换到音频时长模式，间隔: {self.progress_interval}ms")
                logger_manager.info(f"🔄 音频时长模式，当前进度: {progress_value}%", "main")

        elif self.sim_progress < 85:
            # 10%-85%：根据音频时长，每个间隔增加1%
            self.sim_progress += 1.0
            progress_value = int(self.sim_progress)

            self.ui.progressBar.setValue(progress_value)

            # 每10%输出一次日志
            if progress_value % 10 == 0:
                message = f"🔄 转录进度: {progress_value}%"
                #self.write_debug_log(message)
                logger_manager.info(message, "main")
               

        elif self.sim_progress < 90:
            # 85%-90%：缓慢增长
            self.sim_progress += 0.2
            progress_value = int(self.sim_progress)
            self.ui.progressBar.setValue(progress_value)

    def handle_invalid_file_format(self):
        """处理文件格式错误，将焦点设置到textEdit并提示用户重新选择"""
        # 将焦点设置到文件路径输入框
        self.ui.textEdit.setFocus()
        # 选中textEdit中的所有文本，方便用户重新输入
        self.ui.textEdit.selectAll()
        # 重新启用开始按钮
        self.ui.pushButton_2.setEnabled(True)
        # 停止所有定时器
        self.stop_all_timers()
    def stop_all_timers(self):
        """停止所有定时器"""
        self.progress_timer.stop()
        self.working_timer.stop()
        # print("[DEBUG] All timers stopped")

def show_auth_window():
    """显示授权窗口"""
    auth_window = AuthWindow() # AuthWindow
    auth_window.show()
    return auth_window

def show_main_window():
    """显示主窗口"""
    main_window = MainWindow()
    # main_window.setWindowTitle("字幕生成器")
    main_window.setWindowTitle(f"字幕生成器 {VERSION}")
    main_window.show()
    return main_window


# 在 MainWindow 类中添加测试方法
def test_exception_handler(self):
    """测试全局异常处理器"""
    raise Exception("这是一个测试异常，用于验证全局异常处理器是否正常工作")


if __name__ == "__main__":
    # 注册全局异常处理器
    exception_handler = GlobalExceptionHandler()
    sys.excepthook = exception_handler.handle_exception

    app = QApplication(sys.argv)

    # 设置中文语言环境
    from PySide6.QtCore import QLocale, QTranslator, QLibraryInfo

    locale = QLocale(QLocale.Language.Chinese, QLocale.Country.China)
    QLocale.setDefault(locale)

    translator = QTranslator()
    qt_translations_path = QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath)
    if translator.load(locale, "qtbase", "_", qt_translations_path):
        app.installTranslator(translator)
    else:
        if translator.load(locale, "qt", "_", qt_translations_path):
            app.installTranslator(translator)

    # 创建单实例管理器
    instance_manager = SingleInstanceManager("字幕生成器")

    # 检查是否已有实例在运行
    if instance_manager.is_running():
        logger_manager.info("应用程序已运行", "main")
        sys.exit(0)

    # 启动单实例服务器
    if not instance_manager.start_server():
        logger_manager.error("无法启动单实例服务", "main")
        sys.exit(1)

    try:
        # 启动SplashScreen（替换原有的授权检查逻辑）
        splash = SplashScreen()
        splash.show()

        # 进入事件循环
        sys.exit(app.exec())
    except Exception as e:
        import traceback

        logger_manager.error(f"应用程序启动失败: {e}", "main")
        logger_manager.error(f"堆栈跟踪: {traceback.format_exc()}", "main")
        sys.exit(1)



# if __name__ == "__main__":
#     # 注册全局异常处理器（必须在QApplication创建之前）
#     # 在创建QApplication之前注册全局异常处理
#     exception_handler = GlobalExceptionHandler()
#     sys.excepthook = exception_handler.handle_exception
#
#     app = QApplication(sys.argv)
#
#
#
#     # ✅ 添加中文语言环境设置
#     from PySide6.QtCore import QLocale, QTranslator, QLibraryInfo
#
#     # 设置应用程序语言环境为中文
#     locale = QLocale(QLocale.Language.Chinese, QLocale.Country.China)
#     QLocale.setDefault(locale)
#
#     # 加载Qt内置的中文翻译文件（用于右键菜单等系统控件）
#     translator = QTranslator()
#     # 使用正确的Qt翻译文件路径
#     qt_translations_path = QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath)
#     if translator.load(locale, "qtbase", "_", qt_translations_path):
#         app.installTranslator(translator)
#     else:
#         # 备选方案：尝试加载 qt_ 前缀的翻译文件
#         if translator.load(locale, "qt", "_", qt_translations_path):
#             app.installTranslator(translator)
#
#
#     # import whisper
#     # 会自动下载模型到缓存目录
#     # model = whisper.load_model("tiny.en")  # 也可以是 base, small, medium, large
#     # model = whisper.load_model("base.en")
#     # model = whisper.load_model("small.en")
#     # model = whisper.load_model("medium.en")
#     # model = whisper.load_model("large")  # 目前已经没有这个版本了, 下载这个时候, 会默认下载V3的版本
#     # model = whisper.load_model("large-v1")
#     # model = whisper.load_model("large-v2")
#     # model = whisper.load_model("large-v3")
#
#     # 创建单实例管理器, 这个名字要和build-obf.spec里面的名字保持一致
#     instance_manager = SingleInstanceManager("字幕生成器")
#
#     # 检查是否已有实例在运行
#     if instance_manager.is_running():
#         logger_manager.info("应用程序已运行", "main")
#         sys.exit(0)
#
#     # 启动单实例服务器
#     if not instance_manager.start_server():
#         logger_manager.error("无法启动单实例服务", "main")
#         sys.exit(1)
#
#     # 全局变量用于存储主窗口引用
#     main_window = None
#     auth_window = None
#
# #    test_exception_handler( )
#     def bring_window_to_front():
#         """将窗口置于前台"""
#         global main_window, auth_window
#
#         # 优先显示主窗口
#         if main_window and main_window.isVisible():
#             main_window.raise_()
#             main_window.activateWindow()
#             main_window.showNormal()  # 如果窗口被最小化，则恢复
#         # 如果主窗口不可见，显示授权窗口
#         elif auth_window and auth_window.isVisible():
#             auth_window.raise_()
#             auth_window.activateWindow()
#             auth_window.showNormal()
#
#
#     # 连接信号到槽函数
#     instance_manager.show_window_signal.connect(bring_window_to_front)
#
#     # 步骤1: 调用 SettingsManager 的 get_auth_info() 返回授权信息
#     machine_code, auth_time, last_auth_code = settings_manager.get_auth_info()
#     # print("授权信息:", machine_code, auth_time, last_auth_code)
#     # 步骤2: 检查是否有任何一个为空
#     if not machine_code or not auth_time or not last_auth_code:
#         print("授权信息不完整，显示授权窗口")
#         auth_window = show_auth_window()
#         main_window = None
#
#
#         def on_auth_success():
#             global main_window
#             main_window = show_main_window()
#
#
#         auth_window.auth_success.connect(on_auth_success)
#     else:
#         # 步骤3: 对last_auth_code进行第一次解密
#         try:
#             auth_code_one_de = aes_decrypt(last_auth_code)
#             if auth_code_one_de is None:
#                 raise ValueError("第一次解密失败")
#         except Exception as e:
#             print(f"第一次解密失败: {e}，显示授权窗口")
#             auth_window = show_auth_window()
#             main_window = None
#
#
#             def on_auth_success():
#                 global main_window
#                 main_window = show_main_window()
#
#
#             auth_window.auth_success.connect(on_auth_success)
#         else:
#             # 步骤4: 检查分隔后的元素数量
#             auth_parts = auth_code_one_de.split("|")
#             if len(auth_parts) != 2:
#                 #print(f"授权码格式错误，分隔后元素数量为{len(auth_parts)}，应为2，显示授权窗口")
#                 auth_window = show_auth_window()
#                 main_window = None
#
#
#                 def on_auth_success():
#                     global main_window
#                     main_window = show_main_window()
#
#
#                 auth_window.auth_success.connect(on_auth_success)
#             else:
#                 # 步骤5: 提取第一个元素和时间
#                 auth_code_en = auth_parts[0]
#                 temp_time = auth_parts[1]
#
#                 # 对第一个元素再进行一次解密
#                 try:
#                     auth_code = aes_decrypt(auth_code_en)
#                     if auth_code is None:
#                         raise ValueError("第二次解密失败")
#                 except Exception as e:
#                     print(f"第二次解密失败: {e}，显示授权窗口")
#                     auth_window = show_auth_window()
#                     main_window = None
#
#
#                     def on_auth_success():
#                         global main_window
#                         main_window = show_main_window()
#
#
#                     auth_window.auth_success.connect(on_auth_success)
#                 else:
#                     # 按照 | 进行分隔
#                     auth_code_parts = auth_code.split("|")
#                     if len(auth_code_parts) != 2:
#                         print(f"内层授权码格式错误，分隔后元素数量为{len(auth_code_parts)}，应为2，显示授权窗口")
#                         auth_window = show_auth_window()
#                         main_window = None
#
#
#                         def on_auth_success():
#                             global main_window
#                             main_window = show_main_window()
#
#
#                         auth_window.auth_success.connect(on_auth_success)
#                     else:
#                         auth_code_machine = auth_code_parts[0]
#                         auth_code_day = auth_code_parts[1]
#
#                         # 步骤6: 获取当前设备机器码并比较
#                         # temp_auth_window = AuthWindow()
#                         # temp_auth_window.generate_machine_code()
#                         # current_machine_code = temp_auth_window.ui.leMachineCode.text().replace('-', '')
#                         # temp_auth_window.close()
#                         # 获取机器码而不创建AuthWindow实例
#                         current_machine_code = AuthWindow.generate_machine_code_static()
#
#                         if current_machine_code and auth_code_machine.replace('-', '') != current_machine_code.replace('-', ''):
#                             print("机器码不匹配，显示授权窗口")
#                             auth_window = show_auth_window()
#                             main_window = None
#
#
#                             def on_auth_success():
#                                 global main_window
#                                 main_window = show_main_window()
#
#
#                             auth_window.auth_success.connect(on_auth_success)
#                         else:
#                             # 步骤7: 检查授权天数
#                             try:
#                                 auth_days = int(auth_code_day)
#                             except ValueError:
#                                 print("授权天数格式错误，显示授权窗口")
#                                 auth_window = show_auth_window()
#                                 main_window = None
#
#
#                                 def on_auth_success():
#                                     global main_window
#                                     main_window = show_main_window()
#
#
#                                 auth_window.auth_success.connect(on_auth_success)
#                             else:
#                                 if auth_days == 0:
#                                     # 无限制授权
#                                     print("检测到无限制授权，直接启动主程序")
#                                     main_window = show_main_window()
#                                 else:
#                                     # 步骤8-9: 检查授权是否过期
#                                     try:
#                                         # 解析授权时间
#                                         auth_datetime = datetime.strptime(temp_time, "%Y-%m-%d %H:%M:%S")
#                                         # 计算过期时间
#                                         expire_datetime = auth_datetime + timedelta(days=auth_days)
#                                         # 获取当前时间
#                                         current_datetime = datetime.now()
#
#                                         # 检查当前时间是否在合理范围内
#                                         if current_datetime < auth_datetime:
#                                             print(f"检测到系统时间异常（当前时间：{current_datetime} 早于授权时间：{auth_datetime}），显示授权窗口")
#                                             auth_window = show_auth_window()
#                                             main_window = None
#                                         elif current_datetime > expire_datetime:
#                                             print(f"授权已过期（过期时间：{expire_datetime}），显示授权窗口")
#                                             auth_window = show_auth_window()
#                                             main_window = None
#                                         else:
#                                             print(f"授权有效（授权时间：{auth_datetime}，过期时间：{expire_datetime}），直接启动主程序")
#                                             main_window = show_main_window()
#
#                                         # 如果需要重新授权，绑定成功回调
#                                         if main_window is None:
#                                             def on_auth_success():
#                                                 global main_window
#                                                 main_window = show_main_window()
#                                             auth_window.auth_success.connect(on_auth_success)
#                                     except ValueError as e:
#                                         print(f"时间格式解析错误: {e}，显示授权窗口")
#                                         auth_window = show_auth_window()
#                                         main_window = None
#
#
#                                         def on_auth_success():
#                                             global main_window
#                                             main_window = show_main_window()
#
#
#                                         auth_window.auth_success.connect(on_auth_success)
#
#
#     # 在应用程序退出时清理资源
#     def cleanup_on_exit():
#         instance_manager.cleanup()
#
#
#     app.aboutToQuit.connect(cleanup_on_exit)
#
#     sys.exit(app.exec())