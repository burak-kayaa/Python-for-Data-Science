import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))

def generate_login(name: str, surname: str) -> str:
    return (name[0] + surname).lower()

@dataclass
class Student:
    id: str = field(default_factory=generate_id, init=False)
    name: str
    login: str = field(init=False)
    surname: str
    active: bool = True
    def __post_init__(self):
        self.login = generate_login(self.name, self.surname)