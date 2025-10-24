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
import sys
import platform
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

from BatchFileListWindow import BatchFileListWindow
from HelpDialog import HelpDialog
from SystemMonitorWorker import SystemMonitorWorker
from ui_main import Ui_MainWindow
from transcriber import Transcriber
from PySide6.QtCore import QThread,  QMetaObject, Qt, Q_ARG, QTimer ,QSettings
from PySide6.QtGui import QTextCursor
from settings_manager import settings_manager
from datetime import datetime, timedelta
from LoggerManager import logger_manager
from utils import show_info, show_warning, show_error, setup_window_icon, get_system_monitor_info, VERSION, format_size, show_confirm
from disclaimers import DisclaimersHelpDialog
from SingleInstanceManager import SingleInstanceManager
from SplashScreen import SplashScreen
from ui_batchfilelist import Ui_BatchFileList
# 导入全局异常处理器

from GlobalExceptionHandler import GlobalExceptionHandler

# ✅ 第一次启动后, 创建一个主窗口, 并保存大这个变量里面
main_window_instance = None
# ✅ 添加 instance_manager 全局变量声明
instance_manager = None


def activate_main_window():
    """激活主窗口"""
    # 移除这行：global instance_manager

    # 第一层：通过SingleInstanceManager查找
    if instance_manager and hasattr(instance_manager, 'main_window_instance') and instance_manager.main_window_instance:
        try:
            window = instance_manager.main_window_instance
            if window.isVisible():
                window.raise_()
                window.activateWindow()
                if window.isMinimized():
                    window.showNormal()
                return True
        except Exception as e:
            logger_manager.error(f"通过SingleInstanceManager激活窗口失败: {e}", "main")

    # 第二层：通过全局变量查找
    if main_window_instance:
        try:
            if main_window_instance.isVisible():
                main_window_instance.raise_()
                main_window_instance.activateWindow()
                if main_window_instance.isMinimized():
                    main_window_instance.showNormal()
                return True
        except Exception as e:
            logger_manager.error(f"通过全局变量激活窗口失败: {e}", "main")

    # 第三层：通过QApplication遍历查找
    try:
        for widget in QApplication.allWidgets():
            if isinstance(widget, MainWindow) and widget.isVisible():
                widget.raise_()
                widget.activateWindow()
                if widget.isMinimized():
                    widget.showNormal()
                return True
    except Exception as e:
        logger_manager.error(f"通过QApplication遍历激活窗口失败: {e}", "main")

    return False

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
    def __init__(self, trial_mode=False):
        super().__init__()
        self.trial_mode = trial_mode  # 试用模式标识

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 设置拖放事件处理
        self.setup_drag_drop_events()
        setup_window_icon(self)
        # ✅ 使用全局设置管理器
        self.settings = settings_manager.settings
        self.setMaximumSize(800,600)
        self.setMinimumSize(800,600)
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
        self.ui.pushButton_selectDir.setVisible( False)

        # ===== 批量文件常驻数据结构 =====
        self.batch_files = []           # [{'path','name','rel','ext','size','status','selected'}]
        self.batch_base_dir = None      # 最近一次选择的目录
        self.batch_dialog = None        # 非模态详情窗口实例

        # 绑定按钮：选择目录 + 查看详情
        self.ui.pushButton_selectDir.clicked.connect(self.on_select_directory)
        self.ui.viewDetailBtn.clicked.connect(self.on_view_detail)

        # 初始化底部统计
        self.update_selected_summary()


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

        # 绑定按钮, 选择文件
        self.ui.pushButton.clicked.connect(self.select_file)
        # 开始转换, 开始转录
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
        logger_manager.info("✅ 主窗口初始化完成", "main")

        # 连接日志管理器的UI更新信号
        logger_manager.ui_update_signal.connect(self.update_ui_log)
        logger_manager.batch_update_signal.connect(self.batch_update_ui_log)  # 新增批量更新信号

    # 扫描目录并过滤后缀，更新常驻内存与统计
    def on_select_directory(self):
        last_dir = self.settings.value("last_directory", os.getcwd())
        dir_path = QFileDialog.getExistingDirectory(self, "选择目录", last_dir)
        if not dir_path:
            return

        self.settings.setValue("last_directory", dir_path)
        self.batch_base_dir = dir_path

        #把选择的目录写入到 textEdit，并更新提示
        self.ui.textEdit.setText(dir_path)
        self.ui.textEdit.moveCursor(QTextCursor.MoveOperation.End)
        self.update_textEdit_tip()

        # 允许的后缀（小写）
        allowed = {'.mp4', '.mov', '.mkv', '.avi', '.flv', '.wav', '.mp3'}

        # 非递归扫描当前目录；如需递归可改为 os.walk
        try:
            candidates = []
            for name in os.listdir(dir_path):
                full = os.path.join(dir_path, name)
                if not os.path.isfile(full):
                    continue
                ext = os.path.splitext(name)[1].lower()
                if ext in allowed:
                    size = os.path.getsize(full)
                    candidates.append({
                        'path': full,
                        'name': name,
                        'rel': os.path.relpath(full, dir_path),
                        'ext': ext.lstrip('.'),
                        'size': size,
                        'status': '未处理',
                        'selected': True,
                    })
        except Exception as e:
            show_error(self, "错误", f"扫描目录失败：{e}")
            return

        # 追加到常驻列表（去重）
        existing_paths = {f['path'] for f in self.batch_files}
        for item in candidates:
            if item['path'] not in existing_paths:
                self.batch_files.append(item)

        # 更新底部统计
        self.update_selected_summary()

        # 如果详情窗口已打开，则同步表格
        if self.batch_dialog and self.batch_dialog.isVisible():
            self.batch_dialog.populate(self.batch_files, self.batch_base_dir)

    # 打开非模态详情窗口，并填充表格
    def on_view_detail(self):
        # 当没有任何有效或已勾选的文件时，提示并返回
        selected_count = sum(1 for f in self.batch_files if f.get('selected'))
        if selected_count == 0:
            show_warning(self, "提示", "请先选择一个包含音视频文件的【目录】")
            return
        if self.batch_dialog is None:
            self.batch_dialog = BatchFileListWindow(self )
        # 非模态显示
        self.batch_dialog.setWindowModality(Qt.WindowModality.NonModal)
        self.batch_dialog.populate(self.batch_files, self.batch_base_dir)
        self.batch_dialog.show()
        self.batch_dialog.raise_()
        self.batch_dialog.activateWindow()

    # 更新底部“已选择 N 个文件”
    def update_selected_summary(self):
        count = sum(1 for f in self.batch_files if f.get('selected'))
        self.ui.selectedSummary.setText(f"已选择 {count} 个文件")
        # 没有文件时禁用查看详情按钮
        if hasattr(self.ui, "viewDetailBtn"):
            self.ui.viewDetailBtn.setEnabled(count > 0)

    def check_media_duration(self, file_path):
        """检查音视频文件时长"""
        """使用moviepy检查音视频文件时长"""
        try:
            from moviepy.editor import VideoFileClip

            # 使用 VideoFileClip 处理音视频文件
            with VideoFileClip(file_path) as clip:
                duration = clip.duration  # 返回秒数（浮点数）
                return duration

        except Exception as e:
            logger_manager.error(f"使用moviepy检查文件时长失败: {e}", "main")
            return None
        # try:
        #     import subprocess
        #     import json
        #
        #     # 使用ffprobe获取文件信息
        #     cmd = [
        #         'ffprobe', '-v', 'quiet', '-print_format', 'json',
        #         '-show_format', file_path
        #     ]
        #
        #     result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        #
        #     if result.returncode == 0:
        #         data = json.loads(result.stdout)
        #         duration = float(data['format']['duration'])
        #         return duration
        #     else:
        #         logger_manager.warning(f"无法获取文件时长: {file_path}", "main")
        #         return None
        #
        # except Exception as e:
        #     logger_manager.error(f"检查文件时长失败: {e}", "main")
        #     return None


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
        # last_dir = self.settings.value("last_directory", os.getcwd())
        # file_path, _ = QFileDialog.getOpenFileName(
        #     # 请选择视频文件(*.mp4  *.mov  *.mkv  *.avi  *.flv)或音频文件(.wav, .mp3, .ogg, .flac)
        #     self, "选择音视频文件",   last_dir, "音视频文件 (*.mp4  *.mov  *.mkv  *.avi  *.flv *.wav *.mp3 );;所有文件 (*.*)"
        # )
        # if file_path:
        #     self.ui.textEdit.setText(file_path)
        #     self.ui.textEdit.moveCursor(QTextCursor.MoveOperation.End)
        #     # ✅ 保存当前目录作为下次默认目录, 这个文件存储在:
        #     self.settings.setValue("last_directory", os.path.dirname(file_path))
        #     # ✅ 手动更新 tip（虽然 textChanged 信号也会触发，但这样更及时）
        #     self.update_textEdit_tip()
        #
        #     # ✅ 清空批量选择并重置底部统计
        #     self.batch_files.clear()
        #     self.update_selected_summary()
        last_dir = self.settings.value("last_directory", os.getcwd())
        files, _ = QFileDialog.getOpenFileNames(
            self,
            "选择音视频文件",
            last_dir,
            "音视频文件 (*.mp4 *.mov *.mkv *.avi *.flv *.wav *.mp3);;所有文件 (*.*)"
        )
        if not files:
            return

        # 保存下次默认目录
        self.settings.setValue("last_directory", os.path.dirname(files[0]))

        # 重置批量列表并设置基础目录（公共父路径）
        self.batch_files.clear()
        try:
            self.batch_base_dir = os.path.commonpath(files)
        except ValueError:
            self.batch_base_dir = os.path.dirname(files[0])

        allowed = {'.mp4', '.mov', '.mkv', '.avi', '.flv', '.wav', '.mp3'}
        seen = set()

        for full in files:
            if not os.path.isfile(full):
                continue
            ext = os.path.splitext(full)[1].lower()
            if ext not in allowed:
                continue
            norm = os.path.normcase(os.path.abspath(full))
            if norm in seen:
                continue
            seen.add(norm)
            size = os.path.getsize(full)
            self.batch_files.append({
                'path': full,
                'name': os.path.basename(full),
                'rel': os.path.relpath(full, self.batch_base_dir),
                'ext': ext.lstrip('.'),
                'size': size,
                'status': '未处理',
                'selected': True,
            })

        # 单选时显示到 textEdit，多选则清空以避免误判走单文件, 多选的时候, 显示数量
        count = len(self.batch_files)
        if count == 1:
            # 单选：显示路径
            self.ui.textEdit.setText(self.batch_files[0]['path'])
        else:
            # 多选：显示数量
            self.ui.textEdit.setText(f"你选择了{count}个文件")
        self.ui.textEdit.moveCursor(QTextCursor.MoveOperation.End)
        self.update_textEdit_tip()

        # 更新底部统计和详情窗口
        self.update_selected_summary()
        # 如果详情窗口已打开，刷新表格
        if self.batch_dialog and self.batch_dialog.isVisible():
            self.batch_dialog.populate(self.batch_files, self.batch_base_dir)


        """
        ✅ QSettings 文件保存位置
        系统	存储位置	示例
        Windows	注册表路径：HKEY_CURRENT_USER\Software\MyCompany\WhisperApp	使用 regedit 查看
        macOS	~/Library/Preferences/com.MyCompany.WhisperApp.plist	
        Linux	~/.config/MyCompany/WhisperApp.conf
        """

    def start_transcribe(self):
        # 先判断选择的文件
        model_file = self.ui.comboBox.currentText()
        if model_file == "请选择模型":
            show_warning(self, "提示", "请先下载模型文件到model目录")
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
            format_type = 'srt'

        # ========= 优先跑批量（动态调度） =========
        selected = [f for f in self.batch_files if f.get('selected')]
        if selected:

            # 如果选择了多个文件，显示确认对话框
            if len(selected) > 1:
                if not show_confirm(
                        self,
                        "确认批量处理",
                        f"您选择了 {len(selected)} 个文件\r\n可能需要较长时间处理，建议勾选【完成后自动关机】, 夜间处理, 是否继续？"
                ):
                    # 用户点击取消，不执行批量处理
                    return

            self.is_batch_running = True
            # 不再复制静态队列，改为动态从 batch_files 里找下一条
            self._batch_full_model_path = full_model_path
            self._batch_format_type = format_type

            # self.ui.pushButton_2.setEnabled(False)
            # self._start_next_pending()

            # ✅ 优化：多个文件时使用批量模式（模型复用）
            if len(selected) > 1:
                self._start_batch_optimized(selected, full_model_path, format_type)
            else:
                # 单个文件仍使用原有逻辑
                self._start_next_pending()

            return

        # ========= 回退到单文件 =========
        file_path = self.ui.textEdit.toPlainText().strip()
        if not file_path or not os.path.exists(file_path) or not os.path.isfile(file_path):
            show_warning(self, "提示", "请通过“选择文件”选择至少一个音视频文件")
            return

        self._start_one_file(file_path, full_model_path, format_type)



        # # 创建转录器和工作线程
        # self.transcriber = Transcriber(model_path=full_model_path,
        #                                debug_mode=self.ui.yesDebug.isChecked(),# 是否启用调试模式
        #                                log_file_path=self.log_file_path,
        #                                export_format=format_type,
        #                                convert_to_simple=self.ui.yesSimple.isChecked() )  # 简体转换参数
        # self.worker_thread = QThread()
        # self.transcriber.moveToThread(self.worker_thread)
        #
        # # try:
        # #     self.transcriber.progress_signal.disconnect()
        # # except:
        # #     pass
        # # 连接信号槽
        # self.transcriber.log_signal.connect(self.ui.textEdit_2.append)
        # self.transcriber.progress_signal.connect(self.ui.progressBar.setValue)
        # # ✅ 添加调试连接，确认信号是否发出
        # # self.transcriber.progress_signal.connect(lambda val: print(f"[MAIN] Received progress: {val}"))
        #
        # # ✅ 转录开始时启动进度模拟
        # self.transcriber.transcription_started.connect(self.start_progress_simulation)
        # # ✅ 接收音频时长信号
        # self.transcriber.audio_duration_signal.connect(self.set_audio_duration)
        # # ✅ 转录完成时停止所有定时器
        # self.transcriber.transcription_finished.connect(self.stop_all_timers)
        # self.transcriber.transcription_finished.connect(lambda: self.ui.pushButton_2.setEnabled(True))
        # # ✅ 连接文件格式错误信号
        # self.transcriber.invalid_file_format_signal.connect(self.handle_invalid_file_format)
        #
        # # 线程启动时调用transcribe方法
        # # self.worker_thread.started.connect(lambda: self.transcriber.transcribe(file_path))
        # self.worker_thread.started.connect(
        #     lambda: QMetaObject.invokeMethod(
        #         self.transcriber,
        #         "transcribe",
        #         Qt.QueuedConnection,
        #         Q_ARG(str, file_path)
        #     )
        # )
        # # 转录完成后的处理
        # self.transcriber.progress_signal.connect(self.check_finish)
        #
        # # 线程清理
        # self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        # self.worker_thread.finished.connect(lambda: setattr(self, 'transcriber', None))
        #
        # # 启动线程
        # self.worker_thread.start()
        #
        # # 禁用开始按钮防止重复点击
        # self.ui.pushButton_2.setEnabled(False)

    def _start_batch_optimized(self, selected_files, full_model_path, format_type):
        """启动批量优化处理（模型复用）"""
        logger_manager.info(f"🚀 启动批量优化模式，共 {len(selected_files)} 个文件", "main", show_in_ui=True)

        # 提取文件路径列表
        file_paths = [f['path'] for f in selected_files]

        # 创建优化的转录器
        self.transcriber = Transcriber(
            model_path=full_model_path,
            debug_mode=self.ui.yesDebug.isChecked(),
            log_file_path=self.log_file_path,
            export_format=format_type,
            convert_to_simple=self.ui.yesSimple.isChecked()
        )
        self.worker_thread = QThread()
        self.transcriber.moveToThread(self.worker_thread)

        # 连接批量处理信号
        self.transcriber.log_signal.connect(self.ui.textEdit_2.append)
        self.transcriber.batch_file_started.connect(self._on_batch_file_started)
        self.transcriber.batch_file_finished.connect(self._on_batch_file_finished)
        self.transcriber.batch_all_finished.connect(self._on_batch_all_finished)

        # 连接进度条和日志相关信号（批量处理也需要）
        self.transcriber.progress_signal.connect(self.ui.progressBar.setValue)
        self.transcriber.transcription_started.connect(self.start_progress_simulation)
        self.transcriber.audio_duration_signal.connect(self.set_audio_duration)
        self.transcriber.transcription_finished.connect(self.stop_all_timers)


        # 线程启动时调用批量转录方法
        # 将文件路径列表存储到transcriber实例中，避免Q_ARG类型问题
        self.transcriber.batch_files = file_paths
        self.worker_thread.started.connect(
            lambda: QMetaObject.invokeMethod(
                self.transcriber,
                # "transcribe_batch",
                # Qt.QueuedConnection,
                # Q_ARG(list, file_paths)
                "transcribe_batch_from_stored",
                Qt.QueuedConnection
            )
        )

        # 线程清理
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(lambda: setattr(self, 'transcriber', None))

        # 启动线程
        self.worker_thread.start()
        self.ui.pushButton_2.setEnabled(False)

    def _on_batch_file_started(self, file_path):
        """批量处理中单个文件开始的回调"""
        # 标记文件状态为"处理中"
        self._mark_file_status(file_path, '处理中')

        # 更新批量文件列表窗口
        if self.batch_dialog and self.batch_dialog.isVisible():
            self.batch_dialog.populate(self.batch_files, self.batch_base_dir)

        logger_manager.info(f"🔄 开始处理文件: {os.path.basename(file_path)}", "main", show_in_ui=True)

    def _on_batch_file_finished(self, file_path, success):
        """批量处理中单个文件完成的回调"""
        status = '完成' if success else '失败'
        self._mark_file_status(file_path, status)

        # 更新批量文件列表窗口
        if self.batch_dialog and self.batch_dialog.isVisible():
            self.batch_dialog.populate(self.batch_files, self.batch_base_dir)
        # 重置进度条为下一个文件做准备
        self.ui.progressBar.setValue(0)
        logger_manager.info(f"📁 文件处理{status}: {os.path.basename(file_path)}", "main", show_in_ui=True)

    def _on_batch_all_finished(self):
        """批量处理全部完成的回调"""
        self.is_batch_running = False
        self.ui.pushButton_2.setEnabled(True)
        self.on_all_tasks_completed(batch_mode=True)
        logger_manager.info(f"🎉 批量优化处理全部完成！", "main", show_in_ui=True)



    def _start_one_file(self, path, full_model_path, format_type):
        """启动一个转录任务（既用于单文件，也用于批量中的单个文件）"""
        # 在UI上同步显示当前处理的文件
        self.ui.textEdit.setText(path)
        self.ui.textEdit.moveCursor(QTextCursor.MoveOperation.End)

        # 标记文件状态为"处理中"（无论是单文件还是批量模式）
        self._mark_file_status(path, '处理中')

        # 批量模式下的额外处理
        if getattr(self, 'is_batch_running', False):
            self.current_batch_file = path
            # self._mark_file_status(path, '处理中')
            if self.batch_dialog and self.batch_dialog.isVisible():
                self.batch_dialog.populate(self.batch_files, self.batch_base_dir)
        else:
            # 单文件模式下也需要更新批量文件列表窗口（如果文件在批量列表中）
            if self.batch_dialog and self.batch_dialog.isVisible():
                self.batch_dialog.populate(self.batch_files, self.batch_base_dir)

        # 创建转录器和工作线程
        self.transcriber = Transcriber(
            model_path=full_model_path,
            debug_mode=self.ui.yesDebug.isChecked(),
            log_file_path=self.log_file_path,
            export_format=format_type,
            convert_to_simple=self.ui.yesSimple.isChecked()
        )
        self.worker_thread = QThread()
        self.transcriber.moveToThread(self.worker_thread)

        # 连接信号槽
        self.transcriber.log_signal.connect(self.ui.textEdit_2.append)
        self.transcriber.progress_signal.connect(self.ui.progressBar.setValue)
        self.transcriber.transcription_started.connect(self.start_progress_simulation)
        self.transcriber.audio_duration_signal.connect(self.set_audio_duration)
        self.transcriber.transcription_finished.connect(self.stop_all_timers)
        # 文件格式错误：批量模式下标记失败，不中断队列
        #self.transcriber.invalid_file_format_signal.connect(lambda: self._mark_file_status(path, '失败'))
        self.transcriber.invalid_file_format_signal.connect(self.handle_invalid_file_format)

        # 单文件才在完成时立即启用按钮；批量在全部完成后启用
        if not getattr(self, 'is_batch_running', False):
            self.transcriber.transcription_finished.connect(lambda: self.ui.pushButton_2.setEnabled(True))

        # 线程启动时调用transcribe方法
        self.worker_thread.started.connect(
            lambda: QMetaObject.invokeMethod(
                self.transcriber,
                "transcribe",
                Qt.QueuedConnection,
                Q_ARG(str, path)
            )
        )
        # 进度到100时的处理（线程退出等）
        self.transcriber.progress_signal.connect(self.check_finish)

        # 线程清理与批量串联
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(lambda: setattr(self, 'transcriber', None))
        self.worker_thread.finished.connect(self._on_worker_finished)

        # 启动线程
        self.worker_thread.start()

        # 禁用开始按钮防止重复点击
        self.ui.pushButton_2.setEnabled(False)

    def _on_worker_finished(self):
        """一个任务完成后：批量模式下串联下一个或收尾（动态）"""
        if not getattr(self, 'is_batch_running', False):
            return

        # 若之前因格式错误标记为失败则保持失败；否则标记为已完成
        current = getattr(self, 'current_batch_file', None)
        if current:
            status = None
            for f in self.batch_files:
                if f['path'] == current:
                    status = f.get('status')
                    break
            if status != '失败':
                self._mark_file_status(current, '已完成')

        # 刷新详情窗口
        if self.batch_dialog and self.batch_dialog.isVisible():
            self.batch_dialog.populate(self.batch_files, self.batch_base_dir)

        # 动态选择下一条未处理的选中项
        self._start_next_pending()
        # if not getattr(self, 'is_batch_running', False):
        #     return
        #
        # # 若之前因格式错误等标记为失败，则保持失败；否则标记为已完成
        # status = None
        # for f in self.batch_files:
        #     if f['path'] == getattr(self, 'current_batch_file', None):
        #         status = f.get('status')
        #         break
        # if status != '失败':
        #     self._mark_file_status(self.current_batch_file, '已完成')
        #
        # # 从当前队列中移除
        # if self.batch_queue and self.batch_queue[0]['path'] == self.current_batch_file:
        #     self._mark_file_status(self.current_batch_file, '已完成')
        #     self.batch_queue.pop(0)
        #
        # # 刷新详情窗口
        # if self.batch_dialog and self.batch_dialog.isVisible():
        #     self.batch_dialog.populate(self.batch_files, self.batch_base_dir)
        #
        # # 继续下一个或结束批量
        # if self.batch_queue:
        #     next_path = self.batch_queue[0]['path']
        #     self._start_one_file(next_path, self._batch_full_model_path, self._batch_format_type)
        # else:
        #     self.is_batch_running = False
        #     self.ui.pushButton_2.setEnabled(True)
        #     logger_manager.info("🎉 批量处理完成", "main", show_in_ui=True)

    def _start_next_pending(self):
        """启动下一条待处理任务，否则收尾, """
        next_item = self._get_next_pending_file()
        if next_item:
            self._start_one_file(next_item['path'], self._batch_full_model_path, self._batch_format_type)
        else:
            # 没有待处理项，批量完成
            self.is_batch_running = False
            self.ui.pushButton_2.setEnabled(True)
            self.on_all_tasks_completed(batch_mode=True)

    def _get_next_pending_file(self):
        """返回下一条待处理（selected=True 且 status=未处理）的文件字典,
        如果要把“新增的文件优先立即处理”（插队），
        可以把这里的遍历顺序改为把新增项插到列表前面, 当前实现默认保持原列表顺序。
        """
        for f in self.batch_files:
            if f.get('selected') and f.get('status') in ('未处理', '', None):
                return f
        return None

    def _mark_file_status(self, path, status):
        """更新批量文件状态"""
        for f in self.batch_files:
            if f['path'] == path:
                f['status'] = status
                break

    def set_audio_duration(self, duration):
        """设置音频时长并计算进度间隔"""
        self.audio_duration = duration
        # 计算每1%需要的时间（秒）
        time_per_percent = duration / 100
        # 转换为毫秒
        self.progress_interval = int(time_per_percent * 1000)
        logger_manager.debug(f"📊 音频时长: {duration:.2f}秒，每1%进度需要: {time_per_percent:.2f}秒")
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
            # 批量运行时不在此处启用按钮，收尾由 _start_next_pending 控制
            if not getattr(self, 'is_batch_running', False):
                self.ui.pushButton_2.setEnabled(True)
            # 安全地退出线程
            if self.worker_thread and self.worker_thread.isRunning():
                self.worker_thread.quit()
                self.worker_thread.wait()

            # 单文件完成后弹窗并清理
            if not getattr(self, 'is_batch_running', False):
                self.on_all_tasks_completed(batch_mode=False)

    def on_all_tasks_completed(self, batch_mode=False):
        """所有任务完成后的统一弹窗与清理"""
        # 若选中“完成后关机”，则弹出倒计时弹窗；否则弹原来的完成提示
        if hasattr(self.ui, "radioShutdown") and self.ui.radioShutdown.isChecked():
            # 默认5分钟，可按需调整或做成设置项
            self.show_shutdown_countdown(minutes=5)
        else:
            from utils import show_info
            show_info(self, "提示", "字幕已经生成完毕")

        # 清空路径输入框
        self.ui.textEdit.clear()
        self.update_textEdit_tip()
        # 若是批量，清空内存列表并刷新统计与详情窗口
        if batch_mode:
            self.batch_files.clear()
            self.update_selected_summary()
            if self.batch_dialog and self.batch_dialog.isVisible():
                self.batch_dialog.populate(self.batch_files, self.batch_base_dir)

    def _format_shutdown_text(self, remaining_secs: int) -> str:
        """格式化倒计时文案"""
        m = remaining_secs // 60
        s = remaining_secs % 60
        return f"字幕已经生成完毕，电脑将在 {m} 分 {s} 秒后关机"

    def show_shutdown_countdown(self, minutes: int = 5):
        """显示关机倒计时弹窗（仅取消按钮），可动态更新剩余时间"""
        from PySide6.QtWidgets import QMessageBox
        # 持有引用，避免被GC
        self.shutdown_remaining_secs = int(minutes * 60)

        # 创建消息框（只保留取消按钮）
        self.shutdown_msg_box = QMessageBox(self)
        self.shutdown_msg_box.setWindowTitle("提示")
        self.shutdown_msg_box.setIcon(QMessageBox.Icon.Warning)
        self.shutdown_msg_box.setStyleSheet("""
        QMessageBox {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #667eea, stop:1 #764ba2);
            border-radius: 5px;
            color: white;
        }
        QMessageBox QLabel {
            color: white;
            font-size: 14px;
            padding: 10px;
        }
        QMessageBox QPushButton {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 80), stop:1 rgba(255, 255, 255, 60));
            border: 1px solid rgba(255, 255, 255, 100);
            border-radius: 5px;
            color: white;
            font-weight: bold;
            padding: 8px 16px;
            min-width: 80px;
        }
        QMessageBox QPushButton:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 100), stop:1 rgba(255, 255, 255, 80));
            border: 1px solid rgba(255, 255, 255, 150);
        }
        QMessageBox QPushButton:pressed {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 60), stop:1 rgba(255, 255, 255, 40));
        }
    """)

        self.shutdown_msg_box.setText(self._format_shutdown_text(self.shutdown_remaining_secs))
        self.shutdown_msg_box.setStandardButtons(QMessageBox.StandardButton.Cancel)
        # 置顶显示
        self.shutdown_msg_box.setWindowFlags(self.shutdown_msg_box.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)
        # 将“Cancel”按钮文本改为“取消”
        cancel_btn = self.shutdown_msg_box.button(QMessageBox.StandardButton.Cancel)
        if cancel_btn:
            cancel_btn.setText("取消")
            cancel_btn.clicked.connect(self.cancel_shutdown_countdown)

        # 启动每秒更新的定时器
        self.shutdown_timer = QTimer(self)
        self.shutdown_timer.setInterval(1000)
        self.shutdown_timer.timeout.connect(self._tick_shutdown_countdown)
        self.shutdown_timer.start()

        # 使用非阻塞的show，以便计时器正常触发
        self.shutdown_msg_box.show()

    def _tick_shutdown_countdown(self):
        """倒计时每秒回调，更新弹窗文本，时间到则执行关机"""
        if not hasattr(self, "shutdown_remaining_secs"):
            return
        self.shutdown_remaining_secs -= 1
        if self.shutdown_remaining_secs <= 0:
            # 停止定时器并关闭弹窗，执行关机
            if hasattr(self, "shutdown_timer") and self.shutdown_timer:
                self.shutdown_timer.stop()
            if hasattr(self, "shutdown_msg_box") and self.shutdown_msg_box:
                try:
                    self.shutdown_msg_box.close()
                except Exception:
                    pass
            self.execute_shutdown()
        else:
            if hasattr(self, "shutdown_msg_box") and self.shutdown_msg_box:
                try:
                    self.shutdown_msg_box.setText(self._format_shutdown_text(self.shutdown_remaining_secs))
                except Exception:
                    pass

    def cancel_shutdown_countdown(self):
        """用户点击取消，停止倒计时并关闭弹窗"""
        if hasattr(self, "shutdown_timer") and self.shutdown_timer:
            try:
                self.shutdown_timer.stop()
            except Exception:
                pass
        if hasattr(self, "shutdown_msg_box") and self.shutdown_msg_box:
            try:
                self.shutdown_msg_box.close()
            except Exception:
                pass
        # 清理状态
        self.shutdown_msg_box = None
        self.shutdown_remaining_secs = 0

    def execute_shutdown(self):
        """执行关机指令（Windows）"""
        try:
            import subprocess
            # 立即关机；如需显示系统自带倒计时，也可改为 /t 300 并结合 /a 取消
            subprocess.run(["shutdown", "/s", "/t", "0"], check=False)
        except Exception as e:
            from utils import show_error
            show_error(self, "错误", f"关机失败: {e}")

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

    # def write_debug_log(self, message, show_in_ui=False):
    #     """写入调试日志到文件
    #
    #     Args:
    #         message (str): 要写入的日志消息
    #         show_in_ui (bool): 是否同时在UI中显示消息
    #     """
    #     logger_manager.debug(message, "main", show_in_ui)
    def send_working_message(self):
        """在主线程中发送工作提示消息"""
        current_time = datetime.now().strftime("%Y年%m月%d日%H:%M:%S")
        tmp_str = " 正在努力转换中，请稍候..."
        if self.sim_progress >= 90:
            tmp_str = f"并没有死机卡机, 还在努力转换, 请稍候...{random.randint(10000000, 99999999)}"
        str_temp = f"🕐 {current_time}  {tmp_str}"

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
                logger_manager.info(message, "main", show_in_ui=True)
               

        elif self.sim_progress < 90:
            # 85%-90%：缓慢增长
            self.sim_progress += 0.2
            progress_value = int(self.sim_progress)
            self.ui.progressBar.setValue(progress_value)

    def handle_invalid_file_format(self):
        """处理文件格式错误，将焦点设置到textEdit并提示用户重新选择"""
        # 将焦点设置到文件路径输入框
        if getattr(self, 'is_batch_running', False):
            # 批量：标记失败，停止定时器，不提前启用按钮，也不抢焦点
            current = getattr(self, 'current_batch_file', None)
            if current:
                self._mark_file_status(current, '失败')
            self.stop_all_timers()
        else:
            # 单文件：提示并恢复按钮
            self.ui.textEdit.setFocus()
            self.ui.textEdit.selectAll()
            self.ui.pushButton_2.setEnabled(True)
            self.stop_all_timers()
    def stop_all_timers(self):
        """停止所有定时器"""
        self.progress_timer.stop()
        self.working_timer.stop()
        # print("[DEBUG] All timers stopped")

    def setup_drag_drop_events(self):
        """设置拖放事件处理"""
        # 支持的音视频文件扩展名
        self.supported_extensions = {
            '.mp4', '.mov', '.mkv', '.avi', '.flv',  # 视频格式
            '.wav', '.mp3', '.ogg', '.flac'  # 音频格式
        }

        # 重写拖放事件
        self.ui.textEdit.dragEnterEvent = self.textEdit_dragEnterEvent
        self.ui.textEdit.dragMoveEvent = self.textEdit_dragMoveEvent
        self.ui.textEdit.dropEvent = self.textEdit_dropEvent

    def textEdit_dragEnterEvent(self, event):
        """textEdit拖拽进入事件"""
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if len(urls) == 1:  # 只允许拖拽一个文件
                file_path = urls[0].toLocalFile()
                if self.is_supported_file(file_path):
                    event.acceptProposedAction()
                    return
        event.ignore()

    def textEdit_dragMoveEvent(self, event):
        """textEdit拖拽移动事件"""
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if len(urls) == 1:
                file_path = urls[0].toLocalFile()
                if self.is_supported_file(file_path):
                    event.acceptProposedAction()
                    return
        event.ignore()

    def textEdit_dropEvent(self, event):
        """textEdit拖拽放下事件"""
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if len(urls) == 1:
                file_path = urls[0].toLocalFile()
                if self.is_supported_file(file_path) and os.path.exists(file_path):
                    self.ui.textEdit.setText(file_path)
                    self.ui.textEdit.moveCursor(QTextCursor.MoveOperation.End)

                    # 保存目录设置
                    self.settings.setValue("last_directory", os.path.dirname(file_path))
                    # 更新提示
                    self.update_textEdit_tip()
                    # 记录日志
                    logger_manager.info(f"通过拖放选择文件: {file_path}", "main")

                    event.acceptProposedAction()
                    return
        event.ignore()

    def is_supported_file(self, file_path):
        """检查文件是否为支持的音视频格式"""
        if not file_path:
            return False
        file_ext = os.path.splitext(file_path)[1].lower()
        return file_ext in self.supported_extensions


# def show_main_window(trial_mode=False):
#     """显示主窗口"""
#     main_window = MainWindow(trial_mode=trial_mode)
#
#     if trial_mode:
#         main_window.setWindowTitle(f"字幕生成器 (试用) {VERSION}")
#     else:
#         main_window.setWindowTitle(f"字幕生成器 {VERSION}")
#
#     main_window.show()
#     return main_window
def show_main_window(trial_mode=False):
    """显示主窗口"""
    global main_window_instance, instance_manager
    main_window = MainWindow(trial_mode=trial_mode)

    if trial_mode:
        main_window.setWindowTitle(f"字幕生成器 (试用) {VERSION}")
    else:
        main_window.setWindowTitle(f"字幕生成器 {VERSION}")

    main_window.show()

    # 保存全局引用
    main_window_instance = main_window

    # 设置到SingleInstanceManager中
    if instance_manager:
        instance_manager.set_main_window(main_window)

    return main_window

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

    # 添加这行：声明全局变量
    # global instance_manager

    # 创建单实例管理器
    instance_manager = SingleInstanceManager("字幕生成器")

    # 检查是否已有实例在运行
    if instance_manager.is_running():
        logger_manager.info("应用程序已运行，发送激活信号", "main")
        sys.exit(0)

    logger_manager.info("应用程序开始启动", "main")

    # 启动单实例服务器
    if not instance_manager.start_server():
        logger_manager.error("无法启动单实例服务", "main")
        sys.exit(1)

    # 连接信号
    instance_manager.show_window_signal.connect(activate_main_window)

    try:
        # 启动SplashScreen
        splash = SplashScreen()
        splash.show()

        # 进入事件循环
        sys.exit(app.exec())
    except Exception as e:
        import traceback
        logger_manager.error(f"应用程序启动失败: {e}", "main")
        logger_manager.error(f"堆栈跟踪: {traceback.format_exc()}", "main")
        sys.exit(1)

