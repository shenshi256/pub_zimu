# -*- mode: python ; coding: utf-8 -*-
import whisper  #  导入whisper
block_cipher = None


a = Analysis(
    ['dist_obfuscated/main.py'],
    pathex=['dist_obfuscated'],
    binaries=[
        ('ffmpeg.exe', '.'),
        # ✅ 添加 PyArmor 运行时库, PyArmor 的 _pytransform.dll 必须位于可执行文件的同一目录中
        ('dist_obfuscated/pytransform/_pytransform.dll', '.'),
    ],
    datas=[
        ('favicon.ico', '.'),
        ('customer_service.jpg', '.'),
        # ✅ 添加 PyArmor 数据文件
        ('dist_obfuscated/pytransform', 'pytransform'),
         # 添加 Whisper 资源文件
        (whisper.__path__[0] + '/assets', 'whisper/assets'),
    ], 
    excludes=[

    ],
    hiddenimports=[
        # PySide6 相关
        'PySide6.QtCore',
        'PySide6.QtWidgets',
        'PySide6.QtGui',
        'PySide6.QtMultimedia',
        'PySide6.QtMultimediaWidgets',
        
        # 音频处理相关
        'whisper',
        'torch',
        'torchaudio',
        'librosa',
        'librosa.core',
        'librosa.feature',
        'librosa.util',
        'librosa.filters',
        'librosa.onset',
        'librosa.beat',
        'librosa.tempo',
        'librosa.decompose',
        'librosa.effects',
        'soundfile',
        'audioread',
        'resampy',
        'ffmpeg-python',
        
        # 科学计算相关
        'numpy',
        'scipy',
        'scipy.signal',
        'scipy.fft',
        'scipy.sparse',
        'scipy.spatial',
        'scipy.interpolate',
        'numba',
        'numba.core',
        'numba.typed',
        'pandas',
        
        # 加密相关
        'Crypto',
        'Crypto.Cipher',
        'Crypto.Cipher.AES',
        'Crypto.Util',
        'Crypto.Util.Padding',
        'Crypto.Random',
        'Crypto.Hash',
        'Crypto.Protocol',
        
        # 其他依赖
        'opencc',
        'base64',
        'json',
        'datetime',
        'threading',
        'queue',
        'pathlib',
        'configparser',
        # 添加 psutil 相关模块
        'psutil',
        'psutil._psutil_windows',  # Windows 特定模块
        'psutil._common',
        'psutil._compat',
        
        # 项目模块
        'main',
        'settings_manager',
        'transcriber',
        'auth_window',
        'HelpDialog',
        'LoggerManager',
        'SplashScreen',
        'AESEncrypt',
        'SingleInstanceManager',
        'GlobalExceptionHandler',
        'ui_main',
        'ui_auth',
        'ui_helpshow',
        'ui_disclaimers',
        'ui_splashscreen',
        'utils',
        'disclaimers',
        'SystemMonitorWorker',
        
        # PyArmor 相关, 这个是混淆使用的, build.spec不用加这个
        'pytransform'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='字幕生成器',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # 隐藏控制台窗口
    # onefile=True,  # 添加这一行, 没有多大用处
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='favicon.ico'
)