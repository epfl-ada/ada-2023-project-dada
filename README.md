# ADA_Project

# Decoding Regional Preferences and Ratings 
You will find the notebook in the folder 'src'

## Data Story
You can find out how regional preferences influence ratings [here](https://lxc1851588.github.io/DADA_web/).

## Abstract
This research project aims to uncover underlying factors that influence beer ratings and determine how these factors vary across different regions. How regional predictors affect beer ratings, and the pattern of the user factor’s influence on rating . We seek to tell the story of regional beer appreciation, exploring the degree of localized preferences’  impact on a beer’s success and reputation. By analyzing beer ratings and reviews, this project will identify key preferences of beer popularity, investigate regional variations in these preferences. A critical component of the study is to establish a methodology for sourcing representative and reliable data from users to ensure the validity of our findings. The outcomes of this research aims to provide valuable insights for breweries to tailor their products to regional tastes and for enthusiasts to understand global beer trends.

## Research questions:
- What are the preferences in terms of beers ?
- How do those preferences regionalize ?
- Do Breweries cater to their local markets ? 

## Methods
### 1) Dataset construction
The first part of the project is to build the dataset that will be used for the rest of the project. This part is contained in the [preprocess notebook](src/2.preprocess.ipynb) jupyter notebook that has to be run at the beginning of the project. It is responsible for creating pickle the pickle saves of our dataset in order to speed up loading when using numpy. Furthermore it also provides a sampled version of the dataset, which was/is used for testing. This is also the part in which we get rid of the nan's.
### 2) Data Analysis
* The first step is to find the prefered beer type per country. In order to find this we do a linear regression on the categorical data (kind of beer). This is done for each country (i.e. a linear regression per country).
* The second step of the analysis is identifiying which breweries are local and then compare how those breweries compare to the local preferences. The definition of a local brewery was defined as a brewery for which half or more of the ratings are local. Then, the comparison part is done by z-scoring the group of local breweries against all the other breweries. Again this had to be done for each country. Another analysis is to compare the most reviewed category in a country and compare it to the production of the local breweries (we suppose that the most reviewed category is the most consumed).
* The third step being trying to find if the review trends precedes the breweing trend or the other was around. This is done by ploting different temporal analysis.
* To last step consists of finding where are the most positive and negative comments by using sentiment analysis
### 3) Data Representation
In order to plot the data we use the geopandas library, which allows us to plot data on a world map. The data to be plotted is the following:
* Prefered kind of beer per country
* Tendency of local breweries to produce the prefered kind of beer (z-scoring for each country)
* Tendency of local breweries to produce the most reviewd beer (z-scoring for each country)
* Positivity of comments


## Specialization of each team-member
- Anthony did the data structure.
- Benjamin worked on the sentiment analysis.
- Mathieu helped left and right.
- Swann did the category analysis.
- Xingchen built the website and the interactive chart embedding in it. She also worked on the sentiment analysis


