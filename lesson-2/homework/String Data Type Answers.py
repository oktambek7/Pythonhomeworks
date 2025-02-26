#1.Create a program to ask name and year of birth from user and tell them their age.

name = input("What is your name? ")
age = int(input("Age: "))
print("Your name is" + name + "and you are" + str(age) + "years old.")
print(f"Your name is {name} and you are {age} years old.")

#2.Extract car names from this text: txt = 'LMaasleitbtui'
txt = 'LMaasleitbtui'

#3. Write a Python program to Take a string input from the user.
    #Print the length of the string.
    #Convert the string to uppercase and lowercase

a=input("Enter a word:")
print(len(a))
print(a.upper())
print(a.lower())

#4.Write a Python program to check if a given string is palindrome or not.
txt = input("Enter a string to check if it is a palindrome: ")
def is_palindrome(txt):
    if txt==txt[::-1]:
        return True
    else:
        return False

if is_palindrome(txt):
    print(f"Yes")
else:
    print("no")\
#5.Write a program that counts the number of vowels and consonants in a given string.
text = 'fdwefdwfwaf wefdawesdf aEdde'
print(text.count('a'))
print(text.count('w'))
print(text.count('f'))
#6.Write a Python program to check if one string contains another.
def contains_substring(main_string, sub_string):
    if sub_string in main_string:
        return True
    else:
        return False
main_string = input("Enter the main string:")
sub_string = input("Enter the substring to check:")
if contains_substring(main_string, sub_string):
    print(f"'{sub_string}' is found in '{main_string}'.")
else:
    print(f"'{sub_string}' is not found in '{main_string}'.")

#7.Ask the user to input a sentence and a word to replace. Replace that word with another word provided by the user.
matn = 'My name is Oktam'
print(matn.replace('Oktam', 'Oybek'))

#8.Write a program that asks the user for a string and prints the first and last characters of the string.

a=input("Enter a word:")
first_char=a[0]
last_char=a[-1]
print(f"The first character is: {first_char}")
print(f"The last character is: {last_char}")

#9.Ask the user for a string and print the reversed version of it.
word = input("Enter word:")
word_reverse=word[::-1]
print(f'{word_reverse=}')
print(word==word_reverse)
#10.Write a program that asks the user for a sentence and prints the number of words in it.
word=input("Enter word:")
num_of_words=len(word)
print(f"The number of words in the sentence is:{num_of_words}")

#11.Write a program to check if a string contains any digits.

def contains_digits(s):
    for char in s:
        if char.isdigit():
            return True
        return False
    
user_string=input("Entera string:")
if contains_digits(user_string):
    print("The string contains digits.")
else:
    print("The string does not contain any digits.")
#12.Write a program that takes a list of words and joins them into a single string, separated by a character.
a = [1,2,3,4]
a.append(5)
print(a)

#13.Ask the user for a string and remove all spaces from it.

sentence=input('Enter string:')
remove_space=sentence.replace(" ", "")
print("Sentence witout space:", remove_space)
 #14.Write a program to ask for two strings and check if they are equal or not.

sen1=input("Enter first sentence:")
sen2=input("Enter second sentence:")
if sen1==sen2:
    print("The sentences are equal.")
else:
    print("sen1 doesn't equal to sen2.")

#15.Ask the user for a sentence and create an acronym from the first letters of each word.

sentence=input("Enter sentence:")
words=sentence.split()
acronym=''.join(word[0].upper() for word in words)
print("The acronym i:", acronym)

 #16.Write a program that asks the user for a string and a character, then removes all occurrences of that character from the string.

user_string=input("Please enter a string:")
char_to_remove=input("Please enter a character to remove:")
modified_string=user_string.replace(char_to_remove, "")
print("String after removing the character:", modified_string)

#17.Ask the user for a string and replace all the vowels with a symbol   
    
string=input("Enter word:")
for vowel in "Wassuup":
 string=string.replace(vowel, "$")
print(string)

#18.Write a program that checks if a string starts with one word and ends with another.
string=input("Enter a string:")
start_word=input("Enter the starting word:")
end_word=input("Enter the ending word:")
if string.startswith(start_word) and string.endswith(end_word):
    print("The string starts with '{}' and ends with '{}'.".format(start_word, end_word))
else:
    print("The sring doesn't match the given conditions.")


