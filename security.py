import os
import json

def verify_slack_tocken(token):
    result = False
    if token == os.environ.get('SLACK_REQUEST_TOKEN', 'N/A'):
        result = True

    return result


def getrole(channel):
    role = 'none'
    accesslist = json.loads(os.environ.get('SECURITY_ROLES', 'N/A'))

    if channel in accesslist:
        role = accesslist[channel]

    return role