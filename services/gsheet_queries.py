import os
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import requests
import json


def gsheet_query(sid, rangeName, query):
    # If modifying these scopes, delete the file token.json.
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    # The ID and range of a sample spreadsheet.
    SAMPLE_SPREADSHEET_ID = os.environ.get('GSHEET_SAMPLE_SPREADSHEET_ID', 'N/A')
    SAMPLE_RANGE_NAME = os.environ.get('GSHEET_SAMPLE_RANGE_NAME', 'N/A')
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()), cache_discovery=False)
    # Call the Sheets API
    result = service.spreadsheets().values().get(spreadsheetId=sid, range=rangeName).execute()
    return result.get('values', [])

