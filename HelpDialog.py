#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Time    : 2025/6/26 22:38
# @Author  : WXY
# @File    : HelpDialog
# @PROJECT_NAME: whisper_gui
# @PRODUCT_NAME: PyCharm
# -------------------------------------------------------------------------------
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow
from ui_helpshow import Ui_HelpShow  # 你刚生成的 ui 文件
from utils import  setup_window_icon,VERSION, SCROLLBARSTYLE

class HelpDialog(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_HelpShow()
        self.ui.setupUi(self)
        setup_window_icon(self)
        self.setMinimumSize(800, 600)
        self.setMaximumSize(800, 600)
        # 设置标题栏文本（可选）
        self.setWindowTitle(f"模型使用帮助 {VERSION}")
        self.ui.lblHelp.setText("📘 模型使用帮助")
        # 填入帮助信息
        self.ui.textBrowser.setHtml(self.get_help_html())
        # 配置链接在外部浏览器中打开
        self.ui.textBrowser.setOpenExternalLinks(True)
        # 连接关闭按钮
        self.ui.pushButton.clicked.connect(self.close)
        # 在UI初始化后添加
        # self.ui.textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # self.ui.textBrowser.verticalScrollBar().setVisible(True)

        # 设置滚动条样式 , 显示滚动条
        self.ui.textBrowser.setStyleSheet(SCROLLBARSTYLE)
    def get_help_html(self):
        """返回 HTML 格式的帮助内容"""
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                body { font-family: 'Microsoft YaHei', Arial, sans-serif; margin: 20px; line-height: 1.6; }
                h1 { color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }
                h2 { color: #34495e; margin-top: 30px; border-left: 4px solid #3498db; padding-left: 15px; }
                table { width: 100%; border-collapse: collapse; margin: 20px 0; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
                .layout-table { border: none !important; box-shadow: none !important; }
                .layout-table td { border: none !important; }
                th { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: black; padding: 12px; text-align: left; font-weight: bold; }
                td { padding: 10px 12px; border-bottom: 1px solid #ecf0f1; }
                tr:nth-child(even) { background-color: #f8f9fa; }
                tr:hover { background-color: #e8f4fd; transition: background-color 0.3s; }
                .download-link { color: white; text-decoration: none; font-family: 'Consolas', monospace; background: transparent; padding: 2px 6px; border-radius: 3px; }
                .download-link:hover {  color: #3498db; border: 1px solid rgba(52, 152, 219, 0.6);}
                .star { color: #f39c12; }
                .speed-fast { color: #27ae60; font-weight: bold; }
                .speed-medium { color: #f39c12; font-weight: bold; }
                .speed-slow { color: #e74c3c; font-weight: bold; }
                .highlight-box { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 15px; border-radius: 8px; margin: 20px 0; }
                .highlight-box h2 { color: white; border-left: 4px solid white; }
                .highlight-box td { color: white; }
                .highlight-box .model-name { color: #f1c40f; font-weight: bold; }
                .model-name { font-weight: bold; color: #2c3e50; }
                .size-info { color: #7f8c8d; font-style: italic; }
            </style>
        </head>
        <body>
            <h1>🎯 Whisper 模型下载与使用指南</h1>
         
            <h2>📥 模型下载地址</h2>
            <table>
             
                <tr><th>模型名称</th><th>下载链接</th></tr>
                <tr><td class="model-name">网盘整合</td><td><a href="https://pan.baidu.com/s/1mNNWBpeq8Lk19-q3JPqrmA?pwd=b6xx" class="download-link">https://pan.baidu.com/s/1mNNWBpeq8Lk19-q3JPqrmA?pwd=b6xx</a> <span style="color: white;">提取码: b6xx</span></td></tr>
              
                <tr><td class="model-name">tiny.pt</td><td><a href="https://openaipublic.blob.core.windows.net/whisper/models/tiny.pt" class="download-link">https://openaipublic.blob.core.windows.net/whisper/models/tiny.pt</a></td></tr>
                <tr><td class="model-name">tiny.en.pt</td><td><a href="https://openaipublic.blob.core.windows.net/whisper/models/tiny.en.pt" class="download-link">https://openaipublic.blob.core.windows.net/whisper/models/tiny.en.pt</a></td></tr>
                <tr><td class="model-name">base.pt</td><td><a href="https://openaipublic.blob.core.windows.net/whisper/models/base.pt" class="download-link">https://openaipublic.blob.core.windows.net/whisper/models/base.pt</a></td></tr>
                <tr><td class="model-name">base.en.pt</td><td><a href="https://openaipublic.blob.core.windows.net/whisper/models/base.en.pt" class="download-link">https://openaipublic.blob.core.windows.net/whisper/models/base.en.pt</a></td></tr>
                <tr><td class="model-name">small.pt</td><td><a href="https://openaipublic.blob.core.windows.net/whisper/models/small.pt" class="download-link">https://openaipublic.blob.core.windows.net/whisper/models/small.pt</a></td></tr>
                <tr><td class="model-name">small.en.pt</td><td><a href="https://openaipublic.blob.core.windows.net/whisper/models/small.en.pt" class="download-link">https://openaipublic.blob.core.windows.net/whisper/models/small.en.pt</a></td></tr>
                <tr><td class="model-name">medium.pt</td><td><a href="https://openaipublic.blob.core.windows.net/whisper/models/medium.pt" class="download-link">https://openaipublic.blob.core.windows.net/whisper/models/medium.pt</a></td></tr>
                <tr><td class="model-name">medium.en.pt</td><td><a href="https://openaipublic.blob.core.windows.net/whisper/models/medium.en.pt" class="download-link">https://openaipublic.blob.core.windows.net/whisper/models/medium.en.pt</a></td></tr>
                <tr><td class="model-name">large-v2.pt</td><td><a href="https://openaipublic.blob.core.windows.net/whisper/models/large-v2.pt" class="download-link">https://openaipublic.blob.core.windows.net/whisper/models/large-v2.pt</a></td></tr>
                <tr><td class="model-name">large-v3.pt</td><td><a href="https://openaipublic.blob.core.windows.net/whisper/models/large-v3.pt" class="download-link">https://openaipublic.blob.core.windows.net/whisper/models/large-v3.pt</a></td></tr>
            </table>

            <h2>🌍 多语言模型对比 </h2>
            <h3>🌍 支持 100+ 种语言（含中文、日语、韩语等） </h3>
            <table>
                <tr>
                    <th>模型名</th><th>模型大小</th><th>语言支持</th><th>推理速度</th><th>英文精度</th><th>多语言精度</th><th>下载体积</th>
                </tr>
                <tr>
                    <td class="model-name">tiny</td>
                    <td class="size-info">39 MB</td>
                    <td>✅ 多语言</td>
                    <td class="speed-fast">🟢 最快</td>
                    <td><span class="star">⭐⭐</span>（低）</td>
                    <td><span class="star">⭐</span>（较低）</td>
                    <td>~75 MB</td>
                </tr>
                <tr>
                    <td class="model-name">base</td>
                    <td class="size-info">74 MB</td>
                    <td>✅ 多语言</td>
                    <td class="speed-fast">🟢 快</td>
                    <td><span class="star">⭐⭐⭐</span></td>
                    <td><span class="star">⭐⭐</span></td>
                    <td>~142 MB</td>
                </tr>
                <tr>
                    <td class="model-name">small</td>
                    <td class="size-info">244 MB</td>
                    <td>✅ 多语言</td>
                    <td class="speed-medium">🟡 中等</td>
                    <td><span class="star">⭐⭐⭐⭐</span></td>
                    <td><span class="star">⭐⭐⭐</span></td>
                    <td>~462 MB</td>
                </tr>
                <tr>
                    <td class="model-name">medium</td>
                    <td class="size-info">769 MB</td>
                    <td>✅ 多语言</td>
                    <td class="speed-slow">🔴 慢</td>
                    <td><span class="star">⭐⭐⭐⭐⭐</span></td>
                    <td><span class="star">⭐⭐⭐⭐</span></td>
                    <td>~1.5 GB</td>
                </tr>
                <tr>
                    <td class="model-name">large</td>
                    <td class="size-info">1550 MB</td>
                    <td>✅ 多语言</td>
                    <td class="speed-slow">🔴 最慢</td>
                    <td><span class="star">⭐⭐⭐⭐⭐</span></td>
                    <td><span class="star">⭐⭐⭐⭐⭐</span></td>
                    <td>~2.9 GB</td>
                </tr>
            </table>

            <h2>🇺🇸 仅支持英文的模型</h2>
            <table>
                <tr>
                    <th>模型名</th><th>模型大小</th><th>推理速度</th><th>英文识别精度</th><th>支持语言</th><th>下载体积</th>
                </tr>
                <tr>
                    <td class="model-name">tiny.en</td>
                    <td class="size-info">39 MB</td>
                    <td class="speed-fast">🟢 最快</td>
                    <td><span class="star">⭐⭐</span>（较低）</td>
                    <td>仅英文</td>
                    <td>~75 MB</td>
                </tr>
                <tr>
                    <td class="model-name">base.en</td>
                    <td class="size-info">74 MB</td>
                    <td class="speed-fast">🟢 快</td>
                    <td><span class="star">⭐⭐⭐</span>（中等）</td>
                    <td>仅英文</td>
                    <td>~142 MB</td>
                </tr>
                <tr>
                    <td class="model-name">small.en</td>
                    <td class="size-info">244 MB</td>
                    <td class="speed-medium">🟡 中等</td>
                    <td><span class="star">⭐⭐⭐⭐</span>（较好）</td>
                    <td>仅英文</td>
                    <td>~462 MB</td>
                </tr>
            </table>

             <table  class="layout-table"  style="width: 100%; border: none; margin: 20px 0;" >
              <tr>
                    <td style="width: 50%; vertical-align: top; padding-right: 10px; border: none; height: 200px;">
                        <h2>🎯 精度场景推荐</h2>
                        <table  style="margin: 0;">
                            <tr><th>使用场景</th><th>推荐模型</th></tr>
                            <tr><td>英文为主，速度优先</td><td class="model-name">tiny.en</td></tr>
                            <tr><td>英文为主，兼顾精度</td><td class="model-name">base.en 或 small.en</td></tr>
                            <tr><td>识别中文、日语、韩语等多语言</td><td class="model-name">small 以上版本</td></tr>
                            <tr><td>高精度、对错率要求很高（任意语言）</td><td class="model-name">medium 或 large</td></tr>
                        </table>
                    </td>
                    <td style="width: 50%; vertical-align: top; padding-left: 50px; border: none; height: 200px;">
                        <h2>✅ 速度场景推荐</h2>
                        <table style="margin: 0;">
                            <tr><th>使用场景</th><th>推荐模型</th></tr>
                            <tr><td>极致轻量/速度优先（低端机）</td><td class="model-name">tiny.en</td></tr>
                            <tr><td>平衡精度与速度（普通用户）</td><td class="model-name">base.en</td></tr>
                            <tr><td>追求更好识别率（仅英文）</td><td class="model-name">small.en</td></tr>
                        </table>
                    </td>
                </tr>
            </table>
            
             <h3>🧠 所有模型均支持纯 CPU 推理</h3>
                <p>虽然 CPU 推理速度较慢，但在离线、稳定环境下依然是可接受的。建议选择 <b>tiny</b> 或 <b>base</b> 模型。</p>
               <table  class="layout-table"  style="width: 100%; border: none; margin: 20px 0;">
                <tr>
                    <td style="width: 50%; vertical-align: top; padding-right: 10px; border: none;">
                        <h3>📊 显存要求（NVIDIA GPU）</h3>
                        <table>
                            <tr><th>模型</th><th>最低显存</th><th>推荐显存</th></tr>
                            <tr><td class="model-name">tiny</td><td>1GB</td><td>2GB+</td></tr>
                            <tr><td class="model-name">base</td><td>2GB</td><td>4GB+</td></tr>
                            <tr><td class="model-name">small</td><td>4GB</td><td>6GB+</td></tr>
                            <tr><td class="model-name">medium</td><td>6GB</td><td>8GB+</td></tr>
                            <tr><td class="model-name">large</td><td>10GB</td><td>12–16GB</td></tr>
                        </table>
                    </td>
                    <td style="width: 50%; vertical-align: top; padding-left: 50px; border: none;">
                        <h3>🧬 内存要求（RAM）</h3>
                        <table>
                            <tr><th>模型</th><th>最低内存</th><th>推荐内存</th></tr>
                            <tr><td class="model-name">tiny</td><td>4GB</td><td>6–8GB</td></tr>
                            <tr><td class="model-name">base</td><td>4GB</td><td>6–8GB</td></tr>
                            <tr><td class="model-name">small</td><td>8GB</td><td>8–12GB</td></tr>
                            <tr><td class="model-name">medium</td><td>12GB</td><td>16GB+</td></tr>
                            <tr><td class="model-name">large</td><td>16GB</td><td>32GB+</td></tr>
                        </table>
                    </td>
                </tr>
            </table>

<h3>❗️ GPU 加速说明</h3>
<ul>
  <li>Whisper 使用 <b>PyTorch + CUDA</b> 实现 GPU 加速，仅支持 <b>NVIDIA 显卡</b>。</li>
  <li>如您使用 <b>AMD 显卡</b>，需自行安装 <b>ROCm + Linux + 特定 PyTorch</b>，部署复杂，需要一些技术能力。</li>
  <li>如果您是大型商业使用, 推荐使用 <b>Windows + NVIDIA 显卡 + CUDA Toolkit</b> 获得最佳加速体验。</li>
</ul>
        </body>
        </html>
        """
