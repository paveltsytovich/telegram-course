def add(x,y):
    "Функция сложения двух аргументов"
    print(x+y)
def my_sum(l):
    "Функция суммирования элементов списка"
    s = 0
    for i in l:
        s += i
    return s

add(2,4)
print(my_sum([1,2,3,4,5]))