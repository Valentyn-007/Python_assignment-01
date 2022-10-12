# this is a simple program that adds two numbers together and prompts the user to enter the numbers one at a time.

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print("Hello there! Welcome to Python.")
print("I see you want to add up two numbers.")
print("Let's do this!")

First_num = input("Enter First Number: ")
Second_num = input("Enter Second Number: ")

inp_first_num = int(First_num)
inp_second_num = int(Second_num)
result = inp_first_num + inp_second_num

print(Fore.RED + Back.CYAN + "Your answer is: " + str(result))
print("Have a wonderful day!")
