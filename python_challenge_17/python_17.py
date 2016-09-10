import re
import requests
import urllib.request
import bz2
import urllib.parse 
import xmlrpc.client


def get_value_from_cookie():
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345'
    pattern = re.compile('busynothing is ([\d]+)')
    next_page_key = True
    while next_page_key:
        rep = requests.get(url)
        context = rep.content.decode('utf-8')
        next_page_key = ''.join(pattern.findall(context))
        url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=' + next_page_key
        yield rep.cookies.get('info') 

paragraph = ''
for i in get_value_from_cookie():
        paragraph += i

#unquote 把 空格 处理成 '%20';
#unquote_plus 把 空格 处理成 '+';同时把 '/' 处理成 '%2F'
#思路应该是先把 quote_plus 编码的字符转换为符合 quote 处理后的字符规则,
#再用 unquote 解码
#所以应该是把 '+' replace '%20'; '%2F' replace '/'...再调用 unquote_to_bytes 处理


paragraph = paragraph.replace('+','%20').replace('%2F','/')
need_to_decompress = urllib.parse.unquote_to_bytes(paragraph)
password = bz2.decompress(need_to_decompress)


#       解码后的结果
#is it the 26th already? 
#call his father and inform him that "the flowers are on their way". 
#he\'ll understand.

# Mozart 的父亲 Leopold

#用之前的 xmlrpc.client 模块

phone_line = 'http://www.pythonchallenge.com/pc/phonebook.php'
ServerProxy = xmlrpc.client.ServerProxy(phone_line)
ServerProxy.phone('Leopold')
# 关键词 VIOLIN

#利用 cookies 传递信息给他父亲

cookies = {'info':'the flowers are on their way'}
resp = requests.\
        get('http://www.pythonchallenge.com/pc/stuff/violin.php',cookies = cookies)

print(resp.text)

#关键词 balloons 
#结束...靠


















