import requests_cache
from flask import Flask


def create_app(env):
    app = Flask(__name__)
    app.config.from_pyfile('config/%s.cfg' % env)

    return app

env = 'dev'

app = create_app(env)
#app.config.from_object('config')
requests_cache.install_cache('weather_forecast_cache', backend='sqlite', expire_after= 300) #300 = 5 minutes

from app.controllers import routes
