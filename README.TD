# 1. 安装相关的依赖环境
打开 PyCharm 的 Terminal安装相关的包：
pip install pyside6
pip install moviepy
pip install openai-whisper
pip install librosa
pip install opencc-python-reimplemented
如果你使用的是 Windows 中文系统，可能还需要：
pip install numpy scipy tqdm


 pip freeze > requirements.txt   # 列出所有已安装的包（包括依赖的间接包），适合复制完整环境
# 使用 pipreqs（推荐项目用）, 这个需要安装, 它生成的 requirements.txt文件, 只包含项目中实际依赖的包, 这样 requirements.txt 会更干净

# 2. 运行程序, 将qt的界面文件转换成py文件
(base) (20231201_pyGUI) PS D:\PythonProject\whisper_gui\resources\ui_main> # 请注意操作路径
pyside6-uic .\mainwindow.ui -o  ..\..\ui_main.py
# (base) (20231201_pyGUI) PS D:\PythonProject\whisper_gui> pyside6-uic   .\resources\ui_main\mainwindow.ui -o .\ui_main.py

pyside6-uic .\auth.ui -o  ..\..\ui_auth.py
# (base) (20231201_pyGUI) PS D:\PythonProject\whisper_gui> pyside6-uic   .\resources\ui_main\auth.ui -o .\ui_auth.py
pyside6-uic .\helpshow.ui -o  ..\..\ui_helpshow.py
pyside6-uic .\helpshow.ui -o  ..\..\ui_helpshow.py

# 3. 功能算是全部开发完了, 还有一个BUG, 1是main.py中 MainWindow 类的550行, 在新的机器上因为没有setting, 所以会报错
2是main.py MainWindow里面的print 需要替换成全局的log日志
3.1 还有对于模型的显存, cpu , 系统版本的推荐 没有做
3.2 然后在授权页面应该也加一个帮助按钮
3.3 接下来就是打包了
# TODO: 2025年6月29日23:01:22
# 4. 中文时总是使用繁体, 这里还没有做
# 5. 把 输出类型 / 开启调试 / 中文时总是简体 写到setting里面去
# 6. 帮助界面, 不显示模型下载地址, 显示成百度网盘的地址, 把所有的模型都放到百度网盘里面去
# 7. 新增动态刷新模型, 下拉框展开的时候, 刷新一次model目录下的模型

# 4. 开始打包
4.1 基于 pyinstaller 进行打包
4.2 安装 pyinstaller , pip install pyinstaller
4.3 pip list 检查所有的依赖是否都已经安装了
4.4 创建requirements.txt, 便于环境重建, (base) (20231201_pyGUI) PS D:\PythonProject\whisper_gui> pip freeze > requirements.txt
4.5 创建打包脚本, build.spec
4.6 开始打包:(base) (20231201_pyGUI) PS D:\PythonProject\whisper_gui> pyinstaller build.spec


# 5. 防止反编译
5.1 混淆代码, 安装混淆工具

(base) (20231201_pyGUI) PS D:\PythonProject\whisper_gui> pip install pyarmor==7.7.4  # 安装 PyArmor 7 作为 pyarmor-7, 不要安装8.0的版本
(base) (20231201_pyGUI) PS D:\PythonProject\whisper_gui> pyarmor obfuscate --recursive --output dist_obfuscated main.py  # 每次更新完代码之后, 在执行pyinstaller build-obf.spec之前都要先执行这一行
pyarmor obfuscate --recursive --output dist_obfuscated transcriber.py
pyarmor obfuscate --recursive --output dist_obfuscated settings_manager.py
pyarmor obfuscate --recursive --output dist_obfuscated AESEncrypt.py

# 6. 压缩包
6.1 实际测试之后发现没有什么用, torch 库本身就很大（约 200+ MB）, librosa 及其依赖, PySide6 完整的 Qt 框架, ffmpeg-python
upx.exe --best --lzma --force D:\PythonProject\whisper_gui\dist\字幕生成器.exe
# 下载 UPX: https://upx.github.io/

6.2 移除不必要的依赖
pipreqs . --force
所以即使没有模型文件，312MB 对于包含完整 PyTorch + PySide6 + 音频处理库的应用来说是正常的体积。



#PyInstaller 打包的 exe 反编译难度
### 1. 反编译的可能性
PyInstaller 打包的 exe 文件可以被反编译 ，但难度取决于多个因素：
- 容易程度 ：相对容易，有现成工具
- 所需技能 ：中等技术水平
- 时间成本 ：几分钟到几小时不等
### 2. 常见反编译工具
```
#提取PyInstaller打包的文件
pyinstxtractoryour_app.exe

#反编译.pyc文件为.py
uncompyle6your_script.pyc

#或使用其他工具
decompyle3your_script.pyc
```
### 3. 反编译步骤
1. 提取 ：使用 pyinstxtractor 提取 exe 中的 Python 文件
2. 定位 ：找到主要的 .pyc 文件
3. 反编译 ：使用 uncompyle6 等工具还原源码
4. 分析 ：获得可读的 Python 源代码