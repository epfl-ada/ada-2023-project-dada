import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import pycountry
from geopy.geocoders import Nominatim
import statsmodels.formula.api as smf
import plotly.express as px

#from geopy.exc import GeocoderTimedOut, GeocoderServiceError
#import geopandas as gpd
#import contextily as ctx
#import pycountry


""" Preprocessing and loading """

def load_data(dataset_name):
    if dataset_name == "RB":
        # Data from RateBeer 'RB'
        beers_RB = pd.read_table("./data/RateBeer/beers.csv", sep=",")
        breweries_RB = pd.read_table("./data/RateBeer/breweries.csv", sep=",")
        users_RB = pd.read_table("./data/RateBeer/users.csv", sep=",")
        ratings_RB = pd.read_table("./data/RateBeer/ratings.csv", sep=",")
        return beers_RB, breweries_RB, users_RB, ratings_RB
    elif dataset_name == "BA":
        # Data from BeerAdvocate 'BA'
        beers_BA = pd.read_table("./data/BeerAdvocate/beers.csv", sep=",")
        breweries_BA = pd.read_table("./data/BeerAdvocate/breweries.csv", sep=",")
        users_BA = pd.read_table("./data/BeerAdvocate/users.csv", sep=",")
        ratings_BA = pd.read_table("./data/BeerAdvocate/ratings.csv", sep=",")
        return beers_BA, breweries_BA, users_BA, ratings_BA
    elif dataset_name == "MD":
        # Data from MatchedDataset 'MD'
        beers_MD = pd.read_table("./data/matched_beer_data/beers.csv", sep=",")
        breweries_MD = pd.read_table("./data/matched_beer_data/breweries.csv", sep=",")
        users_MD = pd.read_table("./data/matched_beer_data/users.csv", sep=",")
        users_approx_MD = pd.read_table("./data/matched_beer_data/users_approx.csv", sep=",")
        ratings_MD = pd.read_table("./data/matched_beer_data/ratings.csv", sep=",")
        return beers_MD, breweries_MD, users_MD, users_approx_MD, ratings_MD
    else:
        raise NameError

def ratings_text_to_csv(txt_path):
    """
    Rewrite the ratings txt files as a csv file. May require large amount of RAM
    """
    ratings_list = []
    rating_dic = {}
    with open(txt_path, encoding= "utf8") as f:
        for i, line in tqdm(enumerate(f)):
            field = line.split(": ")[0]
            if field == "\n":
                ratings_list.append(rating_dic)
                rating_dic = {}
                continue
            content = line.split(": ")[1:]
            content = ": ".join(content)
            rating_dic[field] = content.strip()
            
    ratings_RB = pd.DataFrame.from_dict(ratings_list)
    ratings_RB.to_csv(txt_path[:-3]+"csv", index=False)

def populate_ratings(ratings, users, breweries, beers, dataset_name):
    """
    Add all available information to the ratings with respect to the corresponding beer, brewery, user and dataset_name
    Rename some columns for clarity
    """
    
    # Rename
    users = users.rename(columns={"location":"user_location",'nbr_ratings':'user_nbr_ratings','nbr_reviews':'user_nbr_reviews'})
    beers = beers.rename(columns={'nbr_ratings':'beer_nbr_ratings','nbr_reviews':'beer_nbr_reviews'})
    breweries = breweries.rename(columns={"id":"brewery_id","location":"brewery_location","name":"brewery_name"})

    # Merge
    ratings_populated = ratings.merge(users ,on="user_id", how="left", suffixes=('', '_drop'))
    ratings_populated = ratings_populated.merge(breweries,on="brewery_id", how="left", suffixes=('', '_drop'))
    ratings_populated = ratings_populated.merge(beers,on="beer_id", how="left", suffixes=('', '_drop'))
    ratings_populated.drop([col for col in ratings_populated.columns if 'drop' in col], axis=1, inplace=True)
    ratings_populated['dataset']=dataset_name

    return ratings_populated

def merge_populated_ratings(ratings_populated_BA, ratings_populated_RB, save_path):
    """
    Write merge populated ratings as a csv file at save_path. 
    Rearange the collumns in a more intuitive order
    """
     
    ratings_mixed = pd.concat([ratings_populated_BA, ratings_populated_RB], axis=0, ignore_index=True)
    
    # Rearrange columns order
    cols = [

        # Beers
        'beer_id',
        'beer_name',
        'style',
        'abv',
        'beer_nbr_ratings',
        'beer_nbr_reviews',
        #'avg',
        #'avg_computed',
        #'ba_score',
        #'bros_score',
        #'overall_score',
        #'style_score',
        #'zscore',
        #'nbr_matched_valid_ratings',
        #'avg_matched_valid_ratings',

        # Breweries
        'brewery_name',
        'brewery_id',
        'brewery_location',
        'nbr_beers',
        
        # Users
        'user_name',
        'user_id',
        'user_location',
        'user_nbr_ratings',
        'user_nbr_reviews',
        #'joined',
        
        # Ratings
        'date',
        'appearance',
        'aroma',
        'palate',
        'taste',
        'overall',
        'rating',
        'text',
        #'review',
        
        'dataset'
    ]
    ratings_mixed = ratings_mixed[cols]

    # Save as a csv file
    ratings_mixed.to_csv(save_path, index=False)
    return ratings_mixed

def save_subsample(dataframe, save_path ,frac=0.1, random_state=0):
    subsample = dataframe.sample(frac=frac, random_state=random_state)
    subsample.to_csv(save_path, index=False)

def save_pickle(dataframe, save_path):
    dataframe.to_pickle(save_path)


""" Geodata representation """

def geocode(location):
    geolocator = Nominatim(user_agent="geoapiExercises")

    try:
        loc = geolocator.geocode(location,language='en')
        if loc:
            location_detail = geolocator.reverse((loc.latitude, loc.longitude), exactly_one=True)
            try:
                address = location_detail.raw['address']
                country = address.get('country', None)
                iso_alpha = address.get('country_code', None).upper()  
                iso_alpha = pycountry.countries.get(alpha_2=iso_alpha.upper()).alpha_3
                return country, iso_alpha
            except:
                return None, None
        else:
            return None, None
    except:
        return None, None
    
def display_user_location(ratings):

    # User locations
    user_unique=ratings.drop_duplicates(subset='user_id', keep='first')  # Keep only one row per user
    user_location_counts = user_unique["user_location"].value_counts()
    user_location_counts_df = user_location_counts.reset_index()
    user_location_counts_df.columns = ['user_location', 'count']
    user_location_counts_df['country_data'] = [geocode(location) for location in tqdm(user_location_counts_df['user_location'])]
    
    # Drop any rows where geocoding failed
    user_location_counts_df = user_location_counts_df.dropna(subset=['country_data'])
    user_location_counts_df[['country', 'iso_alpha']] = pd.DataFrame(user_location_counts_df['country_data'].tolist(), index=user_location_counts_df.index)
    user_country_counts = user_location_counts_df.groupby(['country', 'iso_alpha'])['count'].sum().reset_index()

    # User Map
    fig = px.choropleth(user_country_counts,
                        locations="iso_alpha",
                        color="count",
                        hover_name="country",
                        color_continuous_scale=[
                            (0.0, 'rgb(255, 255, 229)'),  
                            (0.01, 'rgb(255, 247, 188)'),  
                            (0.02, 'rgb(254, 227, 145)'), 
                            (0.03, 'rgb(254, 196, 79)'),   
                            (0.04, 'rgb(254, 153, 41)'),  
                            (0.05, 'rgb(236, 112, 20)'),   
                            (0.1, 'rgb(204, 76, 2)'),    
                            (0.5, 'rgb(153, 52, 4)'),     
                            (1.0, 'rgb(102, 37, 6)'),     
                        ],
                        projection="natural earth")
    fig.update_layout(title_text='World Map of User Locations', title_x=0.5, title_font_size=30)
    fig.show()

def display_brew_location(ratings):
    # For brew locations
    brew_unique=ratings.drop_duplicates(subset='brewery_id', keep='first')  # Keep only one row per user
    brew_location_counts = brew_unique["brewery_location"].value_counts()

    brew_location_counts_df = brew_location_counts.reset_index()
    brew_location_counts_df.columns = ['brew_location', 'count']


    brew_location_counts_df['country_data'] = [geocode(location) for location in tqdm(brew_location_counts_df['brew_location'])]
    # Drop any rows where geocoding failed
    brew_location_counts_df = brew_location_counts_df.dropna(subset=['country_data'])
    brew_location_counts_df[['country', 'iso_alpha']] = pd.DataFrame(brew_location_counts_df['country_data'].tolist(), index=brew_location_counts_df.index)
    brew_country_counts = brew_location_counts_df.groupby(['country', 'iso_alpha'])['count'].sum().reset_index()

    # Brew map
    fig = px.choropleth(brew_country_counts,
                    locations="iso_alpha",
                    color="count",
                    hover_name="country",
                    color_continuous_scale=[
                        (0.0, 'rgb(255, 255, 229)'),  
                        (0.01, 'rgb(255, 247, 188)'),  
                        (0.02, 'rgb(254, 227, 145)'), 
                        (0.03, 'rgb(254, 196, 79)'),   
                        (0.04, 'rgb(254, 153, 41)'),  
                        (0.05, 'rgb(236, 112, 20)'),   
                        (0.1, 'rgb(204, 76, 2)'),    
                        (0.5, 'rgb(153, 52, 4)'),     
                        (1.0, 'rgb(102, 37, 6)'),     
                    ],
                    projection="natural earth")
    fig.update_layout(title_text='World Map of Brewery Locations', title_x=0.5, title_font_size=30)
    fig.show()




""" Linear regression """

def get_LR(data, columns):
    """
    takes a subset of ratings and columns of interest as input and returns a Linear Regresion results
    """
    data_to_process = data.copy() # copy original dataset
    
    # create formula
    columns=list(columns)
    formula = 'rating ~ ' + columns[0]
    for el in columns[1:-1]:
        formula += ' + ' + el
    
    # standardization and creation of the formula
    columns.append('rating')  # add rating for the linear regression and standardization
    data_to_process = data_to_process[columns].dropna().sample(frac=1)  # only keeps columns of interest and shuffle the samples
    data_to_process = (data_to_process - data_to_process.mean()) / data_to_process.std()
    
    # create the model and fit it to the dataset
    mod = smf.ols(formula=formula, data=data_to_process)
    np.random.seed(2)
    res = mod.fit()
    return res


""" Plot rolling """

def plot_rolling(df, window=7):
    daily_reviews = df.groupby(df['date'].dt.date).size()
    # Calculate the moving average with a window size of 7 to remove weeks days
    rolling = daily_reviews.rolling(window=window, center=True)
    rolling_average = rolling.mean()
    
    # Plot the rolling average
    plt.figure(figsize=(14, 7))
    rolling_average.plot(title=f"Number of Reviews Per Day Over One Year with rolling window of {window} days")
    
    # Add labels and grid
    plt.xlabel('Date')
    plt.ylabel('Number of Reviews')
    plt.grid(True)
    plt.show()