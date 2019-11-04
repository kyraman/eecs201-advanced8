#!/usr/bin/env python3

import operator
import readline # for part 3 of advanced homework 8

import colorama # for part 3 of advanced homework 8
from colorama import Fore, Style # for part 3 of advanced homework 8

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input(Fore.GREEN + "rpn calc> "))
        # make negative numbers red
        if result < 0:
            print("Result:  ", end="")
            print(Fore.RED + str(result))
        else:
            print("Result: ", result)

if __name__ == '__main__':
    main()
