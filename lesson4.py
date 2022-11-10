#try, except, finaly, else


# try:
#     input_number = int(input())
#     number = 13 / input_number
#     print(number)
# except ZeroDivisionError as err:
#     number = 13 /1
#     print(number, err)
# except ValueError as err:
#     number = 15
#     print(number, err)
# except (ZeroDivisionError, ValueError):
#     number = 13 / 1
#     print(number)


# try:
#     a = dict() + 5
# except TypeError as err:
#     print(err)
# finally:
#     print("always do")

# try:
#     file = open("text.txt", "r")
#     print(file.read())
# except FileNotFoundError as err:
#     file = open("text.txt", "a+")
#     for i in range(1, 101):
#         file.write(f"{i} ")
#     file.seek(0)
#     print(file.read(), err)
#     file.close()


# import random
# from random import randint, random
from random import *

# a = randint(1, 16)
# print(a)
# random_number = random() #from 0 to 1
# print(random_number)
# range_random = randrange(1, 15, 3)
# print(range_random)
# listt = ["a", "b", "c", "d"]
# print(choice(listt))
# shuffle(listt)
# print(listt)
# print(choices(listt, [6, 1, 1, 3], k=15))

file = open("text.txt", "r")
list_names = file.read().split("\n")
print(list_names)
team_number = 1
counter = 0
while True:
    if len(list_names) == 0:
        raise Exception("list is empty")
        break
    if counter == 2:
        counter = 0
        team_number += 1
        continue
    name = choice(list_names)
    with open(f"team{team_number}.txt", "a") as file:
        print(name)
        file.write(f"{name}\n")
        counter += 1
        list_names.remove(name)





