"""Test for the data_structures.stacks module.

TestStack:
    Tests for the Stack class.
"""

import unittest
from data_structures.stacks import Stack
from random import random


class TestStack(unittest.TestCase):
    """Tests for the Stack class.

    Stacks are a type data structures that contains items with the
    following two rules:
      - items can only be added to the stack from the "top"
      - items can only be removed from the stack from the "top"

    Methods
    -------
    test_push:
        Push must add items to the top of the stack.

    test_peak:
        Peak must show the top element of the stack.

    test_pop:
        Pop must remove the top element from the stack.

    test_size:
        Size must return the amount of items in the stack.
    """

    def test_push(self):
        """Push must add items to the top of the stack."""

        stack = Stack()
        items = []
        for length in range(10):
            number = random()
            stack.push(number)
            items.append(number)
            self.assertEqual(stack._items, items)

        stack.push("asd")
        items.append("asd")
        self.assertEqual(stack._items, items)
        another_stack = Stack()
        stack.push(another_stack)
        items.append(another_stack)
        self.assertEqual(stack._items, items)
        stack.push(1+1j)
        items.append(1+1j)
        self.assertEqual(stack._items, items)

    def test_peak(self):
        """Peak must show the top element of the stack."""

        stack = Stack()
        # empty stack should raise an error when peaking
        self.assertRaises(IndexError, stack.peak)
        for _ in range(100):
            number = random()
            stack.push(number)
            self.assertEqual(stack.peak(), number)

        stack.push("asd")
        self.assertEqual(stack.peak(), "asd")
        stack.push(1-3j)
        self.assertEqual(stack.peak(), 1-3j)

    def test_pop(self):
        """Pop must remove the top element from the stack."""

        stack = Stack()
        # empty stack should raise an error when poping
        self.assertRaises(IndexError, stack.pop)
        for _ in range(100):
            number = random()
            stack.push(number)

        stack.push("asd")
        stack.push(1 - 3j)

        for _ in range(102):
            peak = stack.peak()
            pop = stack.pop()
            self.assertEqual(peak, pop)

        self.assertRaises(IndexError, stack.pop)

    def test_size(self):
        """Size must return the amount of items in the stack."""

        stack = Stack()
        num_elements = 20
        for length in range(num_elements):
            self.assertEqual(stack.size(), length)
            stack.push(random())

        stack.pop()
        self.assertEqual(stack.size(), num_elements - 1)
        stack.pop()
        self.assertEqual(stack.size(), num_elements - 2)
