# <demo> silent
# Title: pandas_demo_3.py
# Usage: %run demobatch.py pandas_demo_3.py
# Description: Elaboration on data handling, cleaning, wrangling
# Date: 20150112
# Revision: 0.5
# Python Version: 3.x
# Author: Chalmer Lowe

# TODO:
# ===========================================================================

# <demo> stop
# We prepare to use pandas by importing pandas with an alias 'pd' AND importing
# DataFrame and Series

import pandas as pd
from pandas import DataFrame, Series

# We will start by reading in two files, both of which include data on 
# comicbook readers. One file is longer than the other, but otherwise the data is 
# generally similar: a column with names and a column with countries.
# For those who are curious... the names are impressionist painters. = )

readers1 = pd.read_csv('reader_stats.csv')
readers2 = pd.read_csv('reader_stats_short.csv')

print("readers1 data:", '\n', readers1)
print('-' * 40)
print("readers2 data:", '\n', readers2)

# <demo> stop
# pandas has built-in functions that allow you to merge data simply and easily
# These functions mirror the merges you might do via database join on a SQL 
# (or similar) database.

readerso = pd.merge(readers1, readers2, how='outer')
readersi = pd.merge(readers1, readers2, how='inner')
readersl = pd.merge(readers1, readers2, how='left')
readersr = pd.merge(readers1, readers2, how='right')

# <demo> stop

print('Outer Join\n')
readerso

# <demo> stop

print('Inner Join\n')
readersi

# <demo> stop

print('Left Join\n')
readersl

# <demo> stop

print('Right Join\n')
readersr

# NOTE: Please be aware, that unless you specify otherwise, these joins 
# are based on the contents of the entire row.
# In many cases, we simply want to join based on the contents one or more columns.

# <demo> stop
# Remember, DataFrames can be built from dictionaries, using the keys of the dictionary
# as the source of the column in the DataFrame.
# Any elements (stored as a sequence) in the values associated with those keys then
# become the elements in the respective column
# Here, we are creating some key columns that we can use to create joins...



dfa = DataFrame({'key':     ['bruce', 'bruce', 'diana', 'bruce', 'hal', 'diana', 'kara'],
                 'emails_left': [112, 111, 201, 109, 113, 203, 204]}) 

dfb = DataFrame({'key':        ['hal', 'bruce', 'selina', 'diana'],
                 'ages_right': [36, 37, 33, 34]})

# dfa
# dfb

# <demo> stop
# Imagine, that using the previous data, we wanted to do an analysis of emails versus
# age (i.e. whether age impacts the number of emails someone receives over time).
# Let's start with a Left Join: 

dfl = pd.merge(dfa, dfb, on='key', how='left')

# <demo> stop
# Now, let's look at an Inner Join:

dfi = pd.merge(dfa, dfb, on='key', how='inner')

# <demo> stop
# Here, again, we create a set of DataFrames based on dictionaries.
# This time we choose to use more than one column that will be used as keys to
# match data in each of the DataFrames.


dfa = DataFrame({'fname_key': ['bruce', 'bruce', 'hal', 'selina', 'hal'],
                 'lname_key': ['wayne', 'jordan', 'wayne', 'kyle', 'jordan'],
                 'ages_left': [37, 53, 54, 33, 36]})

dfb = DataFrame({'fname_key': ['hal', 'bruce', 'hal', 'kara', 'hal'],
                 'lname_key': ['jordan', 'wayne', 'jordan', 'zor-el', 'jordan'],
                 'emails_right': [189, 111, 193, 253, 187]})

# Outer Join 
dfo = pd.merge(dfa, dfb, on=['fname_key', 'lname_key'], how='outer')


# <demo> stop
# Inner Join
dfi = pd.merge(dfa, dfb, on=['fname_key', 'lname_key'], how='inner')


# <demo> stop
# NOTE: DataFrames can be merged on indexes, as opposed to using a column(s).
# A closer look at the 'how' is left as an exercise for the student...

# <demo> stop
# pandas can not only join data, but it can be used to concatenate data as well.
# The default concatenation method is to stack data on top of each other

names1 = Series(['wayne', 'jordan'], index=[1, 2])
names2 = Series(['dinah', 'kent'], index=[4, 5])
names3 = Series(['rayner', 'gordon', 'grayson'], index=[6, 7, 8])

pd.concat([names1, names3, names2], axis=0)

# An alternate method is to stack columns side by side
# pd.concat([names1, names3, names2], axis= 1)


# <demo> stop
names4 = pd.concat([names1, names3])
pd.concat([names1, names4], axis=1)


# <demo> stop
output = pd.concat([names1, names3, names3], keys=['rho', 'sigma', 'tau'])
output


# <demo> stop
output = pd.concat([names1, names3, names3], axis=1, keys=['rho', 'sigma', 'tau'])
output

# <demo> stop
# To prep our next data set, we'll use yet another way to generate DataFrames...
# These nested lists will become the rows in our DataFrame
# AS a reminder, you can assign columns when you generate the Frame
# If you don't have any need for the original indexes, you can ignore
# them and pandas will auto-generate an brand-new index on the fly when you do a 
# concatenation.

dfa = DataFrame([[11, 21, 31, 41],
                 [13, 25, 32, 49],
                 [11, 21, 31, 41],
                 [11, 21, 31, 42]], columns=['iota', 'kappa', 'lambda', 'mu'])

dfb = DataFrame([[55, 66, 77],
                 [53, 63, 73]], columns=['kappa', 'lambda', 'mu'])

print(dfa)
print(dfb)

pd.concat([dfa, dfb], ignore_index=True)

# <demo> stop
# When generating DataFrames, another common method, especially with ranges of
# data OR with randomized data is to use functions in numpy to seed
# the Frame with ranges and/or randomized values. 
# Here, we are creating a Frame with the numbers 100 to 114 and shaping it to be a 
# three by five table.

import numpy as np
df = DataFrame(np.arange(100, 115).reshape((3, 5)),
               index=pd.Index(['kara', 'dinah', 'selina'], name='justiceleague'),
               columns=pd.Index(['wed', 'thu', 'fri', 'sat', 'sun'], name='day'))
df


# <demo> stop
# The default level to unstack is the innermost
df.unstack()


# <demo> stop
# You can refer to the level to unstack by an integer number, starting
# with the farthest left being noted as 0. By default, pandas unstacks from the innermost level of a multi-level hierarchical index.

# The following code comes directly from the pandas documentation:
# http://pandas.pydata.org/pandas-docs/stable/advanced.html
# Several take-aways for this code... 
#     * use the documentation > plenty of great examples are in there.
#     * the inputs can be cut and pasted straight into IPython without removing the
#       In[x] prompts or the ...: prompts. Nice timesaver
#     * This MultiIndex dataframe is a nice setup for demoing multilevel unstacking
 
'''
In [1]: arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
   ...:           ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
   ...: 

In [2]: tuples = list(zip(*arrays))

In [3]: tuples
Out[3]: 
[('bar', 'one'),
 ('bar', 'two'),
 ('baz', 'one'),
 ('baz', 'two'),
 ('foo', 'one'),
 ('foo', 'two'),
 ('qux', 'one'),
 ('qux', 'two')]

In [4]: index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])

In [5]: index
Out[5]: 
MultiIndex(levels=[['bar', 'baz', 'foo', 'qux'], ['one', 'two']],
           labels=[[0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 0, 1, 0, 1, 0, 1]],
           names=['first', 'second'])

In [6]: s = pd.Series(np.random.randn(8), index=index)

In [7]: s
Out[7]: 
first  second
bar    one       0.469112
       two      -0.282863
baz    one      -1.509059
       two      -1.135632
foo    one       1.212112
       two      -0.173215
qux    one       0.119209
       two      -1.044236
dtype: float64
'''

# <demo> stop
# Using the example above, it is possible to demonstrate several levels of unstacking.
# As noted, the default level of unstacking is to unstack from the innermost level
# of a MultiIndex. Levels are numbered started at the outermost level being '0' and 
# incrementing as they move inward.

print(s)
print(s.unstack(1))
print(s.unstack(0))


# <demo> stop
# NOTE: You can refer to the level to unstack by the name of the Index.

s.unstack('second')


# <demo> stop
# Another great tool for looking at your data in more convenient ways is to use a 
# pivot table. Let's start with a DataFrame that has three columns based on 
# this list of lists. A timestamp, a Justice League hero and the number of 
# Tweets they received on a given day.

league = DataFrame([['2016-03-10T00:00:00', 'jordan', 221],
                    ['2016-03-10T00:00:00', 'wayne', 222],
                    ['2016-03-10T00:00:00', 'kyle', 345],
                    ['2016-03-11T00:00:00', 'jordan', 222],
                    ['2016-03-11T00:00:00', 'wayne', 223],
                    ['2016-03-11T00:00:00', 'kyle', 323],
                    ['2016-03-12T00:00:00', 'jordan', 201],
                    ['2016-03-12T00:00:00', 'wayne', 209],
                    ['2016-03-12T00:00:00', 'kyle', 340],
                    ['2016-03-13T00:00:00', 'jordan', 220],
                    ['2016-03-13T00:00:00', 'wayne', 223],
                    ['2016-03-13T00:00:00', 'kyle', 339],
                    ['2016-03-14T00:00:00', 'jordan', 201],
                    ['2016-03-14T00:00:00', 'wayne', 219],
                    ['2016-03-14T00:00:00', 'kyle', 345]],
                    columns=['timestamp', 'jleague', 'tweets'])


# <demo> stop
# From the league DataFrame, we can create a pivot table using the pivot() command:

tweet_view = league.pivot('timestamp', 'jleague', 'tweets')
tweet_view

# <demo> stop

league['fan_index'] = abs(np.random.randn(len(league)))
league



# <demo> stop
tweet_view2 = league.pivot('timestamp', 'jleague')
tweet_view2


# <demo> stop
tweet_view2['fan_index']


# <demo> stop
# Dropping duplicates
dfd = dfa
dfd['zeta'] = [4, 1, 4, 1]
dfd

# <demo> stop
dfd.duplicated()

# <demo> stop
dfd.drop_duplicates()

# dfd.drop_duplicates(['iota', 'kappa'])
# dfd.drop_duplicates(['iota', 'kappa'], take_last=True)

# <demo> stop
# Using .map()

# legend:
# 0 = 'm'
# 1 = 'f'

genders = {'selina kyle': '1',
           'bruce wayne': '0',
           'dinah lance': '1',
           'hal jordan': '0',
           'clark kent': '0',
           'barry allen': '0',
           'arthur curry': '0',
           'billy batson': '0',
           'barbara gordon': '1',
           'kara zor-el': '1',
           'john jones': '0',
           'diana prince': '1',
           'dick grayson': '0',
           'john jones': '0',
           'victor stone': '0',
           'ray palmer': '0',
           'john constantine': '0',
           'kyle rayner': '0',
           'wally west': '0'}


it = pd.read_csv('ig_tweets.csv')
it


# <demo> stop
def gen_conv(x):
    g = genders[x.lower()]
    if g == '0':
        return 'm'
    if g == '1':
        return 'f'

it['gender'] = it['jleague'].map(gen_conv)

# <demo> stop
# What if you want to cleanse some of the data upfront using a simple function 
# associated with strings:
# change all the data to lowercase, uppercase, capitalize it, etc...

it['jleague2'] = it['jleague'].map(str.lower)

# <demo> stop
# You can also replace certain values wholesale if desired, using the replace() function
# Using .replace()
it.gender.replace('f', 'Female')

# <demo> stop
it.gender.replace(['f', 'm'], ['Female', 'Male'])


# <demo> stop
msgs = it.tweets
bins = [2, 5, 9, 15]
labels = ['few', 'medium', "aren't there bad guys to catch"]
categories = pd.cut(msgs, bins, labels)

# <demo> stop
# math notation ... '(' open   OR exclusive
#                   ']' closed OR inclusive
# 2 < x <= 5        (2, 5]

#                   right=True/False

pd.value_counts(categories)

# <demo> stop

it['workload'] = pd.cut(it.tweets, bins, labels=labels)
it


# End of demo .....

# <demo> stop


# <demo> stop
# Filtering outliers


# <demo> stop



# <demo> stop


# <demo> stop
# Using get_dummies


# <demo> stop


# <demo> stop



# <demo> stop
# Using string manipulation


# <demo> stop



# <demo> stop



# <demo> stop



# <demo> stop




#----------- BACKUP ----------------
# m_stats = pd.read_csv('m_avenger_stats.csv', names=['name', 'age', 'height])
# f_stats = pd.read_csv('f_avenger_stats.csv', names=['name', 'age', 'height])

# m_stats
# f_stats