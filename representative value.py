import sys
N = int(sys.stdin.readline().rstrip())
a = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
print("%.0d" %(sum(a)/N)) # 산술평균
a.sort()
print(a[int((N-1)/2)]) # 중앙값

c = list(set(a))
d = []
e = []
for i in range(len(c)):
   d.append(a.count(c[i]))
m = 0
for i in range(len(c)):
   if d[i] > m:
      m = d[i]
for i in range(len(c)):
   if m == d[i]:
      e.append(c[i])
if len(e) > 1:
   e.sort()
   print(e[1])
else:
   print(e[0])
#최빈값
print(a[-1]-a[0]) # 범위