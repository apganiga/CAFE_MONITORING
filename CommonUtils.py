import datetime

def __getDate(dayMinus) :
    '''
    :param dayMinus: No. of day to be subtracted
    :returns String formatted dd/mm/yyyy:
    '''
    dayMinus *= -1
    #### Getting the previous day #################
    today = datetime.datetime.today()
    previousDay = today - datetime.timedelta(dayMinus)
    prevBD = previousDay.strftime("%d/%m/%Y")
    return prevBD
#################################################

def __logging(msg, mode='text') :
    if mode == 'text':
        print(msg)