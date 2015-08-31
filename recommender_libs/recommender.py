#!coding=utf-8
import json
import math
from recommender_helper import RecommenderHelper
from recommender_db import RecommenderDB
from collections import Counter
import os


def filter_by_rating_and_releaseyear(combined_movieid_sim_counter):
    recommenderdb = RecommenderDB()
    imdbrating_dict = recommenderdb.get_imdbid_feature_dict("rating")
    movieid_releaseyear_dict = recommenderdb.get_imdbid_feature_dict("releaseyear")

    for item in combined_movieid_sim_counter:
        try:
            combined_movieid_sim_counter[item] *= imdbrating_dict[item]
            if movieid_releaseyear_dict[item] < 1990:
                combined_movieid_sim_counter[item] *= 0.6
            elif movieid_releaseyear_dict[item] >= 1990 and movieid_releaseyear_dict[item] < 2000:
                combined_movieid_sim_counter[item] *= 0.7
            elif movieid_releaseyear_dict[item] >= 2000 and movieid_releaseyear_dict[item] < 2010:
                combined_movieid_sim_counter[item] *= 0.8
            elif movieid_releaseyear_dict[item] >= 2010 and movieid_releaseyear_dict[item] < 2020:
                combined_movieid_sim_counter[item] *= 0.9
        except KeyError:
            combined_movieid_sim_counter[item] * 0.5
            
    return combined_movieid_sim_counter


def filter_by_language(user_liked_movie_id_list, combined_movieid_sim_counter):
    recommenderdb = RecommenderDB()
    imdbid_language_dict = recommenderdb.get_imdbid_feature_dict("language")

    languages_in_liked_list = []
    for item in user_liked_movie_id_list:
        try:
            languages_in_liked_list += imdbid_language_dict[item]
        except KeyError:
            continue

    languages_in_liked_list = list(set(languages_in_liked_list))
    # print languages_in_liked_list, "77777777777777777"

    delete_list = []
    for imdbid in combined_movieid_sim_counter:
        language_list = imdbid_language_dict[imdbid]
        if not language_list:
            continue
        intersection_list = list(set(languages_in_liked_list).intersection(set(language_list)))
        if not intersection_list: # 如果为空,则排除此电影
            delete_list.append(imdbid)

    for x in delete_list:
        del combined_movieid_sim_counter[x]

    return combined_movieid_sim_counter


def reason_of_recommendation(final_co_recommended_movies, genre_movieid_sim_counter, actor_movieid_sim_counter, director_movieid_sim_counter, keyword_movieid_sim_counter):
    reason_tuple_list = []
    score_dict = {}
    for key in final_co_recommended_movies:
        imdbid = key[0]
        score_dict["genre"] = genre_movieid_sim_counter[imdbid]
        score_dict["actor"] = actor_movieid_sim_counter[imdbid]
        score_dict["director"] = director_movieid_sim_counter[imdbid]
        score_dict["keyword"] = keyword_movieid_sim_counter[imdbid]
        sorted_score_dict = sorted(score_dict.iteritems(), key=lambda d:d[1], reverse=True)
        reason_list = []
        
        for item in sorted_score_dict[:2]:
            if item[1] != 0:
                reason_list.append(item[0])
        reason_tuple_list.append((key[0], reason_list,))

    print reason_tuple_list
    return reason_tuple_list



def recommend(user_liked_movie_id_list, num_of_recommended_movies):

    # 以下可分别得到根据genre和mawid推荐出的结果，均为（movied_id: cos_sim_value）这种的字典
    recommender_helper = RecommenderHelper()
    actor_movieid_sim_dict = recommender_helper.recommend(user_liked_movie_id_list, "actor")
    director_movieid_sim_dict = recommender_helper.recommend(user_liked_movie_id_list, "director")
    genre_movieid_sim_dict = recommender_helper.recommend(user_liked_movie_id_list, "genre")
    keyword_movieid_sim_dict = recommender_helper.recommend(user_liked_movie_id_list, "keyword")

    genre_movieid_sim_counter = Counter(genre_movieid_sim_dict)
    actor_movieid_sim_counter = Counter(actor_movieid_sim_dict)
    director_movieid_sim_counter = Counter(director_movieid_sim_dict)
    keyword_movieid_sim_counter = Counter(keyword_movieid_sim_dict)

    combined_movieid_sim_counter = genre_movieid_sim_counter + actor_movieid_sim_counter + director_movieid_sim_counter + keyword_movieid_sim_counter

    for key in user_liked_movie_id_list:
        del combined_movieid_sim_counter[key]
        del genre_movieid_sim_counter[key]
        del actor_movieid_sim_counter[key]
        del director_movieid_sim_counter[key]
        del keyword_movieid_sim_counter[key]

    

    # filter
    # 乘上rating和releaseYear产生的系数
    combined_movieid_sim_counter = filter_by_rating_and_releaseyear(combined_movieid_sim_counter)
    combined_movieid_sim_counter = filter_by_language(user_liked_movie_id_list, combined_movieid_sim_counter)

    final_co_recommended_movies = combined_movieid_sim_counter.most_common(num_of_recommended_movies)

    # get the features that have the top two scores.
    reason_tuple_list = reason_of_recommendation(final_co_recommended_movies, genre_movieid_sim_counter, actor_movieid_sim_counter, director_movieid_sim_counter, keyword_movieid_sim_counter)

    result_dict = dict()
    result_dict["movie"] = final_co_recommended_movies
    result_dict["reason"] = reason_tuple_list

    return result_dict


###########################################################################
###########################################################################








