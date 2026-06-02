from dataclasses import dataclass
from typing import Dict, List, Any


@dataclass
class Field:
    name: str
    type: str


@dataclass
class Model:
    table: str
    fields: Dict[Field, Any]
