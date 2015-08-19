#Vionel Research

##Introduction
This is a research project of VionLabs. My task is to build the recommender system and design the website.

##Screenshot

####Home page
![image](https://github.com/codermango/web_recommender/raw/master/readme_images/home_page.png)

####Recommender page
![image](https://github.com/codermango/web_recommender/raw/master/readme_images/recommender_page.png)

####Fingerprint page
![image](https://github.com/codermango/vionel_research/raw/master/readme_images/fingerprint_page.png)

####Moviedetail page
![image](https://github.com/codermango/vionel_research/raw/master/readme_images/moviedetail_page.png)


For now, there are two main directions that are under research. Movie Recommender and Movie Fingerprint. 

##Recommender System
We use six features of movie to calculate the similarity. They are genre, main actor, director, language, rating and release year. Different rules are used for each feature. It is a content-based recommendation by TF-IDF and cosine similarity.

As this is a research project and our first goal is to test the usablity and the effects of the methods, our data is totally stored as JSON files, so the performace is not that good. In the future, we will consider to use database to store the movie data, perhaps MongoDB.

##Fingerprint
This part is developed by my friend, I just redesign the UI and add to our main site.
