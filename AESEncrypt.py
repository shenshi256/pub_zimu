#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Time    : 2025/6/26 16:54
# @Author  : WXY
# @File    : AESEncrypt
# @PROJECT_NAME: whisper_gui
# @PRODUCT_NAME: PyCharm
# -------------------------------------------------------------------------------
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
import base64

# 提取密钥和IV为常量
AES_KEY = "4tbtjKFEvUmdyYdCgKXzurHpHodpWjiH"[:32].encode('utf-8')
AES_IV = "0XErJTUsVBhWtjIj"[:16].encode('utf-8')
# A0BnqMlvEmNFoHBfo7I0fgUVfs8H+NCDkTfSXbdZR0Y=
from LoggerManager import logger_manager


def aes_encrypt(plain_text):
    """AES加密函数"""
    # 创建AES加密器
    cipher = AES.new(AES_KEY, AES.MODE_CBC, AES_IV)

    # 对明文进行填充并加密
    padded_data = pad(plain_text.encode('utf-8'), AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)

    # Base64编码
    encrypted_text = base64.b64encode(encrypted_data).decode('utf-8')

    return encrypted_text


def aes_decrypt(encrypted_text):
    """AES解密函数"""
    try:
        # Base64解码
        encrypted_data = base64.b64decode(encrypted_text)

        # 创建AES解密器
        cipher = AES.new(AES_KEY, AES.MODE_CBC, AES_IV)

        # 解密并去除填充
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

        return decrypted_data.decode('utf-8')
    except Exception as e:
        print(f"授权失败: {e}")
        logger_manager.error(f"授权失败: {e}")
        return None


# 使用示例
if __name__ == "__main__":
    # 加密示例
    original_text = "Hello World!"
    encrypted = aes_encrypt(original_text)
    print(f"加密后: {encrypted}")

    # 解密示例
    decrypted = aes_decrypt(encrypted)
    print(f"解密后: {decrypted}")

    # 验证
    print(f"加解密是否一致: {original_text == decrypted}")

# 使用示例
# encrypted = "从C#加密得到的Base64字符串"
# decrypted = aes_decrypt(encrypted)
# print(decrypted)