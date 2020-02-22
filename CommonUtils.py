import datetime
import os

def getDate(dayMinus) :
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

def logging(msg, mode='text') :
    today_date = getDate(0)
    report_file =  os.environ['md_report_dir'] + '/REPORT_' + today_date.replace('/','_') + '.dat'
    with open(report_file, 'a') as fh:
        if mode == 'text':
            print(msg)
            print(msg,file=fh)