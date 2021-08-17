"""Test for the data_structures.queues module.

TestQueue:
    Tests for the Queue class.
"""

import unittest
from data_structures.queues import Queue
from random import random


class TestQueue(unittest.TestCase):
    """Tests for the Queue class.

    Queues are a type of data structures that contains items with the
    following rules:
      - items can only be added to the stack from the "right"
      - items can only be removed from the stack from the "left"

    Methods
    -------
    test_push:
        Push must add items to the right end of the queue.

    test_peak:
        Peak must show the left most element of the queue.

    test_pop:
        Pop must remove the left most element from the queue.

    test_size:
        Size must return the amount of items in the queue.
    """

    def test_push(self):
        """Push must add items to the right end of the queue."""

        queue = Queue()
        items = []
        for length in range(10):
            number = random()
            queue.push(number)
            items.append(number)

        queue.push("asd")
        items.append("asd")
        another_queue = Queue()
        queue.push(another_queue)
        items.append(another_queue)
        queue.push(1 + 1j)
        items.append(1 + 1j)

        self.assertEqual(queue._input_stack._items, items)

        queue._flush_inputs_to_outputs()
        items.reverse()
        self.assertEqual(queue._output_stack._items, items)

    def test_peak(self):
        """Peak must show the left most element of the queue."""

        queue = Queue()
        # empty queue should raise an error when peaking
        self.assertRaises(IndexError, queue.peak)
        items = []
        for _ in range(100):
            number = random()
            items.append(number)
            queue.push(number)

        queue.push("asd")
        items.append("asd")
        queue.push(1 - 3j)
        items.append(1 - 3j)

        self.assertEqual(queue.peak(), items[0])

    def test_pop(self):
        """Pop must remove the left most element from the queue."""

        queue = Queue()
        # empty queue should raise an error when poping
        self.assertRaises(IndexError, queue.pop)
        for _ in range(100):
            number = random()
            queue.push(number)

        queue.push("asd")
        queue.push(1 - 3j)

        for _ in range(102):
            peak = queue.peak()
            pop = queue.pop()
            self.assertEqual(peak, pop)

        self.assertRaises(IndexError, queue.pop)

    def test_size(self):
        """Size must return the amount of items in the queue."""

        queue = Queue()
        num_elements = 20
        for length in range(num_elements):
            self.assertEqual(queue.size(), length)
            queue.push(random())

        queue.pop()
        self.assertEqual(queue.size(), num_elements - 1)
        queue.pop()
        self.assertEqual(queue.size(), num_elements - 2)
