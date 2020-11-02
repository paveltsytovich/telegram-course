# (c) TICSIA
#
#
with open('sandbox.txt','r') as f:
    for current_line in f:
        print(current_line)
        
import codecs

with codecs.open('sandbox.txt','r','utf-8') as f:
    for current_line in f:
        print(current_line)