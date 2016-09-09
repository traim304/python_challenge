#将每一行的粉红色对齐
import PIL
from PIL import Image
from PIL import ImageChops

mozart = Image.open('mozart.gif')

palette = mozart.getpalette()
purple = 195

for y in range(mozart.size[1]):
    rect = 0,y,640,y+1
    croped = mozart.crop(rect)
    data = list(croped.getdata())
    index = data.index(purple)
    croped = ImageChops.offset(croped,-index)
    mozart.paste(croped,rect)

mozart.show()
mozart.save('resault.gif')
#显示 romance
