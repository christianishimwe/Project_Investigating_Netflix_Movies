'''
Perform exploratory data analysis on the netflix_data.csv data to understand more about movies from the 1990s decade.

1. What was the most frequent movie duration in the 1990s? Save an approximate answer as an integer called duration.

2. A movie is considered short if it is less than 90 minutes. Count the number of short action movies released in the
 1990s and save this integer as short_movie_count.
Netflix! What started in 1997 as a DVD rental service has since exploded into one of the largest entertainment and media companies.

Given the large number of movies and series available on the platform, it is a perfect opportunity to flex your exploratory data analysis skills and dive into the entertainment industry.

You work for a production company that specializes in nostalgic styles. You want to do some research on movies released in the 1990's. You'll delve into Netflix data and perform exploratory data analysis to better understand this awesome movie decade!

You have been supplied with the dataset netflix_data.csv, along with the following table detailing the column names and descriptions. Feel free to experiment further after submitting!

The data
netflix_data.csv

Column	Description
show_id	The ID of the show
type	Type of show
title	Title of the show
director	Director of the show
cast	Cast of the show
country	Country of origin
date_added	Date added to Netflix
release_year	Year of Netflix release
duration	Duration of the show in minutes
description	Description of the show
genre	Show genre



'''


# Importing pandas and matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Start coding here! Use as many cells as you like
duration_slot = netflix_df[["duration"]]
plt.hist(duration_slot)
plt.show()
# we can analyze the most frequent movie duration from the histogram
duration = 90
# we can count number of short action movies by counting from a np array
# remember that a panda series is the same as a numpy array
# so we can do math on a panda series
# step 1: we will obtain a series containing only the column of duration
duration_series = netflix_df["duration"]
# step 2: from that series we will subset those movies duration less than 90 minues
dur_series_less90 = duration_series < 90
print(dur_series_less90)

# step 3: we continue to do math on that series
# at this point we can select those movies in that series that were released in 1990
# let's first obtain the data set back
less90_data = netflix_df[dur_series_less90]
print(less90_data)
# step 4: we will now subset, a release_year series from there
release_yr_less90 = less90_data["release_year"]
print(release_yr_less90)
# step 5: from that we subset those released in 1990s, we obtain another series
in_1990s_less90 = np.logical_and(release_yr_less90 > 1989, release_yr_less90 < 2000)
print(in_1990s_less90)

# finally, we will get those true values from our initial panda data set, specifically from the duration column
#fin_1990s_durLess90 = netflix_df[in_1990s_less90]
# the code just above gives an error since we are passing in a smaller series to a huge data set
# so we need to use an equivalently large data set
# so we use less90_data data table to pass in in_1990s_less90
fin_less90_1990s = less90_data[in_1990s_less90]
print(fin_less90_1990s)

# step 6, we will now subset only short movies, as a data set, notice that those are only 7 movies
less90_1990s_short = fin_less90_1990s[fin_less90_1990s["genre"] == "Action"]
print(less90_1990s_short)
short_movie_count = 7

