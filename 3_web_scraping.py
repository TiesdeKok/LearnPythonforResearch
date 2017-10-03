
# coding: utf-8

# # Web scraping

# **Author:** Ties de Kok ([Personal Website](www.tiesdekok.com]))  
# **Last updated:** 2 Oct 2017  
# **Python version:** Python 3.5  
# **License:** MIT License  

# ## <i>Introduction</i>

# Depending on the website it can be very easy or very hard to extract the information you need.  
# 
# Websites can be classified into roughly two categories:
# 1. Computer oriented webpage: API (Application Program Interface)
# 2. Human oriented webpage: regular website
# 
# Option 1 (an API) is designed to be approach programmatically so extracting the data you need is usually easy. However, in many cases you don't have an API available so you might have to resort to scraping the regular website (option 2). 
# 
# It is worth noting that option 2 can put a lot of strain on the server of the website. Therefore, only resort to option 2 if there is no API available, and if you decide to scrape the regular website make sure to do so in a way that is as polite as possible!
# 
# **This notebook is structured as follows:**
# 
# 1. Using the `requests` package to interact with a website or API
# 2. Extract data using an API
# 3. Extract data from a regular website using regular expressions
# 4. Extract data from a regular website by parsing it using LXML
# 5. Extract data from Javascript heavy websites using Selenium
# 6. Advanced webscraping using Scrapy

# **Note:** In this notebook I will often build upon chapter 11 of 'automate the boring stuff' which is available here:  
# https://automatetheboringstuff.com/chapter11/

# ## <span style="text-decoration: underline;">Requests package</span>
# 

# We will use the `requests` module. I like the description mentioned in the book 'automate the boring stuff':
# > The requests module lets you easily download files from the Web without having to worry about complicated issues such as network errors, connection problems, and data compression. The requests module doesn’t come with Python, so you’ll have to install it first. **From the command line, run:**   
# 
# > `pip install requests`

# In[2]:

import requests


# *Note:* If you google around on webscraping with Python you will probably also find mentions of the `urllib2` package. I highly recommend to use `requests` as it will make your life a lot easier for most tasks. 

# ### Basics of  the `requests` package

# The `requests` package takes a URL and allows you to interact with the contents. For example:

# In[4]:

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')


# In[11]:

print(res.text[7:250])


# The `requests` package is incredibly useful because it deals with a lot of connection related issues automatically. We can for example check whether the webpage returned any errors relatively easily:

# In[12]:

res.status_code 


# In[14]:

requests.get('https://automatetheboringstuff.com/thisdoesnotexist.txt').status_code


# You can find a list of most common HTTP Status Codes here:  
# https://www.smartlabsoftware.com/ref/http-status-codes.htm

# ## <u>Extract data using an API</u>

# APIs are designed to be approached and 'read' by computers, whereas regular webpages are designed for humans not computers.  
# 
# An API, in a simplified sense, has two characteristics:
# 1. A request is made using an URL that contains parameters specifiying the information requested
# 2. A response by the server in a machine-readable format. 
# 
# The machine-readable formats are usually either:
# - JSON
# - XML
# - (sometimes plain text)

# ### Demonstration using an example

# Let's say, for the sake of an example, that we are interested in retrieving current and historical Bitcoin prices.  
# 
# After a quick Google search we find that this information is available on https://www.coindesk.com/price/.
# 
# We could go about and scrape this webpage directly, but as a responble web-scraper you look around and notice that coindesk fortunately offers an API that we can use to retrieve the information that we need. The details of the API are here:
# 
# https://www.coindesk.com/api/
# 
# There appear to be two API calls that we are interested in:
# 
# 1) We can retrieve the current bitcoin price using: https://api.coindesk.com/v1/bpi/currentprice.json  
# 2) We can retrieve historical bitcoin prices using: https://api.coindesk.com/v1/bpi/historical/close.json
# 
# Clicking on either of these links will show the response of the server. If you click the first link it will look something like this:
# 
# ![](https://i.imgur.com/CpzgsTo.png)
# 
# Not very readable for humans, but easily processed by a machine!
# 
# 

# ###  Task 1: get the current Bitcoin price

# As discussed above, we can retrieve the current Bitcoin price by "opening" the following URL:  
# https://api.coindesk.com/v1/bpi/currentprice.json
# 
# Using the `requests` library we can easily "open" this url and retrieve the response.

# In[15]:

res = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')


# An important observation is that this API returns information in the so-called `JSON` format.  
# 
# You can learn more about the JSON format here: https://www.w3schools.com/js/js_json_syntax.asp.
# 
# We could, as before, return this results as plain text:

# In[20]:

text_res = res.text
text_res


# This is, however, not desirable because we want see the prices that we want but we have no way of easily and reliably extract these prices from the string.
# 
# We can, however, achieve this by telling `requests` that the response is in the JSON format:

# In[19]:

json_res = res.json()
json_res


# All that is left now is to extract the Bitcoin prices. This is now easy because `res.json()` returns a Python dictionary.

# In[23]:

json_res['bpi']['EUR']


# In[24]:

json_res['bpi']['EUR']['rate']


# ### Task 2: write a function to retrieve historical Bitcoin prices

# We can retrieve historical Bitcoin prices through the following API URL:  
# https://api.coindesk.com/v1/bpi/historical/close.json
# 
# Looking at https://www.coindesk.com/api/ tells us that we can pass the following parameters to this URL:  
# * `index` -> to specify the index
# * `currency` -> to specify the currency 
# * `start` -> to specify the start date of the interval
# * `end` -> to specify the end date of the interval 
# 
# We are primarily interested in the `start` and `end` parameter.
# 
# As illustrated in the example, if we want to get the prices between 2013-09-01 and 2013-09-05 we would construct our URL as such:
# 
# https://api.coindesk.com/v1/bpi/historical/close.json?start=2013-09-01&end=2013-09-05
# 
# **But how do we do this using Python?**
# 
# Fortunately, the `requests` library makes it very easy to pass parameters to a URL as illustrated below.  
# For more info, see: http://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls

# In[25]:

API_endpoint = 'https://api.coindesk.com/v1/bpi/historical/close.json'
payload = {'start' : '2013-09-01', 'end' : '2013-09-05'}


# In[26]:

res = requests.get(API_endpoint, params=payload)


# We can print the resulting URL (for manual inspection for example) using `res.url`:

# In[27]:

print(res.url)


# Again, the result is in the JSON format so we can easily process it:

# In[30]:

bitcoin_2013 = res.json()


# In[33]:

bitcoin_2013['bpi']


# ### Wrap the above into a function

# In the example above we hardcode the parameter values (the interval dates), if we want to change the dates we have to manually alter the string values. This is not very convenient, it is easier to wrap everything into a function:

# In[34]:

API_endpoint = 'https://api.coindesk.com/v1/bpi/historical/close.json'

def get_bitcoin_prices(start_date, end_date, API_endpoint = API_endpoint):
    payload = {'start' : start_date, 'end' : end_date}
    res = requests.get(API_endpoint, params=payload)
    json_res = res.json()
    return json_res['bpi']


# In[35]:

get_bitcoin_prices('2016-01-01', '2016-01-10')


# ## <u>Web scraping using Regular Expressions</u>

# Extracting information from webpages consists of four steps:
# 1. Construct or retrieve the URL
# 2. Have Python visit the URL and download the source of the page (often HTML)
# 3. If needed, parse the source-file
# 4. Extract the information you need

# For very basic webscraping it is possible to use Regular Expression to select parts of an HTML page.  
# **However, for most applications it is a lot better to use a module developed for parsing HTML, like Beautiful Soup.**

# ### The SSRN example

# This is the method used in the example of the first session, where we retrieved information from an SSRN page.  
# I will briefly repeat it:
# 
# The goal is to get the *title*, *author*, and *publication date* of a webpage:  
# e.g. http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2610429
# 

# In[51]:

import re


# In[45]:

def get_ssrn_data(ID):
    payload = {'abstract_id' : ID}
    res = requests.get('http://papers.ssrn.com/sol3/papers.cfm?', params=payload)
    return res.text


# In[55]:

html_text = get_ssrn_data(2610429)


# Now, this is the raw source text of an HTML page, so we need to parse it into something we can actually use

# In[49]:

html_text[:350]


# In this example we will use the observation that some information is included in meta tags:
#     ><title>Financial Accounting Research, Practice, and Financial Accountability by Mary E. Barth :: SSRN</title>
#     
#     <meta name="citation_author" content="Barth, Mary E.">
#     <meta name="citation_title" content="Financial Accounting Research, Practice, and Financial Accountability">
#     <meta name="citation_online_date" content="2015/05/26">

# This makes it relatively easy and consistent to extract this content using Regular Expressions:

# In[56]:

re.findall(r'<meta name="citation_author" content="(.*)">', html_text)


# In[57]:

re.findall(r'<meta name="citation_title" content="(.*)">', html_text)[0]


# In[58]:

re.findall(r'<meta name="citation_online_date" content="(.*)">', html_text)[0]


# ## Web scraping using BeautifulSoup

# In the example above we treat a HTML page as-if it is plain text.  
# However, HTML is a format in which we write web pages, so it actually has an underlying structure that we can use.

# A quick refresher on HTML from 'automate the boring stuff':
# 
# > In case it’s been a while since you’ve looked at any HTML, here’s a quick overview of the basics. An HTML file is a plaintext file with the .html file extension. The text in these files is surrounded by tags, which are words enclosed in angle brackets. The tags tell the browser how to format the web page. A starting tag and closing tag can enclose some text to form an element. The text (or inner HTML) is the content between the starting and closing tags. For example, the following HTML will display Hello world! in the browser, with Hello in bold:
# 
#     <strong>Hello</strong> world!

# You can view the HTML source by right-clicking a page and selecting `view page source`:

# In[60]:

Image('https://automatetheboringstuff.com/images/000009.jpg')


# ### Get started

# We will use the so-called `BeautifulSoup` module to parse HTML pages, run from the command line:
# 
#     pip install beautifulsoup4
#     
# The module name itself is the abbrevation `bs4`

# In[61]:

import bs4


# ### Create a BeautifulSoup Object

# For this example we will follow 'automate the boring stuff' and retrieve data from:  
# http://nostarch.com

# In[63]:

res = requests.get('http://nostarch.com')
noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarchSoup)


# ### Retrieve information from the BeautifulSoup object

# The goal is to, somehow, retrieve the content of a particular section of the HTML document.  
# Now, HTML is like a hierarchical structure, so we can try to select a particular part based on the location in the structure.  
# 
# There are two ways to go about this:  
# 1. Using a `css-selector`
# 2. Using an `XPath`
# 
# BeautifulSoup accepts a `css-selector` expression for the `select()` method.  
# 
# I will not go into much detail on these `css-selectors` but this links lists several tutorials:  
# https://automatetheboringstuff.com/list-of-css-selector-tutorials/

# ### A pragmatic way to go about making CSS selectors

# Creating CSS selectors manually can be a lot of work and require some knowledge on how HTML and CSS works.  
# However, there are tools available that allow you to select what you want and have it generate a CSS selector expression.  
# 
# For example, if you use Chrome you can use the `SelectorGadget` extension.  
# This extension allows you to select what you want and do not want, and it will generate an expression you can use with BeautifulSoup.

# ### For example:
# Let's say we want to extract the title of the first element in the 'New' column:

# In[72]:

Image('https://dl.dropboxusercontent.com/u/1265025/python_tut/python_css.PNG')


# *Note:* The number between brackets after 'Clear' indicates the number of elements selected.

# ### Extract the text from that one element

# In[73]:

first_new = noStarchSoup.select('.view-dom-id-1 .views-row-first .product-body a')


# In[76]:

first_new[0].getText()


# In[77]:

first_new[0].attrs


# ### Extract all the new elements

# In[78]:

all_new = noStarchSoup.select('.view-dom-id-1 .product-body a')


# In[79]:

for x in all_new:
    print(x.getText())


# ### Extract bestsellers

# In[80]:

all_bestsellers = noStarchSoup.select('.imagecache-product_linked .imagecache-product')


# In[93]:

all_bestsellers[0].attrs


# In[95]:

for x in all_bestsellers:
    print(x.attrs['title'])


# ## Advanced webscraping using Scrapy

# In the examples above we provide the URLs in advance.  
# Sometimes you want to create a `spider` which basically 'walks' through webpages and crawls the information.  
# 
# In other words, you might want to create a spider that visits webpages without specifying all the URLs upfront.  
# 
# This, obviously, requires more programming but it can be achieved with frameworks such as `Scrapy`.  
# http://scrapy.org/
# 
# Using this framework requires some more time investment, but if you are serious about web-crawling this is the way to go.  
# `Scrapy` also allows 'spiders' to click on links or use login forms, amongst many other things.

# ## Advanced webscraping using Selenium

# Sometimes you need to interact with a webpage in a way that is not achievable by using URLs.  
# For example, you might need to first login before being able to reach a web-page.  
# 
# In many cases you can use the `scrapy` framework but an alternative that sometimes works better is the `selenium` Module:
# 
# > The selenium module lets Python directly control the browser by programmatically clicking links and filling in login information, almost as though there is a human user interacting with the page. Selenium allows you to interact with web pages in a much more advanced way than Requests and Beautiful Soup; but because it launches a web browser, it is a bit slower and hard to run in the background if, say, you just need to download some files from the Web.
# 
# I will not discuss it here, but it is included here:
# 
# https://automatetheboringstuff.com/chapter11/ 'Controlling the Browser with the selenium Module'
