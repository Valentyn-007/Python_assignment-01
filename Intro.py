import imp
import pyfiglet
import colorama
from colorama import Fore, Back, Style
colorama.init()

print("Hey you! Welcome to Python. I see you want to perform a calculation. Let's do this!")

First_num = input("Enter First Number: ")
Second_num = input("Enter Second Number: ")

inp_first_num = int(First_num)
inp_second_num = int(Second_num)
result = inp_first_num + inp_second_num

print(Fore.RED + "Your answer is: " + str(result))
print("Have a wonderful day!")
