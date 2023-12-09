I worked on the description of the dataset. Here is the result

- Read [this](src/1.exploration.ipynb) to understand the dataset

I have not worked yet on the preprocessing BUT the conversion from txt to csv is done

You can download the dataset [here](data/data link.md)



I tried to make the structure of the project as clear as possible

You'll find the code from milestone 2 [here](docs/milestone_2/)



There is a parameter 'reduced' in the load_data function. It corresponds to the n first rows loaded for the reviews/ratings dataframe. Make it low to avoid running out of memory (1e5 is quite low, approx 0.1% of the data)