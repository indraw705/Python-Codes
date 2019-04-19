import threading


def evenFact(num):
   even = 0
   for i in range(len(num)):
      if num[i] % 2 == 0:
         even += num[i]
   print("even addition= {} \n".format(even))


def oddFact(num):
   odd = 0
   for i in range(len(num)):
      if num[i] % 2 != 0:
         # print(num[i])
         odd += num[i]
   print("odd addition= {}".format(odd))


if __name__ == "__main__":
   num = [1, 2, 4, 5, 45, 7, 4, 23, 34, 5, 6, 45, 4, 7, 4, 57, 5, 6, 72, 32, 9, 5, 789, 2, 4, 7, 50, 24]
   thread1 = threading.Thread(target=evenFact, args=(num,))
   thread2 = threading.Thread(target=oddFact, args=(num,))
   thread1.start()
   thread2.start()
