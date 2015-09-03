#!coding=utf-8
from __future__ import division
import json
import math
import os

from recommender_db import RecommenderDB


class RecommenderHelper:

    def __jsonfile_to_dict(self, json_file_path):
        json_file = open(os.path.split(os.path.realpath(__file__))[0] + json_file_path)
        result_dict = json.loads(json_file.readline())
        return result_dict

    def __intersection_of_values_for_certain_keys(self, item_list, item_with_value_dict):
        """把一个字典中指定key的value出现次数。

        此函数的作用是，根据item_list中的item从item_with_value找出对应value，统计出这些value的次数，剔除只出现一次的情况。

        Args:
            item_list: item_with_value_dict中需要查找的key的列表。
            item_with_value_dict: 需要遍历的字典，找出对应的value，这些value是结果中的key。

        Returns:
            一个字典，key为item_with_value_dict中对应的value，value出现的次数。
            例子：
                item_list = [id1, id2, id3]
                item_with_value_dict = {id1: [actor1, actor2],
                                        id2: [actor2, actor3],
                                        id3: [actor5, actor1],
                                        id4: [actor1, actor7]}
                最后结果：{actor1: 2, actor2: 2}
        """

        result_dict = {}
        value_list = []

        for item in item_list:
            try:
                value_list += item_with_value_dict[item]
            except KeyError:
                continue

        value_set_list = list(set(value_list))
        for value in value_set_list:
            num_of_value = value_list.count(value)
            if num_of_value > 1:
                result_dict[value] = num_of_value

        return result_dict

    # 核心算法
    def __calculate_cosine(self, movieid_list, featureid_list, movieid_with_featureid_dict, featureid_with_movieid_dict, featureid_with_number_dict):
        all_featureid_list = featureid_with_number_dict.keys()
        difference_list = list(set(featureid_list).difference(set(all_featureid_list)))

        featureid_with_number_dict_tmp = {}
        featureid_with_number_dict_tmp.update(featureid_with_number_dict)
        map(lambda x: featureid_with_number_dict_tmp.update({x: 0}), difference_list)

        featureid_list_dict = {}
        map(lambda x: featureid_list_dict.update({x: 0}), featureid_with_number_dict_tmp.keys())
        map(lambda x: featureid_list_dict.update({x: 1}), featureid_list)

        # 算TF-IDF
        movieid_list_num = len(movieid_list)
        all_movie_num = len(movieid_with_featureid_dict)

        tf_dict = {}
        for k, v in featureid_with_number_dict_tmp.items():
            tf_dict[k] = v / movieid_list_num

        idf_dict = {}
        for i, j in featureid_with_number_dict_tmp.items():
            idf_dict[i] = all_movie_num / len(featureid_with_movieid_dict[i])

        tfidf_dict = {}
        for key in tf_dict.keys():
            tfidf_dict[key] = (tf_dict[key] * idf_dict[key]) ** 2

        featureid_with_number_dict_tmp_keys = featureid_with_number_dict_tmp.keys()
        featureid_list_dict_values = featureid_list_dict.values()
        tfidf_dict_values = tfidf_dict.values()

        num1 = sum(map(lambda x: featureid_list_dict[x] * tfidf_dict[x], featureid_with_number_dict_tmp_keys))
        tmp1 = math.sqrt(sum([x ** 2 for x in featureid_list_dict_values]))
        tmp2 = math.sqrt(sum([x ** 2 for x in tfidf_dict_values]))
        num2 = tmp1 * tmp2  # num2=sqrt(a1^2+a2^2+a3^2) * sqrt(b1^2+b2^2+b3^2)

        cosine_score = num1 / num2
        return cosine_score



    def recommend(self, movieid_list, recommended_by):
        recommenderdb = RecommenderDB()

        movieid_with_featureid_dict = {}
        featureid_with_movieid_dict = {}

        movieid_with_featureid_dict = recommenderdb.get_imdbid_feature_dict(recommended_by)

        if recommended_by == "imdb_actor":
            featureid_with_movieid_dict = self.__jsonfile_to_dict("/mainactor_imdbids.json")
        elif recommended_by == "imdb_director":
            featureid_with_movieid_dict = self.__jsonfile_to_dict("/director_imdbids.json")
        elif recommended_by == "imdb_genre":
            featureid_with_movieid_dict = self.__jsonfile_to_dict("/genre_imdbids.json")
        elif recommended_by == "imdb_keyword":
            featureid_with_movieid_dict = self.__jsonfile_to_dict("/keyword_imdbids.json")
        elif recommended_by == "wiki_keyword":
            featureid_with_movieid_dict = self.__jsonfile_to_dict("/wikikeyword_imdbids.json")
        elif recommended_by == "vionel_theme":
            featureid_with_movieid_dict = self.__jsonfile_to_dict("/vioneltheme_imdbids.json")


        featureid_with_number_dict = self.__intersection_of_values_for_certain_keys(movieid_list, movieid_with_featureid_dict)

        result_dict = {}
        all_featureid_list = featureid_with_number_dict.keys()

        for k, v in movieid_with_featureid_dict.items():
            intersection_list = list(set(v).intersection(set(all_featureid_list)))
            if not intersection_list:
                result_dict[k] = 0
                continue

            cosine_score = self.__calculate_cosine(movieid_list, v, movieid_with_featureid_dict, featureid_with_movieid_dict, featureid_with_number_dict)
            result_dict[k] = cosine_score

        return result_dict



# movieid_list = ["tt0133093","tt0137523","tt0468569","tt0172495","tt0114369","tt1375666","tt0361862","tt0482571","tt0268978","tt0110322"]
# # movieid_list = ["tt0468569", "tt0137523", "tt0964517", "tt1375666", "tt0172495", "tt0109830", "tt0112573", "tt0120815", "tt0209144", "tt1130884", "tt0372784", "tt0114369", "tt1504320", "tt0454876", "tt0212720", "tt0111161", "tt0099487", "tt1291584", "tt0110322", "tt1905041", "tt1596343", "tt2103281", "tt0396171", "tt0421715", "tt0814314", "tt0480249", "tt0343818", "tt0181689", "tt2106476", "tt0381061", "tt1392214", "tt0443706", "tt0945513"]
# recommender_helper = RecommenderHelper()
# recommended_by_actor = recommender_helper.recommend(movieid_list, "actor")
# recommended_by_director = recommender_helper.recommend(movieid_list, "director")
# recommended_by_genre = recommender_helper.recommend(movieid_list, "genre")
# # tmp1 = sorted(recommended_by_actor.iteritems(), key=lambda d:d[1], reverse = True)
# # tmp2 = sorted(recommended_by_director.iteritems(), key=lambda d:d[1], reverse = True)
# tmp3 = sorted(recommended_by_genre.iteritems(), key=lambda d:d[1], reverse = True)
# # print tmp1[:10]
# # print tmp2[:10]
# print tmp3[:10]




