from flask import Flask
import os
import logging
import json
import controller
from CommandRouter import CommandRouter
from flask import Response
from flask import request


application = Flask(__name__)
url_prefix = os.environ.get('URL_PREFIX','/dev')


@application.route(url_prefix+'/kalenzabot/', methods=['POST'])
def kalenzabot():
    bc = read_request()
    sync_response_text = controller.kalenzabot(bc)
    return build_response(sync_response_text)


@application.route(url_prefix+'/de/', methods=['POST'])
def de():
    bc = read_request()
    sync_response_text = controller.de(bc)
    return build_response(sync_response_text)


def read_request():
    body = request.get_data().decode('utf8')
    cr = CommandRouter(body)
    bc = cr.route_command()
    return bc


def build_response(sync_response_text):
    if sync_response_text is None:
        r = Response()
    else:
        r = Response(json.dumps({'response_type': 'in_channel', 'text': sync_response_text}, ensure_ascii=False),
                     content_type="application/json")
    return r


@application.route(url_prefix+'/test/', methods=['POST'])
def test():
    return os.environ.get('TEST_TOKEN','na')
