
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
