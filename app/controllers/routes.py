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
    response, response_dict = ServiceConfig.generate_json_object(COMPLETE_URL)

    #aux = json.loads(response_dict)

    temp_weather_info = response_dict["main"]
    current_temperature_kelvin = temp_weather_info["temp"]
    current_temperature_celsius = str(round(current_temperature_kelvin - 273.15, 2))

    city_name = response_dict["name"]
    desc_weather_info = response_dict["weather"]
    current_description = desc_weather_info[0]["description"]

    print(city_name)
    print(current_temperature_celsius)
    print(current_description)

    #return(return_object)
    if response.from_cache:
        print("%s returned from cache" % response_dict["name"])
    else:
        print("%s fetched from the Open Weather API... Caching it..." % response_dict["name"])
    #print(response.from_cache)

    #print(response_object)
    #return response_object

    #Checking if the city is known
    if response_dict['cod'] != 200:
        return ('City Not Found, Error %s' % response_dict['cod'])
    else:
        return (response_dict)

#"Get the cache data for the specified city_name, otherwise fetches from the Open Weather API, caches and returns the results." #jsonify
