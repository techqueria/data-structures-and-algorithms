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

from collections import deque
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class AnimalTypeEnum(Enum):
    DOG = 'dog'
    CAT = 'cat'


@dataclass
class Animal:
    name: str
    species: AnimalTypeEnum

@dataclass
class QueuedAnimal:
    animal: Animal
    timestamp: int

class AnimalShelter:
    """We will have each animal instance
    maintain a timestamp. This timestamp will
    be used to determine the globally "oldest"
    (based on arrival time) animal.
    """
    def __init__(self):
        # FIFO, a queue of QueuedAnimals
        self.dogs: Deque[QueuedAnimal] = deque()
        self.cats: Deque[QueuedAnimal] = deque()
        self._species_map = {
            AnimalTypeEnum.DOG.value: self.dogs,
            AnimalTypeEnum.CAT.value: self.cats
        }
        self._global_timestamp = 0
        self._size = 0
    
    def _enqueue(self, animal: Animal) -> None:
        # list will grow right [<animal_1>, <animal_2>, ..., <animal_n>]
        # Animal will be encapsulated in QueuedAnimal, so hide the timestamp
        # usage from the caller
        queued_animal = QueuedAnimal(animal, self._global_timestamp)
        self._global_timestamp += 1
        self._species_map[animal.species].append(queued_animal)

    def enqueue(self, *animals: Animal, key: str = '') -> None:
        for animal in animals:
            self._enqueue(animal)

    def dequeueAny(self) -> Animal:
        if (len(self.dogs) + len(self.cats)) == 0:
            raise IndexError('Animal Shelter is empty.')
        # oldest animals will be stored in the left-most index of
        # their corresponding queues.
        # we will return the oldest animal of the two queues.
        if len(self.dogs) >= 1 and len(self.cats) == 0:
            return self.dequeueDog()
        elif len(self.dogs) == 0 and len(self.cats) >= 1:
            return self.dequeueCat()
        # otherwise, pick oldest from overall
        oldest_dog: QueuedAnimal = self.dogs[0]
        oldest_cat: QueuedAnimal = self.cats[0]
        if oldest_dog.timestamp < oldest_cat.timestamp:
            return self.dequeueDog()
        else:
            return self.dequeueCat()

    def dequeueDog(self) -> Animal:
        if len(self.dogs) == 0:
            raise IndexError('No dogs available to adopt.')
        return self.dogs.popleft().animal

    def dequeueCat(self) -> Animal:
        if len(self.cats) == 0:
            raise IndexError('No cats available to adopt.')
        return self.cats.popleft().animal

    def __len__(self) -> int:
        return len(self.dogs) + len(self.cats)


class AnimalShelterTest(unittest.TestCase):
    def test_enqueue(self):
        # create animal shelter
        a = AnimalShelter()
        self.assertEqual(len(a), 0)
        # add a few dogs...
        d1 = Animal('Geralt', 'dog')
        d2 = Animal('Taco', 'dog')
        d3 = Animal('Lucky', 'dog')
        d4 = Animal('Nova', 'dog')
        a.enqueue(d1, d2, d3, d4)
        self.assertEqual(len(a), 4)
        self.assertEqual(len(a.dogs), 4)
        self.assertEqual(len(a.cats), 0)
        self.assertEqual(a.dogs[0].timestamp, 0)
        self.assertEqual(a.dogs[1].timestamp, 1)
        self.assertEqual(a.dogs[2].timestamp, 2)
        self.assertEqual(a.dogs[3].timestamp, 3)
        # now, add a few cats...
        c1 = Animal('Curio', 'cat')
        c2 = Animal('Chai', 'cat')
        c3 = Animal('Alma', 'cat')
        c4 = Animal('Blanco', 'cat')
        a.enqueue(c1, c2, c3, c4)
        self.assertEqual(len(a), 8)
        self.assertEqual(len(a.dogs), 4)
        self.assertEqual(len(a.cats), 4)
        self.assertEqual(a.cats[0].timestamp, 4)
        self.assertEqual(a.cats[1].timestamp, 5)
        self.assertEqual(a.cats[2].timestamp, 6)
        self.assertEqual(a.cats[3].timestamp, 7)

    def test_dequeue_dog_and_cat_queue(self):
        a = AnimalShelter()
        self.assertRaises(IndexError, lambda: a.dequeueDog())
        self.assertRaises(IndexError, lambda: a.dequeueCat())
        d1 = Animal('Lucky', 'dog')
        d2 = Animal('Nova', 'dog')
        d3 = Animal('Geralt', 'dog')
        a.enqueue(d1, d2, d3)
        self.assertEqual(len(a), 3)
        self.assertEqual(len(a.dogs), 3)
        self.assertEqual(len(a.cats), 0)
        d = a.dequeueDog()
        self.assertEqual(len(a), 2)
        self.assertEqual(len(a.dogs), 2)
        self.assertEqual(len(a.cats), 0)
        self.assertEqual(d1, d)
        d = a.dequeueDog()
        self.assertEqual(len(a), 1)
        self.assertEqual(len(a.dogs), 1)
        self.assertEqual(len(a.cats), 0)
        self.assertEqual(d2, d)
        d = a.dequeueDog()
        self.assertEqual(len(a), 0)
        self.assertEqual(len(a.dogs), 0)
        self.assertEqual(len(a.cats), 0)
        self.assertEqual(d3, d)
        self.assertRaises(IndexError, lambda: a.dequeueDog())

    def test_dequeue_any(self):
        a = AnimalShelter()
        self.assertRaises(IndexError, lambda: a.dequeueAny())
        # scenario 1: Only dogs
        d1 = Animal('Lucky', 'dog')
        d2 = Animal('Nova', 'dog')
        d3 = Animal('Geralt', 'dog')
        a.enqueue(d1, d2, d3)
        self.assertEqual(len(a), 3)
        self.assertEqual(len(a.dogs), 3)
        self.assertEqual(len(a.cats), 0)
        d = a.dequeueAny()
        self.assertEqual(len(a), 2)
        self.assertEqual(len(a.dogs), 2)
        self.assertEqual(len(a.cats), 0)
        self.assertEqual(d1, d)
        d = a.dequeueAny()
        self.assertEqual(len(a), 1)
        self.assertEqual(len(a.dogs), 1)
        self.assertEqual(len(a.cats), 0)
        self.assertEqual(d2, d)
        d = a.dequeueAny()
        self.assertEqual(len(a), 0)
        self.assertEqual(len(a.dogs), 0)
        self.assertEqual(len(a.cats), 0)
        self.assertEqual(d3, d)
        self.assertRaises(IndexError, lambda: a.dequeueAny())
        # scenario 2: Only cats
        c1 = Animal('Curio', 'cat')
        c2 = Animal('Chai', 'cat')
        c3 = Animal('Alma', 'cat')
        a.enqueue(c1, c2, c3)
        self.assertEqual(len(a), 3)
        self.assertEqual(len(a.dogs), 0)
        self.assertEqual(len(a.cats), 3)
        c = a.dequeueAny()
        self.assertEqual(len(a), 2)
        self.assertEqual(len(a.dogs), 0)
        self.assertEqual(len(a.cats), 2)
        self.assertEqual(c1, c)
        c = a.dequeueAny()
        self.assertEqual(len(a), 1)
        self.assertEqual(len(a.dogs), 0)
        self.assertEqual(len(a.cats), 1)
        self.assertEqual(c2, c)
        c = a.dequeueAny()
        self.assertEqual(len(a), 0)
        self.assertEqual(len(a.dogs), 0)
        self.assertEqual(len(a.cats), 0)
        self.assertEqual(c3, c)
        self.assertRaises(IndexError, lambda: a.dequeueAny())
        # scenario 3: both cats and dogs, but global oldest is dog
        d1 = Animal('Lucky', 'dog')
        d2 = Animal('Nova', 'dog')
        d3 = Animal('Geralt', 'dog')
        c1 = Animal('Curio', 'cat')
        c2 = Animal('Chai', 'cat')
        c3 = Animal('Alma', 'cat')
        a.enqueue(d1, c1, d2, c2, d3, c3)
        self.assertEqual(len(a), 6)
        oldest = a.dequeueAny()
        self.assertEqual(d1, oldest)
        self.assertEqual(len(a), 5)
        self.assertEqual(len(a.dogs), 2)
        self.assertEqual(len(a.cats), 3)
        # scenario 4: both cats and dogs, but global oldest is cat (continuing from scenario 3)
        oldest = a.dequeueAny()
        self.assertEqual(c1, oldest)
        self.assertEqual(len(a), 4)
        self.assertEqual(len(a.dogs), 2)
        self.assertEqual(len(a.cats), 2)

if __name__ == '__main__':
    unittest.main()
