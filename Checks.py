import CommonUtils
from Transaction import Transaction

def isThereDifference(businessDate, OneDayTransaction):

    cashTans = OneDayTransaction.CashAtTheEnd
    nonCashTrans = OneDayTransaction.CardPaytm + OneDayTransaction.Swiggy
    expense = OneDayTransaction.CashExpenses
    difference = OneDayTransaction.TotalSale - (cashTans + nonCashTrans) - expense

    if difference == 0:
        CommonUtils.logging("Entered Transaction data matches for {}".format(businessDate))
    else:
        CommonUtils.logging("Amount Differing for {} is Rs.{}.00".format(businessDate, int(difference)))

def howMuchCashNotDepositedToBank(Last30Days):
    cashNotDepositedToBank = 0
    prevBD = CommonUtils.getDate(-1)
    for dayBefore in range(1 ,30) :
        dayBefore *= -1
        forBusinessDay = CommonUtils.getDate(dayBefore)
        eachDayTran = Transaction(forBusinessDay, Last30Days[forBusinessDay])
        cashNotDepositedToBank += eachDayTran.CashAtTheEnd
        if eachDayTran.bankDepositDoneOnThisDay() :
            break

    if cashNotDepositedToBank > 0 :
        CommonUtils.logging \
            ("Cash to be deposited to bank as of {} is Rs.{}.00".format(prevBD, int(cashNotDepositedToBank)))
    else:
        CommonUtils.logging("Cash deposit to bank as of {} is upto date".format(prevBD))




def sealingMachineCountMatch(t1transaction, t2transaction):
    # print(t1transaction)
    # print(t2transaction)
    try:
        totalSealings = t1transaction.SealingMcCount - t2transaction.SealingMcCount
        totalCupsSold = t1transaction.NoOfRegularCup + t1transaction.NoOfLargeCup
        diff = totalCupsSold == totalSealings
    except (KeyError,ArithmeticError, AttributeError) as er:
        print(er)
        print(t1transaction)
        print(t2transaction)

    if diff == 0  :
        CommonUtils.logging("Sealing Machines Counts Vs Number Of Cups Sold Matched")
    else:
        CommonUtils.logging("There is a difference of {} sealing".format(totalSealings - totalCupsSold))


