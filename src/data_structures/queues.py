"""Queue-like data structures.

Classes
-------

Queue:
    Basic queue data structure.
"""

__all__ = ['Queue']

from data_structures.stacks import Stack
from typing import Any, NoReturn


class Queue:
    """Basic queue data structure.

    Queues are a type of data structures that contains items with the
    following rules:
      - items can only be added to the queue from the "right",
      - items can only be removed from the queue from the "left".

    Queues in this class are implemented via 2 stacks, an input stack
    and an output stack. When popping from an output stack, the input
    stack must be flushed to the output stack.

    Methods
    -------
    push:
        Push a new item to the right end of the queue.

    pop:
        Removes the left most item from the queue and returns it.

    peak:
        Returns the left most item of the queue without removing it.

    size:
        Length of the list of items currently in the queue.
    """

    def __init__(self) -> NoReturn:
        """Iinitializes the input and output stacks."""

        self._input_stack = Stack()
        self._output_stack = Stack()

    def push(self, new_item: Any) -> NoReturn:
        """Push a new item to the right end of the queue.

        Parameters
        ----------
        new_item: any
            An item to push to the right end of the queue, could be
            anything.
        """

        self._input_stack.push(new_item)

    def _flush_inputs_to_outputs(self) -> NoReturn:
        """Pushes all items in the input stack to the output stack.

        This function leaves the input stack empty, popping each and
        every element from the input stack and pushing it to the output
        stack.
        """

        size_of_input_stack = self._input_stack.size()
        for _ in range(size_of_input_stack):
            self._output_stack.push(self._input_stack.pop())

    def peak(self) -> Any:
        """Returns the left most item of the queue without removing it.

        Returns
        -------
        left_item: Any
            The left most item of the queue.

        Raises
        ------
        IndexError:
            When the queue is empty.
        """

        self._flush_inputs_to_outputs()
        try:
            return self._output_stack.peak()
        except IndexError:
            raise IndexError("The Queue is empty!")

    def pop(self) -> Any:
        """Removes the left most item from the queue and returns it.

        Returns
        -------
        left_item: Any
            The left most item of the queue, prior to removal.

        Raises
        ------
        IndexError:
            When the queue is empty.
        """

        self._flush_inputs_to_outputs()
        try:
            return self._output_stack.pop()
        except IndexError:
            raise IndexError("The Queue is empty!")

    def size(self) -> int:
        """Length of the list of items currently in the queue."""

        return self._input_stack.size() + self._output_stack.size()

    def __repr__(self) -> str:
        if self.size() == 0:
            return "Empty " + str(self.__class__.__name__)
        print_val = ("Queue elements:\n"
                     + "\tInput stack:\n\t\t"
                     + str(self._input_stack)
                     + "\n\tOutput stack:\n\t\t"
                     + str(self._output_stack))
        return print_val
