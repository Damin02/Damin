N= int(input())
m = len(list(str(N)))

for i in range(N-9*m, N):
    a= i
    sum = i
    while a > 0:
        sum += a%10
        a=a//10
    if sum ==N:
        print(i)
        exit(0)
print(0)