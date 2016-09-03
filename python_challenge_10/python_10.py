
old_url = 'http://www.pythonchallenge.com/pc/return/bull.html'



def translation(num):
    letter = num[0]
    freq = 0
    next_num = ''
    for cur_letter in num:
        if cur_letter == letter:
            freq += 1
        else:
            next_num += str(freq)
            freq = 1
            next_num += letter
            letter = cur_letter
    #循环结束时 freq 与 letter 的值并没有进入next_num中,所以要加一下
    next_num += str(freq)
    next_num += letter
    return next_num

num = '1'
for i in range(30):
    num = translation(num)

result = len(num)

new_url = old_url.replace('bull',str(result))
print(new_url)
