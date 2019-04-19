'''4.Design python application which creates three threads as small, capital, digits. All the
threads accepts string as parameter. Small thread display number of small characters,
capital thread display number of capital characters and digits thread display number of
digits. Display id and name of each thread.
'''
import threading
import os


def printSmall(*sampleStr):
    smallCount = 0
    for i in range(len(sampleStr)):
        if sampleStr[i].islower():
            smallCount += 1
    print("{} {} {}".format(smallCount, threading.current_thread().name, threading.get_ident()))


def printCapital(*sampleStr):
    capitalCount = 0
    for i in range(len(sampleStr)):
        if sampleStr[i].isupper():
            capitalCount += 1
    print("{} {} {}".format(capitalCount, threading.current_thread().name, threading.get_ident()))


def printDigit(*sampleStr):
    numCount = 0
    for i in range(len(sampleStr)):
        if sampleStr[i].isdigit():
            numCount += 1
    print("{} {} {}".format(numCount, threading.current_thread().name, threading.get_ident()))


sampleStr = "IndRaJitW70511111111ASINDkkansdlknasdndSNAKLS11"


thread1 = threading.Thread(target=printSmall, args=(sampleStr),)
thread2 = threading.Thread(target=printCapital, args=(sampleStr),)
thread3 = threading.Thread(target=printDigit, args=(sampleStr),)


thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()
