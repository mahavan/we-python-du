"""
Task 1
Create a class containing a set of integers. The class should have the following functionality implemented:
The sum of elements in the set.
Arithmetic mean of elements in the set.
Maximum of the elements in the set.
Minimum of the elements in the set.
Test all the possibilities of the created class using unit testing (unittest)."""

class IntegerSet:
    def __init__(self, elements):
        self.elements = set(elements)

    def get_sum(self):
        return sum(self.elements)

    def get_arith_mean(self):
        return sum(self.elements) / len(self.elements)

    def get_max(self):
        return max(self.elements)

    def get_min(self):
        return min(self.elements)

# Unit tests
import unittest

class TestIntegerSet(unittest.TestCase):
    int_set = IntegerSet([1, 2, 10, 3, 4, 5])

    def test_sum(self):
        self.assertEqual(self.int_set.get_sum(), 25)

    def test_arith_mean(self):
        self.assertEqual(self.int_set.get_arith_mean(), 4.1667)
        # záměrně dané periodické číslo ke zjištění přesnosti zaokrouhlování

    def test_max(self):
        self.assertEqual(self.int_set.get_max(), 10)

    def test_min(self):
        self.assertEqual(self.int_set.get_min(), 1)
