#!coding=utf-8
import json
import math
from collections import Counter
import os
import recommender




def exchange_key_value_of_dict(input_dict):
    '''此函数作用:
        把{"a": [1, 2, 3], "b": [1, 3, 5]}转化成{1: ["a", "b"], 2: ["a"], 3: ["a", "b"], 5: ["b"]}
    '''
    union_of_input_dict_values = []
    input_dict_values = input_dict.values()

    for k, v in input_dict.items():
        union_of_input_dict_values += v

    union_of_input_dict_values = set(union_of_input_dict_values)
    print len(union_of_input_dict_values)

    output_dict = {}
    for item in union_of_input_dict_values:
        output_value = []
        for k1, v1 in input_dict.items():
            if item in v1:
                output_value.append(k1)
        output_dict[item] = output_value
        print len(output_dict)

    return output_dict


def generate_imdbid_directors(imdbid_directors_dict):
    imdbid_directors_json = json.dumps(imdbid_directors_dict)
    with open("imdbid_directors.json", "w") as imdbid_directors_file:
         imdbid_directors_file.write(imdbid_directors_json)


def generate_imdbid_mainactors(imdbid_mainactors_dict):
    imdbid_mainactors_json = json.dumps(imdbid_mainactors_dict)
    with open("imdbid_mainactors.json", "w") as imdbid_mainactors_file:
        imdbid_mainactors_file.write(imdbid_mainactors_json)


def genreate_imdbid_ratings(imdbid_ratings_dict):
    imdbid_ratings_json = json.dumps(imdbid_ratings_dict)
    with open("imdbid_ratings.json", "w") as imdbid_ratings_file:
        imdbid_ratings_file.write(imdbid_ratings_json)


def genreate_imdbid_releaseyear(imdbid_releaseyear_dict):
    imdbid_releaseyear_json = json.dumps(imdbid_releaseyear_dict)
    with open("imdbid_releaseyear.json", "w") as imdbid_releaseyear_file:
        imdbid_releaseyear_file.write(imdbid_releaseyear_json)


def generate_director_imdbids(imdbid_directors_dict):
    director_imdbids_dict = exchange_key_value_of_dict(imdbid_directors_dict)
    director_imdbids_json = json.dumps(director_imdbids_dict)
    with open("director_imdbids.json", "w") as director_imdbids_file:
        director_imdbids_file.write(director_imdbids_json)


def generate_mainactor_imdbids(imdbid_mainactors_dict):
    mainactor_imdbids_dict = exchange_key_value_of_dict(imdbid_mainactors_dict)
    mainactor_imdbids_json = json.dumps(mainactor_imdbids_dict)
    with open("mainactor_imdbids.json", "w") as mainactor_imdbids_file:
        mainactor_imdbids_file.write(mainactor_imdbids_json)


def generate_imdbid_genres(imdbid_genres_dict):
    imdbid_genres_json = json.dumps(imdbid_genres_dict)
    with open("imdbid_genres.json", "w") as imdbid_genres_file:
        imdbid_genres_file.write(imdbid_genres_json)

def generate_genre_imdbids(imdbid_genres_dict):
    genre_imdbids_dict = exchange_key_value_of_dict(imdbid_genres_dict)
    genre_imdbids_json = json.dumps(genre_imdbids_dict)
    with open("genre_imdbids.json", "w") as genre_imdbids_file:
        genre_imdbids_file.write(genre_imdbids_json)


def generate_imdbid_language(imdbid_language_dict):
    imdbid_language_json = json.dumps(imdbid_language_dict)
    with open("imdbid_language.json", "w") as imdbid_language_file:
        imdbid_language_file.write(imdbid_language_json)


def generate_keyword_imdbids(imdbid_keywords_dict):
    keyword_imdbids_dict = exchange_key_value_of_dict(imdbid_keywords_dict)
    keyword_imdbids_json = json.dumps(keyword_imdbids_dict)
    with open("keyword_imdbids.json", "w") as keyword_imdbids_file:
        keyword_imdbids_file.write(keyword_imdbids_json)


def generate_wikikeyword_imdbids(imdbid_wikikeywords_dict):
    wikikeyword_imdbids_dict = exchange_key_value_of_dict(imdbid_wikikeywords_dict)
    wikikeyword_imdbids_json = json.dumps(wikikeyword_imdbids_dict)
    with open("wikikeyword_imdbids.json", "w") as wikikeyword_imdbids_file:
        wikikeyword_imdbids_file.write(wikikeyword_imdbids_json)


def generate_vioneltheme_imdbids(imdbid_vioneltheme_dict):
    vioneltheme_imdbids_dict = exchange_key_value_of_dict(imdbid_vioneltheme_dict)
    vioneltheme_imdbids_json = json.dumps(vioneltheme_imdbids_dict)
    with open("vioneltheme_imdbids.json", "w") as vioneltheme_imdbids_file:
        vioneltheme_imdbids_file.write(vioneltheme_imdbids_json)


def transform(all_movies_file_path):

    imdbid_directors_dict = {}
    imdbid_mainactors_dict = {}
    imdbid_ratings_dict = {}
    imdbid_releaseyear_dict = {}
    imdbid_genres_dict = {}
    imdbid_language_dict = {}
    imdbid_keywords_dict = {}
    imdbid_wikikeywords_dict = {}
    imdbid_vioneltheme_dict = {}

    with open(all_movies_file_path) as all_movies_file:
        for line in all_movies_file:
            movie = json.loads(line)
            imdbid = movie["imdbId"]
            mainactors = movie["imdbMainactors"]
            ratings = movie["imdbRating"]
            directors = movie["imdbDirectors"]
            releaseyear = movie["releaseYear"]
            genres = movie["imdbGenres"]
            language = movie["language"]
            keywords = movie["imdbKeywords"]
            wikikeywords = movie["wikiKeywords"]
            vionelthemes = movie["vionelThemes"]

            imdbid_directors_dict[imdbid] = directors
            imdbid_mainactors_dict[imdbid] = mainactors
            imdbid_ratings_dict[imdbid] = ratings
            imdbid_releaseyear_dict[imdbid] = releaseyear
            imdbid_genres_dict[imdbid] = genres
            imdbid_language_dict[imdbid] = language
            imdbid_keywords_dict[imdbid] = keywords
            imdbid_wikikeywords_dict[imdbid] = wikikeywords
            imdbid_vioneltheme_dict[imdbid] = vionelthemes

    # generate_imdbid_directors(imdbid_directors_dict)
    # generate_imdbid_mainactors(imdbid_mainactors_dict)
    # genreate_imdbid_ratings(imdbid_ratings_dict)
    # genreate_imdbid_releaseyear(imdbid_releaseyear_dict)

    # # 生成director_imdbids.json和mainactor_imdbids.json
    generate_director_imdbids(imdbid_directors_dict)
    generate_mainactor_imdbids(imdbid_mainactors_dict)

    # 生成genre_imdbids.json
    generate_genre_imdbids(imdbid_genres_dict)

    # 生成keyword_imdbids
    generate_keyword_imdbids(imdbid_keywords_dict)
    generate_wikikeyword_imdbids(imdbid_wikikeywords_dict)
    generate_vioneltheme_imdbids(imdbid_vioneltheme_dict)

###############################################################################################


def generate_movie_information(infile):
    with open(infile) as infile_file, open("boxer_movies_information.dat", "w") as boxer_movies_information_file:
        for line in infile_file:

            movie = json.loads(line)

            output_dict = {}
            output_dict["imdbGenres"] = movie["genres"]
            output_dict["language"] = movie["language"]
            output_dict["imdbDirectors"] = movie["imdbDirectors"]
            output_dict["imdbKeywords"] = movie["imdbKeywords"]
            output_dict["imdbRating"] = movie["imdbRating"]
            output_dict["imdbMainactors"] = movie["imdbMainactors"]
            output_dict["imdbId"] = movie["imdbId"]
            output_dict["releaseYear"] = movie["releaseYear"]

            wikikeyword_list = []
            for item in movie["wikikeywords"]:
                wikikeyword_list.append(item["keywordWikiId"])

            vioneltheme_list = []
            for theme in movie["vionelThemes"]:
                vioneltheme_list.append(theme["vionelThemeID"])

            output_dict["wikiKeywords"] = wikikeyword_list
            output_dict["vionelThemes"] = vioneltheme_list

            output_json = json.dumps(output_dict)
            boxer_movies_information_file.write(output_json + "\n")




def createweight():
    movie_list = []
    feature_maxscore_dict = {}

    actor_score_list = []
    director_score_list = []
    genre_score_list = []
    imdbkeyword_score_list = []
    wikikeyword_score_list = []
    vioneltheme_score_list = []


    with open("boxer_movies_information.dat") as boxer_movies_information_file:
        for line in boxer_movies_information_file:
            movie = json.loads(line)
            imdbid = movie["imdbId"]
            movie_list.append(imdbid)
            
        max_actorscore = 0
        max_directorscore = 0
        max_genrescore = 0
        max_imdbkeywordscore = 0
        max_wikikeywordscore = 0
        max_vionelthemescore = 0

    count = 0

    for imdbid in movie_list:
        feature_counter_dict = recommender.getallsimscore([imdbid, imdbid])
        actorscore = max(dict(feature_counter_dict["imdb_actor"]).values())
        directorscore = max(dict(feature_counter_dict["imdb_director"]).values())
        genrescore = max(dict(feature_counter_dict["imdb_genre"]).values())
        imdbkeywordscore = max(dict(feature_counter_dict["imdb_keyword"]).values())
        wikikeywordscore = max(dict(feature_counter_dict["wiki_keyword"]).values())
        vionelthemescore = max(dict(feature_counter_dict["vionel_theme"]).values())

        # if max_actorscore < actorscore:
        #     max_actorscore = actorscore
        # elif max_directorscore < directorscore:
        #     max_directorscore = directorscore
        # elif max_genrescore < genrescore:
        #     max_genrescore = genrescore
        # elif max_imdbkeywordscore < imdbkeywordscore:
        #     max_imdbkeywordscore = imdbkeywordscore
        # elif max_wikikeywordscore < wikikeywordscore:
        #     max_wikikeywordscore = wikikeywordscore
        # elif max_vionelthemescore < vionelthemescore:
        #     max_vionelthemescore = vionelthemescore


        actor_score_list.append(actorscore)
        director_score_list.append(directorscore)
        genre_score_list.append(genrescore)
        imdbkeyword_score_list.append(imdbkeywordscore)
        wikikeyword_score_list.append(wikikeywordscore)
        vioneltheme_score_list.append(vionelthemescore)

        count += 1
        print count
        # print max_genrescore
        # print max_actorscore
        # print max_directorscore
        # print max_imdbkeywordscore
        # print max_wikikeywordscore
        # print max_vionelthemescore
        # print 
        print genrescore
        print actorscore
        print directorscore
        print imdbkeywordscore
        print wikikeywordscore
        print vionelthemescore
        print 


    print sum(actor_score_list) / len(actor_score_list)
    print sum(director_score_list) / len(director_score_list)
    print sum(genre_score_list) / len(genre_score_list)
    print sum(imdbkeyword_score_list) / len(imdbkeyword_score_list)
    print sum(wikikeyword_score_list) / len(wikikeyword_score_list)
    print sum(vioneltheme_score_list) / len(vioneltheme_score_list)

    # feature_maxscore_dict["imdbActor"] = max_actorscore
    # feature_maxscore_dict["imdbDirector"] = max_directorscore
    # feature_maxscore_dict["imdbGenre"] = max_genrescore
    # feature_maxscore_dict["imdbKeyword"] = max_genrescore
    # feature_maxscore_dict["wikiKeyword"] = max_wikikeywordscore
    # feature_maxscore_dict["vionelTheme"] = max_vionelthemescore

    # print feature_maxscore_dict









# transform("boxer_movies_information.dat")
# generate_movie_information("boxer_movies.dat")
createweight()

