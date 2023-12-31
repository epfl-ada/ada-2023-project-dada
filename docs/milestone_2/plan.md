# Project plan

## Some project ideas

### Project proposal 1 :	Reviews analysis
* Ben - idea 2 : relationship between the number of reviews and the distribution in the rating.
* Ben - idea 3 : relationship between the length of comment and general orientation of rating. implying sentiment analysis.
* Xingchen - idea 2 : rating the reviewers based on the number/quality/type/... of their reviews.

### Project proposal 2 :	Events 
* Mathieu - idea 1 : Find if there is regular paterns (spikes) in the reviews regarding different features: region, type of beer, brewery, ...
* Mathieu - idea 3 : Looking if beer events have an influence on the reviews.
* Swann - idea 1 : Looking if dramas regarding the breweries have an impact on the reviews.

### Project proposal 3 :	Brewery expertise
* Xingchen - idea 3 : Identifying Beer Specializations Across Breweries, coutries, timeline.
		
### Project proposal 4 :	Corruption
* Ben - extra idea : The webiste "ratebeer.com" has been bought by AB InBev in 2019. We could collect a more ressent dataset and compare if this had an influence on the brands owned by AB.

## Selection between the two more complete ideas

### Project proposal 1 : Reviews analysis
At first, we want to find out the distribution(s) of the ratings. Are there different distributions between ratings and different scales (10 ratings, 1000 ratings, etc) or breweries, beer-types, location, etc. For example, we can find out the rating distribution for different breweries and use these data to evaluate the popularity of these breweries.
In order to give reviewers a score to measure the reliability of their ratings and reviews, we would like to find the users whose rating distribution can best represent most of the information from a global scale distribution, for that we need to define a measure of “distance”, and we will assign higher reliability score to these users. This would also allow us to reduce the dataset and keep most of the information.
For the comments we can use sentiment analysis, TF-IDF methods to assign labels to different beers and breweries.

### Project proposal 2 : Events impact
The goal of this project would be to initially find the impact of preselected beer events on beer reviews (festival, scandales, economic crisis) (for exemple a spike in reviews of german beers after the oktoberfest). Those analysis could allow us to find the geographic scale and the spreading time of such events.
From eventual results, we could then try and analyse it the other way around by searching for similar patterns regarding brands, regions, type of beers, etc and look if the pattern is related to a specific type of event.
A first step would be to build a dataset of beer events with features of interest (id, name, type, location, date, crowd_size, googleTrends).
Then, for each event, we plan to do a first analysis where we sort the review dataset by type of beer, location and date in order to find if the event had a regional impact. And if yes, we would do a second analysis to see how much this impact spread through the continent and describe the pattern of the impact (change in number and rating of reviews and distribution along time).
In order to then find if the patterns that we found during the first analysis can be generalized to any similar events. We plan then to try to find similar patterns on subdatasets sorted by countries and breweries and find if it corresponds to a similar event.


## Choice

Project proposal 1 : Reviews analysis
