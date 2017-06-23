# <demo> silent
# Title: Lesson on pandas, Part 1: Series, DataFrames
# Author: Chalmer Lowe
# Filename: pd_demo_1.py
# Usage: pd_demo_1.py
#     run iPython using this command: ipython
#     in [1]: from iPython.lib.demo import ClearIPDemo as demo
#     in [2]: d = demo('<filename>')
#     in [3]: d()
#     Press enter to execute each subsequent set of commands.
# Date: 2014-12-10
# Revision: 0.5
# Python Version: 3.x
# Desrciption: This file delivers a demo (if used with ipython's demo module)
#              that will provide insight into the uses of pandas and objects
#              such as the Series, DataFrame, index, etc
# TODO:
#     1) introduce pandas (pros/cons)        NOT DONE 
#     2) introduce Series                    DONE
#     3) introduce DataFrames                DONE
#     4) indexing                            NOT DONE
#     5) reindexing
#     x) dropping
#     x) selection/filtering
#     x) data alignment
#     x) functions: map, apply, applymap
#     x) ordering
#     x) summaries and calculations
#     x) missing data (fill/drop)
#     x) multilevel indexing
#     x)
#
# ===========================================================================

# <demo> auto
from pandas import Series, DataFrame
import pandas as pd
logs = pd.read_csv('../../log_file_1000.csv', names=['name',
                                                     'email',
                                                     'fm_ip',
                                                     'to_ip',
                                                     'date_time',
                                                     'lat',
                                                     'long',
                                                     'payload_size'])


# <demo> stop

# LIST:                               |  DICTIONARY:
# mylist = ['A', 'B', 'C']            |  mydict = ('alpha': 1,
#                                     |            'beta': 2,
#                                     |            'gamma': 2)
# indexable: mylisy[0] OR             | 
# sliceable: mylist[0:2] by integer   |  indexable by key:   mydict('alpha')

# ===========================================================================
# SERIES:
# myseries = Series(['bruce', 'selina', 'kara', 'clark])
#         column
# rows
# 0         'bruce'
# 1         'selina'
# 2         'kara'
# 'three'   'clark'

# indexable by row(s): myseries[0] OR myseries [0:3] OR myseries['three']

# ===========================================================================
# DATAFRAME:
# mydataframe = DataFrame(blah, blah, blah...)
#         col1      col2        col3      age
# rows
# 0       'bruce'   'wayne'     'M'       42
# 1       'selina'  'kyle'      'F'       34
# 'two'   'kara'    'zor-el'    'F'       27
# 3       'clark'   'kent'      'M'       35

# indexable by either row(s) or column(s) mydataframe['col1'] OR
#                                         mydataframe[['col1', 'age']]


# <demo> stop
from pandas import Series, DataFrame
import pandas as pd

s = Series([33, 37, 27, 42])

# <demo> stop
s.name = 'Justice League ages'
s.index = ['bruce', 'selina', 'kara', 'clark']

# <demo> stop
s1 = Series([37, 36, 10, 36],
            index=['hal', 'victor', 'diana', 'billy'],
            name='More Justice League ages')
s1

# <demo> stop
s1['billy']

# s1['diana'] = 32
# s1
# s1[s1 >= 35]
# s1*2
# s1
# s1[['diana', 'billy']]*20

# <demo> stop
'diana' in s1

# 'lex' in s1

# <demo> stop
names = {'bruce wayne': 'bwayne@jleague.org',
         'hal jordan': 'hjordan@jleague.org',
         'clark kent': 'ckent@jleague.org',
         'barry allen': 'ballen@jleague.org',
         'diana prince': 'dprince@jleague.org',
         'arthur curry': 'acurry@jleague.org',
         'billy batson': 'bbatson@jleague.org',
         'john jones': 'jjones@jleague.org',
         'victor stone': 'vstone@jleague.org',
         'dick grayson': 'dgrayson@jleague.org',
         'ray palmer': 'rpalmer@jleague.org',
         'dinah lance': 'dlance@jleague.org',
         'kara zor-el': 'kzor-el@jleague.org',
         'john constantine': 'jconstantine@jleague.org',
         'barbara gordon': 'bgordon@jleague.org',
         'kyle rayner': 'krayner@jleague.org',
         'selina kyle': 'skyle@jleague.org',
         'wally west': 'wwest@jleague.org'
         }

emails = Series(names)
# emails.index
# emails.values

# <demo> stop
s1 = Series(range(10, 16), index=['a', 'b', 'c', 'd', 'e', 'f'])
s2 = Series(range(16, 22), index=['a', 'b', 'c', 'x', 'y', 'z'])

# s1
# s2

# <demo> stop
s3 = s1 + s2
s1 + s2

# type(s3)
# pd.isnull(s3)
# s3.isnull()
# s3.<tab>
# 
# How do I learn more?
# s3.<method_name>?        # just ask by typing the method name (sans parenthesis) and 
#                          # adding a question mark to see the builtin help docs
# 
# s3.value_counts?
# s3.value_counts(dropna=False)

# <demo> stop
s3.dropna()

# s3

# <demo> stop
s4 = Series([42, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 5, 6])

# s4.unique()
# s4.value_counts()
# s4.max()
# s4 + 2

# <demo> stop
def transmogrifier(x):
    '''hat tip to Calvin and Hobbes for introducing me to this 
    truly fantastic word. thanks, bill watterson.

    "transform, especially in a surprising or magical manner."
    '''
    new_val = '- ' + str(x ** 3) + ' -'
    return new_val

s4.apply(transmogrifier)

# s4

# <demo> stop
# Making a DataFrame #1
# Using a dictionary

data = {'hero': ['billy', 'billy', 'billy', 'selina', 'selina'],
        'date': ['Jan 10', 'Jan 11', 'Jan 12', 'Jan 10', 'Jan 11'],
        'emails': [111, 121, 93, 211, 210]}

df = DataFrame(data)

# <demo> stop
df = DataFrame(data, columns=['date', 'hero', 'emails'])

# <demo> stop
df = DataFrame(data, columns=['date', 'hero', 'emails', 'instagrams'])

df.index = [1, 2, 3, 4, 5]

# df
# df.columns

# <demo> stop
# df['hero']
# df.hero

# df.ix[3]
# df.ix[3:4]
# df.ix[3:5]
# df.ix[1:5:2]


# <demo> stop
df.instagrams = 50
ins = Series([10, 20, 30], index=[1, 3, 5])

# df.instagrams = ins

# <demo> stop
df['overworked'] = df['emails'] >= 120

# <demo> stop
# Making a DataFrame #2
# Using a dictionary with nested dictionaries...

data = {'billy': {'Jan 10': 202, 'Jan 11': 220, 'Jan 12': 198},
        'selina': {'Jan 09': 246, 'Jan 10': 235, 'Jan 11': 243}}

df2 = DataFrame(data)
# df2.T
dft = df2.T


# <demo> stop
dft.columns.name = 'date'
dft.index.name = 'hero'

# <demo> stop
# using indexes
nums = Series(range(10, 16), index=['t', 'u', 'v', 'x', 'y', 'z'])
i = nums.index
# i
# i[2:4]
# i[::2]
# i[::3]
# i[4]

# <demo> stop
logs = pd.read_csv('../../log_file_1000.csv', names=['name',
                                                     'email',
                                                     'fm_ip',
                                                     'to_ip',
                                                     'date_time',
                                                     'lat',
                                                     'long',
                                                     'payload_size'])


# <demo> stop
logs.fm_ip.unique()

# logs.name.value_counts()
# logs.name.head()

# <demo> stop

g = logs.groupby(logs.fm_ip)

g.ngroups

# g.first()
# g.get_group('106.152.115.161')
# g.get_group('106.152.115.161').head(3)

# <demo> stop

logs.date_time.head()

# <demo> stop
def date_only(dt):
    day = dt.split('T')[0]
    return day

# <demo> stop

logs['date'] = logs.date_time.apply(date_only)

# <demo> stop
logs.columns

# tf = logs.fm_ip == logs.to_ip
# tf
# tf.unique()
# tf.value_counts()

# <demo> stop
