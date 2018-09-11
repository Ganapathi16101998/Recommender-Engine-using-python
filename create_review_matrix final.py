import pandas as pd
import numpy as np
import os
import webbrowser

# Read the dataset into a data table using Pandas
df = pd.read_csv("movie_ratings_data_set.csv")

# Convert the running list of user ratings into a matrix using the 'pivot table' function
ratings_df = pd.pivot_table(df, index='user_id', columns='movie_id', aggfunc=np.max)

print (ratings_df)