from __future__ import print_function
import pickle
import os.path
import sys
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import argparse
import re
from shutil import copy
from collections import OrderedDict
import yaml

##Example Call: python ExtractData.py DAILY_REPORT  A1:E40
class ExtractData:
    def __init__(self, SHEET_NAME, RANGE_NAME):
        self.SHEET_NAME = SHEET_NAME
        self.RANGE_NAME = RANGE_NAME

        # self.SPREADSHEET_ID = '17Jg_zAg5JlorqkZBAi1n3KfU_mFBU0bK3uuKt3YbQsE' # DAILY_OPERATIONS Sheet ID
        self.SPREADSHEET_ID = os.environ['md_' + self.SHEET_NAME + '_SHEET_ID']
        self.secrets_dir = os.environ['md_secrets_dir']
        self.secrets_backup_dir = os.environ['md_secrets_backup_dir']
        self.token_file = self.secrets_dir + '/token.pickle'
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly'] # If modifying these scopes, delete the file token.pickle.
        self.creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is created automatically when the authorization flow completes for the first  time.

    def downloadData(self):
        if os.path.exists(self.token_file) and os.path.getsize(self.token_file) == 0:
            print("Token.Pickle is Found with Zero byte.. Copying the backup...")
            copy(self.secrets_backup_dir + '/token.pickle', self.secrets_dir + '/')

        if os.path.exists(self.token_file) and os.path.getsize(self.token_file) > 0:
            # print("Token.pickle found and is greater than Zero Byte")
            with open(self.token_file, 'rb') as token:
                self.creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                self.flow = InstalledAppFlow.from_client_secrets_file(self.secrets_dir + '/credentials.json', self.SCOPES)
                self.creds = self.flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(self.token_file, 'wb') as token:
                pickle.dump(self.creds, token)

        self.service = build('sheets', 'v4', credentials=self.creds)
        self.sheet = self.service.spreadsheets()   # Call the Sheets API
        self.result = self.sheet.values().get(spreadsheetId=self.SPREADSHEET_ID, range=self.SHEET_NAME + '!' + self.RANGE_NAME).execute()
        self.values = self.result.get('values', [])
        return self.values

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('SheetName', type=str, help="Enter The Sheet Name:")
    parser.add_argument('Range', type=str, help="What Range You want to Extract:")
    args = parser.parse_args()
    data = ExtractData(args.SheetName, args.Range)
    report_data = data.downloadData()
    for line in report_data.keys():
        print(line, '==>>',report_data[line])