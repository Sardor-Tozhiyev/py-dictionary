from typing import Any


class Dictionary:
    initial_capacity = 8
    load_factor = 2 / 3

    def __init__(self) -> None:
        self.capacity = self.initial_capacity
        self.size = 0
        self.table: list = [None] * self.capacity

    def _resize(self) -> None:
        old_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0

        for item in old_table:
            if item is not None:
                self.__setitem__(item[0], item[2])

    def __setitem__(self, key: Any, value: Any) -> None:
        if self.size >= self.capacity * self.load_factor:
            self._resize()

        hash_value = hash(key)
        index = hash_value % self.capacity

        while self.table[index] is not None:
            if (self.table[index][1] == hash_value
                    and self.table[index][0] == key):
                self.table[index] = (key, hash_value , value)
                return
            index = (index + 1) % self.capacity

        self.table[index] = (key, hash_value , value)
        self.size += 1

    def __getitem__(self, key: Any) -> None:
        hash_value = hash(key)
        index = hash_value % self.capacity

        while self.table[index] is not None:
            if (self.table[index][1] == hash_value
                    and self.table[index][0] == key):
                return self.table[index][2]
            index = (index + 1) % self.capacity

        raise KeyError(key)

    def __len__(self) -> int:
        return self.size
