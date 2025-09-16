#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Time    : 2025/7/1 14:09
# @Author  : WXY
# @File    : SingleInstanceManager
# @PROJECT_NAME: whisper_gui
# @PRODUCT_NAME: PyCharm
# -------------------------------------------------------------------------------

import sys
import os
import socket
import tempfile
from PySide6.QtCore import QObject, Signal, Qt
from PySide6.QtNetwork import QLocalServer, QLocalSocket
from PySide6.QtWidgets import QApplication


class SingleInstanceManager(QObject):
    """单实例管理器"""
    show_window_signal = Signal()

    def __init__(self, app_name="WhisperGUI"):
        super().__init__()
        self.app_name = app_name
        self.server = None
        self.socket = None
        self.main_window_instance = None  # ✅ 添加主窗口实例引用

    def set_main_window(self, main_window):
        """设置主窗口实例"""
        self.main_window_instance = main_window

    def activate_main_window(self):
        """激活主窗口"""
        if self.main_window_instance is not None:
            try:
                self.main_window_instance.show()
                self.main_window_instance.activateWindow()
                self.main_window_instance.setWindowState(
                    self.main_window_instance.windowState() & ~Qt.WindowState.WindowMinimized | Qt.WindowState.WindowActive)
                self.main_window_instance.raise_()
                return True
            except Exception:
                return False
        return False
    def is_running(self):
        """检查应用程序是否已经在运行"""
        # 尝试连接到现有实例
        self.socket = QLocalSocket()
        self.socket.connectToServer(self.app_name)

        if self.socket.waitForConnected(1000):
            # 如果连接成功，说明已有实例在运行
            # 发送激活信号给现有实例
            self.socket.write(b"ACTIVATE")
            self.socket.waitForBytesWritten(1000)
            self.socket.disconnectFromServer()
            return True

        return False

    def start_server(self):
        """启动服务器监听新实例的连接"""
        # 清理可能存在的旧服务器
        QLocalServer.removeServer(self.app_name)

        self.server = QLocalServer()
        self.server.newConnection.connect(self._handle_new_connection)

        if not self.server.listen(self.app_name):
            print(f"无法启动单实例服务器: {self.server.errorString()}")
            return False

        return True

    def _handle_new_connection(self):
        """处理新的连接请求"""
        client_socket = self.server.nextPendingConnection()
        if client_socket:
            client_socket.readyRead.connect(lambda: self._handle_client_data(client_socket))

    # def _handle_client_data(self, client_socket):
    #     """处理客户端数据"""
    #     data = client_socket.readAll().data()
    #     if data == b"ACTIVATE":
    #         # 发出显示窗口信号
    #         self.show_window_signal.emit()

    #     client_socket.disconnectFromHost()

    def _handle_client_data(self, client_socket):
        """处理客户端数据"""
        try:
            data = client_socket.readAll().data()
            if data == b"ACTIVATE":
                # 发出显示窗口信号
                self.show_window_signal.emit()
        except Exception as e:
            print(f"处理客户端数据时出错: {e}")
        finally:
            # 确保连接被正确关闭
            if client_socket.state() != QLocalSocket.UnconnectedState:
                client_socket.disconnectFromServer()

    def cleanup(self):
        """清理资源"""
        if self.server:
            self.server.close()
            QLocalServer.removeServer(self.app_name)