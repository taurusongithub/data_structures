"""Stack-like data structures.

Classes
-------

Stack:
    Basic stack data structure.
"""

__all__ = ['Stack', 'TypeRestrictedStack']

import inspect
from typing import NoReturn, Any, Type, Optional
from data_structures.elements import Number


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


class TypeRestrictedStack(Stack):
    """Stack that only allow instances of a certain class to be pushed.

    Properties
    ----------
    acceptable_class: any class
        This is an immutable property, any new item pushed to the stack
        must be an instance of the acceptable class.

    Methods
    -------
    push:
        Push a new item to the top of the stack, must be an instance of
        the acceptable class.

    pop:
        Removes the top item from the stack and returns it.

    peak:
        Returns the top item of the stack without removing it.

    size:
        Length of the list of items currently in the stack.

    type_verification:
        Checks that an item is an instance of the acceptable class.

    verify_types:
        Verifies that all items in the stack are valid.
    """

    def __init__(self,
                 acceptable_class: Optional[Type[Any]] = Number) -> NoReturn:
        """A stack that only allows items of a certain class.

        Parameters
        ----------
        acceptable_class: any class, optional
            Any class, this will be an immutable property. All items
            pushed to this stack will be checked to be an instance of
            that class. The default value is the class Number from the
            data_structures.elements module.

        Raises
        ------
        AssertionError:
            If the value of the acceptable_class parameter is not a
            class.
        """

        msg = "TypeRestrictedStacks should be restricted with a class."
        assert inspect.isclass(acceptable_class), msg
        super().__init__()
        self.__acceptable_class = acceptable_class

    @property
    def acceptable_class(self) -> Type[Any]:
        """The class that is restricting items of the stack."""

        return self.__acceptable_class

    def type_verification(self, item: Any) -> NoReturn:
        """Checks that an item is an instance of the acceptable class

        Parameter
        ---------
        item: any
            Any object.

        Raises
        ------
        ValueError:
            If item is not an instance of the acceptable class.
        """

        if not isinstance(item, self.acceptable_class):
            raise ValueError("items in the stack must be an instance of "
                             + self.acceptable_class.__name__)

    def verify_types(self) -> NoReturn:
        """Verifies that all items in the stack are valid.

        Raises
        ------
        ValueError:
            If any item in the stack is not an instance of the
            acceptable class.
        """

        for item in self._items:
            self.type_verification(item)

    def push(self, new_item: Any) -> NoReturn:
        """Push a new item to the top of the stack.

        Parameters
        ----------
        new_item: instance of the acceptable class
            An item to push to the top to the stack, it must be an
            instance of the acceptable class.

        Raises
        ------
        ValueError:
            If the new_item is not an instance of the acceptable class.
        """

        self.type_verification(new_item)
        super().push(new_item)
