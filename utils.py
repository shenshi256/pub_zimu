#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Time    : 2025/6/30 13:28
# @Author  : WXY
# @File    : utils.py
# @PROJECT_NAME: whisper_gui
# @PRODUCT_NAME: PyCharm
# -------------------------------------------------------------------------------
from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QIcon
import os
import sys
from PySide6.QtCore import QSize, Qt
from LoggerManager import logger_manager
import psutil
import base64

# 在文件开头添加版本号定义
VERSION = "V1.0.1"
UNKNOWNCPU = "UNKNOWN_CPU"
UNKNOWNMOTHERBOARD = "UNKNOWN_MOTHERBOARD"

# 客服微信图片 , 不能使用base64的图片, 打包工具对长字符串兼容不好, 虽然在debug可以运行, 但是一打包就挂了
# CUSTOMERSERVICE = """data:image/jpeg;base64,iVBORw0KGgoAAAA...ElFTkSuQmCC"""
# 客服微信图片结束
CUSTOMERSERVICE = "customer_service.png"

# 垂直滚动条样式
SCROLLBARSTYLE = """
        QScrollBar:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 30), stop:1 rgba(255, 255, 255, 50));
            width: 12px;
            border-radius: 5px;
            margin: 0px;
        }
        
        QScrollBar::handle:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #667eea, stop:1 #764ba2);
            border-radius: 5px;
            min-height: 30px;
            margin: 2px;
        }
        
        QScrollBar::handle:vertical:hover {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #5a6fd8, stop:1 #6a4190);
        }
        
        QScrollBar::handle:vertical:pressed {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #4e5bc6, stop:1 #5e377e);
        }
        
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            border: none;
            background: none;
            height: 0px;
        }
        
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: none;
        }
        
        QScrollBar:vertical:hover {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 50), stop:1 rgba(255, 255, 255, 70));
        }
        """

def setup_window_icon(window, icon_path="favicon.ico"):
    """为窗口设置图标"""
    icon = QIcon()
    icon_full_path = get_resource_path(icon_path)
    if os.path.exists(icon_full_path):
        icon.addFile(icon_full_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        window.setWindowIcon(icon)
    else:
        logger_manager.warning(f"Warning: Icon file not found: {icon_full_path}")
        #print(f"Warning: Icon file not found: {icon_full_path}")


def get_bundled_resource_path(resource_name):
    """获取打包资源的路径（兼容开发和打包环境）"""
    if getattr(sys, 'frozen', False):
        # 打包后的exe环境
        # base_path = sys._MEIPASS
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    else:
        # 开发环境
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, resource_name)


def setup_ffmpeg():
    """设置 ffmpeg 路径"""
    ffmpeg_path = get_bundled_resource_path('ffmpeg.exe')
    if os.path.exists(ffmpeg_path):
        os.environ["FFMPEG_BINARY"] = ffmpeg_path
        return ffmpeg_path
    return None


# def setup_ffprobe():
#     """设置 ffprobe 路径"""
#     ffprobe_path = get_bundled_resource_path('ffprobe.exe')
#     if os.path.exists(ffprobe_path):
#         return ffprobe_path
#     return None

def get_resource_path(filename):
    """获取资源文件路径，兼容打包后的exe"""
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller 打包后的路径
        return os.path.join(sys._MEIPASS, filename)
    else:
        # 开发环境路径
        return filename


def show_message_with_icon(parent, icon_type, title, message, icon_path="favicon.ico"):
    """显示带图标的消息框"""
    msg_box = QMessageBox(parent)
    # 设置当前的弹窗窗口始终保持在最顶层
    msg_box.setWindowFlags(msg_box.windowFlags() | Qt.WindowStaysOnTopHint)

    # 添加自定义样式
    msg_box.setStyleSheet("""
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

    # 设置窗口图标
    icon_full_path = get_resource_path(icon_path)
    if os.path.exists(icon_full_path):
        msg_box.setWindowIcon(QIcon(icon_full_path))

    msg_box.setIcon(icon_type)
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    return msg_box.exec()


def show_info(parent, title, message, icon_path="favicon.ico"):
    """显示信息提示框"""
    return show_message_with_icon(parent, QMessageBox.Information, title, message, icon_path)


def show_warning(parent, title, message, icon_path="favicon.ico"):
    """显示警告提示框"""
    return show_message_with_icon(parent, QMessageBox.Warning, title, message, icon_path)


def show_error(parent, title, message, icon_path="favicon.ico"):
    """显示错误提示框"""
    return show_message_with_icon(parent, QMessageBox.Critical, title, message, icon_path)


def show_question(parent, title, message, icon_path="favicon.ico"):
    """显示询问对话框"""
    return show_message_with_icon(parent, QMessageBox.Question, title, message, icon_path)


# 添加内存监控函数
def log_memory_usage(stage_name):
    try:
        process = psutil.Process(os.getpid())
        memory_info = process.memory_info()
        system_memory = psutil.virtual_memory()
        logger_manager.info(
            f"📊 [{stage_name}] 进程内存: {memory_info.rss // (1024 * 1024)}MB, "
            f"系统内存使用: {system_memory.percent}%, "
            f"可用: {system_memory.available // (1024 * 1024)}MB",
            "transcriber"
        )
    except Exception as e:
        logger_manager.info(f"📊 [{stage_name}] 无法获取内存信息: {e}", "transcriber")


# 添加 CPU 监控函数
def log_cpu_usage(stage_name):
    try:
        process = psutil.Process(os.getpid())
        # 获取进程 CPU 使用率（需要间隔时间计算）
        process_cpu = process.cpu_percent(interval=0.1)
        # 获取系统整体 CPU 使用率
        system_cpu = psutil.cpu_percent(interval=0.1)
        # 获取 CPU 核心数
        cpu_count = psutil.cpu_count()
        # 获取 CPU 频率信息
        cpu_freq = psutil.cpu_freq()

        freq_info = ""
        if cpu_freq:
            freq_info = f", 频率: {cpu_freq.current:.0f}MHz"

        logger_manager.info(
            f"🖥️ [{stage_name}] 进程CPU: {process_cpu:.1f}%, "
            f"系统CPU: {system_cpu:.1f}%, "
            f"核心数: {cpu_count}{freq_info}",
            "transcriber"
        )
    except Exception as e:
        logger_manager.info(f"🖥️ [{stage_name}] 无法获取CPU信息: {e}", "transcriber")


# 添加综合系统监控函数
def log_system_usage(stage_name):
    """综合监控内存和CPU使用情况"""
    try:
        process = psutil.Process(os.getpid())

        # 内存信息
        memory_info = process.memory_info()
        system_memory = psutil.virtual_memory()

        # CPU信息
        process_cpu = process.cpu_percent(interval=0.1)
        system_cpu = psutil.cpu_percent(interval=0.1)

        logger_manager.info(
            f"📊 [{stage_name}] 进程: 内存{memory_info.rss // (1024 * 1024)}MB, CPU{process_cpu:.1f}% | "
            f"系统: 内存{system_memory.percent:.1f}%, CPU{system_cpu:.1f}%",
            "transcriber"
        )
    except Exception as e:
        logger_manager.info(f"📊 [{stage_name}] 无法获取系统信息: {e}", "transcriber")


# 这个是专门用来给UI线程使用的格式化的内容
def get_system_monitor_info():
    """获取系统监控信息，返回格式化的字典"""
    try:
        process = psutil.Process(os.getpid())

        # 获取进程内存信息
        memory_info = process.memory_info()
        process_memory_mb = memory_info.rss // (1024 * 1024)
        process_memory_gb = process_memory_mb / 1024

        # 获取系统内存信息
        system_memory = psutil.virtual_memory()

        # 获取CPU信息
        process_cpu = process.cpu_percent(interval=0.1)
        system_cpu = psutil.cpu_percent(interval=0.1)

        # 格式化内存显示
        if process_memory_gb >= 1.0:
            memory_text = f"{process_memory_gb:.1f}G"
        else:
            memory_text = f"{process_memory_mb}M"

        return {
            'process_memory_text': memory_text,
            'process_cpu': process_cpu,
            'system_memory_percent': system_memory.percent,
            'system_cpu': system_cpu,
            'process_memory_mb': process_memory_mb,
            'system_memory_available_mb': system_memory.available // (1024 * 1024)
        }
    except Exception as e:
        return {'error': str(e)}


def get_image_base64(image_path=None):
    """将图片转换为base64格式"""
    if image_path is None:
        image_path = CUSTOMERSERVICE
    image_full_path = get_resource_path(image_path)
    try:
        if os.path.exists(image_full_path):
            with open(image_full_path, "rb") as img_file:
                img_data = img_file.read()
                img_base64 = base64.b64encode(img_data).decode('utf-8')
                service_img = f"data:image/jpeg;base64,{img_base64}"
    except Exception as e:
        print(f"加载客服图片失败: {e}")
        service_img = ""
    return service_img

# 时间格式化函数
def format_timestamp(seconds):
    """格式化时间戳为HH:MM:SS,mmm"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"


def setup_label_icon(label, icon_path="favicon.ico"):
    """为QLabel设置图标"""
    from PySide6.QtGui import QPixmap
    icon_full_path = get_resource_path(icon_path)
    if os.path.exists(icon_full_path):
        pixmap = QPixmap(icon_full_path)
        # 根据Label大小调整图片
        if not label.size().isEmpty():
            scaled_pixmap = pixmap.scaled(label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            label.setPixmap(scaled_pixmap)
        else:
            label.setPixmap(pixmap)
    else:
        print(f"Warning: Icon file not found: {icon_full_path}")