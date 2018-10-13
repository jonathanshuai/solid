"""Animal class to demonstrate Single Responsibility Principle.

The single responsibility principle says that a class should be responsible for just one thing.
"""

# First, let's look at this design:

class Animal:
    def __init__(self, name):
        self.name = name

    def get_animal_name(self):
        return self.name

    def save_animal(self, file_name):
        with open(file_name, 'w') as f:
            f.write(self.name)

    def load_animal(self, file_name):
        with open(file_name, 'r') as f:
            self.name = f.read()

# This design is bad because Animal class is managing the attributes of animal
# as well as the database.

# Let's create an AnimalDatabase to manage the Animal database for us.

class AnimalDatabase:
    def __init__(self):
        pass

    def save_animal(self, animal, file_name):
        with open(file_name, 'w') as f:
            f.write(animal.name)

    def load_animal(self, file_name):
        with open(file_name, 'r') as f:
            return Animal(f.read())


# We should remove save_animal and load_animal from the Animal class.
