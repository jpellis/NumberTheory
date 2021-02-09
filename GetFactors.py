def getFactors(x):
    """Returns a list of factors of the given number x.
    Basically, finds the numbers between 1 and the given integer that divide the number evenly.

    For example:
    - If we call getFactors(2), we'll get [1, 2] in return
    - If we call getFactors(12), we'll get [1, 2, 3, 4, 6, 12] in return"""

    # create an empty list to store the factors
    factors = []

    # iterate over range from 1 to number x (including itself so "x +1")
    for i in range(1, x + 1):

        # check if i divides number x evenly
        if (x % i == 0):
            factors.append(i)

    return factors


print(getFactors(12))
#help(getFactors)
    
