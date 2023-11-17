from dataclasses import dataclass
from typing import List

from pydantic import Field


@dataclass
class Member:
    name: str
    category: str


@dataclass
class Draw:
    members: List[Member] = Field(min_length=1)
