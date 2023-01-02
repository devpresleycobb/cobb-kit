from dataclasses import dataclass
from typing import Callable


@dataclass
class MenuItem:

    text: str
    command: Callable
