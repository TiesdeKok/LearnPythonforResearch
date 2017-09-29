
# coding: utf-8

# # python basics ("cheatsheet")

# **Author:** Ties de Kok ([Personal Website](www.tiesdekok.com]))  
# **Last updated:** 29 Sep 2017  
# **Python version:** Python 3.5  
# **License:** MIT License  

# This notebook contains an overview of basic Python functionality that you might come across using Python for Social Science Research.   
# The contents of this cheatsheet yield all the nescessary building blocks to use Python for basic programming.  
# 
# **Note:** this cheat sheet is purposely not 100% comprehensive, it only discusses the basic things you need to get started.

# ## Variables

# Basic numeric types in Python are `int` for integers and `float` for floating point numbers.  
# Strings are represented by `str`, in Python 3.x this implies a sequency of Unicode characters.

# In[12]:

a = 5
b = 3.5
c = 'A string'


# In[7]:

type(a), type(b), type(c)


# Converting types:

# In[11]:

int(3.6), str(5)


# Checking types:

# In[43]:

type(a), type(b), type(c)


# In[45]:

isinstance(a, float)


# ## Displaying something

# In[43]:

print('Hello')


# *Note:* `print 'Hello'` does not work in Python 3

# In[44]:

print('Hello ' + 'World')


# In[46]:

apples = 'apples'
print('I have', 2, apples)


# ## Numerical operations

# In[2]:

2+2


# In[3]:

3 / 4


# *Note:* if you use Python 2 you have to do:

# In[4]:

3 / float(4)


# ## String operations

# Define strings with single, double or tipple quotes (for multi-line)

# In[24]:

hello = 'world'
saying = "hello world"
paragraph = """ This is
a paragraph
"""


# ### Variables in strings

# In[25]:

'%d' % 20


# In[26]:

'%.3f %.2f' % (20, 1/3)


# A more clean alternative is to use `.format()`

# In[16]:

'{} {}'.format(20, 1/3)


# In[15]:

'{1} {0}'.format(20, 1/3)


# In[27]:

'{:.3f} {:.2f}'.format(20, 1/3)


# ## Data structures

# There are 4 basic data structures: lists (`list`), tuples (`tuple`), dictionaries (`dict`), and sets (`set`)

# ### Lists

# Lists are enclosed in brackets

# In[19]:

pets = ['dogs', 'cat', 'bird'] 
pets.append('lizard')
pets


# ### Tuple

# Tuples are enclosed in parentheses  
# *Note:* You cannot add or remove elements from a tuple but they are faster and consume less memory

# In[18]:

pets = ('dogs', 'cat', 'bird')
pets


# ### Dictionaries

# Dictionaries are build using curly brackets  
# *Note:* Dictionaries are unordered but have key, value pairs

# In[21]:

person = {'name': 'fred', 'age': 29}
print(person['name'], person['age'])


# In[31]:

person['money'] = 50
del person['age']
person


# ### Set

# A set is like a list but it can only hold unique values.  

# In[26]:

pets_1 = set(['dogs', 'cat', 'bird'])
pets_2 = set(['dogs', 'horse', 'zebra', 'zebra'])
pets_2


# There are many useful operations that you can perform using sets

# In[28]:

pets_1.union(pets_2)


# In[29]:

pets_1.intersection(pets_2)


# In[30]:

pets_1.difference(pets_2)


# ### Combinations

# Data structures can hold any Python object!

# In[23]:

combo = ('apple', 'orange')
mix = {'fruit' : [combo, ('banana', 'pear')]}
mix['fruit'][0]


# ## Slicing

# If an object is ordered (such as a list or tuple) you can select on index  

# In[32]:

pets = ['dogs', 'cat', 'bird', 'lizzard']


# In[33]:

favorite_pet = pets[0]
favorite_pet


# In[34]:

reptile = pets[-1]
reptile


# In[35]:

pets[1:3]


# In[36]:

pets[:2]


# *Note:* this also works on strings:

# In[37]:

fruit = 'banana'
fruit[:2]


# ## Functions

# A Python function takes arguments as input and defines logic to processess these inputs (and possibly returns something).

# In[38]:

def add_5(number):
    return number + 5


# The action of defining a function does not execute the code! It will only execute once you call the function:

# In[39]:

add_5(10)


# You can also add arguments with default values:

# In[40]:

def add(number, add=5):
    return number + add


# In[41]:

add(10)


# In[42]:

add(10, add=3)


# ## Whitespace (blocks)

# Indentations are required by Python to sub-set blocks of code.  
# *Note:* these subsets have their own local scope, notice variable `a`:

# In[47]:

def example():
    a = 'Layer 1'
    print(a)
    
    def layer_2():
        a = 'Layer 2'
        print(a)
        
    layer_2()


# In[48]:

example()


# ## Conditionals

# In[47]:

grade = 95
if grade == 90:
    print('A')
elif grade < 90:
    print('B')
elif grade >= 80:
    print('C')
else:
    print('D')


# ## Looping

# In[51]:

for num in range(0, 6, 2):
    print(num)


# In[52]:

list_fruit = ['Apple', 'Banana', 'Orange']
for fruit in list_fruit:
    print(fruit)


# In[53]:

for num in range(100):
    print(num)
    if num == 2:
        break


# You can also (infinitely) loop using `while`:

# In[50]:

count = 0
while count < 4:
    print(count)
    count += 1


# Looping over a tuple in a list:

# In[49]:

tuple_in_list = [(1, 2), (3, 4)]
for a, b in tuple_in_list:
    print(a + b)


# Looping over a dictionary:  
# *Note:* if using Python 2.7 you need to use `.iteritems()`

# In[54]:

dictionary = {'one' : 1, 'two' : 2, 'three' : 3}
for k, v in dictionary.items():
    print(k, v + 10)


# ## Comprehensions:

# A comprehension makes it easier to generate a list or dictionary using a loop.  

# **List comprehension:**

# In[52]:

new_list = [x + 5 for x in range(0,6)]
new_list


# *Traditional way to achieve the same:*

# In[53]:

new_list = []
for x in range(0,6):
    new_list.append(x + 5)
new_list


# **Dictionary comprehension:**

# In[55]:

new_dict = {'num_{}'.format(x) : x + 5 for x in range(0,6)}
new_dict


# *Traditional way to achieve the same:*

# In[56]:

new_dict = {}
for x in range(0,6):
    new_dict['num_{}'.format(x)] = x + 5
new_dict


# ## Catching Exceptions

# A Python exception looks like this:

# In[57]:

num_list = [1, 2, 3]
num_list.remove(4)


# You can catch exceptions using `try` and `except`:

# In[60]:

try:
    num_list.remove(4)
except:
    print('ERROR!')


# It is usually best practise to specify the error type to except:

# In[61]:

try:
    num_list.remove(4)
except ValueError as e:
    print('Number not in the list')
except Exception as e:
    print ('Generic error')
finally:
    print('Done')


# ## Importing Libraries

# In[64]:

import math
math.sin(1)


# In[65]:

import math as math_lib
math_lib.sin(1)


# In[66]:

from math import sin
sin(1)


# ## OS operations

# In[62]:

import os


# ### Get current working directory

# In[63]:

os.getcwd()


# ### List files/folders in directory

# In[65]:

os.listdir()


# ### Change working directory

# In[70]:

os.chdir(r'C:\Stack\Work\Programming\Active\PythonAccountingResearch')


# *Note:* `r'path'` indicates a raw string  
# A raw string does not see `\` as a special character

# ## File Input/Output

# You can open a file with different file modes:  
# `w` -> write only  
# `r` -> read only  
# `w+` -> read and write + completely overwrite file   
# `a+` -> read and write + append at the bottom
# 

# In[71]:

with open('new_file.txt', 'w') as file:
    file.write('Content of new file. \nHi there!')


# In[72]:

with open('new_file.txt', 'r') as file:
    file_content = file.read()


# In[73]:

file_content


# In[74]:

print(file_content)


# In[75]:

with open('new_file.txt', 'a+') as file:
    file.write('\n' + 'New line')


# In[76]:

with open('new_file.txt', 'r') as file:
    print(file.read())


# *Note:* using `with` is best as it automatically closes the file
