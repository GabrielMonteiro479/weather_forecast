from app import app
from app.cache import DatabaseManager
from app.config import ServiceConfig
from flask import jsonify
import requests, json
import requests_cache
import time

five_minutes = 300       # 5 minutes = 300 seconds
all_responses = []
all_responses_dict = []
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
    ServiceConfig.get_city(city_name)
    COMPLETE_URL = ServiceConfig.generate_complete_url()

    #print(COMPLETE_URL)

    #HTTP requests
    response, response_dict = ServiceConfig.generate_json_object(COMPLETE_URL)
    #print(response)
    #all_responses.append(response)
    #all_responses_dict.append(response_dict)

    #all_responses_len = len(all_responses)

    #count = 0
    #for i in reversed(range(all_responses_len)):
    #while count < 5:
        #if (all_responses_len - count - 1) >= 0:
            #if all_responses[all_responses_len - count - 1].from_cache:
            #if all_responses[i].from_cache:
                #print(all_responses_dict[all_responses_len-count-1])
        #print(all_responses_len)
        #count += 1

        #if i < all_responses_len - 5:
        #    return

    #aux = json.loads(response_dict)
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

        conn = DatabaseManager.DatabaseConn()

        #print(conn)

        #chamar o Select

        sql = "SELECT value FROM responses"
        query = DatabaseManager.Select(conn, sql)


        #for result in query:
            #print(result)
            #print(result.find('{"coord":'))

        #print("\n\n\n\n\n\n\n")
        #byte_result = result[0]
        #string_result = str(byte_result)
        #x = string_result.strip('\\')
        #print(x)



        conn.close()


        if response.from_cache:
            print("%s returned from cache" % response_dict["name"])
            for i in all_responses_dict:
                print(i)
                print("\n")
            return(jsonify(all_responses_dict))
        else:
            all_responses_dict.append(response_dict)

            print("%s fetched from the Open Weather API... Caching it..." % response_dict["name"])

        # Cache lives for 5 minutes and then it is deleted
        if (end_time <= int(time.time())):
            start_time = end_time
            end_time = start_time + five_minutes
            all_responses_dict = []

        #return (response_dict)
        return("%s fetched from the Open Weather API... Caching it..." % response_dict["name"])
