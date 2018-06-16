# Solution to Project Euler problem 8.
# Solution via deque. Includes less unnecessary computations than the original.
# This solution is still not optimal: one could skip computing all the sections in the numberString which begin with a 0.

from collections import deque
from functools import reduce


def run():
    numberString = "731671765313306249192251196744265747423553\
491949349698352031277450632623957831801698480186947885184385\
861560789112949495459501737958331952853208805511125406987471\
585238630507156932909632952274430435576689664895044524452316\
173185640309871112172238311362229893423380308135336276614282\
806444486645238749303589072962904915604407723907138105158593\
079608667017242712188399879790879227492190169972088809377665\
727333001053367881220235421809751254540594752243525849077116\
705560136048395864467063244157221553975369781797784617406495\
514929086256932197846862248283972241375657056057490261407972\
968652414535100474821663704844031998900088952434506585412275\
886668811642717147992444292823086346567481391912316282458617\
866458359124566529476545682848912883142607690042242190226710\
556263211111093705442175069416589604080719840385096245544436\
298123098787992724428490918884580156166097919133875499200524\
063689912560717606058861164671094050775410022569831552000559\
3572972571636269561882670428252483600823257530420752963450"

    thirteen_digits = deque([int(s) for s in numberString[:13]])

    # Compute the initial product.
    product = reduce(lambda a, b: a*b, thirteen_digits)
    largest_product = product

    # Cycle through the numberString via first-in-first-out.
    for digit in numberString[13:]:
        new_factor = int(digit)
        old_factor = thirteen_digits.popleft()
        thirteen_digits.append(new_factor)

        # If the leftmost digit was a zero, we can't divide by it but have to recompute the product instead:
        if old_factor != 0:
            product = product * new_factor // old_factor
        else:
            product = reduce(lambda a, b: a*b, thirteen_digits)

        if product > largest_product:
            largest_product = product

    return largest_product


if __name__ == "__main__":
    print(run())
