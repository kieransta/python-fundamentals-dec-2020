import unittest
from unittest import TestCase
from session6_inheranc import Dog, Snake, Duck

class TestAnimals(TestCase):

    def test_if_dog_is_dog(self):
        dog = Dog()

        self.assertEqual(dog.name, "Dog")

    def test_if_duck_is_a_duck(self):
        snake = Snake()

        self.assertEqual(snake.name, "Snake")

    def test_if_snake_is_a_snake(self):
        duck = Duck()

        self.assertEqual(duck.name, "Duck")

    def test_if_animals_can_walk(self):
        dog = Dog()
        snake = Snake()
        duck = Duck()

        expected_output = "Dog start walking", "The snake doesn't walk","Duck start walking"
        output = dog.walks(), snake.walks(),duck.walks()

        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()