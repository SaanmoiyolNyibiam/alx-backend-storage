#!/usr/bin/env python3
"""
This is a module that defines a schools_by_topic function
"""


def schools_by_topic(mongo_collection, topic):
    """
    This is a function that returns the list of schools having
    a specific topic
    """
    docs = mongo_collection.find({"topics": topic})

    return docs
