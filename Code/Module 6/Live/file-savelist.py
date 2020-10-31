#  (c) TICSIA
#
#
import pickle

source = [1,2,3,3,4,5]
with open('test-list.bin','wb') as f:
    pickle.dump(source,f)
    
with open('test-list.bin','rb') as f:
    destination = pickle.load(f)    
    
print(source)
print(destination)