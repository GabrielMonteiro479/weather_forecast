from app import app
from app.cache import DatabaseManager, Cache
from app.config import ServiceConfig
from flask import jsonify
import requests, json
import requests_cache
import time

five_minutes = 300     # 5 minutes = 300 seconds

all_responses_dict = []
living_cache = []
start_time = int(time.time())
end_time = start_time + five_minutes # 5 minutes after start time

@app.route("/")
def index():
    return("WEATHER FORECAST")

@app.route('/weather/max=', methods=['GET'], defaults = {'max_number': None})
@app.route('/weather/max=<max_number>', methods=['GET'])
# implementar a funcao
def get_cities_max_number(max_number):
    global all_responses_dict
    global response_dict
    weather_return = []


    cache = Cache(response_dict)
    if not max_number or max_number == '0':
        max_number = 5
    try:
        max_number_int = int(max_number)
    except:
        return("'Max number' is not valid")

    living_cache = cache.GetCache()

    lengh = len(living_cache)
    if lengh < max_number_int:
        max_number_int = lengh

    for i in range(max_number_int):
        weather_return.append(living_cache[lengh-i-1])


    print("Get all the cached cities, up to the latest n entries (configurable) or max_number (if specified)")
    return(jsonify(weather_return))

#-----------------------------------------------------------------------------------------------------------------------------------

@app.route('/weather/<city_name>', methods=['GET'])

def get_city_by_name(city_name):
    global start_time
    global end_time
    global all_responses_dict
    global living_cache
    global cache_dict
    global response_dict

    ServiceConfig.get_city(city_name)
    COMPLETE_URL = ServiceConfig.generate_complete_url()

    #HTTP requests
    response, response_dict = ServiceConfig.generate_json_object(COMPLETE_URL)

    cache = Cache(response_dict)

    #Checking if the city is known
    if response_dict['cod'] != 200:
        return ('City Not Found, Error %s' % response_dict['cod'])
    else:
        temp_weather_info = response_dict["main"]
        current_temperature_kelvin = temp_weather_info["temp"]
        current_temperature_celsius = str(round(current_temperature_kelvin - 273.15, 2))

        city_name = response_dict["name"]
        desc_weather_info = response_dict["weather"]
        current_description = desc_weather_info[0]["description"]

        print(city_name)
        print(current_temperature_celsius)
        print(current_description)

#------------------------------------------------------------------------------------------------------------------------------
# TRYING WITH SQL
        #conn = DatabaseManager.DatabaseConn()
        #conn.close()

        #sql = "SELECT value FROM responses"
        #query = DatabaseManager.Select(conn, sql)
#------------------------------------------------------------------------------------------------------------------------------
        # Cache lives for 5 minutes and then it is deleted
        if (end_time <= int(time.time())):
            start_time = end_time
            end_time = start_time + five_minutes
            living_cache = cache.DeleteCache(all_responses_dict)
            cache.SetCache(living_cache)

        #Checking if the city is cached
        if response.from_cache:

            #Returning and printing from Cache as json
            print("%s returned from cache" % response_dict["name"])
            #json_cache = cache.PrintCache(living_cache)
            return(jsonify(response_dict))

        else:
            print("%s fetched from the Open Weather API... Caching it..." % response_dict["name"])
            # Inserting into cache
            living_cache = cache.Caching(all_responses_dict)
            cache.SetCache(living_cache)
            return(jsonify(response_dict))
