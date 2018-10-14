"""This animal class is to look at Open-Closed Principle.

The open-closed principle says software entities should be open for extension,
not modifiation. In other words, we never want to have to go into a class and
do 'surgery' on it.
"""

# We have our animal class again. Let's say we want to add sounds to it.
# Outside in the run.py class, you can see the example of us trying to add 
# sounds to each animal.

class Animal:
    def __init__(self, name):
        self.name = name

    def get_animal_name(self):
        return self.name

    def make_sound(self):
        print("---")


# The better way is to create animals to inherit from Animal and implement 
# their own make_sound.

# Now, adding a new animal and its sound is as easy as creating a new class!
# No need to go into any weird functions.

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)

    def make_sound(self):
        print("Woof!")


class Cat(Animal):
    def __init__(self, name):
        super(Cat, self).__init__(name)

    def make_sound(self):
        print("Meow!")


class Lion(Animal):
    def __init__(self, name):
        super(Lion, self).__init__(name)

    def make_sound(self):
        print("Roar!")


class Snake(Animal):
    def __init__(self, name):
        super(Snake, self).__init__(name)

    def make_sound(self):
        print("Hsss!")
