import json
import yaml
import logging
import json_log_formatter
import random
from flask import Blueprint, jsonify, Flask, render_template
from http_helpers import return_response

# Load configuration file
with open("config/config.yaml", mode="r") as f:
    config = yaml.safe_load(f.read())

# Init logging
logger = logging.getLogger()
if config['logging']['level'] == "DEBUG":
    logger.setLevel(logging.INFO)
else:
    logger.setLevel(logging.INFO)
#logger.info('Example log', extra={'Example Key': 'Example Value'})

bp_api_generate = Blueprint("generate", __name__, url_prefix="/api")

@bp_api_generate.route("generate", methods=["GET"])
def generate_idea():

    data = {}
    data['thing'] = random.choice(config['things'])
    data['action'] = random.choice(config['actions'])
    data['item'] = random.choice(config['items'])
    data['language'] = random.choice(config['languages'])
    data['idea'] = f"How about, {data['thing']} that {data['action']} {data['item']}. Oh, and I could write the code in/using {data['language']}!"

    return return_response(0, "Successfully generated an obscure but probably awesome porject idea!", True, None, data, 200)