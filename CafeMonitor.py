import argparse
from ExtractData import ExtractData
import CommonUtils
from TransactionReconcile import Transaction
import TwillioMessaging as tm

if __name__ == '__main__' :
    parser = argparse.ArgumentParser()
    parser.add_argument('SheetName', type=str, help="Enter The Sheet Name:")
    parser.add_argument('Range', type=str, help="What Range You want to Extract:")
    args = parser.parse_args()

    ed = ExtractData(args.SheetName, args.Range)
    Last30Days = ed.downloadData()
    # print(Last30Days)
    # exit()

    prevBD = CommonUtils.getDate(-1)
    yesterdayTransaction = Transaction(prevBD, Last30Days[prevBD])
    yesterdayTransaction.isThereDifference()

    cashNotDepositedToBank = 0
    for dayBefore in range(1,30) :
        dayBefore *= -1
        forBusinessDay = CommonUtils.getDate(dayBefore)
        eachDayTran = Transaction(forBusinessDay, Last30Days[forBusinessDay])
        cashNotDepositedToBank += eachDayTran.CashAtTheEnd
        if eachDayTran.bankDepositDoneOnThisDay() :
            break

    if cashNotDepositedToBank > 0 :
        CommonUtils.logging("Cash to be deposited to bank as of {} is Rs.{}.00".format(prevBD, int(cashNotDepositedToBank)))
    else:
        CommonUtils.logging("Cash deposit to bank as of {} is upto date".format(prevBD))

    tm.SendWhatsUpReport()









