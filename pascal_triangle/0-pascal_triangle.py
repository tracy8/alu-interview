#!/usr/bin/python3
"""A function that returns a list of lists of integers 
It returns an empty list if n <= 0
"""


def factorial(n):
    """Calculate factorial of n (n!)"""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def combination(n, r):
    """Calculate binomial coefficient C(n, r) = n! / (r! * (n - r)!)"""
    return factorial(n) // (factorial(r) * factorial(n - r))


def pascal_triangle(n):
    """ Function returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    result = []
    for count in range(n):
        row = []
        for element in range(count + 1):
            row.append(combination(count, element))
        result.append(row)
    return result
