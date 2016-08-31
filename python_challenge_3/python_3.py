#map 字符串分片,正则表达式,re模块,re.findall()



old_url = 'http://www.pythonchallenge.com/pc/def/equality.html'
strange_str = open('strange_str.txt','rt').read()

#               最优解
import re
pattern = "[^A-Z]+[A-Z]{3}([a-z]){1}[A-Z]{3}[^A-Z]+"

result = re.findall(pattern,strange_str)
result = ''.join(result)


##           暴力搜索
##       有个坑,可能会在每行的开头或者结尾
#modify_str = ''
#
#def change_func(char):
#    if char.isupper():
#        return 'A'
#    elif char.islower():
#        return 'z'
#    else:
#        return char
#
##返回的是 map object
#modify_str = map(change_func,strange_str)
##转换成列表
#modify_str = list(modify_str)
##转换成字符串
#modify_str = ''.join(modify_str)
#result = ''
#for i in range(len(modify_str)-8):
#    if modify_str[i:i+9] in ['zAAAzAAAz','\nAAAzAAAz','AAAzAAA\n']:
#        result += strange_str[i+4]

new_url = old_url.replace('equality',result)
print(new_url)