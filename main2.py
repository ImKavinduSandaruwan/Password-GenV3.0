#coded by Kavindu Sandaruwan
import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()}{?><:"
numbers = "1234567890"
password_list = []
final_password = ""

print("Wlcome to the PyPassword Generator!")
letter_amount = int(input("How many letters would you like in your password? \n"))
symbol_amount = int(input("How many symbols would you like? \n"))
numbers_amount = int(input("How many numbers would you like? \n"))

for i in range(letter_amount):
    x = random.choice(letters)
    password_list.append(x)

for i in range(symbol_amount):
    x = random.choice(symbols)
    password_list.append(x)

for i in range(numbers_amount):
    x = random.choice(numbers)
    password_list.append(x)

random.shuffle(password_list)
for i in password_list:
    final_password += i
print("Here is your password:",final_password)
