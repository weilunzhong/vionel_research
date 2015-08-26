#!coding=utf-8
import json
import math
from collections import Counter
import os




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


def generate_imdbid_genrevector(imdbid_genres_dict):
    all_genre_list = []
    for imdbid in imdbid_genres_dict:
        all_genre_list += imdbid_genres_dict[imdbid]

    sorted_all_genre_list = sorted(list(set(all_genre_list)))
    num_of_genre = len(sorted_all_genre_list)
    print sorted_all_genre_list
    genre_index_dict = {}
    for i in range(0, num_of_genre):
        genre_index_dict[sorted_all_genre_list[i]] = i

    # print genre_index_dict

    imdbid_genrevector_dict = {}
    for k, v in imdbid_genres_dict.items():
        # print k
        genrevector = [0] * num_of_genre
        for item in v:
            index = genre_index_dict[item]
            genrevector[index] = 1

        imdbid_genrevector_dict[k] = genrevector

    imdbid_genrevector_json = json.dumps(imdbid_genrevector_dict)
    with open("imdbid_genrevector.json", "w") as imdbid_genrevector_file:
        imdbid_genrevector_file.write(imdbid_genrevector_json + "\n")


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


def transform(all_movies_file_path):

    imdbid_directors_dict = {}
    imdbid_mainactors_dict = {}
    imdbid_ratings_dict = {}
    imdbid_releaseyear_dict = {}
    imdbid_genres_dict = {}
    imdbid_language_dict = {}
    imdbid_keywords_dict = {}

    with open(all_movies_file_path) as all_movies_file:
        for line in all_movies_file:
            movie = json.loads(line)
            imdbid = movie["imdbId"]
            mainactors = movie["imdbMainactors"]
            ratings = movie["imdbRating"]
            directors = movie["imdbDirectors"]
            releaseyear = movie["releaseYear"]
            genres = movie["genres"]
            language = movie["language"]
            keywords = movie["keywords"]

            imdbid_directors_dict[imdbid] = directors
            imdbid_mainactors_dict[imdbid] = mainactors
            imdbid_ratings_dict[imdbid] = ratings
            imdbid_releaseyear_dict[imdbid] = releaseyear
            imdbid_genres_dict[imdbid] = genres
            imdbid_language_dict[imdbid] = language
            imdbid_keywords_dict[imdbid] = keywords

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

def generate_imdbid_keywords(keyword_imdbids_json):
    keyword_imdbids_dict = {}
    imdbid_keywords_dict = {}
    with open(keyword_imdbids_json) as keyword_imdbids_file:
        for line in keyword_imdbids_file:
            item = json.loads(line)
            keyword = item["keyword"]
            imdbids = item["imdbid"]

            keyword_imdbids_dict[keyword] = imdbids

    imdbid_keywords_dict = exchange_key_value_of_dict(keyword_imdbids_dict)
    imdbid_keywords_json = json.dumps(imdbid_keywords_dict)
    with open("imdbid_keywords.json", "w") as imdbid_keywords_file:
        imdbid_keywords_file.write(imdbid_keywords_json)


def add_keywords_to_allmovies(imdbid_keywords_json):
    with open(imdbid_keywords_json) as imdbid_keywords_file, open("all10_movies.dat") as all10_movies_file:
        imdbid_keywords_dict = json.loads(imdbid_keywords_file.readline())
        
        all10_movies_imdbids = []
        all10_movies_dict = {} # 变成大json
        for item1 in all10_movies_file:
            movie = json.loads(item1)
            # 变成大json
            imdbid = movie["imdbId"]
            all10_movies_dict[imdbid] = movie

            all10_movies_imdbids.append(imdbid)
        imdbid_keywords_dict_keys = imdbid_keywords_dict.keys()
        print len(all10_movies_imdbids) # 105051
        print len(all10_movies_dict) # 105051
        print len(imdbid_keywords_dict_keys) # 110140

        # 在all中但不在keywords中的
        list1 = list(set(all10_movies_imdbids).difference(set(imdbid_keywords_dict_keys)))

        # 在keywords中但不在all中
        list2 = list(set(imdbid_keywords_dict_keys).difference(set(all10_movies_imdbids)))

        # 交集
        list3 = list(set(imdbid_keywords_dict_keys).intersection(set(all10_movies_imdbids)))

        print len(list1) # 68114
        print len(list2) # 73203
        print len(list3) # 36937

        # 并集
        union_list = list(set(all10_movies_imdbids).union(set(imdbid_keywords_dict_keys)))
        print len(union_list) # 178254

        

        new_all10_movies_file = open("new_all10_movies.json", "w")
        for union_item in union_list:
            new_movie_dict = {}
            print union_item
            if union_item in list2: # 如果在keywords中不在all中
                new_movie_dict["imdbid"] = union_item
                new_movie_dict["imdbMainactors"] = []
                new_movie_dict["imdbRating"] = []
                new_movie_dict["imdbDirectors"] = []
                new_movie_dict["releaseYear"] = []
                new_movie_dict["genres"] = []
                new_movie_dict["language"] = []
                new_movie_dict["keywords"] = imdbid_keywords_dict[union_item]
            if union_item in list1: # 如果在all中不在keywords中
                new_movie_dict["imdbid"] = union_item
                new_movie_dict["imdbMainactors"] = all10_movies_dict[union_item]["imdbMainactors"]
                new_movie_dict["imdbRating"] = all10_movies_dict[union_item]["imdbRating"]
                new_movie_dict["imdbDirectors"] = all10_movies_dict[union_item]["imdbDirectors"]
                new_movie_dict["releaseYear"] = all10_movies_dict[union_item]["releaseYear"]
                new_movie_dict["genres"] = all10_movies_dict[union_item]["genres"]
                new_movie_dict["language"] = all10_movies_dict[union_item]["language"]
                new_movie_dict["keywords"] = []
            if union_item in list3:
                new_movie_dict["imdbid"] = union_item
                new_movie_dict["imdbMainactors"] = all10_movies_dict[union_item]["imdbMainactors"]
                new_movie_dict["imdbRating"] = all10_movies_dict[union_item]["imdbRating"]
                new_movie_dict["imdbDirectors"] = all10_movies_dict[union_item]["imdbDirectors"]
                new_movie_dict["releaseYear"] = all10_movies_dict[union_item]["releaseYear"]
                new_movie_dict["genres"] = all10_movies_dict[union_item]["genres"]
                new_movie_dict["language"] = all10_movies_dict[union_item]["language"]
                new_movie_dict["keywords"] = imdbid_keywords_dict[union_item]

            # 把这一行写入文件
            new_movie_json = json.dumps(new_movie_dict)
            new_all10_movies_file.write(new_movie_json + "\n")
        new_all10_movies_file.close()
        print len(new_movie_dict)




def create_new_movie_file(input_file1, input_file2):
    with open(input_file1) as imdbid_keywords_file, open(input_file2) as all10_movies_file, open("movies.txt", "w") as movies_file:
        imdbid_keywords_dict = json.loads(imdbid_keywords_file.readline())
        count = 0
        for line in all10_movies_file:
            count = count + 1
            print count
            movie = json.loads(line)
            imdbid = movie["imdbId"]
            try:
                movie["keywords"] = imdbid_keywords_dict[imdbid]
            except KeyError:
                movie["keywords"] = []
            movie_json = json.dumps(movie)
            movies_file.write(movie_json + "\n")


###############################################################################################




transform("boxer_movies.dat")
# generate_imdbid_keywords("keyword_imdbids.json")
# add_keywords_to_allmovies("imdbid_keywords.json")
# create_new_movie_file("imdbid_keywords.json", "all10_movies.dat")

