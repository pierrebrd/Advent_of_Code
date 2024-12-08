import copy
import re

file = open("input.txt", "r")
data = file.readlines()
data = [
    [int(char) for char in line.strip().replace(":", "").split(" ")] for line in data
]

# We will go through all the possibilities (* or +) and break as soon as the result is higher than the expected number.


def reccursive_calc(before, after, wanted, operators):
    if after == []:  # End of recursivity
        return (before, operators)  #
    else:
        temp = before + after[0]
        if temp <= wanted:
            result_plus, operators_plus = reccursive_calc(
                temp, after[1:], wanted, operators + ["+"]
            )
            if result_plus == wanted:
                return (result_plus, operators_plus)
        # We didn't get good results with +, let's try with *
        temp = before * after[0]
        if temp <= wanted:
            result_mult, operators_mult = reccursive_calc(
                temp, after[1:], wanted, operators + ["*"]
            )
            if result_mult == wanted:
                return (result_mult, operators_mult)
        # If we arrive here, the equation can't be fixed.
        return (None, [])


valid_eqs = []  # We'll add line numbers of valid equations
valid_eqs_operators = []
sum = 0
for i, eq in enumerate(data):
    print(i)
    n = eq[0]
    result, operators = reccursive_calc(0, eq[1:], n, [])
    if result == n:
        valid_eqs.append(i)
        valid_eqs_operators.append(operators)
        sum += n
sum
