# Title: Pandas Demo 2
# Filename: pandas_demo_2.py
# Usage: Run using IPython and associated demobatch.py script
       # see demobatch.py for usage instructions
# Description: How to use pandas to read data from csv files and sql
             # databases.
# Date: 20160301
# Revision: 0.5
# Python Version: 3.x
# IPython Revision:: n/a
# Author: Chalmer Lowe

# TODO:
# ===========================================================================

# <demo> stop
# When using pandas, it is common to import pandas as pd and to 
# simply import the factory functions: Series and DataFrames

import pandas as pd
from pandas import Series, DataFrame

# <demo> stop
# Pandas is adept at reading in many, many data formats 
# To see which ones, you can type pd.read and use 'tab completion'
# 
# pd.read<Press the tab key>

# <demo> stop
# Let's start by reading from the clipboard after we copy data from a
# table on a webpage.

webdata = pd.read_clipboard()
webdata

# Try some of the following:
# webdata.C<press the tab key>
# webdata.Column1

# <demo> stop
# We will focus on csv and sql for remainder of this discussion
# Let's dive into csv first.

data = pd.read_csv('../../log_file.csv')
data

# In the results, notice the column headers. By default, pandas will use the first
# row as a header row...  'barry allen' shows up a the header for column 1.
# Maybe NOT what you want...
#
# <demo> stop
# if we include a list of names in the function call, pandas will use those
# as the headers instead of the first row.

named_cols = pd.read_csv('../../log_file.csv', names=['name', 'email', 'fmip', 'toip',
                                                     'datetime', 'lat', 'long', 'payload'])

# named_cols.info()

# <demo> stop
# It is not necessary to ingest all the lines from a file. Presuming that certain lines lack
# useful information... metadata, header lines, document data, etc.
# in this case, let's skip rows 1, 2, 3, 7, and 9 from the csv.

skipped_rows = pd.read_csv('../../log_file.csv', names=['name', 'email', 'fmip', 'toip',
                            'datetime', 'lat', 'long', 'payload'],
                            skiprows=[1, 2, 3, 7, 9])

# And let's look at just one of the columns.
skipped_rows.fmip

# <demo> stop
# You may receive files with alternate separators/delimiters. Pandas gives you tools to  
# deal with this situation. This file uses a 'pipe' character as the separator.

piped_data = pd.read_csv('../../log_file_pipes.csv', names=['name', 'email', 'fmip',
                                  'toip', 'datetime', 'lat', 'long', 'payload'],
                                  sep='|')

# piped_data.tail(3)
# piped_data.head(4)

# <demo> stop
# When reading in data, pandas assigns a default index of 0..n. Sometimes we want to use 
# something different than the default indexing.
# We can choose a particular column to be used as an index.
# Here we chose to use the datetime column

date_index = pd.read_csv('../../log_file.csv', names=['name', 'email', 'fmip', 'toip',
                         'datetime', 'lat', 'long', 'payload'],
                         index_col='datetime')

# <demo> stop
# If we have an index, we can select data from the DataFrame based on the
# index. In this case, since we just made the date/time our index, we can
# easily select rows based on the date/time stamps

date_index.ix['2016-02-06T21:44:56':'2016-02-06T21:49:36']

# <demo> stop
# Some files have missing data or markers indicating that data is not
# available.

data_na = pd.read_csv('../../log_file_na.csv', names=['name', 'email', 'fmip',
                         'toip', 'datetime', 'lat', 'long', 'payload'])

data_na
# data_na.dropna()

# <demo> stop
# Checking for na status and converting the value to an NaN flag is a time
# consuming process that might not be optimal for when loading data.
# You _can_ turn this process off


data_na = pd.read_csv('../../log_file_na.csv', names=['name', 'email', 'fmip',
                         'toip', 'datetime', 'lat', 'long', 'payload'],
                         na_filter=False)

data_na


# <demo> stop
# You can provide a list of particular values to use as na values. Some files
# or software will use sentinels or flag values to represent a null value.
data_na = pd.read_csv('../../log_file_na.csv', names=['name', 'email', 'fmip',
                         'toip', 'datetime', 'lat', 'long', 'payload'],
                         na_values=['', '9999'])
# data_na

# NOTE: in this case, it will combine the na_values you give with the built-in na
# values.

# <demo> stop
data_na = pd.read_csv('../../log_file_na.csv', names=['name', 'email', 'fmip',
                         'toip', 'datetime', 'lat', 'long', 'payload'],
                         na_values=['', '9999'], keep_default_na=False)

# data_na

# <demo> stop
data_na = pd.read_csv('../../log_file_na.csv', names=['name', 'email', 'fmip',
                         'toip', 'datetime', 'lat', 'long', 'payload'],
                         na_values=['', '9999'], keep_default_na=False,
                         nrows=15)
# data_na

# <demo> stop
data = pd.read_csv('../../log_file.csv', names=['name', 'email', 'fmip', 'toip',
                           'datetime', 'lat', 'long', 'payload'], chunksize=3)

for chunk in data:
    print('\npre-processing')
    print('more pre-processing')
    print('even more pre-processing')
    print(chunk)
    print('post processing\n')




# <demo> stop
# If you want to convert data in one of your columns, you can use a dictionary
# to define which conversion function(s) to use against which columns(s)
def dsplitter(address):
    userid, domain = address.split('@')
    return userid, domain

def date_only(datetime):
    return datetime.split('T')[0]

data = pd.read_csv('../../log_file.csv', names=['name', 'email', 'fmip', 'toip',
                           'datetime', 'lat', 'long', 'payload'],
                           converters={'email':dsplitter, 'datetime':date_only})
# data

# <demo> stop
data = pd.read_csv('../../log_file.csv', names=['name', 'email', 'fmip', 'toip',
                           'datetime', 'lat', 'long', 'payload'],
                           usecols=['email', 'fmip', 'toip'])

# data

# <demo> stop
import sqlite3
conn = sqlite3.connect('../../log_file.sql')
cur = conn.cursor()

df = pd.read_sql("SELECT * FROM superheroes", conn)

# <demo> stop
df1 = pd.read_sql('''SELECT datetime, email, lat, long FROM superheroes
                          WHERE name LIKE "%wayne%"''', conn)


# <demo> stop
df2 = pd.read_sql('''SELECT datetime, email, lat, long FROM superheroes
                          WHERE name LIKE "%wayne%"''', conn, index_col='datetime')

# <demo> stop
df2.to_csv('class_out.csv',
                  cols=['email', 'lat', 'long', 'name'],
                  header=True, sep='|')

