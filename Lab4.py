
#Function 1: Fibonacci Numbers

def fibonacci(n):
        a = 0
        b = 1
        if n == 0:
            return 0

        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            for i in range(2, n):
                c = a + b
                a = b
                b = c
            return b

#print(fibonacci(6))

#Function 2: Prime Numbers

def is_prime(num):
    if num > 1:
        for i in range(2, (num // 2) + 1):
            if (num % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False

#print(is_prime(1))

#Function 3: Prime Factorization
def print_prime_factors(num):
    if num > 1:
        if num == 2:
            print(f"{num} = {num}")
            return

        for i in range(2, (num // 2) + 1):  # Check if the number is prime
            if num % i == 0:
                break
            else:
                print(f"{num} = {num}")
                return  # Exit if it's a prime number

            # If number is not prime, print its prime factors
        print(f"{num} =", end=" ")
        two = 2
        first = True  # Track first factor to avoid extra "*"

        while num % two == 0:
            if not first:
                print("*", end=" ")
            print(two, end=" ")
            num //= two
            first = False

    three = 3
    while three * three <= num:
            while num % three == 0:
                if not first:
                    print("*", end=" ")
                print(three, end=" ")
                num //= three
                first = False
                three += 2

    if num > 1:  # Remaining prime factor
        if not first:
            print("*", end=" ")
            print(num, end="")
