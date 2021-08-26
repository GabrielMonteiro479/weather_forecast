from app import app
from app.cache import DatabaseManager, Cache
from app.config import ServiceConfig
from flask import jsonify
import requests, json
import requests_cache
import time

five_minutes = 30     # 5 minutes = 300 seconds

cache_dict = {}
all_responses_dict = []
living_cache = []
start_time = int(time.time())
end_time = start_time + five_minutes # 5 minutes after start time

@app.route("/")
def index():
    return("WEATHER FORECAST")

@app.route('/weather/max=<max_number>', methods=['GET'])
# implementar a funcao
def get_cities_max_number(max_number):
    print(max_number)
    return("Get all the cached cities, up to the latest n entries (configurable) or max_number (if specified)") #jsonify












@app.route('/weather/<city_name>', methods=['GET'])

def get_city_by_name(city_name):
    global start_time
    global end_time
    global all_responses_dict
    global living_cache
    global cache_dict

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


        #sql = "SELECT value FROM responses"
        #query = DatabaseManager.Select(conn, sql)
#------------------------------------------------------------------------------------------------------------------------------

        if response.from_cache:

            #Returning and printing from Cache as json
            print("%s returned from cache" % response_dict["name"])

            aux = cache.SearchCache(living_cache, response_dict["name"])
            print(aux)
            json_cache = cache.PrintCache(living_cache)
            return(json_cache)

        else:
            print("%s fetched from the Open Weather API... Caching it..." % response_dict["name"])

            # Cache lives for 5 minutes and then it is deleted
            if (end_time <= int(time.time())):
                #print("DELETING CACHE")
                start_time = end_time
                end_time = start_time + five_minutes
                living_cache = cache.DeleteCache(all_responses_dict)

            # Inserting into cache
            living_cache, cache_dict = cache.Caching(all_responses_dict, cache_dict, response_dict["name"])

            return("%s fetched from the Open Weather API... Caching it..." % response_dict["name"])
