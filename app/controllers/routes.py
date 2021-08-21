from app import app
from app.config import ServiceConfig
import requests, json



@app.route("/")
def index():
    return("WEATHER FORECAST")

@app.route('/weather?max=<max_number>', methods=['GET'])
# implementar a funcao
def get_cities_max_number(max_number):
    return("Get all the cached cities, up to the latest n entries (configurable) or max_number (if specified)") #jsonify

@app.route('/weather/<city_name>', methods=['GET'])

def get_city_by_name(city_name):
    ServiceConfig.get_city(city_name)
    COMPLETE_URL = ServiceConfig.generate_complete_url()

    #print(COMPLETE_URL)

    #HTTP requests
    response = requests.get(COMPLETE_URL).json()
    #print(response)

    #Checking if the city is known
    if response['cod'] != 200:
        return ('City Not Found, Error %s' % response['cod'])
    else:
        return (response)

#"Get the cache data for the specified city_name, otherwise fetches from the Open Weather API, caches and returns the results." #jsonify
