
# coding: utf-8

# # python hands-on session

# By: Ties de Kok  
# Version: Python 2.7 (see any notes for Python 3.5)

# 1. handling files
# 2. **data handling**
# 3. web scraping
# 4. text mining
# 5. (interactive) visualisations

# ## Introduction

# For the data handling part we will be using Python + Pandas.  
# What is `Pandas`?
# 
# > pandas is an open source, BSD-licensed library providing high-performance, easy-to-use  data structures and data analysis tools for the Python programming language.
# 
# In other words, whenever you want to use a datastructure with rows and columns, use `Pandas`!
# 
# A Pandas data object is called a `dataframe`.
# 
# 

# ## Format of this notebook

# The `Pandas` library is massive, it includes an enormous amount of functionality.  
# It is, therefore, impossible to cover everything in this notebook.  
# 
# PyCon 2015 (A Python conference) included a tutorial/talk by Brandon Rhodes.  
# This entire talk is available on YouTube and I think it is really great and I recommend watching it:  
# https://www.youtube.com/watch?v=5JnMutdy6Fw

# # Using pandas:

# ## Import Pandas

# In[1]:

import pandas as pd
import numpy as np


# *Note:* it is usually a good idea to also import `numpy` when you use `pandas`, their functionality is quite intertwined.  

# ## Create a dataframe

# ### Load file into Pandas

# To open a data file such as Excel, CSV, Stata, SAS, HDF see the first notebook.

# In[2]:

df_auto = pd.read_csv(r'auto_df.csv', sep=';', index_col='Unnamed: 0')


# **Create new dataframe and pass data to it**  
# We can pass many different types of data to the `pd.DataFrame()` method.

# In[3]:

d = {'col1': [1,2,3,4], 'col2': [5,6,7,8]}
df = pd.DataFrame(data=d)
df


# In[4]:

d = [(1, 2 ,3 ,4), (5, 6, 7, 8)]
df = pd.DataFrame(data=d)
df


# **Create dataframe from a dictionary**  
# We can also directly convert a dictionary to a dataframe:

# In[5]:

d = {'row1': [1,2,3,4], 'row2': [5,6,7,8]}
df = pd.DataFrame.from_dict(d, orient='index')
df


# ## Rename columns

# We can either manipulate `df.columns` directly or use `df.rename()`

# In[6]:

df.columns = ['col1', 'col2', 'col3', 'col4']
df


# In[7]:

df.rename(columns={'col1' : 'column1', 'col2' : 'column2'})


# **Note:** The above creates a copy, it does not modify it in place!  
# We need to use either the `inplace=True` argument or assign it:

# In[8]:

df = df.rename(columns={'col1' : 'column1', 'col2' : 'column2'})
#or
df.rename(columns={'col1' : 'column1', 'col2' : 'column2'}, inplace=True)


# ## Manipulate dataframe

# ### Add column

# In[9]:

df['col5'] = [10, 10]
df


# ### Add row

# In[10]:

df.loc['row3'] = [11, 12, 13, 14, 15]
df


# ### Inverse the dataframe

# In[11]:

df.T


# ### Remove column

# In[12]:

df = df.drop('col5', axis=1)
df


# ### Remove row

# In[13]:

df = df.drop('row1', axis=0)
df


# ### Set index

# In[14]:

df.set_index('column1')


# *Note:* `Pandas` also allows a multi-index. These can be very powerful. 

# In[15]:

df.set_index('column1', append=True)


# ## View a dataframe

# Something that requires getting used to is the fact that there is no build-in data browser for DataFrames.  
# 
# At some point you will get used to selecting the parts of the data that you want to see using Pandas.  
# However, in the mean time I will also provide a neat workaround that allows you to look at the data in a Notebook:  
# 
# We will use a package called `qgrid`: https://github.com/quantopian/qgrid --> `pip install qgrid`
# 
# First time you use it you have to run, in a notebook, the following code:  
# ```
# import qgrid
# qgrid.nbinstall(overwrite=True)
# ```
# 
# Using it is simple:

# In[16]:

from qgrid import show_grid


# In[17]:

show_grid(df_auto)


# **Several things to note:** 
# - If you save the notebook with these `qgrids` it is going to increase the file-size dramatically, it essentially saves the data with the notebook. Try to avoid this, use it only for inspection.
# - Opening very big dataframes using `show_grid()` is usually not a good idea.  
# - These `qgrids` will only display locally, not on GitHub. Therefore, if you see this on GitHub, you will not see the actual `qgrid`.
# - There are a bunch of options you can use with `show_grid()`, you can for example add `show_toolbar=True`.

# ## Select parts of the dataframe

# It is a very helpful skill to be able to quickly generate a view that you want.   

# ### View entire dataframe

# In[18]:

df_auto


# ### Get top or bottom of dataframe

# In[19]:

df_auto.head(3)


# In[20]:

df_auto.tail(3)


# ### Select columns based on name

# *Note:* If you want multiple columns you need to use double brackets.

# In[21]:

df_auto[['make', 'price', 'mpg']].head(10)


# ### Select columns based on position

# *Note:* In the example below the first `0:5` selects the first 5 rows.

# In[22]:

df_auto.iloc[0:5, 2:5]


# ### Select based on index value

# In[23]:

df = df_auto[['make', 'price', 'mpg', 'trunk', 'headroom']].set_index('make')


# In[24]:

df.loc['Buick Riviera']


# ### Select based on index position

# In[25]:

df.iloc[2:5]


# ### Select based on condition

# In[26]:

df_auto[ df_auto.price < 3800 ]


# In[27]:

df_auto[(df_auto.price < 3800) & (df_auto.foreign == 'Foreign')]


# **Note:** all the above return new dataframes that are removed if we do not assign them.  
# If we want to keep it as a separate dataframe we have to assign it like so:

# In[28]:

df_auto_small = df_auto[(df_auto.price < 3800) & (df_auto.foreign == 'Foreign')]
df_auto_small


# ### Sort dataframe

# In[29]:

df_auto.sort_values(by=['headroom', 'trunk'], inplace=True)
df_auto.head()


# ## Generate new columns from within a dataframe

# You often want to create a new column using values that are already in the dataframe. 

# ### Combine columns

# *Note:* You can select a column using:
# 1. `df_auto['price']`
# 2. `df_auto.price` --> but this one only works if there are no spaces in the column name

# In[30]:

df_auto['price_trunk_ratio'] = df_auto.price / df_auto.trunk
df_auto[['make', 'price', 'trunk', 'price_trunk_ratio']].head()


# ### Generate a column by iterating over the rows

# There are many different ways to iterate over rows.  
# They mainly different in their trade-off between ease-of-use and performance.  
# 
# I will demonstrate the methods I like to use, the example goal:  
# > If the car is a foreign brand, multiple the price by 1.5

# **Using a list comprehension:**

# In[31]:

df_auto['new_price'] = [p*1.5 if f == 'Foreign' else p for p, f in zip(df_auto.price, df_auto.foreign)]
df_auto[['make', 'price', 'foreign', 'new_price']].head()


# **Using `.apply()`**

# *Note:* `lambda` is a so-called anonymous function.

# In[32]:

df_auto['new_price'] = df_auto.apply(lambda x: x.price*1.5 if x.foreign == 'Foreign' else x.price, axis=1)
df_auto[['make', 'price', 'foreign', 'new_price']].head()


# **Using `.apply()` with a function**

# In the example above we use an anonymous `lambda` function.  
# For more complex processing it is possible to use a defined function and call it in `.apply()`  
# 
# **Personal note:** This method is in my opinion prefered as it is a lot easier to read.

# In[33]:

def new_price_function(x):
    if x.foreign == 'Foreign':
        return x.price * 1.5
    else:
        return x.price


# In[34]:

df_auto['new_price'] = df_auto.apply(new_price_function, axis=1)
df_auto[['make', 'price', 'foreign', 'new_price']].head()


# ## Group-by operations

# Pandas `.groupby()` allows us to:  
# 1. Compute a summary statistic about each group
# 2. Perform some group-specific computations
# 3. Filter based on groups
# 
# See: http://pandas.pydata.org/pandas-docs/stable/groupby.html

# ### Create a group object:

# In[35]:

col_list = ['price', 'mpg', 'headroom', 'trunk', 'weight', 'length']
grouped = df_auto[col_list + ['foreign']].groupby(['foreign'])


# ### Compute mean summary statistic:

# In[36]:

grouped.mean()


# ### Retrieve particular group:

# In[37]:

grouped.get_group('Domestic').head()


# ### Group specific iteration

# In[38]:

for name, group in grouped:
    print(name)
    print(group.head())


# ## Combining dataframes

# In[39]:

df_auto_p1 = df_auto[['make', 'price', 'mpg']]
df_auto_p2 = df_auto[['make', 'headroom', 'trunk']]


# In[40]:

df_auto_p1.head(3)


# In[41]:

df_auto_p2.head(3)


# ### Merge datasets

# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.merge.html  
# The `.merge()` function is one of my personal favorites, it is really easy to use.  

# In[42]:

merged_auto = pd.merge(df_auto_p1, df_auto_p2, how='left', on='make')
merged_auto.head(3)


# ### Join datasets on index

# In[43]:

df_auto_p1.set_index('make', inplace=True)
df_auto_p2.set_index('make', inplace=True)


# In[44]:

joined_auto = df_auto_p1.join(df_auto_p2)
joined_auto.reset_index().head(3)


# ### Append data to the dataframe

# See http://pandas.pydata.org/pandas-docs/stable/merging.html#concatenating-objects  
# 
# *Note:* There is also a shortcut function called `.append()`

# In[45]:

df_auto_i1 = df_auto.iloc[0:3]
df_auto_i2 = df_auto.iloc[3:6]


# In[46]:

df_auto_i1


# In[47]:

df_auto_i2


# Using the higher level function `concat()`:

# In[48]:

pd.concat([df_auto_i1, df_auto_i2])


# Using the shortcut fuction `append()`:

# In[49]:

df_auto_i1.append(df_auto_i2)


# ## Reshaping and Pivot Tables

# Pandas includes a variety of tools that allow you to reshape your DataFrame.  
# These tools are very powerful but can be a bit confusing to use. 

# ### Create some sample data:

# In[50]:

tuples = [('bar', 'one',   1, 2),
          ('bar', 'two',   3, 4),
          ('bar', 'three', 5, 6),
          ('baz', 'one',   1, 2),
          ('baz', 'two',   3, 4),
          ('baz', 'three', 5, 6),
          ('foo', 'one',   1, 2),
          ('foo', 'two',   3, 4),
          ('foo', 'three', 5, 6)
         ]
df = pd.DataFrame(tuples)
df.columns = ['first', 'second', 'A', 'B']


# In[51]:

df


# ### Create a pivot table:

# Using the `pivot()` function:  
# http://pandas.pydata.org/pandas-docs/stable/reshaping.html#reshaping-by-pivoting-dataframe-objects

# In[52]:

df.pivot(index='first', columns='second', values='A')


# Using the `pd.pivot_table()` function:  
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.pivot_table.html

# In[53]:

pd.pivot_table(df, values=['A', 'B'], index='first', columns='second')


# *Note* the above illustrates that Pandas essentially has two indexes: the usual 'row index' but also a 'column index'

# ### Stack and Unstack

# `Stack` and `Unstack` are higher level operators to reshape a dataframe based on a multi-level index.

# From the documentation:  
# >stack: “pivot” a level of the (possibly hierarchical) column labels, returning a DataFrame with an index with a new inner-most level of row labels.  
# unstack: inverse operation from stack: “pivot” a level of the (possibly hierarchical) row index to the column axis, producing a reshaped DataFrame with a new inner-most level of column labels.
# 
# http://pandas.pydata.org/pandas-docs/stable/reshaping.html#reshaping-by-stacking-and-unstacking
# 
# In other words:  
# **Stack** --> move the data "down"  
# **Unstack** --> move the data "up"

# ### Stack

# In[54]:

pivot_df = pd.pivot_table(df, values=['A', 'B'], index='first', columns='second')
pivot_df


# In[55]:

pivot_df.stack(level=['second'])


# *Note* We could also just use `pivot_df.stack()` as it will by default choose the 'last' level of the index.

# ### Unstack

# In[56]:

df.set_index(['first', 'second'], inplace=True)


# In[57]:

df


# In[58]:

df.unstack(level=['first'])


# In[59]:

df.unstack(level=['second'])


# ## Handling missing values

# http://pandas.pydata.org/pandas-docs/stable/missing_data.html

# ### Add missing values

# *Note:* We define a missing value as `np.nan` for convenience

# In[60]:

df_auto.loc['UvT_Car'] = [np.nan for x in range(0,len(df_auto.columns))]
df_auto.loc['UvT_Bike'] = [np.nan for x in range(0,len(df_auto.columns))]


# In[61]:

df_auto.loc[['UvT_Car', 'UvT_Bike']]


# ### Condition based on missing values

# Always use `pd.isnull()` or `pd.notnull()` as it is most reliable.  
# `df_auto.make == np.nan` will sometimes work but not always!

# In[62]:

df_auto[pd.isnull(df_auto.make)]


# In[63]:

df_auto[pd.notnull(df_auto.make)].head()


# ### Filling missing values

# To fill missing values with something we can use `.fillna()`

# In[64]:

df = df_auto.fillna('Missing')
df.loc[['UvT_Car', 'UvT_Bike']]


# ### Drop axis with missing values

# To drop missing values we can use `.dropna()`

# In[65]:

df_auto['make'].tail(3)


# In[66]:

df = df_auto.dropna(axis=0)
df['make'].tail(3)


# ## Changing datatypes

# ### Show current datatypes:

# In[67]:

df_auto.dtypes


# ### Convert datatypes

# The official function is called `.astype()`  

# In[68]:

df_auto['length'] = df_auto['length'].astype('str')
df_auto[['length']].dtypes


# In[69]:

df_auto['length'] = df_auto['length'].astype('float')
df_auto[['length']].dtypes


# ## Dates

# Pandas has a lot of build-in functionality to deal with timeseries data  
# http://pandas.pydata.org/pandas-docs/stable/timeseries.html
# 
# A nice overview from the documentation:

# | Class           | Remarks                        | How to create:                               |
# |-----------------|--------------------------------|----------------------------------------------|
# | `Timestamp`     | Represents a single time stamp | `to_datetime`, `Timestamp`                   |
# | `DatetimeIndex` | Index of `Timestamp`           | `to_datetime`, `date_range`, `DatetimeIndex` |
# | `Period`        | Represents a single time span  | `Period`                                     |
# | `PeriodIndex`   | Index of `Period`              | `period_range`, `PeriodIndex`                |

# ### Create a range of dates

# In[70]:

date_index = pd.date_range('1/1/2011', periods=len(df_auto.index), freq='D')
date_index[0:5]


# For the sake of illustration, let's add these dates to our `df_auto`:

# In[71]:

df_ad = df_auto.copy()[['make', 'price']]
df_ad['date'] = date_index


# In[72]:

df_ad.head()


# In[73]:

df_ad.dtypes


# ### Select observation that fall within a certain range

# In[74]:

pd.Timestamp('2011-02-01')


# In[75]:

pd.to_datetime('01-02-2011', format='%d-%m-%Y')


# *Note:* it is usually a good idea to explicitly include the format, to avoid unexpected behavior

# In[76]:

df_ad[df_ad.date > pd.to_datetime('07-03-2011', format='%d-%m-%Y')]


# We can also use the Pandas `.isin()` to use a `date_range` object instead

# In[77]:

df_ad[df_ad.date.isin(pd.date_range('2/20/2011', '3/11/2011', freq='D'))]


# ### Select components of the dates

# See: http://pandas.pydata.org/pandas-docs/stable/timeseries.html#time-date-components

# In[78]:

df_ad['day'] = [x.day for x in df_ad['date']]
df_ad.head()


# ### Manipulate (off-set) the date

# See: http://pandas.pydata.org/pandas-docs/stable/timeseries.html#dateoffset-objects  
# 
# You can even take into consideration stuff like business days / hours, holidays etc.!

# In[79]:

df_ad['new_date'] = df_ad.date.apply(lambda x: x + pd.DateOffset(years=1))
df_ad.head()

