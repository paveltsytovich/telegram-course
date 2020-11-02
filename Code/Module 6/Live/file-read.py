# (c) TICSIA
#
#

with open('sandbox.txt') as f:
    text = f.read()
print(text)

import codecs
with codecs.open('sandbox.txt', 'r', encoding='utf8') as f:
    text = f.read()
print(text)