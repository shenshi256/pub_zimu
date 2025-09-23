#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Time    : 2025/7/1 10:08
# @Author  : WXY
# @File    : disclaimers.py
# @PROJECT_NAME: whisper_gui
# @PRODUCT_NAME: PyCharm
# -------------------------------------------------------------------------------


from PySide6.QtWidgets import QMainWindow
from ui_disclaimers import Ui_MainWindow
from utils import setup_window_icon,VERSION,  get_image_base64, SCROLLBARSTYLE


class DisclaimersHelpDialog(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        setup_window_icon(self)
        self.setMinimumSize(800, 600)
        self.setMaximumSize(800, 600)
        # 设置标题栏文本（可选）
        self.setWindowTitle(f"项目使用说明 {VERSION}")
        self.ui.lblProjectHelp.setText("📘 项目使用说明")
        # 填入帮助信息
        self.ui.textBrowser.setHtml(self.get_help_html())
        # 配置链接在外部浏览器中打开
        self.ui.textBrowser.setOpenExternalLinks(True)
        # 连接关闭按钮
        self.ui.btnClose.clicked.connect(self.close)
        # 设置滚动条样式 , 显示滚动条
        self.ui.textBrowser.setStyleSheet(SCROLLBARSTYLE)
    def get_help_html(self):
        """返回 HTML 格式的帮助内容"""
        # 获取图片的base64编码
        service_img = get_image_base64(  )
        img_html = ""
        if service_img:
            img_html = f'''
            <div style="text-align: center; margin: 10px 0 0px 0;">
                <h3 style="margin: 10px 0; color: #2c3e50;">
                    ✨═══════════════════════════════════════✨<br>
                    🌟    若有帮助, 请支持一杯咖啡    🌟<br>
                    ✨═══════════════════════════════════════✨
                </h3>
                 <p style="margin: 0; padding: 0;">
                <img src="{service_img}" alt="Service" width="500" height="300" style="margin: 5px 0; 
                border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                </p>
            </div>
            '''
        # 静态CSS样式（不使用f-string）, 或者使用{{ }} 也是可以的
        css_styles = """
         body {
                       font-family: 'Microsoft YaHei', Arial, sans-serif;
                       line-height: 1.6;
                       margin: 20px;
                       color: #333;
                   }
                   h1 {
                       color: #2c3e50;
                       border-bottom: 2px solid #3498db;
                       padding-bottom: 10px;
                       margin-bottom: 5px;
                   }
                   h2 {
                       color: #34495e;
                       margin-top: 10px ;
                       margin-bottom: 10px;
                   }
                   .emoji {
                       font-size: 1.2em;
                   }
                   .highlight {
                       background-color: #f8f9fa;
                       padding: 10px;
                       border-left: 4px solid #3498db;
                       margin: 10px 0;
                   }
                   .warning {
                       background-color: #fff3cd;
                       border: 1px solid #ffeaa7;
                       border-radius: 5px;
                       padding: 15px;
                       margin: 15px 0;
                   }
                   .link {
                       color: #3498db;
                       text-decoration: none;
                   }
                   .link:hover {
                       text-decoration: underline;
                   }
                   ul {
                       padding-left: 20px;
                   }
                   li {
                       margin-bottom: 8px;
                   }
        """
        return f"""
           <!DOCTYPE html>
           <html>
           <head>
               <meta charset="utf-8">
               <style>
                   {css_styles}
               </style>
           </head>
           <body>
               <!-- <h1>📘 项目使用说明（字幕生成器）</h1> -->
             
              <h1>✅ 本工具基于 OpenAI 开源模型 Whisper 封装</h1> <!-- ，遵循 MIT License。</h1> --> 
              <h1>✅ 本项目适应于win10或以上系统</h1> 
               
                <h2 >1️⃣ 模型文件下载</h2>
              <!--  <span style="display:block;font-size:20px;font-weight:bold;margin:0;padding:0;">1️⃣ 模型文件下载</span>-->
               <p>首次使用前，请下载 Whisper 模型文件（.pt 格式）：</p>

               <div >
                   <p><strong>🔗 官方地址：</strong><br>
                   👉 <a href="https://github.com/openai/whisper" class="link">https://github.com/openai/whisper</a></p>

                   <p><strong>🇨🇳 网盘下载（推荐）：</strong></p>
                   <ul>  
                   <!-- 通过网盘分享的文件：字幕生成器模型链接: -->
                       <li>📦 百度网盘：<a href="https://pan.baidu.com/s/1mNNWBpeq8Lk19-q3JPqrmA?pwd=b6xx"  class="link" >https://pan.baidu.com/s/1mNNWBpeq8Lk19-q3JPqrmA?pwd=b6xx</a> <span  class="link">提取码: b6xx</span></li>
                       <li>👉 如嫌网盘限速, 可以联系客服, 发邮箱超大附件 </li>
                      <!-- <li>📦 夸克网盘：https://pan.kuake.com/addfgdsa 提取码：Z22C</li> -->
                   </ul>
               </div>

               <p>支持的模型：<strong>tiny, base, small, medium, large-v1, large-v2, large-v3</strong><br>
               建议根据性能和需求选择，详细对比请查看【模型使用帮助】页面。</p>

               <h2>2️⃣ 模型文件放置说明</h2>
               <ul>
                   <li>请将下载的模型文件（.pt）放置于程序所在目录下的 <strong>model</strong> 文件夹中；</li>
                   <li>若 model 文件夹不存在，程序将自动创建；</li>
                   <li>模型文件命名应保持原始格式，例如：tiny.pt, base.en.pt 等。</li>
               </ul>

               <h2>3️⃣ 启动程序</h2>
               <ul>
                   <li>双击运行 <strong>字幕生成器.exe</strong>（首次启动可能略慢，属正常现象）；</li>
                   <li>项目为 <strong>离线独立运行包</strong>，无需联网即可使用；</li>
                   <li>支持 <strong>Windows 10</strong> 及以上版本。不支持苹果系统, </li>
               </ul>

               <h2>4️⃣ 功能说明</h2>
               <ul>
                   <li>📂 支持选择音视频文件（支持常见格式如 .mp3, .mp4, .wav, .mov 等）；</li>
                   <li>📤 支持输出多种字幕格式：<strong>SRT, TXT, VTT, JSON</strong></li>
                   <li>🌐 可选项：
                       <ul>
                           <li>✅ 是否简体中文输出（如果音视频是港台腔大概率会被识别成繁体）</li>
                           <li>🐞 是否开启调试模式（输出详细日志）</li>
                       </ul>
                   </li>
                   <li>🔁 实时显示转写进度与日志，便于观察运行状态</li>
               </ul>

               <h2>5️⃣ 使用说明与免责声明</h2>
               <ul>
                   <li>本项目基于 OpenAI 开源模型 Whisper 开发；</li>
                   <li>本软件为个人开发工具，免费使用, 如果对您有帮助，请给作者赏杯咖啡；</li>
                   <li>严禁用于一切非法用途，开发者不对任何使用结果或法律风险承担责任；</li>
                   <li>请勿用于商业传播、隐私监听、违法活动等用途；</li>
               </ul>

               <div  >
                   <h3>⚠️ 注意事项</h3>
                   <ul>
                       <li>⏳ 首次启动可能稍慢，耐心等待初始化；</li>
                       <li>💾 请确保有足够的磁盘空间保存转写文件；</li>
                       <li>🧠 建议使用 64 位操作系统并预留充足内存（详见模型帮助说明）；</li>
                       <li>🛠 遇到问题时，可尝试开启调试模式查看详细错误信息；</li>
                       <li>📥 输出结果存放于与音视频文件相同目录下，命名一致，仅扩展名不同；</li>
                   </ul>
               </div>
                 {img_html}
           </body>
           </html>
           """
