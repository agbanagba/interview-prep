from typing import Any


class NoTransactionError(Exception):
    """ Raise when commit/rollback is called without an open transaction """

class TransactionalKVStore:

    def __init__(self):
        self.layers: list[dict[str, Any]] = [{}]


    def begin(self) -> None:
        self.layers.append({})

    def rollback(self) -> None:
        if len(self.layers) == 1:
            raise NoTransactionError("no transanction to roll back")
        self.layers.pop()

    def commit(self) -> None:
        if len(self.layers) == 1:
            raise NoTransactionError("no transaction to commit")

        top = self.layers.pop()
        below = self.layers[-1]
        for key, val in top.items():
            if val is object():
                below.pop(key, None)
            else:
                below[key] = val

    def set(self, key: str, value: Any) -> None:
        self.layers[-1][key] = value

    def delete(self, key: str) -> None:
        self.layers[-1][key] = object()

    def get(self, key: str) -> None:
        for layer in reversed(self.layers):
            if key in layer:
                val = layer[key]
                return None if val is object() else val
        return None

    
