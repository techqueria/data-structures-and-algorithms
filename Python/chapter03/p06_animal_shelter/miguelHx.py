"""3.6 - Animal Shelter:
An animal shelter, which holds only dogs and cats, operates on a strictly
"first in, first out" basis. People must adopt either the "oldest" (based on arrival time)
animal of all animals at the shelter, or they can select whether they would prefer
a dog or a cat (and will receive the oldest animal of that type). They cannot
select which specific animal they would like. Create the data structures to maintain this system
and implement operations such as enqueue, dequeueAny, dequeueDog, and
dequeueCat. You may use the built-in LinkedList data structure.
"""
import unittest

from dataclasses import dataclass
from enum import Enum


class AnimalTypeEnum(Enum):
    DOG = 'dog'
    CAT = 'cat'

@dataclass
class Animal:
    name: str
    species: AnimalTypeEnum
    timestamp: int


class AnimalShelter:
    """We will have each animal instance
    maintain a timestamp. This timestamp will
    be used to determine the globally "oldest"
    (based on arrival time) animal.
    """

    def __init__(self):
        # FIFO, a queue of animals
        self.dogs = []
        self.cats = []
    
    def enqueue(self, animal: Animal) -> None:
        pass

    def dequeueAny(self) -> Animal:
        pass

    def dequeueDog(self) -> Animal:
        pass

    def dequeueCat(self) -> Animal:
        pass


if __name__ == '__main__':
    unittest.main()
