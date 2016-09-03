import zipfile
import re


old_url = 'http://www.pythonchallenge.com/pc/def/channel.html'

zf = zipfile.ZipFile('channel.zip')

zf.read('readme.txt')


def find_out(file_number):
    global mystery
    file_name = str(file_number) + '.txt'
    #取出文件的注释
    file_comment = zf.getinfo(file_name).comment
    mystery += (file_comment.decode('ascii'))
    content = zf.read(file_name).decode('ascii')
    next_key = ''.join(re.findall('Next nothing is ([\d]+)',content))
    if not next_key:
        #print('\n Exit and The content is:\n    ' + content + '\n')
        return
    else:
        find_out(next_key)


new_nothing = 90052
mystery = ''
find_out(new_nothing)

print(mystery)

#改成hockey后提示注意构成图案的字母
#oxygen
new_url = old_url.replace('channel','oxygen')
print(new_url)