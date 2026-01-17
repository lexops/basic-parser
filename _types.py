from dataclasses import dataclass
from typing import Literal


@dataclass
class Token:
    kind: Literal["NUMBER", "OPERATOR"]
    val: int
