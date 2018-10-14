from animal import Animal

dog = Animal('dog')
cat = Animal('cat')
lion = Animal('lion')
snake = Animal('snake')

# Really bad way to make sounds for each animal. If we add a new animal,
# we add awkward changes to this function!

def make_sound(animal):
    if animal.name == 'dog':
        print("Woof!")
    elif animal.name == 'cat':
        print("Meow!")
    elif animal.name == 'lion':
        print("Roar!")
    elif animal.name == 'snake':
        print("Hsss!")
    else:
        print("----")

[make_sound(a) for a in [dog, cat, lion, snake]]


print("-" * 10)
# The better way, as we implemented in animial.py, is to create separate classes for these
# new animals to implement an Animal.make_sound function.


from animal import Dog, Cat, Lion, Snake

dog = Dog('dog')
cat = Cat('cat')
lion = Lion('lion')
snake = Snake('snake')

[a.make_sound() for a in [dog, cat, lion, snake]]



# Look how easy it is to add a duck!

class Duck(Animal):
    def __init__(self, name):
        super(Duck, self).__init__(name)

    def make_sound(self):
        print("Quack!")
duck = Duck('duck')

duck.make_sound()
