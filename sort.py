N = int(input())
a=[]
for i in range(N):
    b = list(map(int, input().split(" ")))
    a.append([b[0], b[1]])
a.sort(key= lambda x: (x[0], x[1]))
for i in range(N):
    print(a[i][0], a[i][1])
