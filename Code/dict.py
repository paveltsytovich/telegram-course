d = {"first" : "test", 2: "test", "three": [1,2,3]}
print(d)
print(d["first"])
print(d[2])
print(d["three"])

x = dict.fromkeys(["one","two","three"])
print(x)
print(d.items())
print(d.keys())
print(d.values())