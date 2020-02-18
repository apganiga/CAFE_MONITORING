import argparse
from ExtractData import ExtractData
import CommonUtils

if __name__ == '__main__' :
    parser = argparse.ArgumentParser()
    parser.add_argument('SheetName', type=str, help="Enter The Sheet Name:")
    parser.add_argument('Range', type=str, help="What Range You want to Extract:")
    args = parser.parse_args()
    ed = ExtractData(args.SheetName, args.Range)
    Last30Days = ed.downloadData()
    prevBD = CommonUtils.__getDate(-3)
    print(prevBD)
    try:
        prevDayDict = Last30Days[prevBD]
    except KeyError:
        CommonUtils.__logging("Sheet not updated for {}".format(prevBD))

    cashTans = prevDayDict['CashAtTheEnd']
    nonCashTrans = prevDayDict['CardPaytm'] + prevDayDict['Swiggy']
    expense = prevDayDict['CashExpenses']
    difference = prevDayDict['TotalSale'] - ( cashTans + nonCashTrans) - expense
    CommonUtils.__logging("Amount Differing for {} is Rs.{}.00".format(prevBD, int(difference)))


