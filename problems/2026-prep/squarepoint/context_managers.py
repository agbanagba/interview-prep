
from contextlib import contextmanager
from typing import Callable, Iterator, Optional, Tuple, Generator

# context managers as a class uses enter and exit 
# 

class Transaction:

    def __enter__(self):
        print("BEGIN")
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc_type is None:
            print("COMMIT")
        else:
            print(f"ROLLBACK (due to {exc_type.__name__}: {exc})")
        return False


@contextmanager
def transaction() -> Generator[None]:
    print("BEGIN")
    try:
        yield
    except Exception:
        print("ROLLBACK")
        raise
    else:
        print("COMMIT")



with transaction():
    print(" doing work ")
    raise RuntimeError("boom")
