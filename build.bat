@echo off
chcp 65001 >nul
echo 正在混淆代码...
pyarmor obfuscate --recursive --output dist_obfuscated main.py
echo 正在打包应用...
pyinstaller build-obf.spec
echo 构建完成！
REM pause