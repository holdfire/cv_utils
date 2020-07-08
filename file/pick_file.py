import os
import shutil
import numpy as np

def get_file_list(file_dir, file_list):
    with open(file_list, 'w') as f:
        for i in os.listdir(file_dir):
            i = i.split(".txt")[0] + ".jpg"
            f.writelines(i)
            f.write('\n')
    return


def pick_files(file_list, src_dir, dst_dir, method="copy"):
    """
    pick files in file_list, then move it from src_dir to dst_dir.
    """
    list = np.loadtxt(file_list, dtype='str')
    # # 如果list中包含的文件名后缀需要改，取消下面代码的注释
    # for i in range(len(list)):
    #     list[i] = list[i].split(".json")[0] + ".jpg"

    for file in os.listdir(src_dir):
        if file in list:
            src_path = os.path.join(src_dir, file)
            dst_path = os.path.join(dst_dir, file)
            if method == "copy":
                shutil.copyfile(src_path, dst_path)
            elif method == "move":
                shutil.move(src_path, dst_path)
    return


if __name__ == "__main__":
    file_dir = "../../faceAlignment/dataset_train/train_inspect4/landmark_standard"
    file_list = "../../faceAlignment/dataset_train/train_inspect4/image_list.txt"
    get_file_list(file_dir, file_list)

    src_dir = "../../faceAlignment/dataset_train/original/Blur"
    dst_dir = "../../faceAlignment/dataset_train/train_inspect4/images"
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)

    pick_files(file_list, src_dir, dst_dir)


