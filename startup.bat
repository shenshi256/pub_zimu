@echo off
chcp 65001 > null 2>&1
setlocal enabledelayedexpansion

:: 显示调试信息（可选，用于排查问题）
:: echo 正在检测系统版本...

:: 获取Windows版本 - 使用更兼容的方法
set "winver_output="
for /f "tokens=*" %%i in ('ver 2^>nul') do set "winver_output=%%i"

:: 如果获取版本失败，默认允许运行（避免误杀）
if not defined winver_output (
    echo 无法检测系统版本，程序将继续运行...
    goto :start_program
)

:: 提取版本号 - 更安全的方法
set "major_version=0"
set "minor_version=0"

:: 从ver命令输出中提取版本号
echo !winver_output! | findstr /r "Version.*[0-9]\.[0-9]" >nul
if errorlevel 1 (
    echo 版本检测异常，程序将继续运行...
    goto :start_program
)

:: 提取主版本号和次版本号
for /f "tokens=2 delims=[]" %%i in ("!winver_output!") do (
    for /f "tokens=2 delims= " %%j in ("%%i") do (
        for /f "tokens=1,2 delims=." %%k in ("%%j") do (
            set "major_version=%%k"
            set "minor_version=%%l"
        )
    )
)

:: 调试输出（可选）
:: echo 检测到版本: !major_version!.!minor_version!

:: 检查是否为Windows 10以下版本
if !major_version! LSS 10 (
    cls
    echo.
    echo ================================================
    echo                系统兼容性提示
    echo         System compatibility prompt
    echo ================================================
    echo.
    echo 当前应用不支持Windows 10以下系统
    echo The current application does not support systems earlier than Windows 10
    echo.
    echo 系统要求：Windows 10 或更高版本
    echo System requirements: Windows 10 or later
    
    :: 显示具体系统版本
    if "!major_version!.!minor_version!"=="6.1" (
        echo 当前系统：Windows 7
        echo This OS: Windows 7
    ) else if "!major_version!.!minor_version!"=="6.2" (
        echo 当前系统：Windows 8
        echo This OS: Windows 8
    ) else if "!major_version!.!minor_version!"=="6.3" (
        echo 当前系统：Windows 8.1
        echo This OS: Windows 8.1
    ) else if "!major_version!"=="6" (
        echo 当前系统：Windows Vista或更早版本
        echo This OS: Windows Vista or earlier
    ) else if !major_version! LSS 6 (
        echo 当前系统：Windows XP或更早版本
        echo This OS: Windows XP or earlier
    ) else (
        echo 当前系统：Windows !major_version!.!minor_version!
        echo This OS: Windows !major_version!.!minor_version!
    )
    
    echo.
    echo 请升级到Windows 10或更高版本后再使用本软件。
    echo Please upgrade to Windows 10 or later to use this software.
    echo.
    echo ================================================
    echo.
    echo 按任意键退出...
    echo Press any key to exit...
    pause >nul
    exit /b 1
)

:start_program
:: Windows 10+ 系统，启动主程序
if exist "字幕生成器.exe" (
    start "" "字幕生成器.exe"
) else (
    echo.
    echo 错误：找不到"字幕生成器.exe"文件
    echo 请确保启动器和主程序在同一目录下
    echo.
    pause
)