
from typing import TypedDict

class Persion(TypedDict):
    name: str
    age: int

new_persion: Persion = {'name':'Raja', 'age': 25}

print(new_persion)