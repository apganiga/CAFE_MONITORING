class Transaction:
    '''
    A single day Entry in the Google Sheet is passed to the class constructor as dictonary.
    '''

    def __init__(self, bussinessDate, dictionary):
        self.__dict__ = dictionary
        self.businessDate = bussinessDate #This should be second line or else it will be overwritten

    def __repr__(self):
        obj = "Transaction("
        for k in self.__dict__.keys() :
            obj += "{}={} |".format(k, self.__dict__[k])
        obj += ')'
        return obj


    def bankDepositDoneOnThisDay(self):
        if not hasattr(self, 'DepositedToBank') :
            return False
        else:
            return True