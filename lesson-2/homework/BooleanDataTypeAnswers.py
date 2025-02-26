#1.Write a program that accepts a username and password and checks if both are not empty.

username=input("Enter username:")
password=input("Enter password:")
if username==""or password=="":
    print("Error.")
else:
    print("Credentials are valid.")

#2.Create a program that checks if two numbers are equal and outputs a message if they are.
first_num=input('Enter first number:')
second_num=input('Enter second number:')
if first_num==second_num:
    print('They are aqual')
else:
    print('They are not equal.')
#3.Write a program that checks if a number is positive and even.

a=int(input('Enter number:'))
if a>0 and a%2==0:
 print(f'{a} is is both positive and even.')
else:
 print(f'{a} is not even number.')

 #4.Write a program that takes three numbers and checks if all of them are different.
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
if a==b==c:
   print("They are same")
else:
   print("They are different")

#5.Create a program that accepts two strings and checks if they have the same length.

string_first=input("Enter 1st word:")
string_second=input("Enter 2nd word:")
if len(string_first)==len(string_second):
   print("They have the same lenghs.")
else:
   print("They have different lenghs.")

#6.Create a program that accepts a number and checks if it’s divisible by both 3 and 5.

a=int(input("Enter number"))
if a%3==0 and a%5==0:
 print("a is divisable to both 3 and 5")
else:
   print("Error")

#7.Write a program that checks if the sum of two numbers is greater than 50.8. Create a program that checks if a given number is between 10 and 20 (inclusive)

#part 1
first_num=int(input("Enter num1: "))
second_num=int(input("Eneter num2: "))
if (first_num)+(second_num)>50.8:
   print("yes")
else:
   print("No")

#part 2
a=int(input("Enter number"))
if 10 <= a <= 20:
   print("yes")
else:
   print("No")




               
