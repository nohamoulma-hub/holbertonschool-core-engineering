#!/usr/bin/env python3
def print_last_digit(number):
    digit = abs(number) % 10  # pour connaitre de le dernier chiffre
    print(digit, end="")
    return digit  # return est nécessaire pour que digit soit réutilisable
