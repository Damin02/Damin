N = int(input())

a = []

for i in range(N):
    a.append(int(input()))

for i in range(N):
    changed = False
    for j in range(N-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            changed = True
    if not changed:
        break
    
for i in range(N):
     print(a[i])