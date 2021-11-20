import random
import os
import sys


def addition():

        print("Addition Calculator")

        number = int(input("Enter number: "))
        number2 = int(input("Enter second number: "))
        sum = number + number2

        print("Answer: ", sum)
        print("Repeat?: ")
        con()

def con():
        confir=input("Y / N: ").upper()
        if confir=="Y":
            print("Option accepted")
            addition()
        elif confir=="N":
            print("Option accepted")
            choose()
        else:
            print("Invalid response, please retry")
            con()


def subtraction():

        print("Subtraction Calculator")

        number = int(input("Enter number: "))
        number2 = int(input("Enter second number: "))
        sum = number - number2

        print("Answer: ", sum)
        print("Repeat?: ")
        con2()

def con2():
        confir2=input("Y / N: ").upper()
        if confir2=="Y":
            print("Option accepted")
            subtraction()
        elif confir2=="N":
            print("Option accepted")
            choose()
        else:
            print("Invalid response, please retry")
            con2()


def multiplication():

        print("Multiplication Calculator")

        number = int(input("Enter number: "))
        number2 = int(input("Enter second number: "))
        sum = number * number2

        print("Answer: ", sum)
        print("Repeat?: ")
        con3()

def con3():
        confir3=input("Y / N: ").upper()
        if confir3=="Y":
            print("Option accepted")
            multiplication()
        elif confir3=="N":
            print("Option accepted")
            choose()
        else:
            print("Invalid response, please retry")
            con3()


def division():

        print("Division Calculator")

        number = int(input("Enter number: "))
        number2 = int(input("Enter second number: "))
        sum = number / number2

        print("Answer: ", sum)
        print("Repeat?: ")
        con4()

def con4():
        confir4=input("Y / N: ").upper()
        if confir4=="Y":
            print("Option accepted")
            division()
        elif confir4=="N":
            print("Option accepted")
            choose()
        else:
            print("Invalid response, please retry")
            con4()


def choose():

    choice = input("Addition (A), Subtraction (S), Multiplication (M), Division (D), Exit (X): ").upper()
    if choice == 'A':
        addition()
    elif choice == 'S':
        subtraction()
    elif choice == 'M':
        multiplication()
    elif choice == 'D':
        division()
    elif choice == 'X':
        sys.exit()
    else:
        choose()

choose()
