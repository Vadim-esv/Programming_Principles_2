a = input().split()
#a = [input(i) for i in input().split]
for i in range(0, len(a), 2): # (starting point, end point, step)
    print(a[i], end = ' ')