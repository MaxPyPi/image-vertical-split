import os
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
from PIL import Image

def browse_input_folder():
    global input_folder
    input_folder = filedialog.askdirectory()
    input_folder_label.config(text=input_folder)

def browse_output_folder():
    global output_folder
    output_folder = filedialog.askdirectory()
    output_folder_label.config(text=output_folder)

def split_images():
    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg'):
            filepath = os.path.join(input_folder, filename)
            img = Image.open(filepath)

            width, height = img.size

            left_img = img.crop((0, 0, width/2, height))
            right_img = img.crop((width/2, 0, width, height))

            name, ext = os.path.splitext(filename)
            left_filename = f'{name}_1{ext}'
            right_filename = f'{name}_2{ext}'
            left_filepath = os.path.join(output_folder, left_filename)
            right_filepath = os.path.join(output_folder, right_filename)

            left_img.save(left_filepath)
            right_img.save(right_filepath)

def about():
    messagebox.showinfo("关于", "制作：易开网 www.yikai.cn + ChatGPT\n反馈邮箱：yufz@yikay.com\n时间：2023/04/18")

app = Tk()
app.title("图片中间竖分")
app.geometry("400x400")

menu = Menu(app)
app.config(menu=menu)

helpmenu = Menu(menu)
menu.add_cascade(label="帮助", menu=helpmenu)
helpmenu.add_command(label="关于", command=about)

input_frame = Frame(app)
input_frame.pack(pady=10)
input_folder_label = Label(input_frame, text="源目录：")
input_folder_label.grid(row=0, column=0, padx=5)
input_folder_button = Button(input_frame, text="浏览", command=browse_input_folder)
input_folder_button.grid(row=0, column=1)

output_frame = Frame(app)
output_frame.pack(pady=10)
output_folder_label = Label(output_frame, text="目标目录：")
output_folder_label.grid(row=0, column=0, padx=5)
output_folder_button = Button(output_frame, text="浏览", command=browse_output_folder)
output_folder_button.grid(row=0, column=1)

split_button = Button(app, text="分割执行", command=split_images, bg="green", fg="white")
split_button.pack(pady=20)

app.mainloop()