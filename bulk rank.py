class People:
    def __init__(self, weight, height, rank):
        self.weight = weight
        self.height = height
        self.rank = rank


N = int(input())
p = []
for i in range(N):
    a = input().split(" ")
    p.append(People(int(a[0]), int(a[1]), 1))

for i in range(N):
    for j in range(N):
        if p[i].weight > p[j].weight and p[i].height > p[j].height:
            p[j].rank += 1

for i in range(N):
    print(p[i].rank, end=' ')