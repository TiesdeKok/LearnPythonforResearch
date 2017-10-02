
# coding: utf-8

# # Handling data with python

# **Author:** Ties de Kok ([Personal Website](www.tiesdekok.com]))  
# **Last updated:** 29 Sep 2017  
# **Python version:** Python 3.5  
# **License:** MIT License  

# # *Introduction*

# Getting your data ready for analysis (i.e. "data wrangling") is usually the most time-consuming part of a project. For data wrangling tasks I recommend `Pandas` and `Numpy`.
# 
# What is `Pandas`?
# 
# > Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use  data structures and data analysis tools for the Python programming language.
# 
# In other words, Pandas introduces a datastructure (i.e. `dataframe`) that represents data as a table with columns and rows. Combining Python with `Pandas` yields a very powerful toolkit with which you can process any type of data. 

# ## Format of this notebook

# The `Pandas` library is massive and it is continously expanding in functionality.  
# It is, therefore, impossible to keep it both comprehensive and cover everything in just one notebook.
# 
# The goal of this notebook is to cover the basic functionality that I expect you to encouter for an average project. 
# 
# I have based parts on this notebook on a PyCon 2015 tutorial/talk by Brandon Rhodes. If you want to know more I highly recommend watching his talk and checking the accompanying GitHub page:
#   
# https://www.youtube.com/watch?v=5JnMutdy6Fw  
# https://github.com/brandon-rhodes/pycon-pandas-tutorial

# # *Table of Contents* <a name='toc'></a>

# |   |
# |---|
# |<h2 style="text-align:center">[Import pandas](#import-pandas)</h2>|
# |<h2 style="text-align:center">[Create a dataframe](#create-dataframe)</h2>|
# |<h2 style="text-align:center"> [Manipulate dataframe](#manipulate-dataframe)  </h2>|
# |<h2 style="text-align:center"> [Rename columns](#rename-columns)  </h2>|
# |<h2 style="text-align:center"> [View a dataframe using qgrid](#qgrid)  </h2>|
# |<h2 style="text-align:center"> [View (parts) of a dataframe using Pandas](#view-dataframe)  </h2>|
# |<h2 style="text-align:center"> [Dealing with datatypes](#datatypes)</h2>|
# |<h2 style="text-align:center"> [Handling missing values](#missing-values) </h2>|
# |<h2 style="text-align:center"> [Work with data in the dataframe](#work-with-data)</h2>|
# |<h2 style="text-align:center"> [Combining dataframes](#combining-dataframes)  </h2>|
# |<h2 style="text-align:center"> [Group-by operations](#groupby)</h2>|
# |<h2 style="text-align:center"> [Reshaping and Pivot Tables](#reshaping-pivot)  </h2>|
# |<h2 style="text-align:center"> [Dealing with dates](#dates)    </h2>|

# ## <u>Import Pandas</u><a name='import-pandas'></a> [(to top)](#toc)

# In[1]:

import pandas as pd
import numpy as np


# *Note:* it is usually a good idea to also import `numpy` when you use `pandas`, their functionality is quite intertwined.  

# For convenience we also import `join` to easily create paths:

# In[2]:

import os
from os.path import join


# ### Parameters

# Path to our data

# In[3]:

data_path = join(os.getcwd(), 'example_data')


# ##  <u>Create a dataframe</u><a name='create-dataframe'></a> [(to top)](#toc)

# We can create a dataframe in many ways. Below are a couple of situations:

# ### 1) Load file from drive into Pandas

# For details on opening files such as Excel, CSV, Stata, SAS, HDF see the `1_opening_files` notebook.

# In[4]:

df_auto = pd.read_csv(join(data_path, 'auto_df.csv'), sep=';', index_col='Unnamed: 0')


# ### 2) Create new dataframe and pass data to it

# We can pass many different types of data to the `pd.DataFrame()` method.

# In[5]:

d = {'col1': [1,2,3,4], 'col2': [5,6,7,8]}
df = pd.DataFrame(data=d)
df


# In[6]:

d = [(1, 2 ,3 ,4), (5, 6, 7, 8)]
df = pd.DataFrame(data=d)
df


# ### 3) Create dataframe from a dictionary

# We can also directly convert a dictionary to a dataframe:

# In[7]:

d = {'row1': [1,2,3,4], 'row2': [5,6,7,8]}
df = pd.DataFrame.from_dict(d, orient='index')
df


# ## <u>Manipulate dataframe</u><a name='manipulate-dataframe'></a> [(to top)](#toc)

# ### Add column

# In[8]:

df['col5'] = [10, 10]
df


# ### Add row

# In[9]:

df.loc['row3'] = [11, 12, 13, 14, 15]
df


# ### Inverse the dataframe

# In[10]:

df.T


# ### Remove column

# In[11]:

df = df.drop('col5', axis=1)
df


# ### Remove row

# In[12]:

df = df.drop('row1', axis=0)
df


# ### Set index

# In[14]:

df


# In[15]:

df.set_index(0)


# *Note:* `Pandas` also allows a multi-index. These can be very powerful. 

# In[16]:

df.set_index(0, append=True)


# ### Reset index

# We can convert the index to a regular column using `reset_index()`

# In[17]:

df.reset_index()


# ## <u>Rename columns</u><a name='rename-columns'></a> [(to top)](#toc)

# We can either manipulate `df.columns` directly or use `df.rename()`

# In[18]:

df.columns = ['col1', 'col2', 'col3', 'col4']
df


# In[19]:

df.rename(columns={'col1' : 'column1', 'col2' : 'column2'})


# **Note:** The above creates a copy, it does not modify it in place!  
# We need to use either the `inplace=True` argument or assign it:

# In[20]:

df = df.rename(columns={'col1' : 'column1', 'col2' : 'column2'})
#or
df.rename(columns={'col1' : 'column1', 'col2' : 'column2'}, inplace=True)


# ## <u>View a dataframe using `qgrid`</u><a name='qgrid'></a> [(to top)](#toc)

# Something that requires getting used to is the fact that there is no build-in data browser for DataFrames.  
# 
# The primary workflow for inspecting parts of the data is to just create a new temporary dataframe with the data that you want to see. This is fairly quick once you get used to it, but in the beginning it can feel cumbersome. 
# 
# A neat workaround for beginners is to use a package called `qgrid` to quickly inspect your data:  
# 
# This is the GitHub page for `qgrid`: https://github.com/quantopian/qgrid  
# You can install it by running `pip install qgrid` in your command line. 
# 
# First time you use it you have to run, in a notebook, the following code:  
# ```
# import qgrid
# qgrid.nbinstall(overwrite=True)
# ```
# 
# Using it is simple:

# **First make sure you import the `show_grid` function**

# In[21]:

from qgrid import show_grid


# **You can inspect a Dataframe as follows:**

# In[22]:

show_grid(df_auto)


# **Several things to note about qgrid:** 
# - If you save the notebook with these `qgrids` it is going to increase the file-size dramatically, it essentially saves the data with the notebook. Try to avoid this, use it only for inspection.
# - Opening very big dataframes using `show_grid()` is not a good idea.  
# - These `qgrids` will only display locally, not on GitHub. Therefore, if you see this on GitHub, you will not see the actual `qgrid`.
# - There are a bunch of options you can use with `show_grid()`, you can for example add `show_toolbar=True`.

# ## <u>View (parts) of a dataframe using `Pandas`</u><a name='view-dataframe'></a> [(to top)](#toc)

# Using `qgrid` is a good first start, but it is a very helpful skill to be able to sub-select parts of a dataframe (not only for inspection purposes but also for analysis, exporting parts of the data, and much more). 

# ### View entire dataframe

# *Note:* Pandas will only show the top and bottom parts if the dataframe is large.

# In[23]:

df_auto


# ### Get top or bottom of dataframe

# In[24]:

df_auto.head(3)


# In[25]:

df_auto.tail(3)


# ### Get an X amount of random rows

# In[26]:

X = 5
df_auto.sample(X)


# ### Select column(s) based on name

# *Note:* the below returns a pandas `Series` object, this is different than a pandas `Dataframe` object!   
# You can tell by the way that it looks when shown.

# In[27]:

df_auto['make'].head(3)


# If the column name has no whitespace you can also use a dot followed with the column name:

# In[28]:

df_auto.make.head(3)


# **If you want multiple columns you need to use double brackets:**

# In[29]:

df_auto[['make', 'price', 'mpg']].head(10)


# ### Select  row based on index value

# In[30]:

df = df_auto[['make', 'price', 'mpg', 'trunk', 'headroom']].set_index('make')


# In[31]:

df.loc['Buick Riviera']


# *Note:* notice the appearance, this returned a pandas.Series object not a pandas.Dataframe object 

# ### Select row based on index position

# In[32]:

df.iloc[2:5]


# **You can also include columns based on their column (!) index position:**

# In[33]:

df.iloc[2:5, 1:3]


# *Note:* In the example above the first `0:3` selects the first 3 rows, the second `1:3` selects the 2nd and 3rd column.

# ### Select based on condition

# In many cases you want to filter rows based on a condition. You can do this in Pandas by putting the condition inside square brackets.  
# 
# It is worth explaining the intuition behind this method as a lot of people find it confusing:  
# 
# 1. You request Pandas to filter a dataframe by putting a condition between square brackets: df[ `condition` ] 
# 2. The `condition` is a sequence of `True` or `False` values for each row (so the lenght of the `condition` always has to match the number of rows in the dataframe!)
# 3. In Pandas you can generate a `True` or `False` value for each row by simply writing a boolean expression on the whole column. 
# 4. Pandas will then only show those rows where the value is `True`
# 
# In more practical terms:
# 
# `df_auto['price'] < 3800` will evaluate each row of `df_auto['price']` and return, for that row, whether the condition is `True` or `False`:
# 
# ``
# 0     False
# 1     False
# 2      True
# 3     False
# 4     False
# 5     False
# ``
# 
# By putting that condition in square brackets `df_auto[ df_auto['price'] < 3800 ]` pandas will first generate a sequence of `True` / `False` values and then only display the rows for which the value is `True`.

# In[34]:

df_auto[ df_auto['price'] < 3800 ]


# We can also combine multiple conditions by just chaining the boolean expression.   
# 
# * For an **AND** statement use: `&`
# * For an **OR** statement use: `|`

# In[35]:

df_auto[(df_auto['price'] < 3800) & (df_auto['foreign'] == 'Foreign')]


# **Note:** all the above return new dataframes that are removed if we do not assign them.  
# If we want to keep it as a separate dataframe we have to assign it like so:

# In[36]:

df_auto_small = df_auto[(df_auto.price < 3800) & (df_auto.foreign == 'Foreign')]
df_auto_small


# ### Sort dataframe

# In[37]:

df_auto.sort_values(by=['headroom', 'trunk'], inplace=True)
df_auto.head()


# ## <u>Dealing with datatypes</u><a name='datatypes'></a> [(to top)](#toc)

# It is important to pay attention to the datatypes contained in a column. A lot of errors that you will encounter relate to wrong datatypes (e.g. because of data errors)

# ### Show current datatypes:

# In[67]:

df_auto.dtypes


# ### Convert datatypes

# We can convert the datatype of a column in two ways:  
# 
# 1. Loop over the values and convert them individually
# 2. Use the buildin Pandas functions to convert the column in one go

# *1) Convert values individually*

# In[61]:

df_auto['length'].apply(lambda x: str(x)).dtypes


# Note: `'O'` stands for 'object'

# In[62]:

df_auto['length'].apply(lambda x: int(x)).dtypes


# *2) Convert column directly*

# If you want to convert a column to `string` I recommend to use `.astype(str)`:

# In[65]:

df_auto['length'].astype(str).dtypes


# If you want to convert a column to `numeric` I recommend to use `df.to_numeric()`:

# In[68]:

pd.to_numeric(df_auto['length']).dtypes


# The section `dealing with dates` will discuss how to convert a column with `dates`.

# ## <u>Handling missing values</u><a name='missing-values'></a> [(to top)](#toc)

# Dealing with missing values is easy in Pandas, as long as you are careful in defining them as `np.nan` (and **not** a string value like 'np.nan')

# http://pandas.pydata.org/pandas-docs/stable/missing_data.html

# ### Add some missing values

# *Note:* We define a missing value as `np.nan` so we can consistently select them!

# In[60]:

df_auto.loc['UvT_Car'] = [np.nan for x in range(0,len(df_auto.columns))]
df_auto.loc['UvT_Bike'] = [np.nan for x in range(0,len(df_auto.columns))]


# In[61]:

df_auto.loc[['UvT_Car', 'UvT_Bike']]


# ### Select missing or non-missing values

# Always use `pd.isnull()` or `pd.notnull()` as it is most reliable.  
# `df_auto.make == np.nan` will **not** work consistently.

# In[62]:

df_auto[pd.isnull(df_auto.make)]


# In[63]:

df_auto[pd.notnull(df_auto.make)].head()


# ### Fill missing values

# To fill missing values with something we can use `.fillna()`

# In[64]:

df = df_auto.fillna('Missing')
df.loc[['UvT_Car', 'UvT_Bike']]


# ### Drop rows with missing values

# To drop missing values we can use `.dropna()`

# In[65]:

df_auto['make'].tail(3)


# In[66]:

df = df_auto.dropna(axis=0)
df['make'].tail(3)


# ## <u>Work with data in the dataframe</u><a name='work-with-data'></a> [(to top)](#toc)

# ### Combine columns (and output it to a new column)

# *Remember:* You can select a column using:
# 1. `df_auto['price']`
# 2. `df_auto.price` --> but this one only works if there are no spaces in the column name

# In[38]:

df_auto['price_trunk_ratio'] = df_auto.price / df_auto.trunk
df_auto[['price', 'trunk', 'price_trunk_ratio']].head()


# ### Generate a new column by iterating over the dataframe per row

# There are multiple ways to iterate over rows.  
# They mainly different in their trade-off between ease-of-use, readability, and performance.  
# 
# I will show the three main possibilities.
# 
# For the sake of demonstration, let's say our goal is to achieve the following:    
# > If the car is a foreign brand, multiple the price by 1.5

# **Option 1: use a list comprehension:**

# In[39]:

df_auto['new_price'] = [p*1.5 if f == 'Foreign' else p for p, f in zip(df_auto.price, df_auto.foreign)]
df_auto[['price', 'foreign', 'new_price']].sample(5, random_state=1)


# *Note:* `random_state=1` makes sure that we get the same random sample every time we run it

# **Option 2: use `.apply()` with `lambda`**

# *Note:* `lambda` is a so-called anonymous function.

# In[40]:

logic = lambda x: x.price*1.5 if x.foreign == 'Foreign' else x.price
df_auto['new_price'] = df_auto.apply(logic, axis=1)
df_auto[['make', 'price', 'foreign', 'new_price']].head()


# **Option 3: use `.apply()` with a function**

# In the example above we use an anonymous `lambda` function.  
# For more complex processing it is possible to use a defined function and call it in `.apply()`  
# 
# **Personal note:** This is often my preferred method as it is the most flexible and a lot easier to read.

# In[41]:

def new_price_function(x):
    if x.foreign == 'Foreign':
        return x.price * 1.5
    else:
        return x.price


# In[42]:

df_auto['new_price'] = df_auto.apply(new_price_function, axis=1)
df_auto[['make', 'price', 'foreign', 'new_price']].head()


# *Note:* make sure to include the `axis = 1` argument, this tells Pandas to iterate over the rows and not the columns.

# ## <u name='combining-dataframes'>Combining dataframes</u><a name='combining-dataframes'></a> [(to top)](#toc)

# You can combine dataframes in three ways:
# 
# 1. Merge
# 2. Join
# 3. Append

# I will demonstrate that using the following two datasets:

# In[39]:

df_auto_p1 = df_auto[['make', 'price', 'mpg']]
df_auto_p2 = df_auto[['make', 'headroom', 'trunk']]


# In[40]:

df_auto_p1.head(3)


# In[41]:

df_auto_p2.head(3)


# ### 1) Merge datasets

# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.merge.html  
# The `.merge()` function is one of my personal favorites, it is really easy to use.  

# In[42]:

merged_auto = pd.merge(df_auto_p1, df_auto_p2, how='left', on='make')
merged_auto.head(3)


# ### 2) Join datasets on index

# Both dataframes need to have the same column set as the index

# In[43]:

df_auto_p1.set_index('make', inplace=True)
df_auto_p2.set_index('make', inplace=True)


# In[44]:

joined_auto = df_auto_p1.join(df_auto_p2)
joined_auto.reset_index().head(3)


# ### 3) Append data to the dataframe

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


# ## <u>Group-by operations</u><a name='groupby'></a> [(to top)](#toc)

# Often you want to perform an operation within a group, in Pandas you achieve this by using `.groupby()`.
# 
# Pandas `.groupby()` is a process involving one or more of the following steps (paraphrasing from the docs):  
# 1. **Splitting** the data into groups based on some criteria
# 2. **Applying** a function to each group independently
# 3. **Combining** the results into a data structure
# 
# For the full documentation see: http://pandas.pydata.org/pandas-docs/stable/groupby.html

# ### Split the dataframe by creating a group object:

# Step 1 is to create a `group` object that specifies the groups that we want to create.

# In[43]:

col_list = ['price', 'mpg', 'headroom', 'trunk', 'weight', 'length']
grouped = df_auto[col_list + ['foreign']].groupby(['foreign'])


# After creating a `group` object we can apply operations to it

# ### Applying example 1) Compute mean summary statistic

# In[44]:

grouped.mean()


# ### Applying example 2) Retrieve particular group:

# In[45]:

grouped.get_group('Domestic').head()


# ### Applying example 3) Iterate over the groups in the `group` object

# By iterating over each group you get a lot of flexibility as you can do anything you want with each group.   
# 
# It is worth noting that each group is a dataframe object.

# In[38]:

for name, group in grouped:
    print(name)
    print(group.head())


# It is also possible to use the `.apply()` function on `group` objects:

# In[57]:

grouped.apply(lambda x: x.describe())


# ### Aggregate groupby object to new dataframe

# If you want to aggregate each group to one row in the new dataframe you have many options, below a couple of examples:

# ### 1) `grouped.sum()` and `grouped.mean()`
# 

# In[49]:

grouped.sum()


# In[50]:

grouped.mean()


# ### 2) `grouped.count()` and `grouped.size()`

# In[51]:

grouped.count()


# In[54]:

grouped.size()


# ### 3) `grouped.first()` and `grouped.last()`

# In[52]:

grouped.first()


# In[53]:

grouped.last()


# ** 4) You can also use the `.agg()` function to perform multiple operations**

# In[56]:

grouped.agg([np.sum, np.mean, np.std])


# ### And a lot of other operations!

# There are many-many more things you can do with Pandas `.groupby`, too much to show here.  
# Feel free to check out the comprehensive documentation:  
# https://pandas.pydata.org/pandas-docs/stable/groupby.html

# ## <u>Reshaping and Pivot Tables</u><a name='reshaping-pivot'></a> [(to top)](#toc)

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


# ### Example 1) Create a pivot table:

# Using the `pivot()` function:  
# http://pandas.pydata.org/pandas-docs/stable/reshaping.html#reshaping-by-pivoting-dataframe-objects

# In[52]:

df.pivot(index='first', columns='second', values='A')


# Using the `pd.pivot_table()` function:  
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.pivot_table.html

# In[53]:

pd.pivot_table(df, values=['A', 'B'], index='first', columns='second')


# *Note 1:* the above illustrates that Pandas essentially has two indexes: the usual 'row index' but also a 'column index'  
# *Note 2:* pandas also has an "unpivot" function called `pandas.melt` (https://pandas.pydata.org/pandas-docs/stable/generated/pandas.melt.html)

# ### Example 2: Stack and Unstack

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


# ## <u>Dealing with dates</u><a name='dates'></a> [(to top)](#toc)

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

# In[69]:

date_index = pd.date_range('1/1/2011', periods=len(df_auto.index), freq='D')
date_index[0:5]


# For the sake of illustration, let's add these dates to our `df_auto`:

# In[70]:

df_ad = df_auto.copy()[['make', 'price']]
df_ad['date'] = date_index


# In[71]:

df_ad.head()


# In[73]:

df_ad.dtypes


# **Converting a `str` column to a `date` column**

# In many cases you import data but it is not recognized as a date column. 
# 
# Let's 'sabotage' our date column and convert it to strings:
# 

# In[80]:

df_ad['date'] = df_ad['date'].astype(str)
df_ad['date'].dtypes


# We cannot perform any `datetime` operations on the column now because it has the wrong datatype!  
# 
# Luckily we can fix it as such:

# In[82]:

pd.to_datetime(df_ad['date']).dtypes


# Or

# In[85]:

df_ad['date'] = df_ad['date'].apply(lambda x: pd.to_datetime(x))


# ### Select observation that fall within a certain range

# In[86]:

pd.Timestamp('2011-02-01')


# In[87]:

pd.to_datetime('01-02-2011', format='%d-%m-%Y')


# *Note:* it is usually a good idea to explicitly include the format, to avoid unexpected behavior

# In[88]:

df_ad[df_ad.date > pd.to_datetime('07-03-2011', format='%d-%m-%Y')]


# We can also use the Pandas `.isin()` to use a `date_range` object instead

# In[89]:

df_ad[df_ad.date.isin(pd.date_range('2/20/2011', '3/11/2011', freq='D'))]


# ### Select components of the dates

# You can extract, for example: `day`, `month`, `year`

# See: http://pandas.pydata.org/pandas-docs/stable/timeseries.html#time-date-components

# In[90]:

df_ad['day'] = df_ad['date'].apply(lambda x: x.day)
df_ad.head()


# ### Manipulate (off-set) the date

# See: http://pandas.pydata.org/pandas-docs/stable/timeseries.html#dateoffset-objects  
# 
# You can even take into consideration stuff like business days / hours, holidays etc.!

# In[91]:

df_ad['new_date'] = df_ad.date.apply(lambda x: x + pd.DateOffset(years=1))
df_ad.head()

