def isPrime(x):
    if x == 2 or x == 3: return True
    if x % 2 == 0 or x < 2: return False
    for i in range(3, int(x ** 0.5) + 1, 2):  # only odd numbers
        if x % i == 0:
            return False

    return True

def isComposite(x):
    """Returns whether or not the given number x is composite.

    A composite number has more than 2 factors.
    A natural number greater than 1 that is not prime is called a composite number.
    Note, the number 1 is neither prime nor composite.

    For example:
    - Calling isComposite(9) will return True
    - Calling isComposite(22) will return True
    - Calling isComposite(3) will return False
    - Calling isComposite(41) will return False
    """

    #if x less than or equal to 1, not composite
    if x <= 1:
        return False

    #if x is prime, not composite
    if isPrime(x):
        True
        return False

    #all numbers greater than 1 and not prime as composite
    return True

print(isComposite(41))
#help(isComposite)

