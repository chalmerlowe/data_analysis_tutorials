# <demo> silent
# Title: pd_demo_5.py
# Usage: From an IPython prompt:
#        %run demobatch.py pandas_demo5.py
# Description: Demonstrating Data Aggregation techniques using pandas - borrowing
#     extensively from the book Python for Data Analysis by Wes McKinney
# Date: 20160503
# Revision: 0.5
# Python Version: 3.x
# IPython Version: 2.x
# Author: Chalmer Lowe

# TODO: N/A
# ============================================================================

# <demo> stop
# Agenda
# * Grouping data
# * Aggregating data


# <demo> stop
# Let's start by importing the pertinent libraries and functions

import pandas as pd
from pandas import DataFrame         #, Series
import numpy as np

# Let's start by defining a DataFrame that includes some sample data showing the 
# messages (emails & tweets) received by diana and clark on each of two days

df = DataFrame({'name': ['diana', 'diana', 'clark', 'clark', 'diana'],
                'msgs': ['email', 'tweet', 'email', 'tweet', 'email'],
                'day1': [10, 11, 23, 23, 15],
                'day2': [14, 15, 16, 17, 21]})

df

# <demo> stop
# grouping... 

grouped = df['day1'].groupby(df['name'])

# <demo> stop
#

grouped

# <demo> stop

# Only data from 'day1' is included and it is broken up by justice league
# superhero

for items in grouped:
    for item in items:
        print(item)

# <demo> stop
# With a dataframe broken up into groups, you can perform a number of 
# calculations on the groups. There are many calcs associated with GroupBy
# objects, such as .mean()

grouped.mean()


# <demo> stop
# Hierarchical grouping

means = df['day1'].groupby([df['name'], df['msgs']]).mean()
means


# <demo> stop
# Unstacking allows us to look at the data in a more intuitive way...

means.unstack()


# <demo> stop
# The indices used to group data do not have to be integral to
# the dataframe. 
# Any array, series or column that is the same length as your data 
# can be used to group things. Let's use two numpy arrays
# with 'keys' in them. 
# 1) cities where crime occurred
# 2) day of the week that emails/tweets occurred

cities = np.array(['new york', 'baltimore', 'baltimore', 'new york', 'new york'])
day = np.array(['mon', 'mon', 'tues', 'mon', 'tues'])

# Group the day1 column using our new/external keys and calc the
# mean of each group.

df['day1'].groupby([cities, day]).mean()

# <demo> stop
# You can pass an internal column name from the same df as a key(s)

df.groupby('name').mean()

# OR
# df.groupby(['name', 'msgs']).mean()



# <demo> stop
# The GroupBy method allows you to count the number of values
# in a grouped object's groups. 

df.groupby('name').size()

# <demo> stop
# We can use multiple keys to create a hierarchical
# index. 

df.groupby(['name', 'msgs']).size()


# <demo> stop
# If you iterate over GroupBy objects it parses each object 
# as a series of tuples:
#   *  each tuple contains the name of the group and 
#   *  the content of that group
# Here, we use tuple-unpacking to breakout each part: the name
# and the group-content object

for name, group in df.groupby('msgs'):
    print(name)
    print(group)


# <demo> stop
# The index is hierarchical (i.e. has more than one key) thus the 'name'
# is broken out into a separate tuple with multiple parts for each
# level of the hierarchical index.

for (k1, k2), group in df.groupby(['name', 'msgs']):
    print(k1, k2)
    print(group)


# <demo> stop
# When dealing with large datasets, it may not be desirable to group across the
# entire dataset. Here we display
# just the day1 column.

df.groupby(['name', 'msgs'])['day1'].mean()

# The following line does the same thing, but displays multiple columns.
# df.groupby(['key1', 'key2'])[['day1', 'day2']].mean()


# <demo> stop
# There are multiple ways to implement groups. 
#   * One way is using dictionaries to map columns (or rows) to values.
# In this case, we tie each of the years to a grouping
#   * pre apocalyptic
#   * post apocalyptic
#   * future


heroes = DataFrame([[512, 613, 714, 815, 916],
                    [413, 412, 411, 420, 415],
                    [501, 525, 535, 545, 555],
                    [501, 602, 545, 600, 599],
                    [413, 603, 412, 599, 419]],
                    columns=[2012, 2013, 2014, 2015, 2016],
                    index=['clark', 'bruce', 'diana', 'kara', 'selina'])

mapping = {2012: 'pre',
           2013: 'pre',
           2014: 'post',
           2015: 'post',
           2016: 'post',
           2017: 'future'}  


# <demo> stop
# We simply drop in the dictionary:
# Here, we explicitly identify the grouping axis to be the columns
# by using an axis=1 argument (the default is axis=0 for grouping by rows.)

by_column = heroes.groupby(mapping, axis=1)
by_column.sum()


# <demo> stop
# WARNING: pre/post are lexigraphically sortable, and leads to all the 'post'
# years being displayed infront of the 'pre' years, which seems weird, so
# we tell the function to skip the alphabetical sorting process, which
# leaves the 'pre' group (years 2012, 2013) in front of the 'post' group (years
# 2014, 2015, 2016).

by_column = heroes.groupby(mapping, axis=1, sort=False)
by_column.sum()
# by_dolumn.mean()
# by_column.describe()


# <demo> stop
# You can GroupBy the outputs of functions, as long as it provides an output
# This sample functions counts the number of vowels that show up in a superhero's
# name.

def count_vowels(name):
    count = 0
    for letter in name:
        if letter in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count

# The following will group the heroes based on the number of vowels in their
# name (1, 2 or 3) and then will calculate the means of their emails by group.

heroes.groupby(count_vowels).mean()

# <demo> stop
# What other aggregations can you do on data?
# by_column.mean()
# by_column.sum()
# by_column.min()
# by_column.max()
# by_column.median()
# by_column.first()
# by_column.last()
by_column.describe()

# by_column.<tab>        # pressing the <tab> key in IPython after typing
                         # "by_column.' will display all the methods/attributes


# <demo> stop
# Any aggregation function can be applied to your data. for example
# if we want to know how far off from the max, any given mean is, we can
# calculate that:

def max_mean_diff(arr):
    return arr.max() - arr.mean()

grouped.agg(max_mean_diff)

# <demo> stop
# This is a data that I generated randomly of fictional GPAs.
# Let's read in the data
# and start with a calculation to determine the relative pct between
# the student's gpa and change in the gpa

gpas = pd.read_csv('gpa_short.csv')
gpas['gpa_pct'] = gpas['gpa change'] / gpas['gpa']

# Let's group by the gender and the athlete (or not) statues.

grouped = gpas.groupby(['gender', 'athlete'])

# We can pull out just the gpa_pct column in reference to the groupings

grouped_pct = grouped['gpa_pct']

# <demo> stop
# At this point we can apply some functions to this data.
# NOTE: the use/non-use of quotes. 
#   * with built-in functions, you need to use the quotations
#   * for functions that you defined in the current namespace
# you can get away with not using the quotes:

grouped_pct.agg(['max', 'mean', max_mean_diff])

# <demo> stop
# It is possible to perform multiple aggregations
# against a given column:

functions = ['median', 'min', 'max', 'count']
result = grouped['gpa_pct', 'gpa'].agg(functions)

# <demo> stop
# if we want to turn our attention to a single grouping at a time, we can select
# for that grouping via dictionary-like indexing.

result['gpa_pct']


# <demo> stop
# We can map certain functions to certain columns by using a dictionary to perform the mapping:

mapping = {'gpa change': 'min', 'duration': 'mean'}
grouped.agg(mapping)

# <demo> stop
# This can get pretty sophisticated:

mapping2 = {'gpa change': ['min', 'max', 'median'], 'duration': 'mean'}
grouped.agg(mapping2)

# <demo> stop
# sometimes, we want to perform aggregation, but we want to retain the
# overall shape of the data
# this is where the transform method comes in. Let's look at two attempts
# to examine the mean for our heroes DataFrame

k = ['cat_a', 'cat_b', 'cat_a', 'cat_b', 'cat_a']

# Method 1

heroes.groupby(k).mean()

# Method 2

# heroes.groupby(k).transform('mean')

# NOTE: as before, any function that can be applied to the group can be fed
# into the transform function, for example:
# heroes.groupby(k).transform(max_mean_diff)

# <demo> stop
# there is another fundamental way to apply functions to the data in a Pandas
# object: using apply()
# let's say we want to find the best performers in terms of grade changes across
# each group

def best(df, n=10, column='gpa_pct'):
    return df.sort_index(by=column)[-n:]

# if we simply apply this to the gpas DataFrame, as a whole, we will see the
# most improved students and their characteristics, here we use n=7 to get the
# top seven.

best(gpas, n=7)

# <demo> stop
# if we use a GroupBy and then apply the function to the GroupBy object

gpas.groupby('athlete').apply(best)
# gpas.groupby('athlete').apply(best, n=2, column='gpa_change')

# <demo> stop
#
gpas.groupby(['athlete', 'gender']).apply(best, n=3)[['duration',
                                                      'gpa_pct',
                                                      'gpa change']]

# <demo> stop
#

dfc = gpas[['gpa', 'gpa change', 'gpa_pct']]
gpabins = pd.cut(dfc['gpa change'], 10)
gpabins

# <demo> stop
#

def stat_summary(grp):
    return {'min': grp.min(),
            'max': grp.max(),
            'median': grp.median(),
            'std': grp.std()}

grouped = dfc.gpa_pct.groupby(gpabins)
grouped.apply(stat_summary)
# grouped.apply(stat_summary).unstack()

# <demo> stop
#


# <demo> stop
#


# <demo> stop
#




# heroes2 = DataFrame([[1, 2, 3, 4, 5],
#                     [2, 4, 6, 8, 10],
#                     [1, 25, 50, 75, 100],
#                     [1, 2, 3, 4, 100],
#                     [100, 90, 80, 70, 60]], columns=[2011, 2012, 2013, 2014, 2015],
#                     index=['clark', 'tony', 'diana', 'thor', 'jessica'])
# 
# mapping = {2011: 'pre',
#            2012: 'pre',
#            2013: 'post',
#            2014: 'post',
#            2015: 'post',
#            2016: 'future'}
# 
# by_column2 = heroes.groupby(mapping, axis=1, sort=False)