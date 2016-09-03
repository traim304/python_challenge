old_url = 'http://www.pythonchallenge.com/pc/def/peak.html'

import pickle
from pprint import pprint

with open('banner.txt','rb') as in_file:
    obj = pickle.load(in_file)

def print_banner(a_list):
    str = '';
    for (char,multip) in a_list:
        str += char * multip
    print(str)

for a_list in obj:
    print_banner(a_list)


#看到的是用 # 组成的单词 channel

new_url = old_url.replace('peak','channel')
print(new_url)