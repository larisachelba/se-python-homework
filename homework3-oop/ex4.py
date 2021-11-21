"""
    Create a class WorldEntity.

    public attributes:
        - entity_type: instance of Animal or classes that extend Animal
            - this is on the constructor
            - use https://docs.python.org/3/library/typing.html to force
            the user to initialize this attribute with an Animal (or classes
            that extend Animal)
        - world: instance of World class
            - this is on the constructor
            - this should be the same for every entity
        - current_position: tuple(x, y)
            - this is NOT on the constructor
            - the current position is a tuple of 2 elements, representing
            the current position of the entity on the map
            - initially, the elements of the tuple are two integers between
            map_height and map_height which you have given to the world
            previously.
                - 0 < x < map_height
                - 0 < y < map_width
        - entity_id - int
            - this is NOT on the constructor
            - this is decided at init, when passed the animal type
                - DOG = 1
                - CAT = 2
                - MOUSE = 3

    public methods:
        - move_up - returns nothing
            - moves the entity up on the world map (modifies current_position)
            - updates the world
        - move_down - returns nothing
            - moves the entity down on the world map (modifies current_position)
            - updates the world
        - move_left - returns nothing
            - moves the entity left on the world map (modifies current_position)
            - updates the world
        - move_right - returns nothing
            - moves the entity right on the world map (modifies current_position)
            - updates the world
"""
import random

from ex1 import Animal, AnimalTypeEnum
from ex3 import World
from ex2 import Dog


class WorldEntity:
    def __init__(self, entity_type: Animal, world: World):
        self.entity_id = entity_type.animal_type.value
        self.world = world
        x, y = self.generate_initial_position()
        self.current_position = tuple((x, y))

    def generate_initial_position(self):
        x = random.choice(range(1, self.world.map_height))
        y = random.choice(range(1, self.world.map_width))
        return x, y

    def move_up(self):
        self.current_position = tuple((self.current_position[0] + 1, self.current_position[1]))

    def move_down(self):
        self.current_position = tuple((self.current_position[0] - 1, self.current_position[1]))

    def move_left(self):
        self.current_position = tuple((self.current_position[0], self.current_position[1] - 1))

    def move_right(self):
        self.current_position = tuple((self.current_position[0], self.current_position[1] + 1))


entity = WorldEntity(Dog("brown", 2, AnimalTypeEnum.Mouse), World(3, 6))
print(entity.entity_id)
