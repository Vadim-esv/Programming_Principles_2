a = {int(i) for i in input().split()}
b = {int(i) for i in input().split()}
c = list(a.intersection(b))
c.sort()
for i in range(len(c)):
    print(c[i], end = ' ')
#for i in c:
#    print(i, end = ' ')