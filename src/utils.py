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
def load_data(dataset, reduced=None, reduced_limit=1e12):
    assert(dataset in ['ba', 'rb', 'matched'])
    
    COMPRESSION = 'zip'
    DATASET_BA_DIR = '../data/BeerAdvocate/'
    DATASET_RB_DIR = '../data/RateBeer/'
    DATASET_MATCHED_DIR = '../data/matched_beer_data/'
    
    if reduced is None:
        reduced=reduced_limit

    # Load BeerAdvocate dataset
    if dataset=='ba':
        beers_ba = pd.read_csv(DATASET_BA_DIR+'beers.csv.zip', header=0, compression=COMPRESSION)
        breweries_ba = pd.read_csv(DATASET_BA_DIR+'breweries.csv.zip', header=0, compression=COMPRESSION)
        users_ba = pd.read_csv(DATASET_BA_DIR+'users.csv.zip', header=0, compression=COMPRESSION)
        ratings_ba = pd.read_csv(DATASET_BA_DIR+'ratings.csv.zip', header=0, compression=COMPRESSION, nrows=reduced)
        #reviews_ba = pd.read_csv(DATASET_BA_DIR+'reviews.csv.zip', header=0, compression=COMPRESSION, nrows=reduced)
        return beers_ba, breweries_ba, users_ba, ratings_ba#, reviews_ba

    # Load RateBeer dataset
    if dataset=='rb':
        beers_rb = pd.read_csv(DATASET_RB_DIR+'beers.csv.zip', header=0, compression=COMPRESSION)
        breweries_rb = pd.read_csv(DATASET_RB_DIR+'breweries.csv.zip', header=0, compression=COMPRESSION)
        users_rb = pd.read_csv(DATASET_RB_DIR+'users.csv.zip', header=0, compression=COMPRESSION)
        ratings_rb = pd.read_csv(DATASET_RB_DIR+'ratings.csv.zip', header=0, compression=COMPRESSION, nrows=reduced)
        #reviews_rb = pd.read_csv(DATASET_RB_DIR+'reviews.csv.zip', header=0, compression=COMPRESSION, nrows=reduced)
        return beers_rb, breweries_rb, users_rb, ratings_rb#, reviews_rb

    # Load Matched dataset
    if dataset=='matched':
        beers_matched = pd.read_csv(DATASET_MATCHED_DIR+'beers.csv.zip', header=0, compression=COMPRESSION)
        breweries_matched = pd.read_csv(DATASET_MATCHED_DIR+'breweries.csv.zip', header=0, compression=COMPRESSION)
        users_matched = pd.read_csv(DATASET_MATCHED_DIR+'users.csv.zip', header=0, compression=COMPRESSION)
        users_approx_matched = pd.read_csv(DATASET_MATCHED_DIR+'users_approx.csv.zip', header=0, compression=COMPRESSION)
        ratings_matched = pd.read_csv(DATASET_MATCHED_DIR+'ratings.csv.zip', header=0, compression=COMPRESSION)
        ratings_ba_matched = pd.read_csv(DATASET_MATCHED_DIR+'ratings_ba.csv.zip', header=0, compression=COMPRESSION, nrows=reduced)
        ratings_rb_matched = pd.read_csv(DATASET_MATCHED_DIR+'ratings_rb.csv.zip', header=0, compression=COMPRESSION, nrows=reduced)
        #ratings_with_text_ba_matched = pd.read_csv(DATASET_MATCHED_DIR+'ratings_with_text_ba.csv.zip', header=0, compression=COMPRESSION, nrows=reduced)
        #ratings_with_text_rb_matched = pd.read_csv(DATASET_MATCHED_DIR+'ratings_with_text_rb.csv.zip', header=0, compression=COMPRESSION, nrows=reduced)
        return beers_matched, breweries_matched, (users_matched, users_approx_matched), (ratings_matched, ratings_ba_matched, ratings_rb_matched)#, (ratings_with_text_ba_matched, ratings_with_text_rb_matched)