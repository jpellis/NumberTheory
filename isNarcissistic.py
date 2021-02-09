def isNarcissistic(x):
    """Returns whether or not a given number is Narcissistic.

    A positive integer is called a narcissistic number if it
    is equal to the sum of its own digits each raised to the
    power of the number of digits.

    Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
    Note that by this definition all single digit numbers are narcissistic.
    """

    str_value = str(x)
    num_digits = len(str_value)
    return (x == sum(int(digit) ** num_digits for digit in str_value))

print(isNarcissistic(153))
#help(isNarcissistic)