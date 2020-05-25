import os
import shutil
import numpy as np


def pick_files(file_list, src_dir, dst_dir):
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
            shutil.copyfile(src_path, dst_path)
    return


if __name__ == "__main__":
    file_list = "../../tmp/json1/image_list.txt"
    src_dir = "../../tmp/raptor_result"
    dst_dir = "../../tmp/image1"
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)

    pick_files(file_list, src_dir, dst_dir)


