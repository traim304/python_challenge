#http://www.pythonchallenge.com/pc/def/0.html

num = 2 ** 38
old_url = 'http://www.pythonchallenge.com/pc/def/0.html'
new_url = old_url.replace('0',str(num))

print(new_url)
