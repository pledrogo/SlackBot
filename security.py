import os

def verify_slack_tocken(token):
    result = False
    if token == os.environ.get('SLACK_REQUEST_TOKEN', 'N/A'):
        result = True
    return result


def getrole(channel):
    role = 'none'
    if channel in ['G060NTEDN', 'GDZRVNS8Y']:
        role = 'manager'
    elif channel in ['GBEC535K7', 'G14SAGW9W', 'C6EUPLBDM', 'GDZRVNS8Y', 'GE9EENXSP', 'GAHCZ11GU']:
        role = 'de'

    return role