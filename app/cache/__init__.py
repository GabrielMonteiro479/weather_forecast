import sqlite3
from sqlite3 import Error

class DatabaseManager(object):

    @classmethod
    def DatabaseConn(self):
        path = 'C:\\Users\\Gabriel\\Desktop\\repository\\weather_forecast\\app\\cache\\weather_forecast_cache.sqlite'
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
        return query
