import numpy as np
import cv2


def padding_image(img, pads, value):
    """
    对图像的四个边缘进行填充
    :param img:
    :param pad:
    :return:
    """
    top, bottom, left, right = pads
    img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=value)
    return img

if __name__ == "__main__":
    img = cv2.imread("./test.jpg")
    pads = [10, 10, 10, 10]
    img_new = padding_image(img, pads)
    cv2.imwrite("result.jpg", img_new)

