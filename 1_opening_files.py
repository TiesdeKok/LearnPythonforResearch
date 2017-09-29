
# coding: utf-8

# # opening files with python

# **Author:** Ties de Kok ([Personal Website](www.tiesdekok.com]))  
# **Last updated:** 29 Sep 2017  
# **Python version:** Python 3.5  
# **License:** MIT License  

# # Instruction

# With Python you can open and save a wide variety of files.  
# There are often multiple ways to open a particular file format, the examples below are in my experience the most convenient
# 
# **Note:** All the sample files are in the `example_data` folder. The code to generate these files is at the end of this notebook.

# ## Imports

# In[1]:

import os
import pandas as pd
from glob import glob
import json


# The below is for convenience so we can type `join` instead of `os.path.join`

# In[2]:

from os.path import join


# ## Indexing a folder

# Irrespective of the type of file you are trying to open it is useful to be able to index all files in a folder.  
# This is nescessary if you, for example, want to loop over all files in a folder.

# There are multiple ways to go about this, but I will show `os.listdir`, `glob`, and `os.walk`.

# ### First define the path to the folder that we want to index

# Our examples files are in the `example_data` folder so we can set the directory as such:

# In[19]:

data_path = join(os.getcwd(), 'example_data')


# ### Get all the files in the root of the folder

# *Note:* this will ignore files in sub-folders!

# In[4]:

filenames = os.listdir(data_path)
filenames[:2] # show first two items


# In[5]:

filepaths = [join(data_path, filename) for filename in filenames]
filepaths[:2] # show first two items


# We can alternatively use `glob` as this directly allows to include pathname matching.  
# For example if we only want Excel `.xlsx` files:

# In[6]:

glob(join(data_path, '*.xlsx'))


# ### Get all files, also those in sub-folders:

# If the folder contains multiple levels we need to either use `os.walk()` or `glob`:

# In[12]:

folder = os.getcwd()
filepaths = []
for root,dirs,files in os.walk(folder):
    for i in files:
        filepaths.append(join(root,i))
filepaths[:2]


# Personally, using `glob` yields cleaner code although it is a bit harder to understand:

# In[16]:

filepaths_glob = glob(join(folder, '**/*'), recursive=True)
filepaths_glob[:2]


# ## Text files

# Opening text files is done using the default Python library.

# You can open a file with different file modes:  
# w -> write only  
# r -> read only  
# w+ -> read and write + completely overwrite file  
# a+ -> read and write + append at the bottom  

# ### Opening a file

# In[28]:

with open(join(data_path, 'text_sample.txt'), 'r') as file:
    file_content = file.read()


# In[29]:

print(file_content)


# ### Writing to a file

# In[33]:

with open(join(data_path, 'text_sample.txt'), 'w+') as file:
    file.write('Learning Python is great. \nGood luck!')


# ### Additional information

# Note that I am using a `with` statement when opening files.  
# Another method is to use `open` and `close`:

# In[34]:

f = open(join(data_path, 'text_sample.txt'), 'r')
file_content = f.read()
f.close()


# The `with` method is prefered as it automatically closes the file.  
# This prevents the file from being 'in use' if you forget to use `.close()`

# ### Looping over indexed files

# In[36]:

text_files = glob(join(data_path, '*.txt'))
text_list = []

for i in text_files:
    with open(i, 'r') as f:
        text_list.append(f.read())


# In[37]:

text_list


# ## Excel files

# You can open `Excel`, `csv`, `Stata`, `SAS` files in multiple ways, I like to use `Pandas` as it is the most convenient. 

# ### Open Excel file

# In[38]:

excel_file = pd.read_excel(join(data_path, 'excel_sample.xlsx'))


# This function has a lot of options, see:  
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_excel.html  
# 
# *Note:* You often want to specify the encoding to prevent errors, for example: `, encoding='utf-8'`

# ### Save Excel file

# In[40]:

excel_file.to_excel(join(data_path, 'excel_sample.xlsx'))


# This saves a `Pandas` dataframe object, see the data handling file.  
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_excel.html  
# 
# *Note:* You can save as `.xls` but also `.xlsx`

# ## CSV files

# You can open `Excel`, `csv`, `Stata`, `SAS` files in multiple ways, I like to use `Pandas` as it is the most convenient. 

# ### Open CSV file

# In[41]:

csv_file = pd.read_csv(join(data_path, 'csv_sample.csv'), sep=',')


# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_csv.html

# ### Save CSV file

# In[42]:

csv_file.to_csv(join(data_path, 'csv_sample.csv'), sep=',')


# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_csv.html

# ## Stata files

# ### Open Stata file

# In[43]:

stata_file = pd.read_stata(join(data_path, 'stata_sample.dta'))


# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_stata.html  

# ### Save Stata file

# In[44]:

stata_file.to_stata(join(data_path, 'stata_sample.dta'))


# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_stata.html

# *Note: make sure you have the latest version of Pandas for new Stata versions*

# ## SAS files

# Pandas can only read SAS files but cannot write them:  
# 
# ```
# sas_file = pd.read_sas(r'C:\file.sas7bdat', format='sas7bdat')
# ```

# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_sas.html  
# This function works in most cases but files with text are likely to throw hard to fix encoding errors.

# ## JSON files using pandas

# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_json.html  
# 
# *Note:* The path can also be a url

# ### Read JSON file to dataframe

# In[45]:

json_df = pd.read_json(join(data_path, 'json_sample.json'))


# ### Save dataframe to JSON file

# In[49]:

json_df.to_json(join(data_path, 'json_sample.json'))


# ## JSON files using the `JSON` module

# **Read:**

# In[52]:

with open(join(data_path, 'json_sample.json'), 'r') as f:
    json_data = json.load(f)


# **Write:**

# In[51]:

with open(join(data_path, 'json_sample.json'), 'w') as f:
    json.dump(json_data, f)


# ## HDF files

# You often run into the problem of having to store large amounts of data.  
# The traditional formats such as .csv are not very efficient as big-data file formats.  
# 
# I like to use the `Hierarchical Data Format` or `HDF` in short.
# This `.hdf` file format is designed to store and organize large amounts of data. 
# 
# Writing and reading `.hdf` files is extremely fast compared to `.csv`:
# 
# **Writing:**
# 
# ```
# %timeit test_hdf_fixed_write(df)
# 1 loops, best of 3: 237 ms per loop
# 
# %timeit test_hdf_table_write(df)
# 1 loops, best of 3: 901 ms per loop
# 
# %timeit test_csv_write(df)
# 1 loops, best of 3: 3.44 s per loop
# ```
# 
# **Reading:**
# 
# ```
# %timeit test_hdf_fixed_read()
# 10 loops, best of 3: 19.1 ms per loop
# 
# %timeit test_hdf_table_read()
# 10 loops, best of 3: 39 ms per loop
# 
# %timeit test_csv_read()
# 1 loops, best of 3: 620 ms per loop
# ```

# ### Read HDF files using Pandas

# In[54]:

hdf_df = pd.read_hdf(join(data_path, 'hdf_sample.h5'), 'hdf_sample') # Second argument is the key


# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_hdf.html  
# 
# *Note*: You can give it any `key` you like. I always use the filename without `.h5` as `key`

# ### Write HDF files using Pandas

# In[55]:

hdf_df.to_hdf(join(data_path, 'hdf_sample.h5'), 'hdf_sample')


# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_hdf.html

# ### Using HDF with big data that does not fit into memory

# One big advantage of `HDF` is that it does not require all the data to be load into memory at once. 
# 
# See the page below for a very comprehensive overview:  
# http://pandas.pydata.org/pandas-docs/stable/io.html#io-hdf5

# # Code to generate examples files

# Dictionary with random data:

# In[19]:

raw_data = {'foreign':{1:'Domestic',2:'Domestic',3:'Domestic',6:'Domestic',7:'Domestic',8:'Domestic',9:'Domestic',14:'Domestic',21:'Domestic',23:'Domestic',24:'Domestic',30:'Domestic',31:'Domestic',33:'Domestic',37:'Domestic',38:'Domestic',43:'Domestic',48:'Domestic',50:'Domestic',51:'Domestic',53:'Foreign',56:'Foreign',57:'Foreign',66:'Foreign',70:'Foreign'},
            'make':{1:'AMCPacer',2:'AMCSpirit',3:'BuickCentury',6:'BuickOpel',7:'BuickRegal',8:'BuickRiviera',9:'BuickSkylark',14:'Chev.Impala',21:'DodgeMagnum',23:'FordFiesta',24:'FordMustang',30:'Merc.Marquis',31:'Merc.Monarch',33:'Merc.Zephyr',37:'OldsDelta88',38:'OldsOmega',43:'Plym.Horizon',48:'Pont.GrandPrix',50:'Pont.Phoenix',51:'Pont.Sunbird',53:'AudiFox',56:'Datsun210',57:'Datsun510',66:'ToyotaCelica',70:'VWDiesel'},
            'price': {1:4749,2:3799,3:4816,6:4453,7:5189,8:10372,9:4082,14:5705,21:5886,23:4389,24:4187,30:6165,31:4516,33:3291,37:4890,38:4181,43:4482,48:5222,50:4424,51:4172,53:6295,56:4589,57:5079,66:5899,70:5397},
            'weight':{1:3350,2:2640,3:3250,6:2230,7:3280,8:3880,9:3400,14:3690,21:3600,23:1800,24:2650,30:3720,31:3370,33:2830,37:3690,38:3370,43:2200,48:3210,50:3420,51:2690,53:2070,56:2020,57:2280,66:2410,70:2040}}


# Convert dictionary to Pandas dataframe for easy saving

# In[20]:

df_data = pd.DataFrame(raw_data)
df_data.head()


# Save the different files

# In[ ]:

data_path = os.path.join(os.getcwd(), 'example_data')


# In[22]:

with open(os.path.join(data_path, 'text_sample.txt'), 'w+') as file:
    file.write('Learning Python is great. \nGood luck!')


# In[32]:

df_data.to_excel(os.path.join(data_path, 'excel_sample.xlsx'))
df_data.to_csv(os.path.join(data_path, 'csv_sample.csv'))
df_data.to_stata(os.path.join(data_path, 'stata_sample.dta'))
df_data.to_hdf(os.path.join(data_path, 'hdf_sample.h5'), 'hdf_sample')


# In[33]:

df_data.to_json(os.path.join(data_path, 'json_sample.json'))


# **Note:** pandas does not have a `.to_sas` function
