def isAbundant(x):
    """Returns whether or not the given number x is abundant.

    A number is considered to be abundant if the sum of its factors
    (aside from the number) is greater than the number itself.

    Example: 12 is abundant since 1+2+3+4+6 = 16 > 12.
    However, a number like 15, where the sum of the factors.
    is 1 + 3 + 5 = 9 is not abundant.
    """

    for i in range(1, x + 1):
        def getFactors(x):
            factor_list = []
            for i in range(1, x + 1):
                if (x % i == 0):
                    factor_list.append(i)
            return factor_list
            print(factor_list)

    list = (getFactors(x))
    list.pop()
    sum_list = sum(list)
    if sum_list > x:
        return True
        # print("Number ", x, "is a perfect number.")
        # else:
    return False
    # print("Number ", x, "is not a perfect number.")

print(isAbundant(15))
# help(isAbundant)
