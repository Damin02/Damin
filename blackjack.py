a = input().split(" ")
N = int(a[0])
M = int(a[1])

b = input().split(" ")

max = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1, N):
            sum = int(b[i]) + int(b[j]) + int(b[k])
            if max < sum and sum <= M:
                max = sum
print(max)