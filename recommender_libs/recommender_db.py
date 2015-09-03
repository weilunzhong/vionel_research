import pymongo
from pymongo import MongoClient


class RecommenderDB:
    db = None
    collection = None

    def __init__(self):
        client = MongoClient()
        self.db = client.VionelMovies
        self.collection = self.db.boxerMovies

    def get_imdbid_feature_dict(self, feature_name):
        result_dict = {}
        feature_key = ""
        if feature_name == "imdb_actor":
            feature_key = "imdbMainactors"
        elif feature_name == "imdb_director":
            feature_key = "imdbDirectors"
        elif feature_name == "imdb_genre":
            feature_key = "imdbGenres"
        elif feature_name == "language":
            feature_key = "language"
        elif feature_name == "imdb_rating":
            feature_key = "imdbRating"
        elif feature_name == "releaseyear":
            feature_key = "releaseYear"
        elif feature_name == "imdb_keyword":
            feature_key = "imdbKeywords"
        elif feature_name == "wiki_keyword":
            feature_key = "wikiKeywords"
        elif feature_name == "vionel_theme":
            feature_key = "vionelThemes"
            
        all_movies_list = list(self.collection.find({}, {"imdbId": 1, feature_key: 1, "_id": 0}))

        for movie in all_movies_list:
            imdbid = movie["imdbId"]
            feature = movie[feature_key]
            result_dict[imdbid] = feature
        return result_dict

# recommenderdb = RecommenderDB()
# print recommenderdb.get_imdbid_feature_dict("genre")