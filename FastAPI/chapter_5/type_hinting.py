# name: type
# name: type = value
# thing: str = "yeti"

from typing import Str, Any, Union

thing: Str = "yeti"
physics_magic_number: float = 1.0 / 137.03599913
hp_lovecraft_noun: str = "ichor"
exploading_sheep: tuple = ["sis", "boom", "bah!"]
responses: dict = {"Marco": "Polo", "answer": 42}

# name: dict[keytype, valtype] = {key1: val1, key2: val2}
responses: dict[str, Any] = {"Marco": "Polo", "answer": 42}
responses: dict[str, Union[str, int]] = {"Marco": "Polo", 'answer': 42}
responses: dict[str, str | int] = {"Marco": "Polo", "answer": 42}


def get_thing() -> str:
    return "yeti"
