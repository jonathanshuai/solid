from animal import Animal
from animal import Dog, Duck, Snake

animal = Animal('Jasmine')
dog = Dog('Casey')
duck = Duck('Donald')
snake = Snake('Python')

# We can pass this list of animals animal_barn
def count_all_legs(animal_barn):
    total_legs = 0
    for animal in animal_barn:
        # All of these are instance of animal, and we
        assert isinstance(animal, Animal)
        total_legs += animal.count_legs()

    return total_legs


print(count_all_legs([animal, dog, duck, snake]))

# Okay, this was an awkward example. But the idea is that since they're all
# inheriting from Animal, they should all have the count_legs and no subclass
# of Animal should not have it.
