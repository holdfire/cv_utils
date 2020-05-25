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

if __name__ == "__main__":
    img = cv2.imread("./test.jpg")
    bboxes = [[50, 250, 253, 435], [430, 530, 453, 635]]
    img_new = blur_image(img, bboxes)
    cv2.imwrite("result.jpg", img_new)