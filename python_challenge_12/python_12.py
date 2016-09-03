#将打不开的evil4.jpg 改名为 .txt 后缀
#能够读出 Bert is evil! go back! 然,分析不出啥

#def make_it_readable(data):
#    result = ''
#    for byte in data:
#        if ord(' ') <= byte <= ord('~'):
#            result += chr(byte)
#        else:
#            result += '_'
#    return result
#
#evil_1 = open('evil2.gfx','rb').read(80)
#maybe_readable = make_it_readable(evil_1)
#print(maybe_readable)
#evil_1.close()
##到这里可以看出 evil2.gfx 中包含着5副图案

evil_2_gfx = open('evil2.gfx','rb').read()

for file_name,data in zip(['0.jpg','1.png','2.gif','3.png','4.jpg'],[evil_2_gfx[0::5],evil_2_gfx[1::5],evil_2_gfx[2::5],evil_2_gfx[3::5],evil_2_gfx[4::5]]):
    file_tmp = open(file_name,'wb')
    file_tmp.write(data)
    file_tmp.close()

#图片组成的单词是 disproportional
#So new_url = http://www.pythonchallenge.com/pc/return/disproportional.html