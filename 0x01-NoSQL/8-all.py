#!/usr/bin/env python3
"""
This is a module that defines a list_all function
"""


def list_all(mongo_collection):
    """
	This is a function that lists all documents in a collection
    """
    return mongo_collection.find()
