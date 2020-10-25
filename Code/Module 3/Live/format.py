print('{} {}'.format('one', 'two')) 
print('{1} {0}'.format('one', 'two') )
print('{} {}'.format(1, 2))
print('{first_name} {last_name}'.format(last_name='Picard', first_name='Jean-Luc'))
 
print('{:_<10}'.format('test'))
print('{:_>10}'.format('test'))
print('{:_^10}'.format('test'))
 
print('{result!s:_^20}'.format(result=(1, 2)))
print('{result!r:_^20}'.format(result=(1, 2)))

print('{result:_^ 20.2f}'.format(result=3.141))
print('{result:_^ 20.2f}'.format(result=-3.141))
