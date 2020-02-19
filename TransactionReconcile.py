import CommonUtils


class Transaction:
    '''
    A single day Entry in the Google Sheet is passed to the class constructor as dictonary.
    '''

    def __init__(self, bussinessDate, dictionary):
        self.__dict__ = dictionary
        self.businessDate = bussinessDate #This should be second line or else it will be overwritten

    def isThereDifference(self):
        cashTans = self.CashAtTheEnd
        nonCashTrans = self.CardPaytm + self.Swiggy
        expense = self.CashExpenses
        difference = self.TotalSale - (cashTans + nonCashTrans) - expense

        if difference == 0 :
            CommonUtils.logging("Entered Transaction data matches for {}".format(self.businessDate))
        else:
            CommonUtils.logging("Amount Differing for {} is Rs.{}.00".format(self.businessDate, int(difference)))

    def bankDepositDoneOnThisDay(self):
        if not hasattr(self, 'DepositedToBank') :
            return False
        else:
            return True



