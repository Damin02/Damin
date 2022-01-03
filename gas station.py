# N = int(input())
# D = input().split(" ") #거리   
# C = input().split(" ") #돈

# k = int(C[0])*int(D[0])
# a = int(C[0])
# for i in range(1,N-1):
#     if int(C[i]) < a:
#         a = int(C[i])
#         k += int(C[i])*int(D[i])
#     else:
#         k += a*int(D[i])
# print(k)
import sys
r = sys.stdin.readline
N = int(r())
D = list(map(int,r().split())) #거리   
C = list(map(int,r().split())) #돈

k = C[0]*D[0]
a = C[0]
for i in range(1,N-1):
    if C[i] < a:
        a = C[i]
        k += C[i]*D[i]
    else:
        k += a*D[i]
print(k)
