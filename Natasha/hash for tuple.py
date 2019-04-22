n = int(input("Enter num of inputs"))
l = []
for i in range(n):
    u = int(input())
    l.append(u)
tup = tuple(l)
print(tup)
print (hash(tup))