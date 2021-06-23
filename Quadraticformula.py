import math
num = input()

num = num.split(" ")

a = int(num[0])
b = int(num[1])
c = int(num[2])

if b ** 2 - 4*a*c < 0:
    print("False")
elif b ** 2 - 4*a*c > 0:
    print("True")
    d = round(((-b + math.sqrt(b ** 2 - 4*a*c)) / 2 * a)*100) / 100.0
    e = round(((-b - math.sqrt(b ** 2 - 4*a*c)) / 2 * a)*100) / 100.0
    print(d)
    print(e)
else:
    f = -b / 2 * a
    print("True")
    print(f)
    print(f)