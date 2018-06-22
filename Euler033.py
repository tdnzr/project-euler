# Solution to Project Euler problem 33 by tdnzr.

from fractions import Fraction


def run():
    listNontrivial = []

    # Conditions given in the problem: fraction = numerator / denominator
    # both numerator and denominator contain 2 digits, and numerator < denominator
    # So numerator = 1 ... 98, and denominator = numerator + 1 ... 99.
    for numerator in range(10, 98 + 1):
        # Skip "trivial" cases like 30 / 50 = 3 / 5:
        if numerator % 10 == 0:
            continue
        
        for denominator in range(numerator + 1, 99 + 1):
            # Skip "trivial" cases like 30 / 50 = 3 / 5:
            if denominator % 10 == 0:
                continue
            
            testfraction = Fraction(numerator, denominator)
            # Cycle through digits in the numerator, and check whether
            # they're also in the denominator. If so, create new strings
            # in which exactly one occurrence of the digit is removed.
            for digit in str(numerator):
                if digit in str(denominator):
                    num_stripped = int(str(numerator).replace(digit, "", 1))
                    denom_stripped = int(str(denominator).replace(digit, "", 1))
                    if testfraction == Fraction(num_stripped, denom_stripped):
                        listNontrivial.append(testfraction)

    product = 1
    for fraction in listNontrivial:
        product *= fraction

    return product.denominator


if __name__ == "__main__":
    print(f"The denominator of the product of these four fractions is {run()}.")
