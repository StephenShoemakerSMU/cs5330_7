from pymongo import MongoClient

from pprint import pprint

client= MongoClient("mongodb://root:example@localhost:27017")

db = client["paperDB"]

papers = db["papers"]
papers.create_index("title")
papers.create_index("authors")
papers.create_index("publication.name")
papers.create_index("publication.year")

authors = db["authors"]
papers.create_index("name")

