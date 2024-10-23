#!/usr/bin/env python3
"""
This is a module that defines a update_topics function
"""


def update_topics(mongo_collection, name, topics):
    """
    This is a function that changes all topics
    of a school document based on the name
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
