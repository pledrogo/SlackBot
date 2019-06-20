import os
import json
import logging


def auth_by_token(f):
    def wrapper(x):
        logging.basicConfig()
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        print(x)
        logger.info("token verification:{}".format(x.token))
        if not verify_slack_tocken(x.token):
            raise Exception("not allowed")
        else:
            return f(x)
    return wrapper


def verify_slack_tocken(token):
    result = False
    if token == os.environ.get('SLACK_REQUEST_TOKEN', 'N/A'):
        result = True

    return result


def get_role(channel):

    role = "NONE"

    accesslist = json.loads(os.environ.get('SECURITY_ROLES', 'N/A'))

    if channel in accesslist:
        role = accesslist[channel]

    return role