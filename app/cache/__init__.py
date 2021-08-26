#import time
import sqlite3
from sqlite3 import Error
from flask import jsonify



class DatabaseManager(object):

    @classmethod
    def DatabaseConn(self):
        path = 'C:\\Users\\Gabriel\\Desktop\\repository\\weather_forecast\\weather_forecast\\app\\cache\\weather_forecast_cache.sqlite'
        conn = None
        try:
            conn = sqlite3.connect(path)
        except Error as er:
            print(er)
        return (conn)

    @classmethod
    def Select(self, conn, sql):
        c = conn.cursor()
        c.execute(sql)
        query = c.fetchall()
        conn.close()
        return query


class Cache(object):

    @classmethod
    def __init__(self, response_dict):
        self.response_dict = response_dict

    @classmethod
    def Caching(self, all_responses_dict, cache_dict, city_name):
        # Inserting into cache method


        all_responses_dict.append(self.response_dict)
        cache_dict = dict(name = str(city_name), info = str(self.response_dict) )

        return(all_responses_dict, cache_dict)


    @classmethod
    def DeleteCache(self,all_responses_dict):
        # Cache lives for 5 minutes and then it is deleted

        all_responses_dict.clear()
        return(all_responses_dict)


    @classmethod
    def PrintCache(self,all_responses_dict):
        # Printing cache method. It returns the current cache in json format
        for i in all_responses_dict:
            print(i)
            print("\n")

        return(jsonify(all_responses_dict))
        #return(all_responses_dict)

    @classmethod
    def SearchCache(self,all_responses_dict,city_name):
        if city_name in all_responses_dict:
            return True
        else:
            return False
