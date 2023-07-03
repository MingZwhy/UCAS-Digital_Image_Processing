import cv2
import argparse
import numpy as np
import os

def get_origin_image(file_path):
    print(file_path)
    #读取图片
    img = cv2.imread(file_path)

    return img

def show_style_img(folder_path, style_img, style, show_result, file_path):
    # 获取文件夹路径
    # print(file_path.split('/')[-1].split('.')[0])
    output_path = folder_path + '/' + file_path.split('/')[-1].split('.')[0] + '_' + style + '.jpg'
    cv2.imwrite(output_path, style_img)
    if(show_result):
        cv2.imshow(style+'.jpg', style_img)
        cv2.waitKey()
        cv2.destroyAllWindows()

# 进行处理
def pencil_mode(file_path, folder_path, show_result):
    try:
        img = get_origin_image(file_path)

        # 展示原图
        if(show_result):
            print("show!")
            cv2.imshow('original', img)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Blur the image using Gaussian Blur
        # 高斯核服从正态分布，核数越大，越模糊
        gray_blur = cv2.GaussianBlur(gray, (75, 75), 0)
        # Convert the image into pencil sketch
        pencil_style = cv2.divide(gray, gray_blur, scale=250.0)

        show_style_img(folder_path, pencil_style, 'pencil_mode', show_result, file_path)

        success_result = r'转换成功！'
        print(success_result)

    except:
        fail_result = r'转换失败！'
        print(fail_result)

def Chinese_painting(file_path, folder_path, show_result):
    try:
        img = get_origin_image(file_path)

        # 展示原图
        if (show_result):
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

        show_style_img(folder_path, Chinese_painting, 'Chinese_painting', show_result, file_path)

        success_result = r'转换成功！'
        print(success_result)

    except:
        fail_result = r'转换失败！'
        print(fail_result)

def line_drawing(file_path, folder_path, show_result):
    try:
        img = get_origin_image(file_path)

        # 展示原图
        if (show_result):
            print("show!")
            cv2.imshow('original', img)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 3)
        edges = cv2.Laplacian(gray, -1, ksize=5)
        edges_inv = 255 - edges
        dummy, line_drawing = cv2.threshold(edges_inv, 0, 255, cv2.THRESH_BINARY)

        show_style_img(folder_path, line_drawing, 'line_drawing', show_result, file_path)

        success_result = r'转换成功！'
        print(success_result)

    except:
        fail_result = r'转换失败！'
        print(fail_result)

def oil_painting(file_path, folder_path, show_result):
    try:
        img = get_origin_image(file_path)

        # 展示原图
        if (show_result):
            print("show!")
            cv2.imshow('original', img)

        mix_pixel = int(img.shape[0] / 150)
        #print(mix_pixel)
        oil_painting = cv2.xphoto.oilPainting(img, mix_pixel, 1)

        show_style_img(folder_path, oil_painting, 'oil_painting', show_result, file_path)

        success_result = r'转换成功！'
        print(success_result)

    except:
        fail_result = r'转换失败！'
        print(fail_result)

def grey(file_path, folder_path, show_result):
    try:
        img = get_origin_image(file_path)

        # 展示原图
        if (show_result):
            print("show!")
            cv2.imshow('original', img)

        grey, color = cv2.pencilSketch(img, sigma_s=20, sigma_r=0.15, shade_factor=0.04)

        show_style_img(folder_path, grey, 'grey', show_result, file_path)

        success_result = r'转换成功！'
        print(success_result)

    except:
        fail_result = r'转换失败！'
        print(fail_result)

def color(file_path, folder_path, show_result):
    try:
        img = get_origin_image(file_path)

        # 展示原图
        if (show_result):
            print("show!")
            cv2.imshow('original', img)

        grey, color = cv2.pencilSketch(img, sigma_s=20, sigma_r=0.15, shade_factor=0.04)

        show_style_img(folder_path, color, 'color', show_result, file_path)

        success_result = r'转换成功！'
        print(success_result)

    except:
        fail_result = r'转换失败！'
        print(fail_result)


if __name__ == '__main__':
    # Parse command line arguments
    desc = "Choose file_path, save_folder and mode."

    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument(
        "-f", "--file_path", type = str, required=False, default="../test_img/mountain.png",
        help="the path of test img"
    )
    parser.add_argument(
        "-s", "--save_folder_path", type = str, required=False, default="../output/",
        help="save folder path"
    )
    parser.add_argument(
        "-m", "--trans_mode", type = str, required=False, default="all",
        help="pencil_mode / Chinese_painting / line_drawing / oil_painting / grey / color / all"
    )
    parser.add_argument(
        "-i", "--show_result", type = bool, required=False, default=False,
        help="if True, will show the result of trans"
    )
    gs = parser.parse_args()

    file_path = gs.file_path
    folder_path = gs.save_folder_path
    trans_mode = gs.trans_mode
    show_result = gs.show_result

    if not os.path.exists(file_path):
        if(os.path.exists(file_path.split('png')[0] + 'jpg')):
            file_path = file_path.split('png')[0] + 'jpg'
        else:
            print("file_path ", file_path, " doesn't exist!")
            exit(1)

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print("mkdir ", folder_path )

    if trans_mode == "pencil_mode":
        pencil_mode(file_path, folder_path, show_result)
    elif trans_mode == "Chinese_painting":
        Chinese_painting(file_path, folder_path, show_result)
    elif trans_mode == "line_drawing":
        line_drawing(file_path, folder_path, show_result)
    elif trans_mode == "oil_painting":
        oil_painting(file_path, folder_path, show_result)
    elif trans_mode == "grey":
        grey(file_path, folder_path, show_result)
    elif trans_mode == "color":
        color(file_path, folder_path, show_result)
    elif trans_mode == "all":
        pencil_mode(file_path, folder_path, show_result)
        Chinese_painting(file_path, folder_path, show_result)
        line_drawing(file_path, folder_path, show_result)
        oil_painting(file_path, folder_path, show_result)
        grey(file_path, folder_path, show_result)
        color(file_path, folder_path, show_result)
    else:
        print("wrong mode", trans_mode)
        print("pencil_mode / Chinese_painting / line_drawing / oil_painting / grey / color / all")
        exit(1)


