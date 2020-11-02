try:
    with open('non-exists.txt','r') as f:
        buf = f.read()
except IOError as e:
        print(f'Error of {e}')
        
    