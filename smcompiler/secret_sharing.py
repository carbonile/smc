"""
Secret sharing scheme.
"""

from __future__ import annotations

from typing import List
import random
import json


class Share:
    """
    A secret share in a finite field.
    """

    def __init__(self, *args, **kwargs):
        self.value = value

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value})"

    def __add__(self, other):
        return Share(addProt(self.value, other.value))

    def __sub__(self, other):
        raise NotImplementedError("You need to implement this method.")

    def __mul__(self, other):
        raise NotImplementedError("You need to implement this method.")

    def serialize(self):
        return json.dumps({"value": self.value})

    @staticmethod
    def deserialize(serialized) -> Share:
        data = json.loads(serialized)
        return Share(data["value"])


def share_secret(secret: int, num_shares: int) -> List[Share]:
    shares = []
    nthShareVal = Share(secret)
    for i in range(num_shares - 1):
        iShare = Share(random.randint(0, mod_field))
        nthShareVal -= iShare
        shares.append(iShare)
    shares.append(nthShareVal)
    return shares


def reconstruct_secret(shares: List[Share]) -> int:
    fullSecret = sum(shares, Share(0))
    return fullSecret.value


# Feel free to add as many methods as you want.

#method for add from theory
def addProt(left, right):
    return (left+right) % (mod_field)
