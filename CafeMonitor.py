import argparse
from ExtractData import ExtractData
import CommonUtils
from Transaction import Transaction
import TwillioMessaging as tm
import os
import Checks
import yaml

def loadMaskedDataToEnvironment():
    with open('G:\CAFE_MONITOR\drowssap\MaskedData.yml','r') as masked_data:
        secrets = yaml.load(masked_data,Loader=yaml.FullLoader)
    for secret in secrets.keys():
        # print("{} = {}".format(secret, secrets[secret]))
        os.environ[secret] = secrets[secret]

if __name__ == '__main__' :
    parser = argparse.ArgumentParser()
    parser.add_argument('SheetName', type=str, help="Enter The Sheet Name:")
    parser.add_argument('Range', type=str, help="What Range You want to Extract:")
    args = parser.parse_args()

    loadMaskedDataToEnvironment()

    ed = ExtractData(args.SheetName, args.Range)
    Last30Days = ed.downloadData()

## Check1: Check if Data Entered is Valid
    T1date = CommonUtils.getDate(-1)
    t1Transaction = Transaction(T1date, Last30Days[T1date])
    Checks.isThereDifference(T1date, t1Transaction)

## Check2: How much cash pending for deposit
    Checks.howMuchCashNotDepositedToBank(Last30Days)

## Check3: Sealing Machine Count
    T2date = CommonUtils.getDate(-2)
    t2Transaction = Transaction(T2date, Last30Days[T2date])
    Checks.sealingMachineCountMatch(t1Transaction, t2Transaction)

### Send WhatsApp Message
    tm.SendWhatsUpReport()