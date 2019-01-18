#!/usr/bin/python3
'''Animal Shelter: An animal shelter, which holds only
dogs and cats, operates on a strictly"first in, first
out" basis. People must adopt either the "oldest"
(based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or
a cat (and will receive the oldest animal of that type).
They cannot select which specific animal they would
like. Create the data structures to maintain this
system and implement operations such as enqueue,
dequeueAny, dequeueDog, and dequeueCat. You may use
the built-in Linked list data structure.
Hints: #22, #56, #63'''
import unittest


class ShelterQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, animal):
        if len(self.queue) == 0:
            self.queue.append(animal)
        else:
            self.queue.insert(0, animal)

    def printQueue(self):
        print('----- Beginning of Queue ------')
        for x in self.queue[::-1]:
            print(x)
        print('------ End of Queue ------')

    def dequeueAnimal(self, animal):
        if len(self.queue) == 0:
            return
        temp = False
        for x in self.queue[::-1]:
            if animal in x:
                temp = x
                break
        if temp:
            pet = temp
            self.queue.remove(temp)
            return pet

    def dequeueDog(self):
        return self.dequeueAnimal('D')

    def dequeueCat(self):
        return self.dequeueAnimal('C')

    def dequeueAny(self):
        if len(self.queue) == 0:
            return
        return self.queue.pop()


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        q = ShelterQueue()
        animals = ['D1', 'D2', 'C1', 'D3', 'C2', 'C3', 'C4']
        for x in animals:
            q.enqueue(x)

        q.printQueue()
        print('{}  got adopted!'.format(q.dequeueDog()))  # D1
        print('{}  got adopted!'.format(q.dequeueCat()))  # C1
        q.printQueue()

        print('{}  got adopted!'.format(q.dequeueAny()))  # D2
        print('{}  got adopted!'.format(q.dequeueCat()))  # C2
        print('{}  got adopted!'.format(q.dequeueAny()))  # D3
        print('{}  got adopted!'.format(q.dequeueDog()))  # No Dogs
        print('{}  got adopted!'.format(q.dequeueAny()))  # C3
        print('{}  got adopted!'.format(q.dequeueCat()))  # C4
        print('{}  got adopted!'.format(q.dequeueCat()))  # No Cats

    @classmethod
    def tearDownClass(cls):
        pass

    def test1(self):
        pass


if __name__ == '__main__':
    unittest.main()
