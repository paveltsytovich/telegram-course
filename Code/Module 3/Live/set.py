s1 = set([1,2,3,1,1,1,2,3,4])
s2 = set([2,3,3,3,4,2,1,5])
print(s1)
print(s2)

s3 = s1.copy()

print(s1 == s3)
print(s1.issubset(s2))
print(s1 | s2)
print(s1 & s2)