import pymongo
from pymongo import MongoClient


class RecommenderDB:
    db = None
    collection = None

    def __init__(self):
        client = MongoClient()
        self.db = client.VionelMovies
        self.collection_allmovie = self.db.boxerMovies
        self.collection_director_coefficient = self.db.boxerDirectorCoefficient


    def getDirectorCoefficientDict(self):
        result_dict = {}
        for director in self.collection_director_coefficient.find():
            for element in director:
                if element != '_id':
                    result_dict[element] = director[element]

        return result_dict


    def get_imdbid_feature_dict(self, feature_name):
        result_dict = {}
        feature_key = ""
        if feature_name == "actor":
            feature_key = "imdbActors"
        elif feature_name == "director":
            feature_key = "imdbDirectors"
        elif feature_name == "genre":
            feature_key = "imdbGenres"
        elif feature_name == "language":
            feature_key = "language"
        elif feature_name == "imdbrating":
            feature_key = "imdbRating"
        elif feature_name == "releaseyear":
            feature_key = "releaseYear"
        elif feature_name == "imdbkeyword":
            feature_key = "imdbKeywords"
        elif feature_name == "wikikeyword":
            feature_key = "wikiKeywords"
        elif feature_name == "vioneltheme":
            feature_key = "vionelThemes"
        elif feature_name == "vionelscene":
            feature_key = "vionelScene"
        elif feature_name == "locationcity":
            feature_key = "locationCity"
        elif feature_name == "locationcountry":
            feature_key = "locationCountry"
        elif feature_name == "mainactor":
            feature_key = "imdbMainactors"
            
        all_movies_list = list(self.collection_allmovie.find({}, {"imdbId": 1, feature_key: 1, "_id": 0}))
        # print all_movies_list
        for movie in all_movies_list:
            imdbid = movie["imdbId"]
            feature = movie[feature_key]
            result_dict[imdbid] = feature
        return result_dict

# recommenderdb = RecommenderDB()
# recommenderdb.get_imdbid_feature_dict("actor")