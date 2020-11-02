# (c) TICSIA
#
#
import json

d = {"name" : "test", "age":49, "location" : "Melburne"}
with open("test.json",'w') as j:
    json.dump(d,j)    
    
with open('test.json','r') as j:
    d = json.load(j)    
print(d)
