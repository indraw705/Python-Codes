"""
hackerEarth
https://www.hackerrank.com/challenges/30-inheritance/problem
"""


class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        result = functools.reduce(lambda no1, no2: (no1 + no2), self.scores)
        result = float(result) / len(scores)
        print(result)
        if 90 <= result <= 100:
            return "O"
        elif 80 <= result < 90:
            return "E"
        elif 70 <= result < 80:
            return "A"
        elif 55 <= result < 70:
            return "P"
        elif 40 <= result < 55:
            return "D"
        elif result < 40:
            return "T"

     #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here


    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
import functools
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
