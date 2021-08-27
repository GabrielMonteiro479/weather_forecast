import json
import requests
from flask import Flask, jsonify


class ServiceConfig(object):

    __city_name =  None
    __API_KEY = '16a4e389cf047f7f684e17a5c84db9b2'
    __STD_URL = 'http://api.openweathermap.org/data/2.5/weather?'

    @classmethod
    def get_city(self, city_name):
        self.__city_name = city_name


    @classmethod
    def generate_complete_url(self):
        COMPLETE_URL = self.__STD_URL + 'q=' + self.__city_name + '&appid=' + self.__API_KEY

        return COMPLETE_URL

    @classmethod
    def generate_json_object(self, COMPLETE_URL):
        response = requests.get(COMPLETE_URL)
        response_dict = response.json()

        return (response, response_dict)
