import threading


def evenFact(num):
    even = 0
    for i in range(1, num + 1):
        if num % i == 0:
            if i % 2 == 0:
                # print(i)
                even += i
    print("even addition= {} \n".format(even))


def oddFact(num):
    odd = 0
    for i in range(1, num + 1):
        if num % i == 0:
            if i % 2 != 0:
                # print(i)
                odd += i
    print("odd addition= {}".format(odd))


if __name__ == "__main__":
    num = 90
    thread1 = threading.Thread(target=evenFact, args=(num,))
    thread2 = threading.Thread(target=oddFact, args=(num,))
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print("exit from main")
