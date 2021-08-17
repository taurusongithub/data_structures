"""Stack-like data structures.

Classes
-------

Stack:
    Basic stack data structure.
"""

__all__ = ['Stack']

from typing import NoReturn, Any


class Stack:
    """Basic stack data structure.

    Stacks are a type data structures that contains items with the
    following two rules:
      - items can only be added to the stack from the "top"
      - items can only be removed from the stack from the "top"

    Methods
    -------
    push:
        Push a new item to the top of the stack.

    pop:
        Removes the top item from the stack and returns it.

    peak:
        Returns the top item of the stack without removing it.

    size:
        Length of the list of items currently in the stack.
    """

    def __init__(self) -> NoReturn:
        """Initializes an empty items list for the stack."""

        self._items = []

    def push(self, new_item: Any) -> NoReturn:
        """Push a new item to the top of the stack.

        Parameters
        ----------
        new_item: any
            An item to push to the top to the stack, could be anything.
        """

        self._items.append(new_item)

    def pop(self) -> Any:
        """Removes the top item from the stack and returns it.

        Returns
        -------
        top_item: Any
            The item at the top of the stack, prior to removal.

        Raises
        ------
        IndexError:
            When the stack is empty.
        """

        try:
            top_item = self._items.pop()
            return top_item
        except IndexError:
            raise IndexError("Empty Stack")

    def peak(self) -> Any:
        """Returns the top item of the stack without removing it.

        Returns
        -------
        top_item: Any
            The item at the top of the stack.

        Raises
        ------
        IndexError:
            When the stack is empty.
        """

        try:
            top_item = self._items[-1]
            return top_item
        except IndexError:
            raise IndexError("Empty Stack")

    def size(self) -> int:
        """Length of the list of items currently in the stack."""

        return len(self._items)

    def __repr__(self) -> str:
        if self.size() == 0:
            return "Empty " + str(self.__class__.__name__)
        print_val = ("Stack Elements: "
                     + "; ".join([str(item) for item in self._items]))
        return print_val
