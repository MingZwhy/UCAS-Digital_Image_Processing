from PyQt5 import QtWidgets
from qt_window import Ui_SRS # 导入ui文件转换后的py文件
from PyQt5.QtWidgets import QFileDialog
import pandas as pd

import cv2
import argparse
import numpy as np

class mywindow(QtWidgets.QWidget, Ui_SRS):
    def  __init__ (self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.write_folder)
        self.pushButton.clicked.connect(self.read_file)

        self.pushButton_4.clicked.connect(self.pencil_mode)  # 风格1
        self.pushButton_5.clicked.connect(self.Chinese_painting)  # 风格2
        self.pushButton_6.clicked.connect(self.line_drawing)  # 风格3
        self.pushButton_7.clicked.connect(self.oil_painting)  # 风格4
        self.pushButton_8.clicked.connect(self.grey)  # 风格5
        self.pushButton_9.clicked.connect(self.color)  # 风格6

    def read_file(self):
        #选取文件
        filename, filetype =QFileDialog.getOpenFileName(self, "选取文件", "C:/", "All Files(*);;Text Files(*.csv)")
        print(filename, filetype)
        self.lineEdit.setText(filename)

    def write_folder(self):
        #选取文件夹
        foldername = QFileDialog.getExistingDirectory(self, "选取文件夹", "C:/")
        print(foldername)
        self.lineEdit_2.setText(foldername)

    def get_origin_image(self):
        #style
        #1 for pencil-mode
        #2 for Chinese painting
        #3 for line drawing
        #4 for western painting
        #5 for pencil sketch

        #获取文件路径
        file_path = self.lineEdit.text()
        print(file_path)
        #读取图片
        img = cv2.imread(file_path)

        return img

    def show_style_img(self, style_img, style):
        # 获取文件夹路径
        folder_path = self.lineEdit_2.text()
        output_path = folder_path + '/' + style + '.jpg'
        cv2.imwrite(output_path, style_img)
        cv2.imshow(style+'.jpg', style_img)
        cv2.waitKey()
        cv2.destroyAllWindows()

    # 进行处理
    def pencil_mode(self):
        try:
            img = self.get_origin_image()

            # 展示原图
            #print("show!")
            cv2.imshow('original', img)

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Blur the image using Gaussian Blur
            # 高斯核服从正态分布，核数越大，越模糊
            gray_blur = cv2.GaussianBlur(gray, (75, 75), 0)
            # Convert the image into pencil sketch
            pencil_style = cv2.divide(gray, gray_blur, scale=250.0)

            self.show_style_img(pencil_style, 'pencil_mode')

            success_result = r'转换成功！'
            self.label_3.setText(success_result)

        except:
            fail_result = r'转换失败！'
            self.label_3.setText(fail_result)

    def Chinese_painting(self):
        try:
            img = self.get_origin_image()

            # 展示原图
            print("show!")
            cv2.imshow('original', img)

            # convert the image into grayscale image
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Blur the grayscale image with median blur中值滤波
            gray_blur = cv2.medianBlur(gray, 3)
            # Apply adaptive thresholding to detect edges检测图像边缘
            edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9,
                                              9)  # 自适应均值滤波
            # Sharpen the image锐化图像
            color = cv2.detailEnhance(img, sigma_s=5, sigma_r=0.5)
            Chinese_painting = cv2.bitwise_and(color, color, mask=edges)

            self.show_style_img(Chinese_painting, 'Chinese_painting')

            success_result = r'转换成功！'
            self.label_3.setText(success_result)

        except:
            fail_result = r'转换失败！'
            self.label_3.setText(fail_result)

    def line_drawing(self):
        try:
            img = self.get_origin_image()

            # 展示原图
            print("show!")
            cv2.imshow('original', img)

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray = cv2.medianBlur(gray, 3)
            edges = cv2.Laplacian(gray, -1, ksize=5)
            edges_inv = 255 - edges
            dummy, line_drawing = cv2.threshold(edges_inv, 0, 255, cv2.THRESH_BINARY)

            self.show_style_img(line_drawing, 'line_drawing')

            success_result = r'转换成功！'
            self.label_3.setText(success_result)

        except:
            fail_result = r'转换失败！'
            self.label_3.setText(fail_result)

    def oil_painting(self):
        try:
            img = self.get_origin_image()

            # 展示原图
            print("show!")
            cv2.imshow('original', img)

            mix_pixel = int(img.shape[0] / 150)
            #print(mix_pixel)
            oil_painting = cv2.xphoto.oilPainting(img, mix_pixel, 1)

            self.show_style_img(oil_painting, 'oil_painting')

            success_result = r'转换成功！'
            self.label_3.setText(success_result)

        except:
            fail_result = r'转换失败！'
            self.label_3.setText(fail_result)

    def grey(self):
        try:
            img = self.get_origin_image()

            # 展示原图
            print("show!")
            cv2.imshow('original', img)

            grey, color = cv2.pencilSketch(img, sigma_s=20, sigma_r=0.15, shade_factor=0.04)

            self.show_style_img(grey, 'grey')

            success_result = r'转换成功！'
            self.label_3.setText(success_result)

        except:
            fail_result = r'转换失败！'
            self.label_3.setText(fail_result)

    def color(self):
        try:
            img = self.get_origin_image()

            # 展示原图
            print("show!")
            cv2.imshow('original', img)

            grey, color = cv2.pencilSketch(img, sigma_s=20, sigma_r=0.15, shade_factor=0.04)

            self.show_style_img(color, 'color')

            success_result = r'转换成功！'
            self.label_3.setText(success_result)

        except:
            fail_result = r'转换失败！'
            self.label_3.setText(fail_result)

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    ui = mywindow()
    ui.show()
    sys.exit(app.exec_())