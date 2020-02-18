def main():
    import smtplib
    user='modifiedtea@gmail.com'
    recipient = 'BubbleTea1$'
    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = 'test test test'
    TEXT = 'TEST TEST'

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")

if __name__ == '__main__' : 
    main()