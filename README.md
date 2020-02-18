## Cafe Monitoring Automation
Bunch of python script written to monitor Google Sheet data entered in cafe. <br>
monitors below:



##Command
cd G:\CAFE_MONITOR

Command:
``` 
	python ExtractData.py DAILY_REPORT  A1:O500 
	python CafeMonitor.py DAILY_REPORT A1:O500 < main Wrapper
```
### Assumption Made:
1. This Report Will run every day Singapore morning around 8AM (This time I will be home, so the Whatsapp connection can work if required)

### Reconciliations and Checks:
1. If the Data for previous Business Day has been entered. (This will be 99.99% done, but still need to be done)
2. Transaction Reconciliation For the Previous Business day: <br>
    ___Cash Transaction + SwiggyZomato + CardPayment - Expense = TotalTransaction___