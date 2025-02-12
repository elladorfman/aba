
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
