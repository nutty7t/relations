from collections import namedtuple
from collections.abc import Iterable
from functools import partial
from itertools import (
    chain,
    combinations,
    product,
    tee
)
from operator import ne
from typing import (
    Callable,
    Iterable,
    NamedTuple,
    Optional,
    Set,
    Tuple,
    Union,
)


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


class Relation:
    """
    A relation on a relation scheme is a subset of the Cartesian product
    of the domains of the attributes in the relation scheme.
    """

    # [NOTE] Because `tuple` is a keyword in Python, some variables are
    # named `row` or `rows`. Just know that rows and tuples are
    # interchangeable.

    def __init__(self, scheme: RelationScheme) -> None:
        self.tuples = set()
        self.scheme = scheme
        # self.Tuple enforces the scheme on every tuple in the relation.
        self.Tuple = NamedTuple('Tuple', self.scheme.attributes)

    def validate_tuples(func: Callable) -> Callable:
        """Check that the rows argument conforms to the relation scheme."""

        def decorating_function(self, rows: Iterable[NamedTuple]) -> None:
            # wrap single values into an iterable
            if type(rows) == self.Tuple:
                rows = [rows]
            def is_valid(row):
                return type(row) == self.Tuple
            if all(map(is_valid, rows)):
                func(self, rows)
            else:
                raise TypeError(f'invalid tuple(s)')

        return decorating_function

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

    def superkeys(self) -> Set:
        """Return all superkeys for this relation instance."""

        # A superkey of a relation is a subset of the relation scheme
        # attributes such that no two distinct tuples in the relation
        # have the same values for all attributes in the subset.
        superkeys = set()

        # Get all distinct pairs of tuples in the relation.
        pairs: Iterable[Tuple[NamedTuple]] = product(self.tuples, self.tuples)
        distinct_pairs: Iterable = list(filter(lambda pair: ne(*pair), pairs))

        def matching_attribute(pair: Tuple, attribute: Attribute) -> bool:
            """
            Return True if the values for the given attribute are equal
            for both tuples; false otherwise.
            """
            return getattr(pair[0], attribute.name) == \
                   getattr(pair[1], attribute.name)

        def all_matching_attributes(pair: Tuple, attributes: Iterable) -> bool:
            """
            Return True if all of the values for each attribute in
            attributes are equal in the pair of tuples.
            """
            return all(map(partial(matching_attribute, pair), attributes))

        # All possible combinations of attributes in the scheme.
        powerset: Iterable[Set[Attribute]] = chain.from_iterable(
            combinations(self.scheme.attributes, arity)
            for arity in range(len(self.scheme.attributes) + 1)
        )

        for attributes in powerset:
            if not any(map(
                partial(all_matching_attributes, attributes=attributes),
                distinct_pairs
            )):
                superkeys |= {attributes}

        return superkeys

    def keys(self) -> Set:
        """Return all of the (candidate) keys for this relation instance."""

        # A (candidate) key is a minimal superkey.
        superkeys: Set = self.superkeys()
        keys: Set = set(superkeys)

        # Remove non-minimal keys from the set of superkeys.
        for superkey in superkeys:
            membership: Callable = lambda key: set(key) < set(superkey)
            if any(map(membership, superkeys - {superkey})):
                keys -= {superkey}

        return keys

