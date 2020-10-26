def print_bool(arg):
    if arg:
        print("True")
    else:
        print("False")

print_bool(True)          
print_bool(5)             
print_bool("False")       
print_bool([1,2,3])       
print_bool(print_bool)  

print_bool(False)         
print_bool(None)          
print_bool(0)             
print_bool("")            
print_bool([])            
print_bool(not True)      

print_bool( 3 > 2 and 3 <5) 
print_bool( "abc" == "abc") 

a = [1]; b = [1]; c = [1, -100]; d = [-1, 100]
print_bool(a == b)    
print_bool(c > a)     
print_bool(d > a)     
