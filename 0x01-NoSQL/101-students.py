#!/usr/bin/python3
"""
This is a module that defines a top_students function
"""


def top_students(mongo_collection):
    """Python function that returns all students sorted by average score"""
    sorted_students = mongo_collection.aggregate(
        [{
            "$project": {
                "name": "$name",
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ])
    return sorted_students
