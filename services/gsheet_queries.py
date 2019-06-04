import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import logging

def query(sid, rangeName, query):

    logging.basicConfig()
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    scopes = ['https://spreadsheets.google.com/feeds']
    json_creds = os.environ.get('GSHEET_CREDS', 'N/A')

    #logger.info(json_creds)
    logger.info(sid)
    logger.info(rangeName)
    creds_dict = json.loads(json_creds)
    #logger.info("private key before :{}".format(creds_dict["private_key"]))
    creds_dict["private_key"] = creds_dict["private_key"].replace("\\\\n", "\n")
    #logger.info("private key after:{}".format(creds_dict["private_key"]))

    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scopes)
    client = gspread.authorize(creds)

    # Find a workbook by url
    spreadsheet = client.open_by_key(sid)
    result = spreadsheet.values_get(rangeName)

    return result.get('values', [])

