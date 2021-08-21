from flask import Flask


def create_app(env):
    app = Flask(__name__)
    app.config.from_pyfile('config/%s.cfg' % env)

    return app

env = 'dev'

app = create_app(env)
#app.config.from_object('config')


from app.controllers import routes
