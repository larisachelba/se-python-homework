"""
    Create a class "Animal". You will use this class later to extend it
    with other types of animals.

    This should be an abstract class (no functionality, only works as an
    interface for the other classes). https://docs.python.org/3/library/abc.html

    public attributes:
        - color: str
        - age: int
        - animal_type: Enum (https://docs.python.org/3/library/enum.html)

    public methods:
        - sound() - returns str
            - should return the sound the animal makes
                e.g. Dog - "woof"
        - tell_age() - returns int
            - returns the current animal age
        - age_up() - returns nothing
            - should add 1 year to the current age
        - all_implemented() - returns bool
            - this method must have a functionality, if all the methods
            above have been implemented, then this should return True,
            otherwise it should return False.

    This is an abstract class! Pay attention, this class MUST NOT have any
    functionality in it (besides all_implemented()).
    The explanations for what the methods should do are mainly for the classes
    that will extend the Animal class.
"""
from abc import ABC, abstractmethod
from enum import Enum


class AnimalTypeEnum(Enum):
    Dog = 1
    Cat = 2
    Mouse = 3


class Animal(ABC):
    def __init__(self, color: str, age: int, animal_type):
        self.color = color
        self.age = age
        self.animal_type = animal_type

    @abstractmethod
    def sound(self):
        raise NotImplementedError()

    @abstractmethod
    def tell_age(self):
        raise NotImplementedError()

    @abstractmethod
    def age_up(self):
        raise NotImplementedError()

    @classmethod
    def all_implemented(cls):
        if len(cls.__abstractmethods__):
            return False
        else:
            return True

