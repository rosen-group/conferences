Scale out from the very beginning
=================================

In this talk the authors journey of making the pool of Dark Data available to teams with quite different goals is reflected, emphasising on creating a simple and robust set of tools matching each other and addressing the several needs of the teams based mainly on solutions such as `dask distributed`, `dask` based dataframes, `bokeh` and `flask`.

The key to success was to prevent structuring too much at the very beginning and postpone this task into the several projects of the users consuming the results of these services giving them the freedom to create and use their own models.

It is shown how we implemented a distributed filesystem scanning utility to crawl for data in our 1.5 PB storage system every night ending up in a simple, yet useful table of contents, and how this result set is processed further to fulfill all the project teams requirements.

These services are for example used to
* find expensive duplicates of datasets
* create customer as well as product and service orientated views on the available data
* find data suitable to test algorithms, software and procedures, and to derive current performance
* serve training and education material
* show the usage frequency of the datasets to support an optimised data tiering process

Finally the involved procedures helped to gain more awareness of the value the available data had, both helping to build more trust in Big Data based solutions and to reduce the volume of the data itself that is available online, which in turn keeps the corresponding costs at a reasonable rate.

Author
------

**Jens Nie** ([@jneines](http://twitter.com/jneines))

Jens works primarily as a Technology Scout focusing on Big Data and Data
Science at the ROSEN Technology & Research Center in Lingen, Germany. In
this role he screens for latest developments in these areas and
evaluates and demonstrates their possible use and benefit for the
company. Looking back to more than 20 years in using Python and Linux,
he considers him to be an Open Source enthusiast and committed Python
advocate.

Description
-----------

Most companies a very well aware of the potential behind Big Data solutions today and happily start collecting every piece of information building huge pools of Dark Data. How could Data Science teams create an initial overview on what's available? A simple search strategy, optimised and refined to scale could be a promising way to start.

[![Empowered by Python - A success story](https://img.youtube.com/vi/s7cWVydFpCU/0.jpg)](https://www.youtube.com/watch?v=s7cWVydFpCU)
