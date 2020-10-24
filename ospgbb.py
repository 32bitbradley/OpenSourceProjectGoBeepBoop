import yaml
import logging
import json_log_formatter
import waitress
from flask import Flask, jsonify, Blueprint
from blueprints.api_core import bp_api_core
from blueprints.api_generate import bp_api_generate
from blueprints.page_index import bp_page_index


# Load configuration file
with open("config/config.yaml", mode="r") as f:
    config = yaml.safe_load(f.read())

# Init logging
formatter = json_log_formatter.JSONFormatter()
json_handler = logging.FileHandler(filename=config['logging']['location'])
json_handler.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(json_handler)
if config['logging']['level'] == "DEBUG":
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)
#logger.info('Example log', extra={'Example Key': 'Example Value'})

ospgbp = Flask(__name__)

ospgbp.register_blueprint(bp_api_core)
ospgbp.register_blueprint(bp_api_generate)
ospgbp.register_blueprint(bp_page_index)


if config == None:
    logger.error("No config file has been loaded.")

if __name__ == "__main__":

    if config['server']['debug'] == True:
        ospgbp.run(host=config['server']['host'], port=config['server']['port'], debug=True)
    else:
        waitress.serve(ospgbp, host=config['server']['host'], port=config['server']['port'])
