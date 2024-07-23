#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        result = []
    elif length == 1:
        result = [0]
    elif length == 2:
        result = [0, 1]
    else:
        result = [0, 1]
        while len(result) < length:
            next = result[len(result) - 1] + result[len(result) - 2]
            result.append(next)
    print(result)