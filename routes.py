from flask import Flask
import os
import logging
import security
import controller
from flask import Response
from urllib.parse import parse_qs

from services import slack_queries as slack

application = Flask(__name__)
url_prefix = os.environ.get('URL_PREFIX','/Z3AELDdzzE09KLk210jNbcDuY8jnd0823x42zARkdQCVx0Lm')


@application.route(url_prefix+'/kalenzabot/', methods=['POST'])
def kalenzabot():

    body = request.get_data().decode('utf8')
    text = ' '
    token = ''
    channel = ''

    logging.basicConfig()
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    logger.info("body:{}".format(body))
    print("body:{}".format(body))

    payload = parse_qs(body)
    logger.info("payload:{}".format(payload))

    print(payload.keys())
    if 'text' in payload.keys():
        text = payload['text'][0]
    if 'token' in payload.keys():
        token = payload['token'][0]
    if 'channel_id' in payload.keys():
        channel = payload['channel_id'][0]

    if security.verify_slack_tocken(token):
        role = security.getrole(channel)
        response = controller.kalenzabot(role, text)
        logger.info("response:{}".format(response))
    else:
        return "not allowed"

    async_msg = slack.send(channel, response['text'], response['username'], response['icon_url'])

    logger.info("async status:{}".format(asyncMsg))

    if (async_msg):
        syncMsg = Response()
    else:
        syncMsg = Response(
            json.dumps({'response_type': 'in_channel', 'text': response['text']}, ensure_ascii=False),
            content_type="application/json")

    logger.info("sync msg:{}".format(syncMsg))

    return syncMsg


@application.route(url_prefix+'/test/', methods=['POST'])
def test():
    return os.environ.get('TEST_TOKEN','na')
