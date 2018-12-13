## Course Recommendation System: 
***Current State:*** Pulls the data, allows you to recommend courses based on their popularity or similarity scores using their description loaded from UMD.io API.

# Test it out! [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cricketthomas/recommendations/master?filepath=https%3A%2F%2Fgithub.com%2Fcricketthomas%2Frecommendations%2Fblob%2Fmaster%2FumdioCourseRecommender.ipynb)

## Algorithm mods: 
I am not certain about the accuracy. My popularity scores are computed from the sections available, which is generally inline with major requirements. The content based one might be skewed aswell, I didn't remove common words like "introduction" which can skew the results for any courses that use that word to match more closesly. Short fun project. 

Algorithm is from: https://datacamp.com/community/tutorials/recommender-systems-python
 
