from dataclasses import dataclass
from typing import List

from pydantic import Field


@dataclass
class Participant:
    name: str = Field(max_length=50)
    category: str = Field(max_length=50)


@dataclass
class Draw:
    participants: List[Participant] = Field(min_length=2, max_length=100)
