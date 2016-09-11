import gzip
import difflib
import binascii


lines = gzip.open('deltas.gz').readlines()
#观察发现前一组到 53截止 
#后一组从 56 开始

left = []
right = []

for line in lines:
    line = line.decode('utf-8')
    left.append(line[:53])
    right.append(line[56:-1])
    

compare = difflib.Differ().compare
different = compare(left,right)

plus = []
substraction = []
space = []

for line in different:
    if line[0] == '+':
        plus.append(line[1:])
    elif line[0] == '-':
        substraction.append(line[1:])
    elif line[0] == ' ':
        space.append(line[1:])

result_1 = (''.join(plus)).replace(' ','').replace('\n','')
result_2 = (''.join(substraction)).replace(' ','').encode('utf-8')
result_3 = (''.join(space)).replace(' ','').encode('utf-8')

with open('1.png','wb') as outfile:
    outfile.write(binascii.unhexlify(result_1))
with open('2.png','wb') as outfile:
    outfile.write(binascii.unhexlify(result_2))
with open('3.png','wb') as outfile:
    outfile.write(binascii.unhexlify(result_3))