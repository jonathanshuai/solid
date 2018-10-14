"""This animal class is to look at Liskov Substitution Principle.

The Liskov substitution principle says a sub-class must be substitutable for its
super class. In other words, we should be able to put a subclass in place of a 
super class and run without errors.
"""

# We have our animal class again. Let's say we want to add sounds to it.
# Outside in the run.py class, you can see the example of us trying to add 
# sounds to each animal.

class Animal:
    def __init__(self, name):
        self.name = name

    def get_animal_name(self):
        return self.name

    def count_legs(self):
        return 0


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)

    def count_legs(self):
        return 4

class Duck(Animal):
    def __init__(self, name):
        super(Duck, self).__init__(name)

    def count_legs(self):
        return 2

class Snake(Animal):
    def __init__(self, name):
        super(Snake, self).__init__(name)

    def count_legs(self):
        return 0