# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QWidget
from MainWin import Ui_MainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys
import os
from PIL import Image, ImageQt
import numpy as np
import image_utils
from stylize import Stylizer



class MainWindow(QMainWindow, QWidget):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 样式映射
        self.style_list = {
            'style1': ['style1.pt', 'images/styleImgs/1.jpg'],
            'style2': ['style2.pt', 'images/styleImgs/2.jpg'],
            'style3': ['style3.pt', 'images/styleImgs/3.jpg']
        }
        self.ch_style_dict = {'梵高风格': 'style1', '网格风格': 'style2', '彩笔风格': 'style3'}

        self.show_height = 330
        self.show_width = 420

        self.init_ui()
        self.connect_signals()

    def init_ui(self):
        # 初始化状态
        self.org_path = None
        self.stylized_img = None
        self.ui.label_4.setStyleSheet("color: red;")

        # 初始化下拉框和风格图
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(self.ch_style_dict.keys())
        self.choose_style = self.ch_style_dict[self.ui.comboBox.currentText()]
        self.ui.styleLb.setPixmap(QPixmap(self.style_list[self.choose_style][1]))

        # 模型加载
        self.model_path = os.path.join('models', self.style_list[self.choose_style][0])
        self.model = Stylizer(self.model_path)

        # 设置背景图片（推荐设置在 centralwidget 上）
        self.ui.centralwidget.setStyleSheet("background-image: url(./images/backgroud-pic.jpg); background-repeat: no-repeat; background-position: center;")

    def connect_signals(self):
        self.ui.imgBtn.clicked.connect(self.get_image_file)
        self.ui.chageBtn.clicked.connect(self.change_img_style)
        self.ui.comboBox.currentIndexChanged.connect(self.change_style)
        self.ui.saveBtn.clicked.connect(self.save_img)
        self.ui.actionopen.triggered.connect(self.get_image_file)
        self.ui.action.triggered.connect(self.save_img)

    def get_image_file(self):
        file_path, _ = QFileDialog.getOpenFileName(None, '打开图片', './', "Image files (*.jpg *.gif *.png)")
        if not file_path:
            return

        self.org_path = file_path
        self.org_img = Image.open(self.org_path)
        img_width, img_height = self.get_resize_size(self.org_img)

        pixmap = QPixmap(self.org_path).scaled(img_width, img_height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.orgImg.setPixmap(pixmap)
        self.ui.orgImg.setAlignment(Qt.AlignCenter)
        self.ui.TransImg.setPixmap(QPixmap(""))

        self.ui.lineEdit.setText(file_path)

    def change_style(self):
        self.choose_style = self.ch_style_dict[self.ui.comboBox.currentText()]
        self.ui.styleLb.setPixmap(QPixmap(self.style_list[self.choose_style][1]))
        self.model_path = os.path.join('models', self.style_list[self.choose_style][0])
        self.model = Stylizer(self.model_path)

    def get_resize_size(self, img):
        img_width, img_height = img.size
        ratio = img_width / img_height
        if ratio >= self.show_width / self.show_height:
            width = self.show_width
            height = int(width / ratio)
        else:
            height = self.show_height
            width = int(height * ratio)
        return width, height

    def resize_image(self, img):
        width, height = self.get_resize_size(img)
        return img.resize((width, height), Image.LANCZOS)

    def change_img_style(self):
        if self.org_path is None:
            QMessageBox.information(self, '提示', '请先选择一张图片！')
            return

        image_pil = Image.open(self.org_path).convert("RGB")
        img_width, img_height = self.get_resize_size(image_pil)
        resized = image_pil.resize((img_width * 2, img_height * 2), Image.LANCZOS)

        image_np = np.array(resized).astype(np.float32) / 255.0
        self.stylized_img = self.model.stylize(image_np)

        final_img = image_utils.to_pil(self.stylized_img)
        resized_final = self.resize_image(final_img)

        self.ui.TransImg.setPixmap(ImageQt.toqpixmap(resized_final))
        self.ui.TransImg.setAlignment(Qt.AlignCenter)

    def save_img(self):
        if self.stylized_img is None:
            QMessageBox.information(self, '提示', '请先转换图片！')
            return

        _, img_name = os.path.split(self.org_path)
        save_path = os.path.join('save_imgs', self.choose_style + '_' + img_name)
        image_utils.save(self.stylized_img, save_path)

        QMessageBox.information(self, '提示', '图片保存成功！')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

