#!/usr/bin/env python3
"""This is module that defines a get page function"""
from functools import wraps
from typing import Callable
import requests
import redis


redis = redis.Redis()
redis.flushdb()


def cache_count(method: Callable) -> Callable:
    """
    This is a method that decorates the get_page function
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        url = args[0]
        url_key = f"count:{url}"
        url_count = redis.incr(url_key)
        redis.setex(url_key, 10, url_count)
        return method(*args, **kwargs)
    return wrapper


@cache_count
def get_page(url: str) -> str:
    """
    It uses the requests module to obtain the HTML content of
    a particular URL and returns it.
    """
    page_content = requests.get(url)
    return page_content


if __name__ == '__main__':
    get_page('http://slowwly.robertomurray.co.uk')
    get_page('http://slowwly.robertomurray.co.uk')
    get_page('http://slowwly.robertomurray.co.uk')

    print(redis.get('count:http://slowwly.robertomurray.co.uk'))
