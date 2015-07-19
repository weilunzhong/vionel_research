from django.shortcuts import render
from django.http import HttpResponse

from recommender_libs import recommender


# Create your views here.

def index(request):
    return render(request, 'base.html')

def recommend(request):
    input_movies = request.GET.get('inputMovies')
    input_movie_list = input_movies.split(',')
    trimed_movie_list = map(lambda x: x.strip(), input_movie_list)

    recommend_movie_list = recommender.recommend(trimed_movie_list)

    movies_to_show = {}
    movies_to_show['input_movie_list'] = trimed_movie_list
    movies_to_show['recommend_moive_list'] = recommend_movie_list

    return render(request, 'base.html', {'movies_to_show': movies_to_show})
