old_url = 'http://www.pythonchallenge.com/pc/def/oxygen.html'

import PIL
from PIL import Image
import re


oxygen_png = Image.open('oxygen.png')
width,height = oxygen_png.size



save_color = []
for x in range(0,width,7):
    r,g,b,a = oxygen_png.getpixel((x,50))
    save_color.append(r)
    

trans_str = ''
for asc in save_color:
    trans_str += chr(asc)
trans_str = trans_str[:-3]

next_level = ''.join(re.findall('(\[.*\])',trans_str))
next_level = eval(next_level)

result = map(chr,next_level)
print(''.join(result))

new_url = old_url.replace('oxygen','intergiry')
print(new_url)

