<h1 align="center">
   <img src="https://i.imgur.com/KZGIDj0.png" alt="Get started with Python for Research" title="Get started with Python for Research" />
</h1>
<p align="center">  
 <a href="https://gitter.im/TiesdeKok/PythonAccountingResearch"><img src="https://img.shields.io/gitter/room/nwjs/nw.js.svg"></a>
 <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
 <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=2UKM4JREAPTBG"><img src="https://img.shields.io/badge/Buy%20me%20a-coffee-yellow.svg"></a>
</p>

<p align="center">
  Want to learn how to use <strong>Python for (Accounting) Research</strong>? <br>
  This repository has everything that you need to get started! <br><br>
  <span style='font-size: 15pt'><strong>Author:</strong> Ties de Kok (<a href="http://www.TiesdeKok.com">Personal Page</a>)</span>
</p>

## Table of contents

  * [Introduction](#introduction)
  	* [Who is this repository for?](#audience)
  	* [How to use this repository?](#howtouse)
  * [Getting your Python setup ready](#setup)
  * [Using Python](#usingpython)
  	 * [Jupyter Notebook](#jupyter)
  	 * [Installing packages](#packages)
  * [Tutorial Notebooks](#notebooks)
  	* [Exercises](#exercises)
  * [Code along](#codealong)
     * [Binder](#binder)
     * [Clone repository](#clonerepo)
  * [Questions?](#questions)
  * [License](#license)
  * [Special thanks](#specialthanks)

<h2 id="introduction">Introduction</h2>

The goal of this GitHub page is to provide you with everything you need to get started with Python for actual research projects.   

<h3 id="audience">Who is this repository for?</h3>

The topics and techniques demonstrated in this repository are primarily oriented towards empirical research projects in fields such as Accounting, Finance, Marketing, Political Science, and other Social Sciences. 

However, many of the basics are also perfectly applicable if you are looking to use Python for any other type of Data Science!

<h3 id="howtouse">How to use this repository?</h3>

This repository is written to facilitate learning by doing 

**If you are starting from scratch I recommend the following:**

1. Familiarize yourself with the [`Getting your Python setup ready`](#setup) and [`Using Python`](#usingpython) sections below
2. Check the [`Code along!`](#codealong) section to make sure that you can interactively use the Jupyter Notebooks 
3. Work through the [`0_python_basics.ipynb`](0_python_basics.ipynb) notebook and try to get a basics grasp on the Python syntax
4. Do the "Basic Python tasks" part of the [`exercises.ipynb`](exercises.ipynb) notebook
5. Work through the [`1_opening_files.ipynb`](#), [`2_handling_data.ipynb`](2_handling_data.ipynb), and [`3_visualizing_data.ipynb`](3_visualizing_data.ipynb) notebooks.  
   **Note:** the [`2_handling_data.ipynb`](2_handling_data.ipynb) notebook is very comprehensive, feel free to skip the more advanced parts at first.  
6. Do the "Data handling tasks (+ some plotting)" part of the [`exercises.ipynb`](exercises.ipynb) notebook

If you are interested in web-scraping:

7. Work through the [`4_web_scraping.ipynb`](4_web_scraping.ipynb) notebook
8. Do the "Web scraping" part of the [`exercises.ipynb`](exercises.ipynb) notebook

**If you are already familiar with the Python basics:**

Use the notebooks provided in this repository selectively depending on the types of problems that you try to solve with Python.

Everything in the notebooks is purposely sectioned by the task description. So if you, for example, are looking to merge two Pandas dataframes together, you can use the `Combining dataframes` section of the [`2_handling_data.ipynb`](2_handling_data.ipynb) notebook as a starting point. 


<h2 id="setup">Getting your Python setup ready</h2>

There are multiple ways to get your Python environment set up. To keep things simple I will only provide you with what I believe to be the best and easiest way to get started: download the Anaconda distribution. 

<h3 id="anaconda">Anaconda Distribution</h3>

The Anaconda Distribution bundles Python with a large collection of Python packages from the (data) science Python eco-system.  

By installing the Anaconda Distribution you essentially obtain everything you need to get started with Python for Research!

<h4 id="anacondainstall">Install Anaconda</h4>

 1. Go to [anaconda.com/download/](https://www.anaconda.com/download/) 
 2. Download the **Python 3.6 version** installer
 3. Install Anaconda. A couple of notes:
 	* For a first install, I recommend ticking the boxes to make it your primary installation and adding it to your path.
 	* It is worth to take note of the installation directory in case you ever need to find it again.
 4. Check if the installation works by launching a command prompt (terminal) and type `python`, it should say Anaconda at the top.
 	* On Windows I recommend using the `Anaconda Prompt` 

*Note:* Anaconda also comes with the `Anaconda Explorer`, I haven't personally used it yet but it might be convenient. 

<h4 id="pythonversion">Python 3 vs Python 2?</h4>

Python 3.x is the newer and superior version over Python 2.7 so I strongly recommend to use Python 3.x (Python 3.6) whenever possible.

The only reason to occasionally use Python 2.7 would be if you are "forced" to (i.e. there is a package that you have to use but that is not yet updated to work with Python 3). In this unlikely scenario I would recommend to just install Python 2.7 alongside Python 3.6, and only use Python 2.7 when you need to.

<h2 id="usingpython">Using Python</h2>

**Basic methods:**  

The native way to run Python code is by saving the code to a file with the ".py" extension and executing it from the console / terminal:

```python code.py```

Alternatively, you can run some quick code by starting a python or ipython interactive console by typing either `python` or `ipython` in your console / terminal.

<h3 id="jupyter">Jupyter Notebook</h3>

The above is, however, not very convenient for research purposes as we desire easy interactivity and good documentation options.  
Fortunately, the awesome **Jupyter Notebooks** provide a great alternative way of using Python for research purposes. 

[Jupyter](http://jupyter.org/) comes pre-installed with the Anaconda distribution so you should have everything already installed and ready to go. 

***What is the Jupyter Notebook?***

From the [Jupyter](http://jupyter.org/) website:
> The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and explanatory text. 

In other words, the Jupyter Notebook allows you to program Python code straight from your browser!

***How does the Jupyter Notebook work in the background?***

The diagram below sums up the basics components of Jupyter:

<img src="https://i.imgur.com/1zFzbyw.png" title="Jupyter Notebook" width = 400px/>

At the heart there is the *Jupyter Server* that handles everything, the *Jupyter Notebook* which is accessed and used through your browser, and the *kernel* that executes the code. We will be focusing on the natively included *Python Kernel* but Jupyter is language agnostic so you can also use it with other languages/software such as 'R'.

It is worth noting that in most cases you will be running the `Jupyter Server` on your own computer and will connect to it locally in your browser (i.e. you don't need to be connected to the internet). However, it is also possible to run the Jupyter Server on a different computer, for example a high performance computation server in the cloud, and connect to it over the internet.

***How to start a Jupyter Notebook?***

The primary method that I would recommend to start a Jupyter Notebook is to use the command line (terminal) directly:

1. Open your command prompt / terminal (on Windows I recommend the Anaconda Prompt)
2. `cd` (i.e. Change) to the desired starting directory   
   for example: `cd "C:\Files\Work\Project_1"`  
   *Note:* if you are changing do folder on another drive you might have to also switch drives by typing, for example, `E:` 
3. Start the Jupyter Notebook server by typing: `jupyter notebook` 

This should automatically open up the corresponding Jupyter Notebook in your default browser.
You can also manually go to the Jupyter Notebook by going to `localhost:8888` with your browser.

***How to close a Jupyter Notebook server?***

If you want to close down the Jupyter Server: open up the command prompt window that runs the server and press `CTRL + C` twice.   
Make sure that you have saved any open Jupyter Notebooks!

***How to use the Jupyter Notebook?***

I recommend to watch this excellent YouTube video: [Awesome Data Science: 1.0 Jupyter Notebook Tour
](https://www.youtube.com/watch?v=e9cSF3eVQv0)

*Some shortcuts are worth mentioning for reference purposes:*

`command mode` --> enable by pressing `esc`   
 `edit mode` --> enable by pressing `enter`   

|  `command mode` |`edit mode` 	| `both modes`
|---	|---	|---
|  `Y` : cell to code	|  `Tab` : code completion or indent | `Shift-Enter` : run cell, select below
| `M` : cell to markdown  |   `Shift-Tab` : tooltip | `Ctrl-Enter` : run cell 
| `A` : insert cell above  	|   	`Ctrl-A` : select all | 
| `B` : insert cell below  	|   `Ctrl-Z` : undo | 
| `X`: cut selected cell |   


<h3 id="packages">Installing Packages</h3>

The Python eco-system consists of many packages and modules that people have programmed and made available for everyone to use.  
These packages/modules are one of the things that makes Python so useful. 

Some packages are natively included with Python and Anaconda, but anything not included you need to install first before you can import them.  
I will discuss the three primary methods of installing packages:

**Method 1:** use `pip`

> Many packages are available on the "Python Package Index" (i.e. "PyPI"): [https://pypi.python.org/pypi](https://pypi.python.org/pypi)  
>
> You can install packages that are on "PyPI" by using the `pip` command:
>
> Example, install the `requests` package: run `pip install requests` in your command line / terminal (not in the Jupyter Notebook!).
>
> To uninstall you can use `pip uninstall` and to upgrade an existing package you can add the `-U` flag (`pip install -U requests`)

**Method 2:** use `conda`

>Sometimes when you try something with `pip` you get a compile error (especially on Windows). You can try to fix this by configuring the right compiler but most of the times it is easier to try to install it directly via Anaconda as these are pre-compiled. For example:
>
>`conda install scipy`
>
>Full documentation is here: [Conda documentation](https://conda.io/docs/user-guide/tasks/manage-pkgs.html)

**Method 3:** install directly using the `setup.py` file

>Sometimes a package is not on pypi and conda (you often find these packages on GitHub). Follow these steps to install those:
>
>1. Download the folder with all the files (if archived, make sure to unpack the folder)
>2. Open your command prompt (terminal) and `cd` to the folder you just downloaded
>3. Type: `python setup.py install`

<h2 id="notebooks">Tutorial Notebooks</h2>

This repository currently contains the follow elements:

* [`0_python_basics.ipynb`](0_python_basics.ipynb): Basics of the Python syntax
* [`1_opening_files.ipynb`](1_opening_files.ipynb): Examples on how to open Txt, CSV, Excel, Stata, Sas, JSON, and HDF files. 
* [`2_handling_data.ipynb`](2_handling_data.ipynb): A comprehensive overview on how to use the `Pandas` library for data wrangling.
* [`3_visualizing_data.ipynb`](3_visualizing_data.ipynb): Examples on how to generate visualizations with `Pandas`, `Seaborn`, and `Bokeh`.
* [`4_web_scraping.ipynb`](4_web_scraping.ipynb): A comprehensive overview on how to use `Requests`, `LXML`, and `Selenium` for APIs and web scraping.

<h4 id="exercises">Exercises</h4>

I have provided several tasks / exercises that you can try to solve in the [`exercises.ipynb`](exercises.ipynb) notebook.

<h2 id="codealong">Code along!</h2>

You can code along in two ways:

<h3><strong>Option 1:</strong> use Binder</h3>

To be added. 

<h3><strong>Option 2:</strong> clone repository</h3>

You can essentially "download" the contents of this repository by cloning the repository. 

You can do this by clicking "Clone or download" button and then "Download ZIP":

<img src="https://i.imgur.com/Ysak4s3.png" title="Jupyter Notebook" width = 300px/>

If you extract the downloaded ZIP to a folder you can start the Jupyter Notebook in that folder and access the notebooks.

<h2 id="questions">Questions?</h2>

If you have questions or experience problems please use the `issues` tab of this repository.

<h2 id="license">License</h2>

[MIT](LICENSE) - Ties de Kok - 2017

<h2 id="specialthanks">Special Thanks</h2>

https://github.com/teles/array-mixer for having an awesome readme that I used  as a template. 
