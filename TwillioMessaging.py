from twilio.rest import Client
import CommonUtils

def SendWhatsUpReport():
    account_sid = 'AC91dc806a2552d64a68b4427e323dc12a'
    auth_token = '89d7e1600fb0cffeeaaac119fa802f46'
    client = Client(account_sid, auth_token)

    today_date = CommonUtils.getDate(0)
    report_file = 'G:\CAFE_MONITOR\DAILY_REPORT\REPORT_' + today_date.replace('/', '_') + '.dat'
    with open(report_file, 'r') as fh:
        msg_body = fh.readlines()

    message = client.messages.create(
        # from_='whatsapp:+6597894065',
        from_='whatsapp:+14155238886',
        body= '\n'.join(msg_body),
        to='whatsapp:+6597894065'
    )

    print(message.sid)