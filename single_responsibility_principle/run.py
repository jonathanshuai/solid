from animal import Animal
from animal import AnimalDatabase

# Here we save an animal using the Animal class. This is awkward.
snake = Animal('snake')
snake.save_animal('./dump/saved_snake')

# Here, we can use the AnimalDatabase to save the animal instead.
animal_db = AnimalDatabase()
animal_db.save_animal(snake, './dump/snake')

loaded_snake = animal_db.load_animal('./dump/snake')
