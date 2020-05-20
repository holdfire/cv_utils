"""
image processing utils, created by Liu Xing on 2020/05/20. including:
blur_image
draw_point
draw_rect
padding_image
"""
import numpy as np
import cv2



def blur_image(img, bboxes, ksize=(25, 25)):
    """
    在原图矩形范围进行高斯模糊（打马赛克）
    :param img: 经过cv2读取后的numpy.ndarray类型数据
    :param bboxes: 每个bbox的顺序是x1, x2, y1, y2。示例：[[50, 250, 253, 435], [430, 530, 453, 635]]
    :param ksize: 默认参数
    :return:
    """
    bboxes = np.array(bboxes).reshape((-1, 4))
    bboxes = bboxes.astype(np.int32)
    for bbox in bboxes:
        x1, x2, y1, y2 = bbox
        img[y1:y2+1, x1:x2+1, ] = cv2.blur(img[y1:y2+1, x1:x2+1, ], ksize)
    return img

def draw_point(img, pts):
    """
    在原图中画点
    :param img:
    :param points: 示例：[[100, 100], [200, 200], [300, 300]]
    :return:
    """
    pts = np.array(pts).reshape((-1, 2))
    pts = pts.astype(np.int32)
    for pt in pts:
        x, y = pt
        img = cv2.circle(img, (x,y), radius=2, color=(0,0,255), thickness=-1)
    return img

def draw_rect(img, bboxes):
    """
    在原图中画矩形框
    :param img: 经过cv2读取后的numpy.ndarray类型数据
    :param bboxes: 每个bbox的顺序是x1, y1, x2, y2，示例[[50.3, 200, 220, 335], [230, 350, 453, 535]]
    :return:
    """
    bboxes = np.array(bboxes).reshape((-1, 4))
    bboxes = bboxes.astype(np.int32)
    for bbox in bboxes:
        x1, y1, x2, y2 = bbox
        img = cv2.rectangle(img, (x1, y1), (x2, y2), color=(0, 0, 255), thickness=1)
    return img

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
    pts = [[100, 100], [200, 200], [300, 300]]
    img_new = draw_point(img, pts)
    cv2.imwrite("result.jpg", img_new)





