#http://www.pythonchallenge.com/pc/def/linkedlist.php
#点击图片

old_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'


#python3 中 urllib2 被封装进了 urllib.request
import urllib.request
import re

def get_next_url(old_url):
    html = urllib.request.urlopen(old_url)
    content = str(html.read())
    
    #中间出现了 除以二 的提示,所以进行捕捉
    if 'Yes' in content:
        old_key = re.findall('([0-9]+)',old_url)
        key_of_num = ''.join(old_key)
        new_url = old_url.replace(key_of_num, str(int(key_of_num)//2))
        return new_url,content
    
    
    pattern = 'nothing is ([\d]+)'
    next_page_key = re.findall(pattern,content)
    print(next_page_key)
    
    #当匹配不到,说明找到结果
    if not next_page_key:
        print("Maybe this is result: " + content)
        return 666,666

    new_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='\
            + ''.join(next_page_key)
    return new_url,content




new_url = old_url
for i in range(400):
    new_url,content = get_next_url(new_url)
    if new_url == 666 and content == 666:
        break
    print(str(i) + ':  ' + str(content))



    
    
