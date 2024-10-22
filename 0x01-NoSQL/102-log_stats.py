#!/usr/bin/python3
"""
This is a Python script that provides some
stats about Nginx logs stored in MongoDB,
including the top 10 of the most present
IPs in the collection nginx of the database logs
"""
from pymongo import MongoClient
# establish connection to database
client = MongoClient("mongodb://localhost:27017")

# retrieve cursor object to database and collection
db = client.logs
docs = db.nginx

# query collection and return required data
number_of_docs = docs.count_documents({})
number_of_gets = docs.count_documents({"method": "GET"})
number_of_posts = docs.count_documents({"method": "POST"})
number_of_puts = docs.count_documents({"method": "PUT"})
number_of_patches = docs.count_documents({"method": "PATCH"})
number_of_deletes = docs.count_documents({"method": "DELETE"})
number_of_mget_pstatus = docs.count_documents({"method": 'GET', "path": "/status"})

# print output based on sample format provided
print(f"{number_of_docs} logs")

print(f"Methods:\n"
      f"    method GET: {number_of_gets}\n"
      f"    method POST: {number_of_posts}\n"
      f"    method PUT: {number_of_puts}\n"
      f"    method PATCH: {number_of_patches}\n"
      f"    method DELETE: {number_of_deletes}")

print(f"{number_of_mget_pstatus} status check")

print("IPs:")

top_IPs = docs.aggregate([
        {"$group":
         {
             "_id": "$ip",
             "count": {"$sum": 1}
         }
         },
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}
    ])
for top_ip in top_IPs:
    count = top_ip.get("count")
    ip_address = top_ip.get("ip")
    print("\t{}: {}".format(ip_address, count))
