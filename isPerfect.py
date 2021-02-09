def isPerfect(x):
    """Returns whether or not the given number x is perfect.

    A number is said to be perfect if it is equal to the sum of all its
    factors (for obvious reasons the list of factors being considered does
    not include the number itself).

    Example: 6 = 3 + 2 + 1, hence 6 is perfect.
    Example: 28 is another example since 1 + 2 + 4 + 7 + 14 is 28.
    Note, the number 1 is not a perfect number.
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
    if sum_list == x:
        #return True
        print("Number " , x, "is a perfect number.")
    else:
    #return False
        print("Number ", x, "is not a perfect number.")

(isPerfect(33550336))
#help(isPerfect)