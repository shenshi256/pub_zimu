#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Time    : 2025/7/2 21:39
# @Author  : WXY
# @File    : SystemMonitorWorker
# @PROJECT_NAME: whisper_gui
# @PRODUCT_NAME: PyCharm
# -------------------------------------------------------------------------------
from PySide6.QtCore import QThread,Signal
from utils import get_system_monitor_info


class SystemMonitorWorker(QThread):
    monitor_updated = Signal(dict)

    def __init__(self):
        super().__init__()
        self.running = True

    def run(self):
        while self.running:
            try:
                monitor_info = get_system_monitor_info()
                self.monitor_updated.emit(monitor_info)
            except Exception as e:
                self.monitor_updated.emit({'error': str(e)})

            # 使用线程安全的等待
            self.msleep(5000)  # 等待5秒

    def stop(self):
        self.running = False
        self.quit()
        self.wait()