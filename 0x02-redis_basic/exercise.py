#!/usr/bin/env python3
"""This is module that defines a Cache class"""
from typing import Union, Callable
import uuid
import redis


class Cache():
    """This is a class that defines a Cache"""
    def __init__(self):
        """Initializes the Cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

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

    def get(self, key: str, fn: Callable=None) -> any:
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
