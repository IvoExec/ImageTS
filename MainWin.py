# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(932, 850)
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.centralLayout.setContentsMargins(10, 10, 10, 10)
        self.centralLayout.setSpacing(10)

        font_title = QtGui.QFont("微软雅黑", 30)
        font_subtitle = QtGui.QFont("微软雅黑", 16)
        font_label = QtGui.QFont("微软雅黑", 14)
        font_btn = QtGui.QFont("微软雅黑", 14)
        font_input = QtGui.QFont("微软雅黑", 16)

        # 顶部标题栏
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame2_layout = QtWidgets.QVBoxLayout(self.frame_2)
        frame2_layout.setContentsMargins(10, 10, 10, 10)
        self.label = QtWidgets.QLabel("图片风格转换系统")
        self.label.setFont(font_title)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4 = QtWidgets.QLabel("By IvoExec")
        self.label_4.setFont(font_subtitle)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        frame2_layout.addWidget(self.label)
        frame2_layout.addWidget(self.label_4)
        self.centralLayout.addWidget(self.frame_2)

        # 中部图片展示区域
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        imageLayout = QtWidgets.QHBoxLayout(self.frame)
        imageLayout.setSpacing(20)

        self.groupBox = QtWidgets.QGroupBox("原图")
        self.groupBox.setFont(font_label)
        self.orgImg = QtWidgets.QLabel()
        self.orgImg.setStyleSheet("background-color: white;")
        self.orgImg.setScaledContents(True)
        self.orgImg.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        groupBoxLayout1 = QtWidgets.QVBoxLayout()
        groupBoxLayout1.addWidget(self.orgImg)
        self.groupBox.setLayout(groupBoxLayout1)

        self.groupBox_2 = QtWidgets.QGroupBox("风格转换图")
        self.groupBox_2.setFont(font_label)
        self.TransImg = QtWidgets.QLabel()
        self.TransImg.setStyleSheet("background-color: white;")
        self.TransImg.setScaledContents(True)
        self.TransImg.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        groupBoxLayout2 = QtWidgets.QVBoxLayout()
        groupBoxLayout2.addWidget(self.TransImg)
        self.groupBox_2.setLayout(groupBoxLayout2)

        imageLayout.addWidget(self.groupBox)
        imageLayout.addWidget(self.groupBox_2)
        self.centralLayout.addWidget(self.frame)

        # 功能区域 frame_3
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setStyleSheet("background-color: rgb(232, 232, 232);")
        funcLayout = QtWidgets.QVBoxLayout(self.frame_3)
        funcLayout.setContentsMargins(20, 20, 20, 20)
        funcLayout.setSpacing(20)

        # 顶部功能按钮
        topFuncLayout = QtWidgets.QHBoxLayout()

        # 左侧：选择风格
        left = QtWidgets.QVBoxLayout()
        lblStyle = QtWidgets.QLabel("选择风格")
        lblStyle.setFont(font_label)
        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.setFont(QtGui.QFont("Agency FB", 16))
        left.addWidget(lblStyle)
        left.addWidget(self.comboBox)

        # 中间：风格图
        center = QtWidgets.QVBoxLayout()
        self.styleLb = QtWidgets.QLabel()
        self.styleLb.setStyleSheet("background-color: white;")
        self.styleLb.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.styleLb.setScaledContents(True)
        center.addWidget(self.styleLb)

        # 右侧：按钮
        right = QtWidgets.QVBoxLayout()
        self.chageBtn = QtWidgets.QPushButton("风格转换")
        self.chageBtn.setFont(font_btn)
        self.saveBtn = QtWidgets.QPushButton("保存图片")
        self.saveBtn.setFont(font_btn)
        right.addWidget(self.chageBtn)
        right.addWidget(self.saveBtn)

        topFuncLayout.addLayout(left)
        topFuncLayout.addStretch()
        topFuncLayout.addLayout(center)
        topFuncLayout.addStretch()
        topFuncLayout.addLayout(right)

        # 图片载入栏
        bottomLayout = QtWidgets.QHBoxLayout()
        self.label_3 = QtWidgets.QLabel("图片载入")
        self.label_3.setFont(QtGui.QFont("微软雅黑", 20))
        self.imgBtn = QtWidgets.QPushButton()
        self.imgBtn.setFixedSize(30, 30)
        self.imgBtn.setStyleSheet("border-image: url(:/img/fileIcon2.png);")
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setFont(font_input)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setPlaceholderText("请选择一张图片")

        bottomLayout.addWidget(self.label_3)
        bottomLayout.addWidget(self.imgBtn)
        bottomLayout.addWidget(self.lineEdit)

        funcLayout.addLayout(topFuncLayout)
        funcLayout.addLayout(bottomLayout)
        self.centralLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        # 菜单栏
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menu = QtWidgets.QMenu("文件")
        self.menu_2 = QtWidgets.QMenu("帮助")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.actionopen = QtWidgets.QAction("图片载入", MainWindow)
        self.action = QtWidgets.QAction("保存图片", MainWindow)
        self.menu.addAction(self.actionopen)
        self.menu.addAction(self.action)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图片风格转换系统"))


