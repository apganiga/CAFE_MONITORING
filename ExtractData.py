
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

##Example Call: python ExtractData.py DAILY_REPORT  A1:E40

class ExtractData:
    def __init__(self, SHEET_NAME, RANGE_NAME):
        self.SHEET_NAME = SHEET_NAME
        self.RANGE_NAME = RANGE_NAME
        self.SPREADSHEET_ID = '17Jg_zAg5JlorqkZBAi1n3KfU_mFBU0bK3uuKt3YbQsE' # DAILY_OPERATIONS Sheet ID
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly'] # If modifying these scopes, delete the file token.pickle.
        self.creds = None
        self.datatype = { 'DAILY_REPORT': [ str,float,int,int,int,float,float,float,int,int,float,str,int,float,float ],
                           'Attendance': [str, str, str, str]
                          }
    # The file token.pickle stores the user's access and refresh tokens, and is created automatically when the authorization flow completes for the first  time.

    def downloadData(self):
        if os.path.exists('G:/CAFE_MONITOR/token.pickle') and os.path.getsize('G:/CAFE_MONITOR/token.pickle') == 0:
            print("Token.Pickle is Found with Zero byte.. Copying the backup...")
            copy('G:/CAFE_MONITOR/token_backup/token.pickle', 'G:/CAFE_MONITOR/')

        if os.path.exists('token.pickle') and os.path.getsize('token.pickle') > 0:
            print("Token.pickle found and is greater than Zero Byte")
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                self.flow = InstalledAppFlow.from_client_secrets_file('credentials.json', self.SCOPES)
                self.creds = self.flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)

        self.service = build('sheets', 'v4', credentials=self.creds)
        self.sheet = self.service.spreadsheets()   # Call the Sheets API
        self.result = self.sheet.values().get(spreadsheetId=self.SPREADSHEET_ID, range=self.SHEET_NAME + '!' + self.RANGE_NAME).execute()
        self.values = self.result.get('values', [])
        self.headers= self.values[0]
        self.headers = [ str(col).replace("\n",' ').title().replace(' ', "") for col in self.headers ]
        self.headers = [ re.sub(r'\W', '',header) for header in self.headers]
        print(self.headers, "<<<<<")
        self.values = self.values[1:]
        print("====>", self.datatype[self.SHEET_NAME])
        new_values = list()
        # We only take last 30 days data. This number is orbiatary. If requierd can be made more or less
        data_dict = OrderedDict()
        for each_day_record in self.values[len(self.values)-30:]:
            for lineno, val in enumerate(each_day_record) :
                try:
                    # Zippiing the Data Type and the Value split of each row.. cleansing the value and converting to data type
                    func = self.datatype[self.SHEET_NAME][lineno]
                    val = func(val.replace(',','').replace(' ','').replace("-",'0'))
                    key_2ndLevel = self.headers[lineno]
                    if lineno == 0 :
                        key_name = val
                        data_dict[key_name] = dict()
                    else:
                        data_dict[key_name][key_2ndLevel] = val
                    #new_values.append([func(v.replace(',','').replace(' ','').replace("-",'0')) for func,v in  zip(self.datatype[self.SHEET_NAME], val)])
                except ValueError as err:
                    print("Line {}:error={}".format(lineno, err))

        return data_dict

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('SheetName', type=str, help="Enter The Sheet Name:")
    parser.add_argument('Range', type=str, help="What Range You want to Extract:")
    args = parser.parse_args()
    data = ExtractData(args.SheetName, args.Range)
    report_data = data.downloadData()
    for line in report_data.keys():
        print(line, '==>>',report_data[line])