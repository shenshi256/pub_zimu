#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Time    : 2025/6/26 9:53
# @Author  : WXY
# @File    : auth_window.py
# @PROJECT_NAME: whisper_gui
# @PRODUCT_NAME: PyCharm
# -------------------------------------------------------------------------------

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Time    : 2025/6/26 9:53
# @Author  : WXY
# @File    : auth_window.py
# @PROJECT_NAME: whisper_gui
# @PRODUCT_NAME: PyCharm
# -------------------------------------------------------------------------------
import hashlib
import platform
import subprocess
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PySide6.QtCore import Signal
from AESEncrypt import aes_decrypt, aes_encrypt
from ui_auth import Ui_Auth
from settings_manager import settings_manager
from datetime import datetime
from LoggerManager import logger_manager
from HelpDialog import HelpDialog
from disclaimers import DisclaimersHelpDialog
from utils import show_info, show_warning, show_error, setup_window_icon, VERSION, UNKNOWNMOTHERBOARD, UNKNOWNCPU


class AuthWindow(QMainWindow):
    # 定义信号，当授权成功时发出
    auth_success = Signal()
    trial_mode_success = Signal()  # 试用模式成功信号
    def __init__(self, clear_registry=True):
        super().__init__()

        # 根据参数决定是否清空注册表中的auth相关信息
        if clear_registry:
            self.clear_auth_registry()

        self.ui = Ui_Auth()
        self.ui.setupUi(self)
        setup_window_icon(self)
        # 添加版本号到标题
        self.setWindowTitle(f"字幕生成器 {VERSION}")
        #
        self.ui.btnHelp.clicked.connect(self.open_disclaimers_dialog)
        # 初始化帮助窗口为None
        self.help_dialog = None
        # 初始化免责声明窗口为None
        self.disclaimers_dialog = None
        # 生成并显示机器码
        self.generate_machine_code()

        # 绑定按钮事件
        self.ui.pushButton.clicked.connect(self.copy_machine_code)
        self.ui.btnOk.clicked.connect(self.authorize)

        # ✅ 添加调试开关的事件绑定和初始化
        self.ui.chkDebug.stateChanged.connect(self.on_debug_changed)
        self.load_debug_setting()

        # 连接试用按钮事件
        self.ui.btnTryUse.clicked.connect(self.start_trial_mode)

        logger_manager.info("授权窗口初始化完成", "auth_window")

    def start_trial_mode(self):
        """启动试用模式"""
        try:
            # 检查试用次数限制
            if not self.check_trial_limit():
                return

            # 记录试用次数
            self.record_trial_usage()

            # 发出试用模式成功信号
            self.trial_mode_success.emit()
            self.close()  # 关闭授权窗口

            logger_manager.info("用户选择试用模式", "auth_window")

        except Exception as e:
            logger_manager.error(f"启动试用模式失败: {e}", "auth_window")
            show_error(self, "错误", f"启动试用模式失败: {e}")

    def check_trial_limit(self):
        """检查试用次数限制（每天3次）"""
        try:
            settings = settings_manager.settings
            today = datetime.now().strftime('%Y-%m-%d')

            # 获取今日试用次数
            trial_date = settings.value("trial/last_trial_date", "")
            trial_count = settings.value("trial/trial_count", 0, type=int)

            # 如果是新的一天，重置试用次数
            if trial_date != today:
                trial_count = 0
                settings.setValue("trial/last_trial_date", today)
                settings.setValue("trial/trial_count", 0)
                settings.sync()

            # 检查是否超过限制
            if trial_count >= 3:
                show_warning(self, "试用限制",
                             "今日试用次数已用完（每天限制3次）\n\n" +
                             "如需继续使用，请联系客服获取授权码")
                return False

            return True

        except Exception as e:
            logger_manager.error(f"检查试用次数失败: {e}", "auth_window")
            return False

    def record_trial_usage(self):
        """记录试用次数"""
        try:
            settings = settings_manager.settings
            trial_count = settings.value("trial/trial_count", 0, type=int)
            trial_count += 1

            settings.setValue("trial/trial_count", trial_count)
            settings.sync()

            remaining = 3 - trial_count
            if remaining > 0:
                show_info(self, "试用模式",
                          f"进入试用模式成功！\n\n" +
                          f"今日剩余试用次数：{remaining}次\n" +
                          f"试用模式限制：音视频时长不超过10分钟")
            else:
                show_info(self, "试用模式",
                          f"进入试用模式成功！\n\n" +
                          f"这是今日最后一次试用机会\n" +
                          f"试用模式限制：音视频时长不超过10分钟")

        except Exception as e:
            logger_manager.error(f"记录试用次数失败: {e}", "auth_window")


    def clear_auth_registry(self):
        """清空注册表中auth下的所有键值"""
        try:
            settings = settings_manager.settings

            # 获取auth组下的所有键
            settings.beginGroup("auth")
            auth_keys = settings.allKeys()
            settings.endGroup()

            # 删除所有auth相关的键值
            for key in auth_keys:
                settings.remove(f"auth/{key}")

            # 确保立即同步到注册表
            settings.sync()

            logger_manager.info(f"清空信息，共删除 {len(auth_keys)} 个键值", "auth_window")

        except Exception as e:
            logger_manager.error(f"清空信息失败: {e}", "auth_window")

    def load_debug_setting(self):
        """加载调试设置"""
        try:
            _, debug_enabled, _ = settings_manager.get_ui_settings()
            self.ui.chkDebug.setChecked(debug_enabled)
            logger_manager.info(f"加载调试设置: {debug_enabled}", "auth_window")
        except Exception as e:
            logger_manager.error(f"加载调试设置失败: {e}", "auth_window")
            self.ui.chkDebug.setChecked(False)  # 默认关闭

    def on_debug_changed(self, state):
        """调试开关状态改变时的处理"""
        try:
            debug_enabled = state == 2  # Qt.Checked = 2

            # 获取当前的其他UI设置
            output_type, _, simple_enabled = settings_manager.get_ui_settings()

            # 保存更新后的设置（只更新调试设置，保持其他设置不变）
            settings_manager.save_ui_settings(output_type, debug_enabled, simple_enabled)

            logger_manager.info(f"调试模式已{'开启' if debug_enabled else '关闭'}", "auth_window")

        except Exception as e:
            logger_manager.error(f"保存调试设置失败: {e}", "auth_window")

    @staticmethod
    def get_cpu_serial_static():
        """获取CPU序列号（静态方法）"""
        try:
            if platform.system() == "Windows":
                # 方法1：尝试获取CPU ProcessorId
                try:
                    result = subprocess.run(
                        ['wmic', 'cpu', 'get', 'ProcessorId', '/value'],
                        capture_output=True, text=True,
                        creationflags=subprocess.CREATE_NO_WINDOW,
                        timeout=10  # 添加超时
                    )
                    if result.returncode == 0:
                        for line in result.stdout.split('\n'):
                            if 'ProcessorId=' in line:
                                cpu_id = line.split('=')[1].strip()
                                if cpu_id and cpu_id != "":
                                    logger_manager.info(f"获取到IDC: {cpu_id}", "auth_window")
                                    return cpu_id
                except subprocess.TimeoutExpired:
                    logger_manager.warning("IDC命令超时", "auth_window")
                except Exception as e:
                    logger_manager.warning(f"IDC命令失败: {e}", "auth_window")
                # 方法2：尝试获取CPU名称作为备选
                try:
                    result = subprocess.run(
                        ['wmic', 'cpu', 'get', 'Name', '/value'],
                        capture_output=True, text=True,
                        creationflags=subprocess.CREATE_NO_WINDOW,
                        timeout=10
                    )
                    if result.returncode == 0:
                        for line in result.stdout.split('\n'):
                            if 'Name=' in line:
                                cpu_name = line.split('=')[1].strip()
                                if cpu_name and cpu_name != "":
                                    logger_manager.info(f"使用IDC名称作为标识: {cpu_name}", "auth_window")
                                    return hashlib.md5(cpu_name.encode()).hexdigest()[:16]
                except Exception as e:
                    logger_manager.warning(f"获取IDC名称失败: {e}", "auth_window")
                # 方法3：使用系统信息作为备选
                try:
                    import os
                    computer_name = os.environ.get('COMPUTERNAME', '')
                    username = os.environ.get('USERNAME', '')
                    if computer_name and username:
                        fallback_id = f"{computer_name}_{username}"
                        logger_manager.info(f"sys为IDC标识: {fallback_id}", "auth_window")
                        return hashlib.md5(fallback_id.encode()).hexdigest()[:16]
                except Exception as e:
                    logger_manager.warning(f"获取sys失败: {e}", "auth_window")

            else:
                # Linux/Mac系统
                try:
                    with open('/proc/cpuinfo', 'r') as f:
                        for line in f:
                            if 'Serial' in line:
                                return line.split(':')[1].strip()
                except Exception as e:
                    logger_manager.warning(f"读取/idc失败: {e}", "auth_window")

        except Exception as e:
            logger_manager.error(f"获取IDC序列号失败: {e}", "auth_window")

        logger_manager.warning("所有IDC信息获取方法都失败，使用默认值", "auth_window")
        return UNKNOWNCPU

    @staticmethod
    def get_motherboard_info_static():
        """获取主板信息（静态方法）"""
        try:
            if platform.system() == "Windows":
                # 方法1：尝试获取主板序列号
                try:
                    result = subprocess.run(
                        ['wmic', 'baseboard', 'get', 'SerialNumber', '/value'],
                        capture_output=True, text=True,
                        creationflags=subprocess.CREATE_NO_WINDOW,
                        timeout=10
                    )
                    if result.returncode == 0:
                        for line in result.stdout.split('\n'):
                            if 'SerialNumber=' in line:
                                serial = line.split('=')[1].strip()
                                if serial and serial != "To be filled by O.E.M." and serial != "":
                                    logger_manager.info(f"获取到D序: {serial}", "auth_window")
                                    return serial
                except subprocess.TimeoutExpired:
                    logger_manager.warning("D命令超时", "auth_window")
                except Exception as e:
                    logger_manager.warning(f"D命令失败: {e}", "auth_window")

                # 方法2：尝试获取主板型号
                try:
                    result = subprocess.run(
                        ['wmic', 'baseboard', 'get', 'Product', '/value'],
                        capture_output=True, text=True,
                        creationflags=subprocess.CREATE_NO_WINDOW,
                        timeout=10
                    )
                    if result.returncode == 0:
                        for line in result.stdout.split('\n'):
                            if 'Product=' in line:
                                product = line.split('=')[1].strip()
                                if product and product != "" and product != "To be filled by O.E.M.":
                                    logger_manager.info(f"获取到D序: {product}", "auth_window")
                                    return product
                except Exception as e:
                    logger_manager.warning(f"获取D序失败: {e}", "auth_window")

                # 方法3：尝试获取主板制造商
                try:
                    result = subprocess.run(
                        ['wmic', 'baseboard', 'get', 'Manufacturer', '/value'],
                        capture_output=True, text=True,
                        creationflags=subprocess.CREATE_NO_WINDOW,
                        timeout=10
                    )
                    if result.returncode == 0:
                        for line in result.stdout.split('\n'):
                            if 'Manufacturer=' in line:
                                manufacturer = line.split('=')[1].strip()
                                if manufacturer and manufacturer != "" and manufacturer != "To be filled by O.E.M.":
                                    logger_manager.info(f"获取到D商: {manufacturer}", "auth_window")
                                    return manufacturer
                except Exception as e:
                    logger_manager.warning(f"获取D商失败: {e}", "auth_window")

                # 方法4：使用BIOS信息作为备选
                try:
                    result = subprocess.run(
                        ['wmic', 'bios', 'get', 'SerialNumber', '/value'],
                        capture_output=True, text=True,
                        creationflags=subprocess.CREATE_NO_WINDOW,
                        timeout=10
                    )
                    if result.returncode == 0:
                        for line in result.stdout.split('\n'):
                            if 'SerialNumber=' in line:
                                bios_serial = line.split('=')[1].strip()
                                if bios_serial and bios_serial != "" and bios_serial != "To be filled by O.E.M.":
                                    logger_manager.info(f"使用BD序: {bios_serial}", "auth_window")
                                    return bios_serial
                except Exception as e:
                    logger_manager.warning(f"获取BD序失败: {e}", "auth_window")

            else:
                # Linux系统
                try:
                    with open('/sys/class/dmi/id/board_serial', 'r') as f:
                        board_serial = f.read().strip()
                        if board_serial and board_serial != "":
                            return board_serial
                except:
                    try:
                        with open('/sys/class/dmi/id/product_name', 'r') as f:
                            product_name = f.read().strip()
                            if product_name and product_name != "":
                                return product_name
                    except Exception as e:
                        logger_manager.warning(f"读取lsys失败: {e}", "auth_window")

        except Exception as e:
            logger_manager.error(f"获取BD序失败: {e}", "auth_window")

        logger_manager.warning("所有BD序获取方法都失败，使用默认值", "auth_window")
        return UNKNOWNMOTHERBOARD

    @staticmethod
    def generate_machine_code_static():
        """生成机器码（静态方法）"""
        try:
            # 获取硬件信息
            cpu_serial = AuthWindow.get_cpu_serial_static()
            motherboard_info = AuthWindow.get_motherboard_info_static()

            # 构造字符串：'w' + CPU序列号 + 'x' + 主板信息 + 'y'
            hardware_string = f"w{cpu_serial}x{motherboard_info}y"
            if hardware_string == f"w{UNKNOWNCPU}x{UNKNOWNMOTHERBOARD}y":
                logger_manager.warning("无法获取硬件信息", "auth_window")
                return None

            # 使用SHA256哈希生成机器码
            machine_code = hashlib.sha256(hardware_string.encode('utf-8')).hexdigest()[:16].upper()

            # 格式化机器码（每4位用-分隔）
            formatted_code = '-'.join([machine_code[i:i + 4] for i in range(0, len(machine_code), 4)])

            return formatted_code

        except Exception as e:
            logger_manager.error(f"生成机器码失败: {str(e)}", "auth_window")
            return None

    def get_cpu_serial(self):
        """获取CPU序列号（实例方法，调用静态方法）"""
        return self.get_cpu_serial_static()

    def get_motherboard_info(self):
        """获取主板信息（实例方法，调用静态方法）"""
        return self.get_motherboard_info_static()

    def generate_machine_code(self):
        """生成机器码（实例方法）"""
        try:
            formatted_code = self.generate_machine_code_static()

            if formatted_code is None:
                show_error(self, "错误", "无法获取硬件信息")
                self.ui.leMachineCode.setText("生成失败")
                return

            # 显示在输入框中
            self.ui.leMachineCode.setText(formatted_code)

        except Exception as e:
            error_msg = f"生成机器码失败: {str(e)}"
            logger_manager.error(error_msg, "auth_window")
            self.ui.leMachineCode.setText("生成失败")
            show_error(self, "错误", error_msg)

    def copy_machine_code(self):
        """复制机器码到剪贴板"""
        machine_code = self.ui.leMachineCode.text()
        if machine_code and machine_code != "生成失败":
            clipboard = QApplication.clipboard()
            clipboard.setText(machine_code)
            logger_manager.info("机器码已复制到剪贴板", "auth_window")
            show_info(self, "提示", "机器码已复制到剪贴板")
        else:
            logger_manager.warning("没有有效的机器码可复制", "auth_window")
            show_warning(self, "警告", "没有有效的机器码可复制")

    def authorize(self):
        """授权验证"""
        machine_code = self.ui.leMachineCode.text()

        auth_code = self.ui.leAuthCode.text().strip()
        if not auth_code:
            show_warning(self, "警告", "请输入授权码")
            return

        decrypted = aes_decrypt(auth_code)
       # print(decrypted) 
        # 如果decrypted为None，则说明解密失败
        if decrypted is None:
            show_warning(self, "错误", "授权码不正确")
            return
        # 将decrypted按照 | 进行分隔
        auth_code_list = decrypted.split('|')
        machine_auth_code = auth_code_list[0]  # 第一位必然是机器码
        # 修复授权验证逻辑（原来的判断有问题）
        if machine_code.replace('-', '') == machine_auth_code.replace('-', ''):
            # ✅ 授权成功后保存到QSettings
            temp_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 当前授权时间
            # 保存授权信息
            settings_manager.save_auth_info(
                machine_code,  # 设备唯一标识码
                temp_time
            )

            # 可以保存更多授权相关信息
            settings = settings_manager.settings
            # 第一次保存的时候, 应该把当前的时间也保存下来, 不要去使用  auth/auth_time 注册表里面这个时间 和 auth/is_authorized
            # 这只是个幌子
            auth_code_encryption = aes_encrypt(auth_code + "|" + temp_time)
            settings.setValue("auth/last_auth_code", auth_code_encryption)  # 保存输入的授权码
            settings.setValue("auth/is_authorized", True)  # 设置授权状态为真
            settings.sync()

            self.auth_success.emit()  # 发出授权成功信号
            self.close()  # 关闭授权窗口
        else:
            logger_manager.warning("授权码无效", "auth_window")
            show_warning(self, "错误", "授权码无效，请检查后重试")

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
            QMessageBox.warning(self, "错误", f"无法打开帮助窗口: {str(e)}")

    def open_disclaimers_dialog(self):
        """打开免责声明窗体"""
        try:
            # 清空注册表中auth相关的键值
            # self.clear_auth_registry()

            # 如果免责声明窗口已经存在且可见，则将其置于前台
            if self.disclaimers_dialog and self.disclaimers_dialog.isVisible():
                self.disclaimers_dialog.raise_()
                self.disclaimers_dialog.activateWindow()
                return

            # 创建新的免责声明窗口
            self.disclaimers_dialog = DisclaimersHelpDialog()
            self.disclaimers_dialog.show()
            logger_manager.info("使用帮助窗口已打开，auth注册表信息已清空", "auth_window")

        except Exception as e:
            logger_manager.error(f"打开使用帮助窗口时发生错误: {str(e)}", "auth_window")
            QMessageBox.warning(self, "错误", f"无法打开使用帮助窗口: {str(e)}")


