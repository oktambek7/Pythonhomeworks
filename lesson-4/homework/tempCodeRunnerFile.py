
def is_prime(n):
    if n < 2:
        return False 
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_prime_numbers():
    """Print all prime numbers between 1 and 100."""
    print("Pritme numbers beween 1 and 100:")
    for num in range(1, 101): 
        if is_prime(num):
            print(num, end=" ")
print_prime_numbers()
