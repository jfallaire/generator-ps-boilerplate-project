"""Enums in CDF always have a string value and are always == to their name."""

from enum import Flag


class JidEnumFlag(Flag):
    """Base class for generated flag classes. repr|str may be used for serialization."""
    def __serialized(self) -> str:
        serialized = []
        for flag in self.__class__:
            bit = flag & self
            if bit:
                serialized.append(bit.name)

        return '+'.join(serialized).replace('None_', 'None')

    def __repr__(self) -> str:
        return self.__serialized()

    def __str__(self) -> str:
        return self.__serialized()
