import argparse
from ExtractData_test import ExtractData
import CommonUtils
from Transaction import Transaction
import TwillioMessaging as tm
import os
import Checks
import yaml
import pandas as pd

def loadMaskedDataToEnvironment():
    with open('G:\CAFE_MONITOR\drowssap\MaskedData.yml','r') as masked_data:
        secrets = yaml.load(masked_data,Loader=yaml.FullLoader)
    for secret in secrets.keys():
        os.environ[secret] = secrets[secret]

if __name__ == '__main__' :
    parser = argparse.ArgumentParser()
    parser.add_argument('SheetName', type=str, help="Enter The Sheet Name:")
    parser.add_argument('Range', type=str, help="What Range You want to Extract:")
    args = parser.parse_args()

    loadMaskedDataToEnvironment()

    ed = ExtractData(args.SheetName, args.Range)
    Last30Days = pd.DataFrame(ed.downloadData(), )

    print(Last30Days)
       # print(eachDayData)