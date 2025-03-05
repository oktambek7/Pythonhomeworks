#Qestions

#Q1. What is the difference between the continue and break statements in Python?

#break stops a loop once its condition is met, while continue skips over the current iteration of a loop and continues to the next iteration based on its condition

#Q2.Can you explain the difference between for loop and while loop?

#A "for loop" is used when you know exactly how many times you want to repeat a block of code, while a "while loop" is used when you want to repeat a block of code until a certain condition becomes false

#Q3.How would you implement a nested for loop system? Provide an example.

a=10
b=3
c=-4
if b>0:
    if a>5:
        print("True")
else:
    print("False")
    
#TASKS that go with creating program:
   
#1.Return uncommon elements of lists. Order of elements does not matter.

my_list1=[1,2,2,3,4,4]
my_list2=[5,5,6,7,7,8]

set1=set(my_list1)
set2=set(my_list2)

uncommon_elements=set1.symmetric_difference(set2)
print(list(uncommon_elements))

"""
input:
    list1 = [1, 1, 2]
    list2 = [2, 3, 4]
output: [1, 1, 3, 4]
"""
list1 = [1, 1, 2]
list2 = [2, 3, 4]

uncommon1=[num for num in list1 if num not in list2]

uncommon2=[num for num in list2 if num not in list1]

uncommon_elements=uncommon1 + uncommon2

print(uncommon_elements)

""""
input:
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
output: [1, 2, 3, 4, 5, 6]

"""
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combine_elements=list1 + list2
print(combine_elements)

"""
input:
    list1 = [1, 1, 2, 3, 4, 2]
    list2 = [1, 3, 4, 5]
output: [2, 2, 5]

"""

list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]

uncommon1=[num for num in list1 if num not in list2]

uncommon2=[num for num in list2 if num not in list1]

combine=uncommon1 + uncommon2

print(combine)

#2.Print the square of each number which is less than n on a separate line.

"""
input: n = 5
output:
    1
    4
    9
    16
"""
n=5
for n in range(1, n):
    print(n**2)
    
#3.txt nomli string saqlovchi o'zgaruvchi berilgan. txtdagi har uchinchi belgidan keyin pastgi chiziqcha (underscore) qo'yilsin. Agar belgi unli harf yoki orqasidan ostki chiziqcha qo'yilgan harf bo'lsa, ostki chiziqcha keyingi harfdan keyin qo'yilsin. Agar belgi satrdagi oxirgi belgi bo'lsa chiziqcha qo'yilmasin.

'''
input: hello
output: hel_lo
'''
s = "hello"
print(s[:len(s)//2] + "_" + s[len(s)//2:])

'''
input: assalom
output: ass_alom
'''
w="assalom"
print(w[:len(w)//2]+"_"+w[len(w)//2:])


'''
input: abcabcdabcdeabcdefabcdefg
output: abc_abcd_abcdeab_cdef_abcdefg
'''





#4.Number Guessing Game Create a simple number guessing game.

#The computer randomly selects a number between 1 and 100.

import random

number=random.randint(1,100)
print("Randomly selected number is: ", number)

#If the guess is high, print "Too high!".

import random

number=random.randint(1, 150)
print("Randomly selected number is: ", number)
if number>100:
    print("Too high !")
        
#If the guess is low, print "Too low!".

import random
number=random.randint(1, 150)
print("Randomly selected number is: ", number)
if number<100:
    print("Too low !")

#If they guess correctly, print "You guessed it right!" and exit the loop.

import random
number=random.randint(1,50)
if number>25 and number<30:
    print("You guessed it right!") 
else:
    print(number)

#The player has 10 attempts to guess it. If the player can not find the correct number in 10 attempts, print "You lost. Want to play again? ".

import random

def play_game():
    number = random.randint(1, 100)  # Generate a random number
    attempts = 10  # Maximum attempts allowed

    for i in range(attempts):
        try:
            guess = int(input(f"Attempt {i+1}/10 - Enter your guess: "))

            if guess == number:
                print(f" Congratulations! You guessed the number {number} in {i+1} attempts!")
                break  # Exit loop if guessed correctly
            elif guess < number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

        except ValueError:
            print("Invalid input! Please enter a number.")

    else:
        print(f" You lost! The correct number was {number}.")




#If the player types one of 'Y', 'YES', 'y', 'yes', 'ok' then start the game from the beginning.

import random

def play_game():
    number = random.randint(1, 100)  # Generate a random number
    attempts = 10  # Maximum attempts allowed

    for i in range(attempts):
        try:
            guess = int(input(f"Attempt {i+1}/10 - Enter your guess: "))

            if guess == number:
                print(f" Congratulations! You guessed the number {number} in {i+1} attempts!")
                break  # Exit loop if guessed correctly
            elif guess < number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

        except ValueError:
            print("Invalid input! Please enter a number.")

    else:
        print(f" You lost! The correct number was {number}.")

    restart = input("Want to play again? (Y/YES/ok to restart): ").strip().lower()
    if restart in ['y', 'yes', 'ok']:
        play_game()  # Restart the game

# Start the game
play_game()


#5.Password Checker Task: Create a simple password checker.

def password_checker():
    password = input("Enter the password: ")

    # Check if password length is less than 8
    if len(password) < 8:
        print("Password is too short. It must be at least 8 characters.")
        return  # Exit function if condition fails

    # Check if password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
        return  # Exit function if condition fails

    print("Password is strong!")  # If both conditions are met

# Run the password checker
password_checker()

#6.Prime Numbers Task: Write a Python program that prints all prime numbers between 1 and 100.

def is_prime(n):
    if n < 2:
        return False 
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_prime_numbers():
    print("Pritme numbers beween 1 and 100:")
    for num in range(1, 101): 
        if is_prime(num):
            print(num, end=" ")
print_prime_numbers()

        
        
       
       


    










