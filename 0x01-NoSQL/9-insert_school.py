#!/usr/bin/python3
"""
This is a module that defines insert_school function
"""


def insert_school(mongo_collection, **kwargs):
    """
    This is a Python function that inserts a new
    document in a collection based on kwargs
    """
    doc = {}
    for key, value in kwargs.items():
        doc.update({key: value})
    result_obj = mongo_collection.insert_one(doc)

    return result_obj.inserted_id
