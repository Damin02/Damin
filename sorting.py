def sorting(a):
    b = [i for i in a] 
    b.sort()
    return b

import sys
a = list(map(int, sys.stdin.readline().split()))
print(sorting(a))
print(a)