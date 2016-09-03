import PIL
from PIL import Image

cave = Image.open('cave.jpg')

wigth,height = cave.size

for wide in range(wigth):
    for high in range(height):
        if (wide%2 ^ high%2 == 1):
            cave.putpixel((wide,high),0)

cave.show()

#看到处理后的图片隐约有 evil 单词
