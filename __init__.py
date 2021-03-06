"""
VyPR analysis library.
Authors:
Marta Han - University of Zagreb, CERN
Joshua Dawes - University of Manchester, CERN.
"""
import json
import sys

from VyPRAnalysis.http_requests import VerdictServerConnection

config_dict = None
server_url = None
connection = None
vypr_path = "VyPRAnalysis"
monitored_service_path = None

sys.path.append(vypr_path)


def set_config_file(config_file_name='config.json'):
    """
    Given config_file_name, read the configuration.
    """
    global config_dict, server_url, monitored_service_path, vypr_path
    config_dict = json.loads(open(config_file_name).read())
    server_url = config_dict["verdict_server_url"]
    monitored_service_path = config_dict["monitored_service"]
    vypr_path = config_dict["vypr_path"]

    set_server(server_url)
    set_vypr_path(vypr_path)


def set_server(given_url):
    """
    server_url is a global variable which can be changed
    by passing a string to the set_server() function
    """
    global server_url, connection
    server_url = given_url
    # try to connect
    connection = VerdictServerConnection(server_url)
    try:
        response = connection.handshake()
    except:
        print("Failed to connect to server.")


def get_server():
    global server_url
    return server_url


def get_connection(handshake=False):
    global connection
    if get_server() is None:
        raise Exception("No verdict server set.")
    if handshake:
        # try the handshake - most of the time this will just be done
        # when the server is set initially during configuration
        response = connection.handshake()
    return connection


def set_vypr_path(path):
    global vypr_path
    vypr_path = path
    sys.path.append(vypr_path)


def get_monitored_service_path():
    global monitored_service_path
    return monitored_service_path


"""
Import all functions from various modules.
"""

from utils import *
from orm import *
