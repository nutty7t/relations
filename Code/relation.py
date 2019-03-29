from collections import namedtuple
from collections.abc import Iterable
from typing import Callable, Iterable, NamedTuple, Optional, Set, Union


class Attribute(NamedTuple):
    """
    An attribute is an ordered pair of attribute name and type name.
    """
    name: str
    type: type


class RelationScheme:
    """
    A relation scheme is a finite set of attribute names, { A₁, A₂, ...,
    Aₙ }. Corresponding to each attribute name Aᵢ is a set Dᵢ, 1 <= i <=
    n, called the domain of Aᵢ.
    """

    def __init__(self, attributes: Iterable[Attribute] = []) -> None:
        for attribute in attributes:
            if type(attribute.name) != str:
                raise TypeError(f'invalid attribute name: {attribute.name}')
            if type(attribute.type) != type:
                raise TypeError(f'invalid attribute type: {attribute.type}')

        self.attributes = set(attributes)
        self.domains = {}
        for attribute in attributes:
            self.domains[attribute.name] = Optional[attribute.type]


class Relation:
    """
    A relation on a relation scheme is a subset of the Cartesian product
    of the domains of the attributes in the relation scheme.
    """

    # [NOTE] Because `tuple` is a keyword in Python, some variables are
    # named `row` or `rows`. Just know that rows and tuples are
    # interchangeable.

    def validate_tuples(func: Callable) -> Callable:
        """Check that the rows argument conforms to the relation scheme."""
        def decorating_function(self, rows: Iterable[NamedTuple]) -> None:
            # wrap single values into an iterable
            if type(rows) == self.Tuple:
                rows = [rows]
            # check that tuples are valid
            def is_valid(row):
                return type(row) == self.Tuple
            if all(map(is_valid, rows)):
                func(self, rows)
            else:
                raise TypeError(f'invalid tuple(s)')
        return decorating_function

    def __init__(self, scheme: RelationScheme) -> None:
        self.tuples = set()
        self.scheme = scheme
        # self.Tuple enforces the scheme on every tuple in the relation
        self.Tuple = NamedTuple('Tuple', self.scheme.attributes)

    @validate_tuples
    def add(self, rows: Union[NamedTuple, Iterable[NamedTuple]]) -> None:
        """Add a tuple(s) to the relation."""
        self.tuples |= set(rows)

    @validate_tuples
    def delete(self, rows: Union[NamedTuple, Iterable[NamedTuple]]) -> None:
        """Delete a tuple(s) from the relation."""
        self.tuples -= set(rows)

    def change(self, old: NamedTuple, new: NamedTuple) -> None:
        """Modifies a tuple in the relation."""
        # Not implemented. I'm feeling lazy. Anyway, the change
        # operation is mainly a convenience. The same result can be
        # obtained with a delete followed by an add.
        pass

