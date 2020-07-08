import os
import cv2
from pathlib import Path

def move_images(original_folder, save_folder):
    '''
    处理一个三层嵌套的文件夹original_folder，该文件夹的子目录，的子目录下面为jpg图片
    本函数将第三层的所有jpg图片移动到一个新的文件夹save_folder下
    注意：用cv2保存的jpeg格式图片，内容会被压缩
    '''
    for i in os.listdir(original_folder):
        path1 = os.path.join(original_folder, i)
        path1_new = Path(path1)
        if path1_new.is_dir():
            for j in os.listdir(path1):
                path2 = os.path.join(path1, j)
                path2_new = Path(path2)
                if path2_new.is_dir():
                    for k in os.listdir(path2):
                        path3 = os.path.join(path2, k)
                        if path3.split(".")[-1] == "jpg":
                            image = cv2.imread(path3)
                            cv2.imwrite(os.path.join(save_folder, k), image)
    return


if __name__ == "__main__":
    original_folder = "../../tmp/face-capture-20200422"
    save_folder = "../../datasets/face_capture"
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
    move_images(original_folder, save_folder)