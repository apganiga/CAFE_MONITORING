from twilio.rest import Client
import CommonUtils
import yaml
import os

def SendWhatsUpReport():
    account_sid = os.environ['md_twillio_account_sid']
    auth_token = os.environ['md_twillio_auth_token']
    report_dir = os.environ['md_report_dir']
    whatsapp_to_number = os.environ['md_whatsapp_to_number']

    client = Client(account_sid, auth_token)

    today_date = CommonUtils.getDate(0)
    report_file = report_dir + '\REPORT_' + today_date.replace('/', '_') + '.dat'
    with open(report_file, 'r') as fh:
        msg_body = fh.readlines()

    message = client.messages.create(
        # from_='whatsapp:+6597894065',
        from_='whatsapp:+14155238886',
        body= '\n'.join(msg_body),
        to='whatsapp:' + whatsapp_to_number
    )

    print(message.sid)