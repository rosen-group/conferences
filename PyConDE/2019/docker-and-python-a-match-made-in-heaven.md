Docker and Python - A Match made in Heaven
==========================================

Docker has revolutionized the way we build and ship software
by providing a great toolset for Linux containers. This talk is aimed at 
newcomers and people with limited experience with Docker and will cover
the basics of Docker and how it can be used alongside Python. There will 
be examples of building and deploying Python applications in containers
and integration of Docker with pytest using the official Python SDK for Docker. 

Author
------

**Dr. Hendrik Niemeyer** ([@hniemeye](http://twitter.com/hniemeye))

I am a Data Scientist working on applying machine learning solutions to
sensor data from non-destructive testing of pipelines in order to detect
and size internal damage.

Description
-----------

Docker provides tooling for building,
running and communication between Linux containers. Containers are a lightweight 
alternative to virtual machines and are a great way of isolating resources
and preventing dependency conflicts in software. The basic concepts and pros
and cons of containerization will be discussed. 

This talk will show how to build and ship a Python application (flask web app)
with Docker and why this is beneficial compared to running it directly on the
machine. Docker also provides an official SDK / API for Python which can be used
alongside Pytest for writing integration and end to end tests for Docker containers
which will be shown for an example application.
