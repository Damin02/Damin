N = int(input())
a = []
for i in range(N):
   n = input().split(" ")
   a.append([int(n[0]), int(n[1])])
a.sort(key=lambda x: (x[0], x[1]))
for i in range(N):
   print(a[i][0], a[i][1])