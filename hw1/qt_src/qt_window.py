# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'srs1.0.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SRS(object):
    def setupUi(self, SRS):
        SRS.setObjectName("SRS")
        SRS.resize(900, 600)
        self.widget = QtWidgets.QWidget(SRS)
        self.widget.setGeometry(QtCore.QRect(10, 10, 800, 500))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 4, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_3.setMouseTracking(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setDefault(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 4, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 2)
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_3.raise_()
        self.label_3.raise_()

        #后面添加
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.gridLayout.addLayout(self.horizontalLayout, 10, 5, 2, 2)

        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.gridLayout.addLayout(self.horizontalLayout, 10, 5, 2, 2)

        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.gridLayout.addLayout(self.horizontalLayout, 10, 5, 2, 2)

        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.gridLayout.addLayout(self.horizontalLayout, 10, 5, 2, 2)

        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout.addWidget(self.pushButton_8)
        self.gridLayout.addLayout(self.horizontalLayout, 10, 5, 2, 2)

        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        self.pushButton_9.setObjectName("pushButton_8")
        self.horizontalLayout.addWidget(self.pushButton_9)
        self.gridLayout.addLayout(self.horizontalLayout, 10, 5, 2, 2)

        self.retranslateUi(SRS)
        self.pushButton_3.clicked.connect(SRS.close)
        QtCore.QMetaObject.connectSlotsByName(SRS)


    def retranslateUi(self, SRS):
        _translate = QtCore.QCoreApplication.translate
        SRS.setWindowTitle(_translate("SRS", "Dialog"))
        self.label.setText(_translate("SRS", "请输入文件所在路径："))
        self.pushButton.setText(_translate("SRS", "选择图片"))
        self.pushButton_2.setText(_translate("SRS", "选择输出路径"))
        self.label_2.setText(_translate("SRS", "输出文件夹："))
        self.label_3.setText(_translate("SRS", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_3.setText(_translate("SRS", "退出"))

        #后面添加
        self.pushButton_4.setText(_translate("SRS", "铅笔素描"))
        self.pushButton_5.setText(_translate("SRS", "中国画"))
        self.pushButton_6.setText(_translate("SRS", "白描"))
        self.pushButton_7.setText(_translate("SRS", "油画"))
        self.pushButton_8.setText(_translate("SRS", "单色素描"))
        self.pushButton_9.setText(_translate("SRS", "彩色素描"))
