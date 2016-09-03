from PIL import Image,ImageDraw
import PIL
from dot import first,second


old_url = 'http://www.pythonchallenge.com/pc/return/good.html'


color = {'green':(118,240,18),'red':(219,64,43),'white':(255,255,255),'black':(0,0,0)}

canvas = Image.new('RGB',(480,480),color['white'])

draw = ImageDraw.Draw(canvas)

draw.line(first,color['black'],3)
draw.polygon(second,color['red'],2)

canvas.show()

new_url = 'http://www.pythonchallenge.com/pc/return/bull.html'
print(new_url)

canvas.save('result.png')