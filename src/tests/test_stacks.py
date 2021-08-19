"""Test for the data_structures.stacks module.

TestStack:
    Tests for the Stack class.

TestTypeRestrictedStack:
    Tests for the TypeRestrictedStack class.
"""

import unittest
from data_structures.elements import Number
from data_structures.stacks import Stack, TypeRestrictedStack
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


class TestTypeRestrictedStack(unittest.TestCase):
    """Tests for the TypeRestrictedStack class.

    Methods
    -------
    test_init:
        TestTypeRestrictedStack must be initialized with a class.

    test_accept_cls_immutability:
        Type restricted stacks should have an immutable restriction.

    test_type_verification:
        TypeRestrictedStack.type_verification should raise only with
        forbidden objects.

    test_verify_types:
        TypeRestrictedStack.verify_types raise with any forbidden item in it.

    test_restricted_push:
        Pushes in TypeRestrictedStacks must apply type restrictions.
    """

    def test_init(self):
        """TypeRestrictedStack must be initialized with a class."""

        x = TypeRestrictedStack()
        self.assertEqual(x.acceptable_class, Number)

    def test_accept_cls_immutability(self):
        """TRS should have an immutable restriction."""

        def redefine_acceptable_class(another_object_or_class):
            x = TypeRestrictedStack()
            x.acceptable_class = another_object_or_class

        self.assertRaises(AttributeError, redefine_acceptable_class, 1.2)
        self.assertRaises(AttributeError, redefine_acceptable_class, int)

    def test_type_verification(self):
        """TRS.type_verification raise only with forbidden objects."""

        x = TypeRestrictedStack(float)
        try:
            x.type_verification(1.21)
        except ValueError:
            msg = ("TypeRestrictedStack.verify_types"
                   + "raised an unexpected error")
            self.fail(msg)

        self.assertRaises(ValueError, x.type_verification, 1)
        self.assertRaises(ValueError, x.type_verification, "asd")
        y = TypeRestrictedStack(str)
        try:
            y.type_verification("pepe")
        except ValueError:
            msg = ("TypeRestrictedStack.type_verification"
                   + "raised an unexpected error")
            self.fail(msg)

        self.assertRaises(ValueError, y.type_verification, 1.2)

    def test_verify_types(self):
        """TRS.verify_types raise with any forbidden item in it."""

        x = TypeRestrictedStack(str)
        x._items = ["asd", "dqw", "123"]
        try:
            x.verify_types()
        except ValueError:
            msg = ("TypeRestrictedStack.verify_types"
                   + "raised an unexpected error")
            self.fail(msg)

        x._items.append(1.2)
        self.assertRaises(ValueError, x.verify_types)

    def test_restricted_push(self):
        """Pushes in TRSs must apply type restrictions."""

        x = TypeRestrictedStack(int)
        try:
            x.push(2)
            x.push(3)
        except ValueError:
            msg = ("TypeRestrictedStack.push"
                   + "raised an unexpected error")
            self.fail(msg)

        self.assertRaises(ValueError, x.push, 1.2)
        self.assertRaises(ValueError, x.push, "asd")
        y = TypeRestrictedStack()
        self.assertRaises(ValueError, y.push, 3.14)
