#!/usr/bin/env python3
"""This is module that defines a Cache class"""
from typing import Union, Callable
from functools import wraps
import uuid
import redis


def count_calls(method: Callable) -> Callable:
    """
    This is a decorator function that takes
    in a Callable and returns Callable
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        This is a wrapper function that uses the qualified
        name of a method as a key, and increments the count
        for that key each time the method is called
        """
        key = method.__qualname__

        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    This is a decorator that
    Stores the input and output of a particular function
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        This is a wrapper function that appends the inputs and
        outputs of method to a list
        """
        input_list = f"{method.__qualname__}:inputs"
        output_list = f"{method.__qualname__}:outputs"

        input_value = str(args)
        self._redis.rpush(input_list, input_value)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(output_list, output)
        return output
    return wrapper


def replay(method: Callable) -> Callable:
    """
    This is a function that displays the history
    of calls of a particular function.
    """
    key = method.__qualname__

    calls_count = method.__self__._redis.get(key)
    input_list = method.__self__._redis.lrange(f"{key}:inputs", 0, -1)
    output_list = method.__self__._redis.lrange(f"{key}:outputs", 0, -1)

    print(f"Cache.store was called {calls_count.decode('utf-8')} times:")
    for key, value in zip(input_list, output_list):
        utf_key = key.decode('utf-8')
        utf_value = value.decode('utf-8')
        print(f"Cache.store(*{utf_key}) -> {utf_value}")


class Cache():
    """This is a class that defines a Cache"""
    def __init__(self):
        """Initializes the Cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        This is a method that method that takes a data argument and
        returns a string. The method should generate a random
        key (e.g. using uuid),
        store the input data in Redis using the random key and return the key.
        """
        rand_key = str(uuid.uuid4())
        self._redis.set(rand_key, data)
        return rand_key

    def get(self, key: str, fn: Callable = None) -> any:
        """
        This is a method that take a key string argument and
        an optional Callable argument named fn. This callable
        will be used to convert the data back to the desired format.
        """
        key_value = self._redis.get(key)

        # Validate and retrieve value
        if fn is None:
            return key_value
        desired_format = fn(key_value)

        return desired_format

    def get_str(self, key: str) -> str:
        """
        Automatically parametrizes Cache.get to
        return a string
        """
        return str(self.get(key, lambda v: v.decode("utf-8")))

    def get_int(self, key: str) -> int:
        """
        Automatically parametrizes Cache.get to
        return an int
        """
        return self.get(key, int)
