from PIL import Image
import os

# 设置原始图像文件夹路径和目标文件夹路径
input_folder = '01'
output_folder = '02'

# 遍历所有图像文件
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg'):  # 只处理.jpg文件
        # 打开图像
        filepath = os.path.join(input_folder, filename)
        img = Image.open(filepath)

        # 获取图像的宽度和高度
        width, height = img.size

        # 将图像从中间垂直剪切
        left_img = img.crop((0, 0, width/2, height))
        right_img = img.crop((width/2, 0, width, height))

        # 创建新的文件名
        name, ext = os.path.splitext(filename)
        left_filename = f'{name}_1{ext}'
        right_filename = f'{name}_2{ext}'
        left_filepath = os.path.join(output_folder, left_filename)
        right_filepath = os.path.join(output_folder, right_filename)

        # 保存两个剪切后的图像
        left_img.save(left_filepath)
        right_img.save(right_filepath)