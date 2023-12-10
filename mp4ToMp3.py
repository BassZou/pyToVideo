from pydub import AudioSegment

# 输入文件名
input_file = "input.mp4"

# 读取mp4文件
audio = AudioSegment.from_file(input_file, format="mp4")

# 输出文件名
output_file = "output.mp3"

# 导出mp3文件
audio.export(output_file, format="mp3")
