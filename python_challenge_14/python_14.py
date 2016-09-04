import PIL
from PIL import Image

all_data = Image.open('wire.png').getdata()

#<!-- remember: 100*100 = (100+99+99+98) + (...  -->
#意思是以顺时针打印

#画布的大小为 x * y, 
#初始执行序列 x, y-1, x-1,y-2
def clockwise_paint(x,y):
    real_pic = Image.new("RGB",(x,y),(255,255,255))
    xiang_you,xiang_xia,xiang_zuo,xiang_shang = (x, y-1, x-1,y-2)
    cur_x=0
    cur_y=0
    i_of_data = 0
    def main_func(xiang_you,xiang_xia,xiang_zuo,xiang_shang):
        nonlocal cur_x,cur_y,i_of_data
        for i in range(xiang_you):
            real_pic.putpixel((cur_x,cur_y),all_data[i_of_data])
            cur_x += 1
            i_of_data += 1
        
        cur_x -= 1
        cur_y += 1
        for i in range(xiang_xia):
            real_pic.putpixel((cur_x,cur_y),all_data[i_of_data])
            cur_y += 1
            i_of_data += 1
        

        cur_y -= 1
        cur_x -= 1
        for i in range(xiang_zuo):
            real_pic.putpixel((cur_x,cur_y),all_data[i_of_data])
            cur_x -= 1
            i_of_data += 1
        

        cur_y -= 1
        cur_x += 1
        for i in range(xiang_shang):
            real_pic.putpixel((cur_x,cur_y),all_data[i_of_data])
            cur_y -= 1
            i_of_data += 1

    while xiang_you > 0:
        main_func(xiang_you,xiang_xia,xiang_zuo,xiang_shang)
        xiang_shang -= 2;xiang_xia -= 2;xiang_zuo-= 2;xiang_you -= 2;cur_x += 1;cur_y += 1

    return real_pic



real_pic = clockwise_paint(100,100)
real_pic.show()
#处理后出来一只猫

            



    





# http://www.pythonchallenge.com/pc/return/uzi.html