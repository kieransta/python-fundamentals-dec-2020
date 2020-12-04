###create first class
##class is a blueprint for object

class Animal:

    def __init__(self, name, type):
        print("Animal",name,"of type",type,"was created")

        self.name =name
        self.type = type

    def noise(self):

        if self.name == "Snake":
            return "Tsssss"
        elif self.name == "Dog":
            return "Woof woof"
        elif self.name == "Duck":
            return "Quack quack"
        else:
            return "No noise"

    def walk(self):

        if self.name == "Snake":
            return "Snake doesn't walk"
        elif self.name == "Dog":
            return "Dogs can walk"
        elif self.name == "Duck":
            return "Ducks can walk and swim"
        else:
            return"Animal unknown"

    def eat(self, food):
        if self.name == "Snake" and food == "rat":
            return "Snake eats this food"
        elif self.name == "Dog" and food == "rat":
            return "Dog eats this food"
        elif self.name == "Duck" and food == "bread":
            return "Duck eats this food"
        else:
            return self.name + " doesn't eat this food"



dog = Animal("Dog", "Mammal")
snake = Animal("Snake", "Reptile")
duck = Animal("Duck","Bird")

print("Dog says", dog.noise())
print("Snake says", snake.noise())
print("Duck says", duck.noise())

print(dog.walk())
print(snake.walk())
print(duck.walk())

print(snake.eat("pasta"))
print(snake.eat("rat"))
print(snake.eat("cabbage"))
print(snake.eat("metal"))
print(snake.eat("water"))
print(snake.eat("cheese"))
print(snake.eat("rat"))
print(dog.eat("rat"))
print(dog.eat("snake"))
print(duck.eat("rat"))
print(duck.eat("bread"))
