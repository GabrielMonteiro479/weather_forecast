#from app import app
#from app.controllers import routes
import sqlite3
from sqlite3 import Error

class DatabaseManager(object):

    @classmethod
    def DatabaseConn():
        path = 'C:\\Users\\Gabriel\\Desktop\\repository\\weather_forecast\\app\\cache\\weather_forecast_cache.sqlite'
        con = None
        try:
            con = sqlite3.connect(path)
        except Error as er:
            print(er)
        return (con)

    #vcon = DatabaseConn()

    #print(vcon)
    #vcon.close()
