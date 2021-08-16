"""Test for the data_structures.elements module.

TestNumber:
    Tests for the Number class.
"""

import unittest
from data_structures.elements import Number
from random import uniform


class TestNumber(unittest.TestCase):
    """Tests for the Number class.

    The Number class should be an implementation for immutable
    real numbers with total ordering.

    Methods
    -------
    test_numbers_copying:
        A copy should be a different instance with equal value.

    test_numbers_equality:
        Equality of Number instances is defined by it's values.

    test_numbers_inequalities:
        Inequalities should work by the real values of instances.

    test_numbers_values:
        Initialization without real numbers should raise error.

    test_numbers_immutability:
        Number instances should be immutable.
    """

    def test_numbers_copying(self):
        """A copy should be a different instance with equal value."""

        x = Number(4)
        y = x.copy()
        self.assertEqual(x, y, "A copy should be equal to the original!")
        self.assertIsNot(x, y, "A copy should be a different instance!")

    def test_numbers_equality(self):
        """Equality of Number instances is defined by it's values."""

        x = Number(3)
        y = Number(3.)
        z = Number(4)
        self.assertEqual(x, y, "x and y should be considered equal!")
        self.assertNotEqual(x, z, "x and z should not be equal!")

    def test_numbers_inequalities(self):
        """Inequalities should work by the real values of instances."""

        n_examples = 100
        values = [uniform(-10, 10) for _ in range(n_examples)]
        numbers = [Number(value) for value in values]
        for index in range(n_examples-1):
            if values[index] <= values[index+1]:
                self.assertLessEqual(numbers[index], numbers[index+1])
            else:
                self.assertGreater(numbers[index], numbers[index+1])

    def test_numbers_values(self):
        """Initialization without real numbers should raise error."""

        self.assertRaises(AssertionError, lambda x: Number(x), "anything")
        # complex numbers shouldn't be allowed
        self.assertRaises(AssertionError, lambda x: Number(x), 1 + 1j)

    def test_numbers_immutability(self):
        """Number instances should be immutable."""
        y = Number(3.14)

        def evil_assignment(x):
            nonlocal y
            y.number = x

        self.assertRaises(AttributeError, evil_assignment, 3)
        y.__number = 3
        y._number = 3
        self.assertNotEqual(y.number, 3)
        self.assertEqual(y.number, 3.14)
