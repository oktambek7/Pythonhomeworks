def round_number():
    num = float(input("Enter a float number: "))
    print(f"Rounded to 2 decimal places: {round(num, 2)}")

def largest_and_smallest():
    nums = [float(input(f"Enter number {i+1}: ")) for i in range(3)]
    print(f"Largest: {max(nums)}, Smallest: {min(nums)}")

def km_to_m_cm():
    km = float(input("Enter distance in kilometers: "))
    meters = km * 1000
    centimeters = km * 100000
    print(f"Meters: {meters}, Centimeters: {centimeters}")

def integer_division():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"Integer division result: {num1 // num2}, Remainder: {num1 % num2}")

def celsius_to_fahrenheit():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"Temperature in Fahrenheit: {fahrenheit}")

def last_digit():
    num = int(input("Enter a number: "))
    print(f"Last digit: {abs(num) % 10}")

def check_even():
    num = int(input("Enter a number: "))
    print("Even" if num % 2 == 0 else "Odd")

if __name__ == "__main__":
    print("Choose a program to run:")
    print("1. Round a number")
    print("2. Find largest and smallest of three numbers")
    print("3. Convert kilometers to meters and centimeters")
    print("4. Perform integer division and find remainder")
    print("5. Convert Celsius to Fahrenheit")
    print("6. Find the last digit of a number")
    print("7. Check if a number is even or odd")
    
    choice = int(input("Enter your choice (1-7): "))
    
    functions = [round_number, largest_and_smallest, km_to_m_cm, integer_division, 
                 celsius_to_fahrenheit, last_digit, check_even]
    
    if 1 <= choice <= 7:
        functions[choice - 1]()
    else:
        print("Invalid choice!")
