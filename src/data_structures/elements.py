"""Basic elements to use in data structures.

Classes
-------

Number:
    Immutable real numbers.
"""

__all__ = ['Number']

from typing import NoReturn, Union
from functools import total_ordering


@total_ordering
class Number:
    """Immutable real numbers.

    Properties
    ----------
    number: float or int
        Read-only/immutable number (float or int).

    Methods
    -------
    copy:
        Returns a copy of the instance (a new instance).
    """

    def __init__(self, number: Union[int, float]) -> NoReturn:
        """Creates an instance of the class Number.

        Parameters
        ----------
        number: int or float
            The value for the Number instance.

        Raises
        ------
        AssertionError:
            Raises an assertion error when attempting to initialize
            with a value that it's not a real number.
        """

        msg = "Number must be float or string"
        assert isinstance(number, int) or isinstance(number, float), msg
        self.__number = number

    @property
    def number(self) -> Union[int, float]:
        """Number property of the instance, it's immutable real value.

        Returns
        -------
        number: int or float
            A real number.
        """

        return self.__number

    def __eq__(self, other: 'Number') -> bool:
        """Verify equality of values for two Number instances.

        Parameters
        ----------
        other: Number
            Another instance of the Number class.

        Returns
        -------
        bool:
            True if instances should be considered equal for ordering,
            else False.

        Raises
        ------
        NotImplementedError:
            When comparing with an object that is not an instance of
            Number.
        """

        if not isinstance(other, self.__class__):
            raise NotImplementedError
        return self.number == other.number

    def __lt__(self, other: 'Number') -> bool:
        """Verify equality of values for two Number instances.

        Parameters
        ----------
        other: Number
            Another instance of the Number class.

        Returns
        -------
        bool:
            True if this instance, 'self' has a value strictly lower
            than the value of the 'other' instance.

        Raises
        ------
        NotImplementedError:
            When comparing with an object that is not an instance of
            Number.
        """

        if not isinstance(other, self.__class__):
            raise NotImplementedError
        return self.number < other.number

    def __repr__(self) -> str:
        """Prints the number value of the instance."""

        return f"{self.number}"

    def copy(self) -> 'Number':
        """Returns a copy of the instance (a new instance)."""

        return self.__class__(self.number)
