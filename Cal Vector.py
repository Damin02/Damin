class Vector:
    def __init__(self, val):
        self.value = val
        self.amp = self.cal_amp()
        
    def cal_amp(self):
        return (sum((self.value[i]) ** 2 for i in range(len(self.value))) ** (1/2))
    
    def __add__(self, obj):
        tem = [self.value[i] + obj.value[i] for i in range(len(self.value))]
        return Vector(tem)

    def __sub__(self, obj):
        tem = [self.value[i] - obj.value[i] for i in range(len(self.value))]
        return Vector(tem)

    def __mul__(self, obj):
        sum = 0
        for i in range(len(self.value)):
           sum += self.value[i]*obj.value[i] 
        return sum

    def __str__(self):
        return str(self.value)

A = Vector([1,2,3,4])
print(A.amp) # sqrt(30)
B = Vector([3,1,-1,2])

C = A+B
print(C)  # [4, 3, 2, 6]

C=A*B
print(C)    #10

C=A-B
print(C)  #[-2, 1, 4, 2]