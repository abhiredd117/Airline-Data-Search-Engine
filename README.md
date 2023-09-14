# Airline-Data-Search-Engine
This repository contains code for an airline data search engine I developed to optimize flight planning and travel. The project utilizes Python, React, Flask, and Neo4j to clean, organize, and visualize a large dataset of airline route information.

The Python scripts clean and prepare the raw data from the OpenFlights database of over 19,000 airports and daily passenger statistics. Neo4j is implemented to create a graph database where airports are nodes connected by flight route relationships.

The backend API is built with Flask to handle queries and serve data to the front end. React components allow users to search for and view airports by country, city, and specific routes. While the front end and back end were unable to be fully integrated, the two elements were developed and tested independently.

Overall, this project demonstrates skills in:

Data cleaning and preparation with Python
Database modeling and implementation with Neo4j
Developing and consuming REST APIs with Flask
Frontend development with React
