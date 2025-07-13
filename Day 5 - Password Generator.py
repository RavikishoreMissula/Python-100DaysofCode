import random

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','$','#','%','&','*','(',')','^']

print("Welcome to Password Generator!\n")
num_of_letters = int(input("Please enter how may letters needed in the password: "))
num_of_number = int(input("\nPlease enter how may numbers needed in the password: "))
num_of_symbols = int(input("\nPlease enter how may special characters needed in the password: "))

password_list = []

for letter in range(0, num_of_letters):
    password_list += random.choice(alphabets)

for letter in range(0, num_of_number):
    password_list += random.choice(numbers)

for letter in range(0, num_of_symbols):
    password_list += random.choice(symbols)

print(password_list)
random.shuffle(password_list)
#print("".join(password))

password = ""

for char in password_list:
    password += char

print(f'Your Password is: {password}')
