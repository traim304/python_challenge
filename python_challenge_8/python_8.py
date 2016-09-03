old_url = 'http://www.pythonchallenge.com/pc/def/integrity.html'

import bz2


#将 字符串 转为 字节流 用 encode 
#测试发现 转为 utf-8 源数据会发生改变 而用 latin1 则不会..暂时不清楚为什么.
un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

un = un.encode('latin1')
un = bz2.decompress(un)
print('Username: ' + un.decode('utf-8'))

pw = pw.encode('latin1')
pw = bz2.decompress(pw)
print('Password: ' + pw.decode('utf-8'))

