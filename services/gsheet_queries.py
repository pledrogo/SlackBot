import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

def query(sid, rangeName, query):


    scopes = ['https://spreadsheets.google.com/feeds']
    json_creds = os.environ.get('GSHEET_CREDS', 'N/A')

    creds_dict = json.loads(json_creds)
    creds_dict["private_key"] = creds_dict["private_key"].replace("\\\\n", "\n")

    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scopes)
    client = gspread.authorize(creds)

    # Find a workbook by url
    spreadsheet = client.open_by_key(sid)
    result = spreadsheet.values_get(rangeName)

    return result.get('values', [])

