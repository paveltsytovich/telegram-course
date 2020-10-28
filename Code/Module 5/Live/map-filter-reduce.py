from functools import reduce

source = [('a',2),('b',3),('c','4'),('e',1)]
map_result = list(map(lambda x: str(x[0] * int(x[1])),source))
print(map_result)
filter_result = list(filter(lambda x: len(x) >= 3,map_result))
print(filter_result)
reduce_result = reduce(lambda sum,x: sum + len(x),filter_result,0)
print(reduce_result)