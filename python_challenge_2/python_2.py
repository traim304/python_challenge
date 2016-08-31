strange_str = open('strange_str.txt','rt').read()
old_url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
unique = set(strange_str)

#set集合  isalpha, count, join

result = ''.join([ch for ch in strange_str if ch.isalpha()])
new_url = old_url.replace('ocr',result)

print(new_url)

