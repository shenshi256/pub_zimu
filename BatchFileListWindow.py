#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Time    : 2025/10/14 13:53
# @Author  : WXY
# @File    : BatchFileListWindow
# @PROJECT_NAME: whisper_gui
# @PRODUCT_NAME: PyCharm
# -------------------------------------------------------------------------------
# 非模态详情窗口包装：使用 Ui_BatchFileList，负责表格填充与交互
from PySide6.QtWidgets import QCheckBox, QTableWidgetItem, QPushButton, QWidget, QHBoxLayout
import os
from PySide6.QtWidgets import  QMainWindow, QFileDialog, QStyledItemDelegate, QToolTip
from PySide6.QtCore import  Qt
from ui_batchfilelist import Ui_BatchFileList
from utils import format_size, setup_window_icon,VERSION, show_warning, show_confirm
from LoggerManager import logger_manager

class ElideTooltipDelegate(QStyledItemDelegate):
    def helpEvent(self, event, view, option, index):
        text = index.data(Qt.ItemDataRole.DisplayRole)
        if not text:
            return super().helpEvent(event, view, option, index)
        fm = option.fontMetrics
        try:
            width = fm.horizontalAdvance(str(text))
        except Exception:
            width = fm.width(str(text))
        if width > option.rect.width() - 8:
            QToolTip.showText(event.globalPos(), str(text), view)
            return True
        return super().helpEvent(event, view, option, index)

class BatchFileListWindow(QMainWindow):
    def __init__(self, parent ):
        super().__init__( parent )
        self.parent = parent
        self.ui = Ui_BatchFileList()
        self.ui.setupUi(self)
        self.setMaximumSize(800,600)
        self.setMinimumSize(800,600)
        setup_window_icon(self)
        self.setWindowTitle(f"批量处理列表 {VERSION}")
        # 事件绑定
        self.ui.selectAllBtn.clicked.connect(self.on_select_all_toggle)
        self.ui.clearBtn.clicked.connect(self.on_clear)
        self.ui.addMoreBtn.clicked.connect(self.on_append_files)
        self.ui.closeDetailBtn.clicked.connect(self.close)

        # 不需要重选
        self.ui.selectAllBtn.setVisible(False)

        self._select_all_state = True  # 切换用：第一次点击执行全选

        # 表头尺寸（可按需调整）
        self.ui.fileTable.horizontalHeader().setStretchLastSection(False)
        # 新增：禁用表头高亮，避免选中行时表头跟随加粗/高亮
        self.ui.fileTable.horizontalHeader().setHighlightSections(False)
        self.ui.fileTable.verticalHeader().setHighlightSections(False)
        # 新增：明确设定表头字体为非加粗（双保险）
        hfont = self.ui.fileTable.horizontalHeader().font()
        hfont.setBold(False)
        self.ui.fileTable.horizontalHeader().setFont(hfont)
        vfont = self.ui.fileTable.verticalHeader().font()
        vfont.setBold(False)
        self.ui.fileTable.verticalHeader().setFont(vfont)

        self.ui.fileTable.setTextElideMode(Qt.TextElideMode.ElideRight)
        self.ui.fileTable.setMouseTracking(True)
        _delegate = ElideTooltipDelegate(self.ui.fileTable)
        for _col in (1, 2, 5):
            self.ui.fileTable.setItemDelegateForColumn(_col, _delegate)

        # 隐藏"选择"列（第0列），保留功能以备后续业务变更
        self.ui.fileTable.setColumnHidden(0, True)

        # 连接表格点击事件
        self.ui.fileTable.itemClicked.connect(self.on_table_item_clicked)
    # 填充表格
    def populate(self, files: list, base_dir: str | None):
        table = self.ui.fileTable
        table.clearContents()
        table.setRowCount(len(files))

        for row, f in enumerate(files):
            # 0 选择
            chk = QCheckBox()
            chk.setChecked(bool(f.get('selected')))
            chk.stateChanged.connect(lambda state, p=f['path']: self.on_checked_changed(p, state))
            #table.setCellWidget(row, 0, chk)
            # 新增：用容器 + 居中布局包裹复选框，实现居中
            container = QWidget()
            layout = QHBoxLayout(container)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(chk)
            table.setCellWidget(row, 0, container)

            # 1 文件名
            item_name = QTableWidgetItem(f.get('name', ''))
            table.setItem(row, 1, item_name)

            # 2 文件路径
            # rel = f.get('rel', os.path.basename(f.get('path', '')))
            full_path = os.path.abspath(f.get('path', ''))
            item_rel = QTableWidgetItem(full_path)
            item_rel.setToolTip(full_path)
            table.setItem(row, 2, item_rel)

            # 3 类型
            item_ext = QTableWidgetItem(f.get('ext', '').upper())
            item_ext.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            table.setItem(row, 3, item_ext)

            # 4 大小
            item_size = QTableWidgetItem(format_size(f.get('size', 0)))
            item_size.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            table.setItem(row, 4, item_size)

            # 5 状态
            item_status = QTableWidgetItem(f.get('status', ''))
            item_status.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            table.setItem(row, 5, item_status)

            # 6 移除按钮
            btn = QPushButton("移除")
            btn.setProperty("path", f['path'])
            btn.clicked.connect(self.on_remove_clicked)
            table.setCellWidget(row, 6, btn)

        # 更新数量条
        self.update_count_label()

        # 可选：设置列宽
        try:
            table.setColumnWidth(0, 60)  # 隐藏列，保留原设置
            table.setColumnWidth(1, 193)  # 原160 + 30 = 190
            table.setColumnWidth(2, 233)  # 原200 + 30 = 230
            table.setColumnWidth(3, 60)
            table.setColumnWidth(4, 80)
            table.setColumnWidth(5, 100)
            table.setColumnWidth(6, 80)
        except Exception:
            pass

    def update_count_label(self):
        count = sum(1 for f in self.parent.batch_files if f.get('selected'))
        self.ui.fileCount.setText(f"已选择文件：{count} 个")
        self.parent.update_selected_summary()

    # 选择/反选切换
    def on_select_all_toggle(self):
        for f in self.parent.batch_files:
            f['selected'] = self._select_all_state
        # 刷新表格复选框状态
        self.populate(self.parent.batch_files, self.parent.batch_base_dir)
        # 翻转下次状态
        self._select_all_state = not self._select_all_state

    # 清空列表
    def on_clear(self):
        # # 如果列表为空，直接返回
        # if not self.parent.batch_files :
        #     return
        #
        # # 显示确认对话框
        # if not show_confirm(
        #     self,
        #     "确认清空",
        #     "是否清空转换列表？\n\n注意：当前正在转换的任务不会被清除，也不会被停止。"
        # ):
        #     # 用户点击取消，什么也不做
        #     return
        #
        # self.parent.batch_files.clear()
        # 检查是否有非"未处理"状态的文件
        processed_files = []
        unprocessed_files = []

        for f in self.parent.batch_files:
            file_status = f.get('status', '未处理')
            if file_status in ['完成', '处理中', '失败']:
                processed_files.append(f)
            else:
                unprocessed_files.append(f)

        # 如果有已处理的文件，提示用户
        if processed_files:
            processed_count = len(processed_files)
            unprocessed_count = len(unprocessed_files)

            if unprocessed_count == 0:
                # 全部都是已处理的文件
                show_warning(self, "无法清空",
                             f"列表中的 {processed_count} 个文件都已处理完成，无法清空。\n只能清空状态为【未处理】的文件。")
                return
            else:
                # 部分文件已处理
                if not show_confirm(self, "部分清空",
                                    f"列表中有 {processed_count} 个已处理的文件无法清空。\n\n是否清空剩余的 {unprocessed_count} 个【未处理】文件？"):
                    return

                # 只清空未处理的文件，保留已处理的文件
                self.parent.batch_files = processed_files
        else:
            # 全部都是未处理的文件，正常清空流程
            if not show_confirm(self, "确认清空",
                                "是否清空转换列表？\n\n您可以稍后重新添加这些文件。"):
                return

            self.parent.batch_files.clear()

        # 同步更新批量处理缓存
        if hasattr(self.parent, 'transcriber') and self.parent.transcriber:
            if hasattr(self.parent.transcriber, 'batch_files') and self.parent.transcriber.batch_files:
                # 从转录器的批量文件列表中移除被清空的文件
                remaining_paths = {f['path'] for f in self.parent.batch_files}
                self.parent.transcriber.batch_files = [path for path in self.parent.transcriber.batch_files
                                                       if path in remaining_paths]
                logger_manager.info(f"🗑️ 已同步更新批量处理缓存", "BatchFileListWindow", show_in_ui=True)

        # 重新填充表格
        self.populate(self.parent.batch_files, self.parent.batch_base_dir)
        
        # # 清空父窗口的textEdit内容
        # self.parent.ui.textEdit.clear()
        # # 更新textEdit的提示
        # self.parent.update_textEdit_tip()
        # 如果列表完全清空，清空父窗口的textEdit内容
        if not self.parent.batch_files:
            self.parent.ui.textEdit.clear()
            # 更新textEdit的提示
            self.parent.update_textEdit_tip()

        # 更新底部统计信息
        self.parent.update_selected_summary()

    # 追加文件
    def on_append_files(self):
        """
        追加文件, 如果想把新增项插入到列表前面, 那么就可以在这里将新项插入到batch_files的头部, 而不是append
        """
        allowed = "音视频文件 (*.mp4 *.mov *.mkv *.avi *.flv *.wav *.mp3);;所有文件 (*.*)"
        start_dir = self.parent.batch_base_dir or self.parent.settings.value("last_directory", os.getcwd())
        files, _ = QFileDialog.getOpenFileNames(self, "追加文件", start_dir, allowed)
        if not files:
            return
        # existing_paths = {f['path'] for f in self.parent.batch_files}
        # 已存在的文件集合
        existing_paths = {
            os.path.normcase(os.path.abspath(f['path'])) for f in self.parent.batch_files
        }
        for full in files:
            if not os.path.isfile(full):
                continue
            ext = os.path.splitext(full)[1].lower()
            if ext not in {'.mp4', '.mov', '.mkv', '.avi', '.flv', '.wav', '.mp3'}:
                continue

            full_norm = os.path.normcase(os.path.abspath(full))
            if full_norm in existing_paths:
                # 重复：弹提示并跳过
                base = os.path.basename(full)
                name_noext, ext_upper = os.path.splitext(base)
                display = f"{name_noext}{ext_upper.upper()}"
                show_warning(self, "提示", f"您选择的文件  【 {display} 】已存在于列表中, 请重新选择")
                continue

            size = os.path.getsize(full)
            # 如果想把新增项插入到列表前面, 那么就可以在这里将新项插入到batch_files的头部, 而不是append
            self.parent.batch_files.append({
                'path': full,
                'name': os.path.basename(full),
                'rel': os.path.relpath(full, self.parent.batch_base_dir or os.path.dirname(full)),
                'ext': ext.lstrip('.'),
                'size': size,
                'status': '未处理',
                'selected': True,
            })
            # 将本次成功追加的文件也加入已存在集合，避免同一批次内重复
            existing_paths.add(full_norm)

        self.populate(self.parent.batch_files, self.parent.batch_base_dir)

    # 勾选变更
    def on_checked_changed(self, path: str, state: int):
        for f in self.parent.batch_files:
            if f['path'] == path:
                f['selected'] = (state == Qt.Checked)
                break
        self.update_count_label()

    # 移除一行
    def on_remove_clicked(self):
        btn = self.sender()
        path = btn.property("path")

        # 检查文件状态，只允许移除"未处理"的文件
        # 获取文件名和状态
        file_name = os.path.basename(path)
        file_status = None
        for f in self.parent.batch_files:
            if f['path'] == path:
                file_status = f.get('status', '未处理')
                break

        # 如果文件状态不是"未处理"，则禁止移除
        for f in self.parent.batch_files:
            if f['path'] == path:
                file_status = f.get('status', '未处理')
                break

        if file_status in ['完成', '处理中', '失败']:
            from utils import show_warning
            show_warning(self, "无法移除", f"无法移除状态为【{file_status}】的文件。\n只能移除状态为【未处理】的文件。")
            return

        # 对于"未处理"状态的文件，弹出确认对话框
        if not show_confirm(self, "确认移除", f"是否删除 {file_name} ？\n\n您可以稍后重新添加。"):
            return  # 用户点击取消，不执行移除操作
        # 从数据移除
        self.parent.batch_files = [f for f in self.parent.batch_files if f['path'] != path]

        # ✅ 同步更新批量处理缓存：如果当前有批量处理正在进行，需要同步更新缓存的文件列表
        if hasattr(self.parent, 'transcriber') and self.parent.transcriber:
            if hasattr(self.parent.transcriber, 'batch_files') and self.parent.transcriber.batch_files:
                # 从转录器的批量文件列表中移除该文件
                self.parent.transcriber.batch_files = [f for f in self.parent.transcriber.batch_files if f != path]
                logger_manager.info(f"🗑️ 已从批量处理缓存中移除文件: {os.path.basename(path)}", "BatchFileListWindow",
                                    show_in_ui=True)

        # 重新填充表格
        self.populate(self.parent.batch_files, self.parent.batch_base_dir)

    def on_table_item_clicked(self, item):
        """处理表格项点击事件"""
        if not item:
            return

        # 获取点击行的文件路径和状态
        row = item.row()
        table = self.ui.fileTable

        # 获取文件路径（第2列）
        path_item = table.item(row, 2)
        if not path_item:
            return
        file_path = path_item.text()

        # 获取文件状态（第5列）
        status_item = table.item(row, 5)
        if not status_item:
            return
        file_status = status_item.text()

        # 如果状态为"完成"或"处理中"，弹出提示
        if file_status in ['完成', '处理中', '失败']:
            from utils import show_warning
            file_name = os.path.basename(file_path)
            show_warning(self, "文件状态提示",f"文件：{file_name}\n状态：{file_status}\n\n只能移除状态为【未处理】的文件。")