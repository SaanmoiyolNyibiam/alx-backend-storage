#!/usr/bin/env python3
"""This is module that defines a Cache class"""
from typing import Union
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
