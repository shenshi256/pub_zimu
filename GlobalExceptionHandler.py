#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Time    : 2025/7/2 9:00
# @Author  : WXY
# @File    : GlobalExceptionHandler
# @PROJECT_NAME: whisper_gui
# @PRODUCT_NAME: PyCharm
# -------------------------------------------------------------------------------
import sys
import traceback
from datetime import datetime
from PySide6.QtWidgets import QApplication, QMessageBox
from LoggerManager import logger_manager

class GlobalExceptionHandler:
    """
    全局异常处理器类
    """

    def __init__(self):
        self.crash_count = 0
        self.max_crashes = 5  # 最大崩溃次数

    def handle_exception(self, exc_type, exc_value, exc_traceback):
        """
        处理未捕获的异常
        """
        # 如果是KeyboardInterrupt，正常退出
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return

        self.crash_count += 1

        # 格式化异常信息
        error_msg = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 记录详细的崩溃信息
        crash_info = f"""
                        === 程序崩溃报告 ===
                        时间: {timestamp}
                        崩溃次数: {self.crash_count}
                        异常类型: {exc_type.__name__}
                        异常信息: {str(exc_value)}
                        详细堆栈:
                        {error_msg}
                        ========================
                        """

        # 记录到日志
        try:
            logger_manager.critical(crash_info, "global_exception")
        except:
            # 备用日志记录
            try:
                with open("crash_log.txt", "a", encoding="utf-8") as f:
                    f.write(crash_info)
            except:
                pass

        # 如果崩溃次数过多，强制退出
        if self.crash_count >= self.max_crashes:
            try:
                logger_manager.critical(f"程序连续崩溃{self.crash_count}次，强制退出", "global_exception")
            except:
                pass
            sys.exit(1)

        # 显示错误对话框
        self.show_error_dialog(error_msg, self.crash_count)

    def show_error_dialog(self, error_msg, crash_count):
        """
        显示错误对话框
        """
        try:
            app = QApplication.instance()
            if app is not None:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Icon.Critical)
                msg_box.setWindowTitle("程序异常")
                msg_box.setText(f"程序遇到未处理的错误（第{crash_count}次）")
                msg_box.setDetailedText(error_msg)

                if crash_count >= 3:
                    msg_box.setInformativeText("程序多次出现异常，建议立即重启程序！")
                else:
                    msg_box.setInformativeText("错误已记录到日志文件。程序将尝试继续运行。")

                msg_box.exec()
        except Exception as e:
            print(f"无法显示错误对话框: {e}")
            print(f"原始错误: {error_msg}")


# 创建全局异常处理器实例
exception_handler = GlobalExceptionHandler()