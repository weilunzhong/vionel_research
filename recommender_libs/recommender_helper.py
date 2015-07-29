#!coding=utf-8
from __future__ import division
import json
import math
import os


class RecommenderHelper:

    def jsonfile_to_dict(self, json_file_path):
        json_file = open(os.path.split(os.path.realpath(__file__))[0] + json_file_path)
        result_dict = json.loads(json_file.readline())
        return result_dict


    def recommend(self, movieid_list, recommended_by="actor"):
        if recommended_by == "actor":
            imdbid_with_actorid_dict = jsonfile_to_dict("/imdbid_mainactors.json")
        elif recommended_by == "director":

        else:





recommender_helper = RecommenderHelper()
recommended_by_actor = recommender_helper.recommend(movieid_list, "actor")