#3. Write a Python func9on to check whether a given number is prime.
#If n is less than 2, return False because numbers less than 2 are not prime.
#Loop from 2 to √n (since a factor larger than √n would have a corresponding smaller factor).
#If n is divisible by any number in this range, return False (not a prime).
#If no factors are found, return True (it's a prime number).
#The main program takes user input, calls is_prime(num), and prints the result.


def is_prime(n):
    
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print("Given number is prime.")
else:
    print("Given number is not prime.")
