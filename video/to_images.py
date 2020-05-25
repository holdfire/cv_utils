"""
video processing utils, created by Liu Xing on 2020/05/20. including:
video2images

"""
import os
import cv2

def video2images(video_path, image_save_dir, frame_interval=3, resize=False, new_size=(128, 128)):
    video = cv2.VideoCapture(video_path)
    count = 0
    rval = video.isOpened()
    while rval:
        count = count + 1
        rval, frame = video.read()
        if count % frame_interval != 0:
            continue
        if resize:
            frame = cv2.resize(frame, new_size, interpolation=cv2.INTER_CUBIC)
        # 最后一帧为空，需要丢弃掉
        if frame is not None:
            image_name = video_path + "_" + str(count) + ".png"
            image_path = os.path.join(image_save_dir, image_name)
            cv2.imwrite(image_path, frame)
    return image_save_dir




if __name__ == "__main__":
    video_path = ""