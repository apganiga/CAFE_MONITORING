## Cafe Monitoring Automation
Bunch of python script written to monitor Google Sheet data entered in cafe. <br>
monitors below:
1. Transaction Reconciliation For the day: Meaning:<br>
Cash Transaction + SwiggyZomato + CardPayment - Expense = TotalTransaction


##Command
cd G:\CAFE_MONITOR

Command:
``` 
	python ExtractData.py DAILY_REPORT  A1:O500 
	python CafeMonitor.py DAILY_REPORT A1:O500 < main Wrapper
```
