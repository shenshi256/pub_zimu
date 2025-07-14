#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Time    : 2025/7/8 16:05
# @Author  : WXY
# @File    : SplashScreen
# @PROJECT_NAME: whisper_gui
# @PRODUCT_NAME: PyCharm
# -------------------------------------------------------------------------------

import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QTimer, QThread, Signal, Qt
from ui_splashscreen import Ui_SplashScreen
from utils import   setup_label_icon, VERSION
from auth_window import AuthWindow
from settings_manager import settings_manager
from AESEncrypt import aes_decrypt
from datetime import datetime, timedelta


class ModelLoadWorker(QThread):
    """模型加载工作线程"""
    progress_updated = Signal(int)
    finished = Signal()

    def run(self):
        """模拟模型加载过程"""
        # 模拟加载过程，分多个阶段
        stages = [
            ("初始化环境", 20),
            ("加载配置文件", 40),
            ("准备模型资源", 60),
            ("加载AI模型", 80),
            ("完成初始化", 100)
        ]

        for stage_name, progress in stages:
            # 模拟每个阶段的加载时间
            self.msleep(500)  # 等待500毫秒
            self.progress_updated.emit(progress)

        self.finished.emit()


class SplashScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # 设置窗口属性以支持圆角和透明背景
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.Tool)
        #self.setAttribute(Qt.WA_TranslucentBackground)

        # 初始化UI
        self.init_ui()

        # 初始化模型加载线程
        self.model_worker = ModelLoadWorker()
        self.model_worker.progress_updated.connect(self.update_progress)
        self.model_worker.finished.connect(self.on_loading_finished)

        # 授权检查完成标志
        self.auth_ready = False
        self.model_ready = False
        self.next_window_shown = False  # 防止重复调用标志位, 重复调用就会重复显示2个main窗口
        # 启动加载过程
        self.start_loading()

    def show_main_window(self):
        """显示主窗口"""
        # 延迟导入，避免循环导入
        from main import show_main_window
        self.main_window = show_main_window()

    def init_ui(self):
        """初始化UI界面"""
        # 设置窗口图标 , 不用设置了, 因为把标题栏隐藏了
        #setup_window_icon(self)
        self.ui.versionLabel.setText(VERSION)
        # 设置logoLabel的图标
        setup_label_icon(self.ui.logoLabel)

        # 连接关闭按钮事件
        # self.ui.closeButton.clicked.connect(self.close_application)
        # 为QLabel添加鼠标点击事件（替换原来的clicked.connect）
        self.ui.closeButton.mousePressEvent = lambda  event: self.close_application() if event.button() == Qt.LeftButton else None
        # 初始化进度条
        self.ui.progressBar.setValue(0)

        # 设置初始状态文本（如果有statusLabel的话）
        # self.ui.statusLabel.setText("正在初始化...")

    def close_application(self):
        """关闭整个应用程序"""
        # 如果还在加载过程中，终止加载线程
        if self.model_worker.isRunning():
            self.model_worker.terminate()
            self.model_worker.wait()

        # 退出应用程序
        QApplication.quit()

    def start_loading(self):
        """开始加载过程"""
        # 同时启动授权检查和模型加载
        self.check_authorization()
        self.model_worker.start()

    def check_authorization(self):
        """检查授权状态"""
        # 获取授权信息
        machine_code, auth_time, last_auth_code = settings_manager.get_auth_info()

        # 检查授权信息完整性
        if not machine_code or not auth_time or not last_auth_code:
            self.auth_ready = True  # 需要显示授权窗口
            self.check_ready_state()
            return

        try:
            # 第一次解密
            auth_code_one_de = aes_decrypt(last_auth_code)
            if auth_code_one_de is None:
                raise ValueError("第一次解密失败")

            # 检查分隔后的元素数量
            auth_parts = auth_code_one_de.split("|")
            if len(auth_parts) != 2:
                raise ValueError("授权码格式错误")

            auth_code_en = auth_parts[0]
            temp_time = auth_parts[1]

            # 第二次解密
            auth_code = aes_decrypt(auth_code_en)
            if auth_code is None:
                raise ValueError("第二次解密失败")

            # 解析内层授权码
            auth_code_parts = auth_code.split("|")
            if len(auth_code_parts) != 2:
                raise ValueError("内层授权码格式错误")

            auth_code_machine = auth_code_parts[0]
            auth_code_day = auth_code_parts[1]

            # 验证机器码
            current_machine_code = AuthWindow.generate_machine_code_static()
            if current_machine_code and auth_code_machine.replace('-', '') != current_machine_code.replace('-', ''):
                raise ValueError("机器码不匹配")

            # 检查授权天数
            auth_days = int(auth_code_day)

            if auth_days == 0:
                # 无限制授权
                self.auth_ready = True
                self.check_ready_state()
                return

            # 检查授权是否过期
            auth_datetime = datetime.strptime(temp_time, "%Y-%m-%d %H:%M:%S")
            expire_datetime = auth_datetime + timedelta(days=auth_days)
            current_datetime = datetime.now()

            if current_datetime < auth_datetime or current_datetime > expire_datetime:
                raise ValueError("授权已过期或时间异常")

            # 授权有效
            self.auth_ready = True
            self.check_ready_state()

        except Exception as e:
            print(f"授权检查失败: {e}")
            self.auth_ready = True  # 需要显示授权窗口
            self.check_ready_state()

    def update_progress(self, value):
        """更新进度条"""
        self.ui.progressBar.setValue(value)

    def on_loading_finished(self):
        """模型加载完成"""
        self.model_ready = True
        self.check_ready_state()

    def check_ready_state(self):
        """检查是否所有准备工作都完成"""
        if self.auth_ready and self.model_ready and not self.next_window_shown:
            self.next_window_shown = True  # 设置标志位
            # 延迟一点时间让用户看到100%的进度
            QTimer.singleShot(500, self.show_next_window)

    def show_next_window(self):
        """显示下一个窗口"""
        # 如果授权信息不完整或验证失败，显示授权窗口
        if not self.is_auth_valid():
            self.show_auth_window()
            # 注意：授权窗口显示后不要关闭启动界面，等授权成功后再处理
        else:
            # 授权有效，直接显示主窗口
            self.show_main_window()
            # 关闭启动界面
            self.close()

    def is_auth_valid(self):
        """检查授权是否有效"""
        try:
            machine_code, auth_time, last_auth_code = settings_manager.get_auth_info()

            if not machine_code or not auth_time or not last_auth_code:
                return False

            # 重复授权验证逻辑（简化版）
            auth_code_one_de = aes_decrypt(last_auth_code)
            if not auth_code_one_de:
                return False

            auth_parts = auth_code_one_de.split("|")
            if len(auth_parts) != 2:
                return False

            auth_code = aes_decrypt(auth_parts[0])
            if not auth_code:
                return False

            auth_code_parts = auth_code.split("|")
            if len(auth_code_parts) != 2:
                return False

            # 验证机器码
            current_machine_code = AuthWindow.generate_machine_code_static()
            if auth_code_parts[0].replace('-', '') != current_machine_code.replace('-', ''):
                return False

            # 检查授权天数
            auth_days = int(auth_code_parts[1])
            if auth_days == 0:
                return True  # 无限制授权

            # 检查是否过期
            auth_datetime = datetime.strptime(auth_parts[1], "%Y-%m-%d %H:%M:%S")
            expire_datetime = auth_datetime + timedelta(days=auth_days)
            current_datetime = datetime.now()

            return auth_datetime <= current_datetime <= expire_datetime

        except Exception:
            return False

    def show_auth_window(self):
        """显示授权窗口"""
        self.auth_window = AuthWindow()
        self.auth_window.auth_success.connect(self.on_auth_success)
        self.auth_window.show()
        # 授权窗口显示后关闭启动界面
        self.close()


    def on_auth_success(self):
        """授权成功回调"""
        self.auth_window.close()
        # 授权成功后显示主窗口
        self.show_main_window()
        # 关闭启动界面
        self.close()


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        splash = SplashScreen()
        splash.show()
        sys.exit(app.exec())
    except Exception as e:
        import traceback
        print(f"错误详情: {e}")
        print(f"堆栈跟踪: {traceback.format_exc()}")
        input("按回车键退出...")  # 防止窗口立即关闭

    # # 确保必要的初始化
    # import os
    #
    # # 确保工作目录正确
    # if not os.path.exists('model'):
    #     os.makedirs('model', exist_ok=True)
    #
    # app = QApplication(sys.argv)
    #
    # # 设置应用程序属性
    # app.setApplicationName("字幕生成器")
    # app.setApplicationVersion("1.0")
    #
    # try:
    #     splash = SplashScreen()
    #     splash.show()
    #     sys.exit(app.exec())
    # except Exception as e:
    #     print(f"启动失败: {e}")
    #     sys.exit(1)