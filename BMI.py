cnt = input()

cnt = cnt.split(" ")

H = float(cnt[0])
W = float(cnt[1])

BMI = round((W / (H / 100) ** 2)*100) / 100.0


if BMI >= 23:
    print("over")
elif BMI < 18.5:
    print("under")
else:
    print("standard")