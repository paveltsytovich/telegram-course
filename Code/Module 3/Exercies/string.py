x = input("введите строку >")
y = input("введите вторую строку >")
print(x*5)
print(x+y)
print(len(x)+len(y))
if y in x:
    print("Вторая строка является подстрокой первой")
else:
    print("строки являютеся разными")
