"""
Defines some useful functions.
"""

import ski_rental_algos as sr


def array_to_int(x):
    return x[0]

def print_result(alg_cost, opt):
    return "Cost: " + str(alg_cost) + "\nCompetitive ratio: " + str(sr.comp_ratio(alg_cost,opt))

def self_guess(guessed_x, x, b):
    guessed_x += 1
    if guessed_x > x:
        return x
    else:
        return guessed_x - 1 + b