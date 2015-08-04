import pymongo
from pymongo import MongoClient


class RecommenderDB:

    db = None

    def __init__(self):
        client = MongoClient()
        self.db = client.VionelMovies

    def get_collections(self, name):
        all_movies = self.db[name]
        return all_movies


recommenderdb = RecommenderDB()
all_movies = recommenderdb.get_collections("allMovies")
print all_movies.count()