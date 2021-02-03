# Public code for the OOSA course.

There is a separate directory for each week's work. As we progress, suggested answers will be uploaded.

## Foundations

The **foundations** folder contains some warm up exercises to transition on to the course. There are two folders within:

* basic\_features
* iterating

The **basic\_features** folder contains a set of scripts introducing the basic Python features (data types, loops, plotting etc.). Other than **06_objects.py**, which will be covered in week 2, these should already be familar to you and are included here for revision.

The **iterating** directory contains some exercises to practice using loops and work up to movoing around a raster dataset.


## Week 1

Week 1 covers:

***Aspects***
* Github version control and code repository
* Computer basics 
* Revision of loops and file I/O

***Algorithm***
* Introduction to algorithm design: Finding minima and sorting


### fileIO

Contains two scripts to demonstrate reading from a text file and writing to a text file. The ***data*** folder contains the data for the file reading example.


### sort

This includes an example of a selection sort algorithm, which finds the minimum of a list and copies that to the start of an array.


## Week 2

This week covers

***Aspects***
* Using the command line to make programmable programs
* Objects and classes

***Algorithm***
* Binary search: Loop and recursion

### command\_line

Contains two files. *commandExample.py* is a minimum workable example for a command line interface. *commandLineIllus.py* shows an example of most of the common options you might want to add to a command line, in terms of the data types read.

### main

Contains *mainTest.py* to give an example of defining the main block.

### data

Contains an ASCII data file to use if needed.

### objects

Contains an example of an object to show how attributes (data) and methods (functions) can be combined within an object.


### docu\_strings

Contains an illustration of docu strings in python.


### binary\_search

Contains a class with a data sorter. This should be built upon to add a binary search method.


***binarySearches.py*** contains an examples of functioasn to perform a binary search by both looping and recursion.

***finishedQuartiles.py*** Combines the binary search functions with a dataSorter array to read some wages data, sort it and then return the quantiles for a given value, specified on the command line.

***randomWages.py*** shows an example of this being used in practice, importing the functions and classes from the other scripts to read in a file of wages and determine quantiles.

Command line options:

    --wage WAGE     Wage to determine the quantile of. Default is 27,000
    --input INNAME  Input file to read data rom. Default is ../data/wages.csv

Usage example:

   python3 finishedQuartiles.py --wage 16000


## Week 3

Contains the scripts for week 3's session. Week 3 will cover:

***Aspects***
* Geospatial packages: pyproj and gdal
* Function fitting
* note on function input/output
* mention of pandas

***Algorithm***
* Douglas-Peucker line generalization


### data

Contains two data files, both in .csv format. One contains synthetic wage and age data. The other contains the GPS track of a sdquirrel.


### reproject

Contains an example of using the ***pyproj*** package to reproject vector data and the ***GDAL*** package to reproject raster data.


### function\_fit

Shows an exmaple of using numpy's polyfit function to fit a straight line. It does this within a class which includes a method for plotting the inut data and the fitted line.

Example usage:

    python3 exampleFit.py

This will print the correlation coefficient to screen and create a graph in .png format.

### pandas

Contains a very brief example of the pandas package. This builds upon numpy arrays in a way that recreates the utility of R dataframes. Some users prefer pandas to numpy arrays. The geopandas package builds upon pandas and is a very powerful package for geospatial analysis.


### dp-line-general

Contains an example solution of the Douglas-Peucker line-generalistion, using recursion. Note that this depends upon two other files within this repository and uses the ***PYTHONPATH*** to import these. These dependecies are:

    vectorExample.py
    perpendicular_distance

The options are:

    --input INNAME   Input filename
    --tolerance TOL  Tolerance of generalisation Default = 10
    --epsg EPSG      EPSG to do analysis in Default = 27700

An example usage would be:

    python3 exampleDP.py --epsg 32630


## Week 5

Week 5 covers

***Aspects***
* Raster analysis
* More batch processing
* A few more useful packages

***Algorithm***
* Practice all of the above

### geopandas

Includes an example of using geopandas to read some vector data from a .csv file, reproject and write to a shape file.

