def isPrime(x):
    """Returns whether or not the given number x is prime.

       A prime number is a natural number greater than 1 that cannot be formed
       by multiplying two smaller natural numbers.

       For example:
       - Calling isPrime(11) will return True
       - Calling isPrime(71) will return True
       - Calling isPrime(12) will return False
       - Calling isPrime(76) will return False
       """

    if x == 2 or x == 3: return True
    if x % 2 == 0 or x < 2: return False
    for i in range(3, int(x ** 0.5) + 1, 2):  # only odd numbers
        if x % i == 0:
            return False

    return True


print(isPrime(76))
#help(isPrime)

