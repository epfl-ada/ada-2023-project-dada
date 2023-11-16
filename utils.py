import pandas as pd
from tqdm import tqdm

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
    elif dataset_name == "matched":
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
    """
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
        'beer_name',
        'beer_id',
        'style',
        'abv',
        'nbr_ratings',
        'nbr_reviews',
        'avg',
        'ba_score',
        'bros_score',
        'avg_computed',
        'zscore',
        'overall_score',
        'style_score',
        'nbr_matched_valid_ratings',
        'avg_matched_valid_ratings',
        'joined',
        'brewery_name',
        'brewery_id',
        'brewery_location',
        'nbr_beers',
        'date',
        'user_name',
        'user_id',
        'user_location',
        'appearance',
        'aroma',
        'palate',
        'taste',
        'overall',
        'rating',
        'text',
        'review',
        'dataset'
    ]
    ratings_mixed = ratings_mixed[cols]

    # Save as a csv file
    ratings_mixed.to_csv(save_path, index=False)
    return ratings_mixed

def save_subsample(dataframe, save_path ,frac=0.1, random_state=0):
    subsample = dataframe.sample(frac=frac, random_state=random_state)
    subsample.to_csv(save_path, index=False)