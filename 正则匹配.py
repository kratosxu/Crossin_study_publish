import re

op = open ('from.txt', 'r', encoding = 'utf-8')
string = str(op.readlines())
op.close()

str_pattern = r'\b[A-z]+'

with open('to.text', 'w') as w:
    for i in (re.findall(str_pattern, string)):
        w.write(i+'\n')
