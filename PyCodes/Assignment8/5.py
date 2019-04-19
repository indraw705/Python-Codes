'''5.Design python application which contains two threads named as thread1 and thread2.
Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on
screen. After execution of thread1 gets completed then schedule thread2.'''

import threading


def printASC():
    for i in range(51):
        print(i),


def printDESC():
    for i in range(50, 0, -1):
        print(i),


thread1 = threading.Thread(target=printASC)
thread2 = threading.Thread(target=printDESC)


thread1.start()
thread1.join()
thread2.start()
thread2.join()
