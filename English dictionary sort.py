import sys
r = sys.stdin.readline
N = int(r())
a = set()
for i in range(N):
    a.add(r().rstrip())
a=list(a)
a.sort(key=lambda x : (len(x), x))
for s in a:
    print(s)
