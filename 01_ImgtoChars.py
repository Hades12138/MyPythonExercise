# encoding = utf-8
from PIL import Image
import argparse

# <----------------------命令行输入参数处理-------------------->

# 创建新对象
parser = argparse.ArgumentParser()

# 在创建的对象中添加关注的命令行参数和选项
parser.add_argument('file')   # 输入文件
parser.add_argument('-o-','--output') # 输出文件
parser.add_argument('--width',type = int,default = 80) # 输出字符画的宽度
parser.add_argument('--height',type = int,default = 80) # 输出字符画的宽度


# 调用parse_args（）方法进行解析
args = parser.parse_args()

# 使用
Img = args.file
Width = args.width
Height = args.height
output = args.output


#<----------------------处理图片----------------------->

ascii_chars = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 字符与RGB的对应映射关系
def get_char(r, g, b, alpha = 256):  # 256个灰度级，0-255
    if alpha == 0:
        return ' '
    lenght = len(ascii_chars)
    gray = int (0.2126 * r + 0.7152 * g + 0.0722 * b) # 灰度化计算方法，可以自己修改RGB的权重
    unit = 256.0 / lenght  # 定义单位，含义是一个字符长度可以表示几个灰度级，相当于采样精度
    return ascii_chars[int(gray / unit)]  # 根据灰度选择返回不同的字符，灰度除以单位，得到该灰度级有几个单位长度，即第几个字符


# 如果是自己执行的话，就执行下面的，如果是作为导入模块就不执行
if __name__ == '__main__' :
    im = Image.open(Img)

    im = im.resize((Width,Height),Image.NEAREST)
    # 第二个参数表示图片的质量，一共有4种，低质量Image.NEARSET,双线性Image.BILINEAR，三次样条插值Image.BICUBIC，高质量Image.ANTIALIAS
    txt = ""  # 预定义变量

    # 图像的惯例，xy和行列是反的
    for i in range (Height):
        for j in range(Width):
            txt += get_char(*im.getpixel((j, i)))  # 内部两个括号是为了把i,j作为一个元组传参进去；外面*是表示解析参数，把得到的像素参数解析出来

        txt += '\n'   # 循环一行之后要加回车，以便输出下一行

    print(txt)


# 字符输出到文件
if output:
    with open(output,'w') as  f:
        f.write(txt)
else:
    with open("output.txt",'w') as f:
        f.write(txt)


