# (c) TICSIA
#
#
buf = "Это строка текста,\nкоторая будет записана в файл"
with open('test.txt','w') as f:
    f.write(buf)

import codecs
with codecs.open('test-utf8.txt','w','utf-8') as f:
    f.write(buf)
    
    