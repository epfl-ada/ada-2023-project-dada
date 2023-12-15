import pandas as pd
from tqdm import tqdm
import glob

# Convert txt files to csv files
def ratings_text_to_csv():
    """
    Rewrite the ratings txt files in data folder as a csv file.
    ! Don't put any other txt files in the data folder !
    """
    path = r'../data/**/*.txt'
    files = glob.glob(path, recursive=True)

    for file in files:
        ratings_list = []
        rating_dic = {}
        with open(file, encoding= "utf8") as f:
            for i, line in tqdm(enumerate(f)):
                field = line.split(": ")[0]
                if field == "\n":
                    ratings_list.append(rating_dic)
                    rating_dic = {}
                    continue
                content = line.split(": ")[1:]
                content = ": ".join(content)
                rating_dic[field] = content.strip()
                
        ratings = pd.DataFrame.from_dict(ratings_list)
        ratings.to_csv(file.replace('txt', 'csv'), index=False)


# Load csv data
def load_data(dataset, reduced=None):
    assert(dataset in ['ba', 'rb', 'matched', 'pre_ba', 'pre_rb'])
    
    BA_DIR = '../data/BeerAdvocate/'
    RB_DIR = '../data/RateBeer/'
    MATCHED_DIR = '../data/matched_beer_data/'
    PREPROCESSED_BA_DIR = '../data/preprocessed/BeerAdvocate/'
    PREPROCESSED_RB_DIR = '../data/preprocessed/RateBeer/'

    if reduced is None:
        reduced=1e15 # Assume no dataset longer than this value

    # Load BeerAdvocate dataset
    if dataset=='ba':
        beers_ba = pd.read_csv(BA_DIR+'beers.csv.zip')
        breweries_ba = pd.read_csv(BA_DIR+'breweries.csv.zip')
        users_ba = pd.read_csv(BA_DIR+'users.csv.zip')
        ratings_ba = pd.read_csv(BA_DIR+'ratings.csv.zip', nrows=reduced)
        #reviews_ba = pd.read_csv(BA_DIR+'reviews.csv.zip', nrows=reduced)
        return beers_ba, breweries_ba, users_ba, ratings_ba#, reviews_ba

    # Load RateBeer dataset
    if dataset=='rb':
        beers_rb = pd.read_csv(RB_DIR+'beers.csv.zip')
        breweries_rb = pd.read_csv(RB_DIR+'breweries.csv.zip')
        users_rb = pd.read_csv(RB_DIR+'users.csv.zip')
        ratings_rb = pd.read_csv(RB_DIR+'ratings.csv.zip', nrows=reduced)
        #reviews_rb = pd.read_csv(RB_DIR+'reviews.csv.zip', nrows=reduced)
        return beers_rb, breweries_rb, users_rb, ratings_rb#, reviews_rb

    # Load Matched dataset
    if dataset=='matched':
        beers_matched = pd.read_csv(MATCHED_DIR+'beers.csv.zip')
        breweries_matched = pd.read_csv(MATCHED_DIR+'breweries.csv.zip')
        users_matched = pd.read_csv(MATCHED_DIR+'users.csv.zip')
        users_approx_matched = pd.read_csv(MATCHED_DIR+'users_approx.csv.zip')
        ratings_matched = pd.read_csv(MATCHED_DIR+'ratings.csv.zip')
        ratings_ba_matched = pd.read_csv(MATCHED_DIR+'ratings_ba.csv.zip', nrows=reduced)
        ratings_rb_matched = pd.read_csv(MATCHED_DIR+'ratings_rb.csv.zip', nrows=reduced)
        #ratings_with_text_ba_matched = pd.read_csv(MATCHED_DIR+'ratings_with_text_ba.csv.zip', nrows=reduced)
        #ratings_with_text_rb_matched = pd.read_csv(MATCHED_DIR+'ratings_with_text_rb.csv.zip', nrows=reduced)
        return beers_matched, breweries_matched, (users_matched, users_approx_matched), (ratings_matched, ratings_ba_matched, ratings_rb_matched)#, (ratings_with_text_ba_matched, ratings_with_text_rb_matched)
    
    if dataset=='pre_ba':
        preprocessed_ratings_ba = pd.read_csv(PREPROCESSED_BA_DIR+'preprocessed_ratings_ba.csv.zip', nrows=reduced)
        return preprocessed_ratings_ba

    if dataset=='pre_rb':
        preprocessed_ratings_rb = pd.read_csv(PREPROCESSED_RB_DIR+'preprocessed_ratings_rb.csv.zip', nrows=reduced)
        return preprocessed_ratings_rb
    
    