"""
This is a module that defines a list_all function
"""

def list_all(mongo_collection):
	return mongo_collection.find()

