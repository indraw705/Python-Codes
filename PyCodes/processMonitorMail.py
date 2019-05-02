import os
import time
import psutil
import smtplib
import schedule
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import urllib.request as urllib2


def is_connected():
    try:
        urllib2.urlopen("http://google.com", timeout=4)
        return True
    except urllib2.URLError as E:
        return False


def mailSender(filename, time):
    try:
        fromAddr = 'indrajitpractice@gmail.com'
        toAddr = 'indrajitnarvekar@gmail.com'
        msg = MIMEMultipart()
        msg['fromAddr'] = fromAddr
        msg['toAddr'] = toAddr

        body = '''
        Hello {}
        please find the attached document has logs of runnig processes
        Log file is created at : {}
        This is systerm generated mail do not reply to this mail

        Thanks & Regards
        IndraW705
        '''.format(toAddr, time)

        Subject = 'System process log generated at'

        msg['Subject'] = Subject
        msg.attach(MIMEText(body, 'plane'))
        attachment = open(filename, 'rb')
        p = MIMEBase('application', 'octate-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename = {}" .format(filename))
        msg.attach(p)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromAddr, "gmindraw705")
        text = msg.as_string()

        s.sendmail(fromAddr, toAddr, text)
        s.quit()
        print('mail sent successfully')

    except Exception as e:
        print("unable to send mail", e)


def processLog(log_dir="indra's"):
    listProcesses = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass
    separator = "=" * 80
    log_path = os.path.join(log_dir, "indraProc{}.log".format(time.ctime()))
    f = open(log_path, 'w')
    f.write(separator + "\n")
    f.write("process logger: " + time.ctime() + "\n")
    f.write(separator + "\n\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
            listProcesses.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    for element in listProcesses:
        f.write("{}\n".format(element))

    print("log file successfully generated at location {} ".format(log_path))

    connected = is_connected()

    if connected:
        mailSender(log_path, time.ctime())
    else:
        print('there is no internet connected')


def main():

    if (len(argv) != 2):
        print("Error : invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("this Application is designed for mailing the process logs")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : log file mail ")
        exit()

    try:
        schedule.every(int(argv[1])).minute.do(processLog)
        while(True):
            schedule.run_pending()
            time.sleep(1)
    except ValueError:
        print("invalid Data type of input")
    except Exception as e:
        print("Error : Invalid input", e)


if __name__ == '__main__':
    main()
