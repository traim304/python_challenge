#http://www.pythonchallenge.com/pc/def/map.html

#ord,chr,zip

import string

strange_str = open('strange_str.txt','rt').read()

original_alphabet = "abcdefghijklmnopqrstuvwxyz"
changed_alphabet =  "cdefghijklmnopqrstuvwxyzab"

map_relation = str.maketrans(original_alphabet,changed_alphabet)
print(strange_str.translate(map_relation))

old_url = 'http://www.pythonchallenge.com/pc/def/map.html'
new_url = old_url.replace('map','map'.translate(map_relation))

print('This is new URL:')
print(new_url)
