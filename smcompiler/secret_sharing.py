"""
Secret sharing scheme.
"""

from __future__ import annotations

from typing import List
from random import randint
import json

# our p to establish the Field F
field = 307


class Share:
    """
    A secret share in a finite field.
    """

    def __init__(self, *args, **kwargs):
        self.value = value % field

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
    shares = [Share() for _ in range(num_shares)]
        shares[0] = Share(secret)
        for i in range(1, num_shares): 
            shares[i] = Share(randint(0, Share.p))
            shares[0] -= shares[i]
        return shares 


def reconstruct_secret(shares: List[Share]) -> int:
    res = Share()
    for share in shares:
        res += share
    return res.value


# Feel free to add as many methods as you want.

#method for add from theory
def addProt(left, right):
    return (left+right) % (field)
