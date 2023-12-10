import os
import random
from moviepy.editor import VideoFileClip, concatenate_videoclips,AudioFileClip, CompositeVideoClip, vfx
from moviepy.audio.fx.volumex import volumex




"""设置参数
music_file 使用什么音乐
video_folder 来源那里的视频
output_folder 输出到什么文件夹
----------------------------
cue_point 顺序之间间隔多长时间
video_angle 反转多少度
videlo_factor 对比度增加多少倍

"""
music_file = "input_music/music.mp3"
video_folder = "input_videos/"
output_folder = "output_videos/"

# 瓜瓜
cue_point = 1600 
video_angle = -0.1
videlo_factor = 1.11

# 黄冈
# cue_point = 2000 
# video_angle = -0.2
# videlo_factor = 1.2


# 获得所有视频文件
# video_files = [f for f in os.listdir(video_folder) if f.endswith(".MP4")]
video_files = [f for f in os.listdir(video_folder) if f.lower().endswith(".mp4")]


# 处理每一个视频文件
for video_file in video_files:

     
    video = VideoFileClip(video_folder + video_file)
    
    # 跳过小于9秒的视频
    video_duration = video.duration
    if video_duration < 8.5:  
        continue
    
    # 去掉音轨
    video_without_audio = video.without_audio()
    video_without_audio.write_videofile(video_folder + video_file.split(".")[0] + "_new.mp4")

    # 分割视频
    video_clips = []
    duration = int(video.duration * 1000)
    for start in range(0, duration, cue_point):
        end = min(start + cue_point, duration)
        video_clips.append(video.subclip(start/1000, end/1000))

    # 打乱顺序
    random.shuffle(video_clips)

    # 合并视频
    max_video = concatenate_videoclips(video_clips)

    # 如果需要水平翻转视频（镜像），可以打开此行代码👇 不需要刻意注释掉
    # 水平翻转
    max_video = max_video.fx(vfx.mirror_x)
    # 如果需要水平翻转视频（镜像），可以打开此行代码👆

    # 增加对比度和反转180度
    max_video = max_video.fx(vfx.colorx, factor=videlo_factor).fx(vfx.rotate, angle=video_angle)

    # 获得音乐文件并进行剪辑
    music = AudioFileClip(music_file)
    if max_video.duration > music.duration:
        max_video = max_video.set_duration(music.duration)
    else:
        max_video = max_video.set_duration(max_video.duration)


    # 增加音量
    music = volumex(music, 0.5)

    # 添加音轨
    final_video = max_video.set_audio(music)
    # 导出合成的视频
    final_video.write_videofile(output_folder + video_file.split(".")[0] + "_final.mp4", audio_codec='aac')





# ******************备份**********************
# import os
# import random
# from moviepy.editor import VideoFileClip, concatenate_videoclips,AudioFileClip, CompositeVideoClip
# from moviepy.audio.fx.volumex import volumex

# # 设置参数
# music_file = "input_music/music.mp3"
# cue_point = 1500
# video_folder = "input_videos/"
# output_folder = "output_videos/"

# # 获得所有视频文件
# # video_files = [f for f in os.listdir(video_folder) if f.endswith(".MP4")]
# video_files = [f for f in os.listdir(video_folder) if f.lower().endswith(".mp4")]


# # 处理每一个视频文件
# for video_file in video_files:

#      # 去掉音轨
#     video = VideoFileClip(video_folder + video_file)
#     video_without_audio = video.without_audio()
#     video_without_audio.write_videofile(video_folder + video_file.split(".")[0] + "_new.mp4")

#     # 分割视频
#     video_clips = []
#     duration = int(video.duration * 1000)
#     for start in range(0, duration, cue_point):
#         end = min(start + cue_point, duration)
#         video_clips.append(video.subclip(start/1000, end/1000))

#     # 打乱顺序
#     random.shuffle(video_clips)

#     # 合并视频
#     max_video = concatenate_videoclips(video_clips)

#     # 获得音乐文件并进行剪辑

#     music = AudioFileClip(music_file)
#     if max_video.duration > music.duration:
#         # music = music.set_duration(max_video.duration)
#         max_video = max_video.set_duration(music.duration)
#     else:
#         # max_video = max_video.set_duration(music.duration)
#         max_video = max_video.set_duration(max_video.duration)


#     # 增加音量
#     music = volumex(music, 0.5)

#     # 添加音轨
#     final_video = max_video.set_audio(music)
#     # 导出合成的视频
#     final_video.write_videofile(output_folder + video_file.split(".")[0] + "_final.mp4", audio_codec='aac')


