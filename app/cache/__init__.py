#import time
import sqlite3
from sqlite3 import Error
from flask import jsonify
import os



class DatabaseManager(object):

    @classmethod
    def DatabaseConn(self):

        cache_path = '\\app\\cache\\weather_forecast_cache.sqlite'
        abs_path = os.path.abspath('') + cache_path
        #print(abs_path)
        conn = None
        try:
            conn = sqlite3.connect(abs_path)
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
    living_cache = []


    @staticmethod
    def GetCache():
        global living_cache

        return(living_cache)

    @staticmethod
    def SetCache(cached_data):
        global living_cache
        living_cache = cached_data

    @classmethod
    def __init__(self, response_dict):
        self.response_dict = response_dict

    @classmethod
    def Caching(self, all_responses_dict):
        # Inserting into cache method

        all_responses_dict.append(self.response_dict)


        return(all_responses_dict)


    @classmethod
    def DeleteCache(self,all_responses_dict):
        # Cache lives for 5 minutes and then it is deleted

        all_responses_dict.clear()
        return(all_responses_dict)
