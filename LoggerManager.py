#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Time    : 2025/6/26 21:30
# @Author  : WXY
# @File    : LoggerManager
# @PROJECT_NAME: whisper_gui
# @PRODUCT_NAME: PyCharm
# -------------------------------------------------------------------------------
import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler
from PySide6.QtWidgets import QTextEdit
from PySide6.QtCore import QObject, Signal, QTimer
import threading


class LoggerManager(QObject):
    _instance = None
    _logger = None
    _ui_text_edit = None

    # 信号
    ui_update_signal = Signal(str)  # 单条消息更新
    batch_update_signal = Signal(list)  # 批量消息更新

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LoggerManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            super().__init__()
            self._initialized = True

            # 批量更新相关
            self._pending_messages = []
            self._batch_timer = QTimer()
            self._batch_timer.setSingleShot(True)
            self._batch_timer.timeout.connect(self._flush_pending_messages)
            self._batch_delay = 300  # 300ms防抖延迟
            self._message_lock = threading.Lock()

        if self._logger is None:
            self._setup_logger()
        self._main_thread_id = threading.get_ident()

    def _is_main_thread(self):
        """检查当前是否在主线程"""
        return threading.get_ident() == self._main_thread_id

    def _flush_pending_messages(self):
        """清空待处理消息并批量更新UI"""
        with self._message_lock:
            if self._pending_messages:
                messages = self._pending_messages.copy()
                self._pending_messages.clear()
                self.batch_update_signal.emit(messages)

    def _setup_logger(self):
        """设置日志器"""
        self._logger = logging.getLogger('whisper_gui')
        self._logger.setLevel(logging.DEBUG)

        # 避免重复添加处理器
        if self._logger.handlers:
            return

        # 创建格式器
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # 控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        self._logger.addHandler(console_handler)

    def set_ui_text_edit(self, text_edit: QTextEdit):
        """设置UI文本框引用，用于向界面输出日志"""
        self._ui_text_edit = text_edit

    def setup_file_logging(self, log_file_path: str = None, enable_debug: bool = True):
        """设置文件日志（兼容原有的调试模式）"""
        if not enable_debug:
            return

        try:
            if not log_file_path:
                # 如果没有指定路径，使用默认路径
                today = datetime.now().strftime("%Y%m%d")
                log_file_path = os.path.join(os.getcwd(), f"{today}_log.log")

            # 移除旧的文件处理器
            for handler in self._logger.handlers[:]:
                if isinstance(handler, (logging.FileHandler, RotatingFileHandler)):
                    self._logger.removeHandler(handler)

            # 创建新的文件处理器
            formatter = logging.Formatter(
                '[%(asctime)s] %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )

            file_handler = RotatingFileHandler(
                log_file_path,
                maxBytes=10 * 1024 * 1024,  # 10MB
                backupCount=5,
                encoding='utf-8'
            )
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)
            self._logger.addHandler(file_handler)

            # 写入会话开始标记
            with open(log_file_path, 'a', encoding='utf-8') as f:
                f.write(f"\n=== 新的转录会话开始 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n")

            self.info(f"调试模式已开启，日志将保存到: {log_file_path}", "logger")

        except Exception as e:
            self.error(f"文件日志设置失败: {e}", "logger")

    def log(self, level: str, message: str, module_name: str = None, show_in_ui: bool = False):
        """通用日志方法"""
        logger = self._logger
        if module_name:
            logger = logging.getLogger(f'whisper_gui.{module_name}')

        # 输出到日志系统
        getattr(logger, level.lower())(message)

        # UI更新策略
        if show_in_ui and self._ui_text_edit:
            if self._is_main_thread():
                # 主线程直接更新
                self._ui_text_edit.append(message)
            else:
                # 子线程使用信号更新（改为直接发射单条消息信号）
                self.ui_update_signal.emit(message)
                # # 子线程使用智能批量更新
                # with self._message_lock:
                #     self._pending_messages.append(message)
                #
                # # 重启防抖定时器
                # self._batch_timer.start(self._batch_delay)

    def debug(self, message: str, module_name: str = None, show_in_ui: bool = False):
        """调试日志"""
        self.log('debug', message, module_name, show_in_ui)

    def info(self, message: str, module_name: str = None, show_in_ui: bool = False):
        """信息日志"""
        self.log('info', message, module_name, show_in_ui)

    def warning(self, message: str, module_name: str = None, show_in_ui: bool = False):
        """警告日志"""
        self.log('warning', message, module_name, show_in_ui)

    def error(self, message: str, module_name: str = None, show_in_ui: bool = False):
        """错误日志"""
        self.log('error', message, module_name, show_in_ui)

    def critical(self, message: str, module_name: str = None, show_in_ui: bool = False):
        """严重错误日志"""
        self.log('critical', message, module_name, show_in_ui)

    def ui_message(self, message: str, also_log: bool = True, log_level: str = 'info', module_name: str = None):
        """专门用于UI消息的方法（兼容原有的UI输出需求）"""
        # 输出到UI
        if self._ui_text_edit:
            self._ui_text_edit.append(message)

        # 可选择性地记录到日志
        if also_log:
            self.log(log_level, message, module_name)


# 创建全局日志管理器实例
logger_manager = LoggerManager()