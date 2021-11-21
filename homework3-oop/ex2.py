"""
    Create 3 classes:
        - Cat
        - Dog
        - Mouse

    All of these 3 classes must inherit from the Animal class.

    public attributes:
        - inherited from Animal (on init (or also called constructor))
        - enemy (on constructor (init))
            - is reference to the enemy of the current Animal
            e.g. Dog is the enemy of Cat

    private attributes:
        - specific_sound: str

    public methods:
        - inherited from Animal

    private methods:
        - enemy_fear_sound() - returns str
            - this is called inside the sound() method, and if an enemy has
            been passed on the constructor, then the sound should be different
            than the usual sound of the animal

            e.g.
                if Cat is called with enemy = Dog, then the cat should make
            a "meoooooow scared" sound.
                else the cat makes a "meow" sound
"""
from ex1 import Animal
from ex1 import AnimalTypeEnum


class Cat(Animal):
    def __init__(self, color, age, enemy: AnimalTypeEnum):
        super().__init__(color, age, AnimalTypeEnum.Cat)
        self.enemy = enemy
        self.__specific_sound = "meow"

    def __enemy_fear_sound(self):
        return "meoooooow scared"

    def sound(self):
        if self.enemy is AnimalTypeEnum.Dog:
            return self.__enemy_fear_sound()
        else:
            return self.__specific_sound

    def tell_age(self):
        return self.age

    def age_up(self):
        self.age += 1
        return self.age


class Dog(Animal):
    def __init__(self, color, age, enemy: AnimalTypeEnum):
        super().__init__(color, age, AnimalTypeEnum.Dog)
        self.enemy = enemy
        self.__specific_sound = "woof"

    def __enemy_fear_sound(self):
        return "woooof scared"

    def sound(self):
        if self.enemy is AnimalTypeEnum.Mouse:
            return self.__enemy_fear_sound()
        else:
            return self.__specific_sound

    def tell_age(self):
        return self.age

    def age_up(self):
        self.age += 1
        return self.age


class Mouse(Animal):
    def __init__(self, color, age, enemy: AnimalTypeEnum):
        super().__init__(color, age, AnimalTypeEnum.Mouse)
        self.enemy = enemy
        self.__specific_sound = "chit chit"

    def __enemy_fear_sound(self):
        return "chiiiiiit scared"

    def sound(self):
        if self.enemy is AnimalTypeEnum.Cat:
            return self.__enemy_fear_sound()
        else:
            return self.__specific_sound

    def tell_age(self):
        return self.age

    def age_up(self):
        self.age += 1
        return self.age


if __name__ == '__main__':
    cat1 = Cat("red", 3, AnimalTypeEnum.Dog)
    print(cat1.sound(), cat1.tell_age(), cat1.age_up(), cat1.all_implemented())

