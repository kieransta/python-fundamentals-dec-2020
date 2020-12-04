class Animal:

    def __init__(self, name, type):
        print("Animal",name,"of type",type,"was created")

        self.name =name
        self.type = type

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self, "Dog", "Mammal")

    def walks(self):
        return "Dog start walking"

    def noise(self):
        return "Woof woof"

    def eats(self, food):
        if food == "steak":
            return "Dog eats steak"
        else:
            return "Dog doesn't eat " +food

class Duck(Animal):

    def __init__(self):
        Animal.__init__(self, "Duck", "Bird")

    def walks(self):
        return "Duck start walking"

    def noise(self):
        return "Quack quack"

    def eats(self, food):
        if food == "bread":
            return "The duck eats bread"
        else:
            return "The duck doesn't eat " + food

class Snake(Animal):

    def __init__(self):
        Animal.__init__(self, "Snake", "Reptile")

    def walks(self):
        return "The snake doesn't walk"

    def noise(self):
        return "Tsssss"

    def eats(self, food):
        if food == "rats":
            return "The snake eats rats"
        else:
            return "The snake doesn't eat " +food

dog = Dog()
snake = Snake()
duck = Duck()

print(dog.walks())
print(dog.noise())
print(dog.eats("steak"))
print(dog.eats("pasta"))

print(snake.walks())
print(snake.noise())
print(snake.eats("rats"))
print(snake.eats("llamas"))

print(duck.walks())
print(duck.noise())
print(duck.eats("bread"))
print(duck.eats("nandos"))