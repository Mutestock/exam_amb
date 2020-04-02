import sys
from logic.decorators import Decorators
import configparser

# logic goes here

@Decorators.determine_environment
def retrieve_environment():
    conf = configparser.ConfigParser()
    conf.read("./settings/configuration.ini")
    return conf["DEFAULT"]['ActiveEnvironment']
