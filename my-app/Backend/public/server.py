#Imports
from flask import Flask, request
from flask_restful import Resource, Api
from neo4j import GraphDatabase
import logging

#Initialize Flask application
app = Flask(__name__)

api = Api(app)


#Database information and connection
class Database():

	def __init__(self, uri, user, password):
		self.driver = GraphDatabase.driver(uri, auth=(user, password))

	def close(self):
        # Don't forget to close the driver connection when you are finished with it
		self.driver.close()

	@staticmethod
	def get_airports_city(tx, city):
		query = f"Match (d:DestinationAirport) where d.city = \"{city}\" return d"
		result = tx.run(query, city = city)
		return [row for row in result]

	@staticmethod
	def get_airports_country(tx, country):
		query = f"Match (p:DestinationAirport) Where p.country = \"{country}\" return p"
		result = tx.run(query, country = country)
		return [row for row in result]

	@staticmethod
	def get_airports_city_country(tx, city, country):
		query = f"Match (d:DestinationAirport) where d.city = \"{city}\" and d.country = \"{country}\" return d"
		result = tx.run(query, city = city, country = country)
		return [row for row in result]

#Database Information
uri = "neo4j+s://0f1d534d.databases.neo4j.io"
user = "neo4j"
password = "qFc33tBBc1_r22N_EFz9tTTSyuz0hXTv4k7SSfL2UF0"
db = Database(uri, user, password)

airport_data = [{
  "identity": 9746,
  "labels": [
    "DestinationAirport"
  ],
  "properties": {
    "country": "Germany",
    "altitiude": 157,
    "airportName": "Berlin-Schönefeld Airport",
    "dst": "Europe/Berlin",
    "iata": "SXF",
    "timezoneDST": "E",
    "city": "Berlin",
    "timezone": 1.0,
    "airportID": 337,
    "latitude": 52.380001,
    "icao": "EDDB",
    "longitude": 13.5225
  },
  "elementId": "9746"
},
{
  "identity": 9752,
  "labels": [
    "DestinationAirport"
  ],
  "properties": {
    "altitiude": 167,
    "country": "Germany",
    "airportName": "Berlin-Tempelhof International Airport",
    "dst": "Europe/Berlin",
    "iata": "THF",
    "timezoneDST": "E",
    "city": "Berlin",
    "timezone": 1.0,
    "airportID": 343,
    "latitude": 52.47299957,
    "icao": "EDDI",
    "longitude": 13.40390015
  },
  "elementId": "9752"
},
{
  "identity": 9760,
  "labels": [
    "DestinationAirport"
  ],
  "properties": {
    "altitiude": 122,
    "country": "Germany",
    "airportName": "Berlin-Tegel Airport",
    "dst": "Europe/Berlin",
    "iata": "TXL",
    "timezoneDST": "E",
    "city": "Berlin",
    "timezone": 1.0,
    "airportID": 351,
    "latitude": 52.5597,
    "icao": "EDDT",
    "longitude": 13.2877
  },
  "elementId": "97600"
}]

class Home(Resource):
	def get(self):
		return airport_data

class AirportCountry(Resource):
	def get(self, str):
		return db.get_airports_country(self, str)

class AirportCityCountry(Resource):
	def get(self, str):
		return db.get_airports_city_country(self, str)

class AirportCity(Resource):
	def get(self, str):
		return db.get_airports_city(self, str)

api.add_resource(Home, '/')
api.add_resource(AirportCountry, '/airport_country/<string:str>')
api.add_resource(AirportCity, '/airport_city/<string:str>')
api.add_resource(AirportCityCountry, '/airport_city_country/<string:str>')


#Run Flask application
if __name__ == "__main__":
	app.run(debug=True)

	