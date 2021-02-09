def isTriangular(n):
    """Returns whether or not a given number x is triangular.

    The triangular number Tn is a number that can be represented in the form of a triangular
    grid of points where the first row contains a single element and each subsequent row contains
    one more element than the previous one.

    We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

    Example: 3 is triangular since 3 = 2(3) / 2
    3 --> 2nd position: (2 * 3 / 2)

    Example: 15 is triangular since 15 = 5(6) / 2
    15 --> 5th position: (5 * 6 / 2)
    """

    if n == 0 or n == 1:
        return True

    triangular_sum = 0

    for i in range(n):
        triangular_sum += i

        if triangular_sum == n:
            return True

        if i == n:
            return False


print(isTriangular(3))
#help(isTriangular)