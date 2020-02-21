import random
from random import randint
n = randint(0, 100)
guess = 5
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