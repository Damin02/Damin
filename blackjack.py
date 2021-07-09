a = input().split(" ")
N = int(a[0])
M = int(a[1])

b = input().split(" ")

c = []
d = []
max = 0

for i in range(N):
    c.append(int(b[i])%M)


for i in range(N):
    if max < c[i]:
        max = c[i]

for i in range(max):
    d.append(0)

for i in range(max):
    d[c[i]] += 1

for i in range(max):
    print("%d개 : %d" %(int(d[i])), i)