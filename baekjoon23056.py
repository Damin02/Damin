N = input().split(' ')
a1 = []
a2 = []
c = [0 for _ in range(int(N[0]))]

while True:
    b = input().split(' ')
    if int(b[0]) == 0:
        b = []
        break

    c[int(b[0])-1] += 1 

    if c[int(b[0])-1] <= int(N[1]):
        if int(b[0])%2 == 0:
            a1.append([int(b[0]), b[1], len(b[1])])
        else:
            a2.append([int(b[0]), b[1], len(b[1])])
    b = []
a1.sort(key = lambda x: (x[0], x[2], x[1]))
a2.sort(key = lambda x: (x[0], x[2], x[1]))

for i in range(len(a2)):
    print(a2[i][0], a2[i][1])
for i in range(len(a1)):
    print(a1[i][0], a1[i][1])
