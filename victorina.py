import random
from random import randint
n = randint(0, 100)
guess = 5
lang = input('EN/RUS?')
if lang == 'RUS' or lang == 'rus':
    print("Угадаешь число?")
    print("Поехали..")
    a = input("число")
    for i in range(guess):
        if int(a) < n:
            print("Мало!")
            guess = guess - 1
            a = input()
        elif int(a) > n:
            print("Много!")
            guess = guess - 1
            a = input()
        else:
            print("Ты угадал!")
        if guess == 0:
            print("Ты проиграл!")
            print("число - ", n)
elif lang == 'EN' or lang == 'en':
    print("Can you guess the number?")
    print("Let's go!")
    a = input("number..")
    for i in range(guess):
        if int(a) < n:
            print("so little!")
            guess = guess - 1
            a = input()
        elif int(a) > n:
            print("so many!")
            guess = guess - 1
            a = input()
        else:
            print("You are right!")
        if guess == 0:
            print("You lose!")
            print("number - ", n)