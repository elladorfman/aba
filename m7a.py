#Decimal to Binary Conversion

#Write a function bin, that converts a decimal (base-10) number to its binary (base-2) representation.
#The function should take an integer as input and return a string containing the binary representation.

def bin(n):
    if n==0:
        return '0'
    elif n==1:
        return '1'
    else:
        return bin(n//2) + str(n%2)

#print(bin(0))

#Capitalize Characters
#Write a function capitalize that takes in a string as input and returns a new string where every character is lowercase
#except for the first character in each word.
# Additionally, if the first character is one of (o, u, s, n, d), the character should remain lowercase.

def capitalize(n):
    words = n.split()
    result = []

    for word in words:
        if word[0].lower() in ('o', 'u', 's', 'n', 'd'):
            result.append(word.lower())
        else:
            result.append(word[0].upper() + word[1:].lower())

    return ' '.join(result)

#print(capitalize("SIZE OF DESK"))
#returns “size of desk”

#List Partitioning
#Write a function partition, that partitions a given list into smaller lists of a specified length.
#The function should take a list and a partition size as input and return a list of sublists.
#If the list cannot be divided evenly, the last partition may contain fewer elements than the specified size.
#Assume that the partition size will be greater than zero.

numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def partition(numbers, n):
    return [numbers[i:i + n] for i in range(0, len(numbers), n)]

#print(partition(numbers, 5))
