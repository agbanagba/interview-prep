import functools
import time
from contextlib import contextmanager
from typing import Callable, Iterator, Optional, Tuple


# Simple case. 
def changecase(func: Callable):
    @functools.wraps(func)
    def myinner(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return myinner

@changecase
def myfunction(name):
    return f"Hello {name}"


# More complicated case of the decorator taking an argument
def changecase1(n):
    def changecase(func: Callable):
        def myinner(*args, **kwargs):
            if n == 1:
                a = func(*args, **kwargs).lower()
            else:
                a = func(*args, **kwargs).upper()
            return a
        return myinner
    return changecase

def retry(
    max_attempts: int = 3,
    delay: float = 0.5,
    exceptions: Tuple[type, ...] = (Exception,),
    backoff: bool = False,
):

    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exc: Optional[BaseException] = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    last_exc = exc
                    is_last = attempt == max_attempts - 1
                    if is_last:
                        break
                    sleep_for = delay * (2 ** attempt) if backoff else delay
                    time.sleep(sleep_for)
            return last_exc
        return wrapper
    return decorator


attempts = {"n": 0}

@retry(max_attempts=5)
def retry_func(name):
    attempts["n"] += 1
    print(f"attempt {attempts["n"]}")
    if attempts["n"] < 4:
        raise ValueError("transient failure")
    return f"Hello, {name}"

print(myfunction.__name__)

# I have to understand why we use functools.wraps
import functools


# a keargs value can 
def memoize(func):
    cache = OrderedDict() # here, we can use a hashmap + doubly linked list implementation. 

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = repr(args, tuple(sorted(kwargs.item())))
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper

@memoize
def square(n):
    return n*n

print(square.__name__)