#
#
# (c) TICSIA

import requests
with open('sandbox.txt','w') as f:
    f.write("<h1>test</h1>" * 100)
file = {'file': ('sandbox.txt',open('sandbox.txt','rb'),'text/html')}
response = requests.post('https://httpbin.org/post',files = file)
print(response.text)