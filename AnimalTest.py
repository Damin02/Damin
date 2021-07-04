class Animal:
    def __init__(self):
        self.name = None

    def getName(self):
        if self.name == None:
            return self.__class__.__name__
        else:
            return self.name

    def move(self):
        if isinstance(self, Human) == True:
            return "On Your Left"
        else:
            return "Step One-Two-One-Two"



class Cat(Animal):
    def talk(self):
        return "Mew~"

class Dog(Animal):
    def talk(self):
        return "Bow-wow"

class Human(Animal):
    def talk(self):
        return "Hello"

class Monkey(Animal):
    def talk(self):
        return "Grrrrr"


if __name__ == "__main__":
    tmp = input().split(" ")
    numberOfFoot = int(tmp[0])
    howTall = int(tmp[1])
    name = tmp[2]

    anyAnimal = None

    if numberOfFoot == 4:
        if howTall > 100:
            anyAnimal = Dog()
            anyAnimal.name = name
        else:
            anyAnimal = Cat()
            anyAnimal.name = name

    elif numberOfFoot == 2:
        if howTall > 100:
            anyAnimal = Human()
            anyAnimal.name = name
        else:
            anyAnimal = Monkey()

    if anyAnimal == None:
        print("It is Not Animal")
        exit(0)
    print(anyAnimal.getName())
    print(anyAnimal.talk())
    print(anyAnimal.move())