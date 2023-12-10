import os

# 获取文件夹中所有文件的列表
files = os.listdir("input_videos")

# 遍历所有文件
for file in files:
    # 判断文件名是否包含 "new"
    if "new" in file:
        # 构造文件的完整路径
        file_path = os.path.join("input_videos", file)
        # 删除文件
        os.remove(file_path)
