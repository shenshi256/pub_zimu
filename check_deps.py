#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Time    : 2025/6/30 17:09
# @Author  : WXY
# @File    : check_deps
# @PROJECT_NAME: whisper_gui
# @PRODUCT_NAME: PyCharm
# -------------------------------------------------------------------------------

# 分析还有哪些依赖没有包含到build.spec里面去

import modulefinder
import sys


def analyze_dependencies(script_path):
    finder = modulefinder.ModuleFinder()
    finder.run_script(script_path)

    print("找到的模块:")
    for name, mod in finder.modules.items():
        print(f"  {name}: {mod.__file__ if mod.__file__ else '(built-in)'}")

    print("\n缺失的模块:")
    for name in finder.badmodules:
        print(f"  {name}")

    return finder.badmodules


if __name__ == "__main__":
    # 分析混淆后的主文件
    missing = analyze_dependencies("dist_obfuscated/main.py")

    print(f"\n需要添加到 hiddenimports 的模块: {list(missing.keys())}")