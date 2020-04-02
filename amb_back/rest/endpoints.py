import werkzeug

werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask
from flask_restplus import Api, Resource
from logic.decorators import Decorators
import configparser

app = Flask(__name__)
api = Api(app)
ns = api.namespace("rest", description="Assignment Rest")


@ns.route("/hi")
@api.response(404, "Nothing here but us lemmings")
class ResToFrom(Resource):
    def get(self):
        return {"msg": "hi"}

    def post(self):
        pass


@Decorators.determine_environment
def flask_run():
    conf = configparser.ConfigParser()
    conf.read("./settings/configuration.ini")
    if conf["DEFAULT"]["activeenvironment"] == "PRODUCTION":
        app.run(host="0.0.0.0")
    else:
        app.run(debug=True)
