import os
from moviepy.editor import VideoFileClip

# 获取当前文件夹下的所有文件
file_list = os.listdir()

# 循环遍历每个文件
for file in file_list:
    # 判断是否是.mov文件
    if file.endswith(".mov"):
        # 打开视频文件
        video = VideoFileClip(file)

        # 将.mov文件转换为.mp4文件
        video.write_videofile(file[:-4] + ".mp4")

        # 删除原始.mov文件
        os.remove(file)

