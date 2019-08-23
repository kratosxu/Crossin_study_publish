import re

article = open ('words.txt', 'r', encoding = 'utf-8')
data = article.read()
article.close()
word_len = len(re.findall(r'\b[A-z]+\b', data))
print ('There are %i words in words.txt.' % word_len)