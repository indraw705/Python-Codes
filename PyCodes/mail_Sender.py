from sys import *
import time
import smtplib
import urllib.request as urllib2


def is_connected():
    try:
        urllib2.urlopen("http://google.com", timeout=4)
        return True
    except urllib2.URLError as E:
        return False


def mailSender(gmail_usr, gmail_pwd):
    sendFrom = gmail_usr
    to = "indrajitnarvekar@gmail.com"
    emailText = 'Hey Indrajit this is mail sent from a python program dont reply to this thanks buddy!!!!'
    try:

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        print("HI")
        server.ehlo()
        server.login(gmail_usr, gmail_pwd)
        server.sendmail(sendFrom, to, emailText)
        server.close()
        print("mail sent successfully")
    except Exception as E:
        print(E)
        print("unable to send mail")


def main():
    print("Application Name+++++++++++>", argv[0])
    try:
        gmail_usr = "indrajitpractice@gmail.com"
        gmail_pwd = "gmindraw705"
        connected = is_connected()
        print("internet on")
        print(connected)
        if connected:
            mailSender(gmail_usr, gmail_pwd)

    except Exception as E:
        print("check your internet Connection")


if __name__ == '__main__':
    main()
