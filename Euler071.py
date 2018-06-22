# Solution to Project Euler problem 71 by tdnzr.

# After multiple solution attempts turned out to be impossibly slow,
# I looked up a tip from the web: if n / d <= 3/7, then n <= 3/7 * d
# -> Since I need the *biggest* numerator which fulfills the relation
# and also fulfills HCF(n, d) = 1, it's enough if I just check
# n = trunc(3/7 * d - 1) each time, i.e. one n per d, or ~1,000,000 calculations altogether.
# This is much more efficient than my earlier attempts of looping through d, then through all n < d,
# i.e. 1 + ... + n = n*(n+1)/2 ~= 1/2 * n^2 calculations, i.e. one million squared.


from fractions import Fraction


def run():
    maxNumerator = 0
    for d in range(1, 1_000_000 + 1):
        n = 3 * d // 7 - 1
        reducedNumerator = Fraction(n, d).numerator
        if reducedNumerator > maxNumerator:
            maxNumerator = reducedNumerator
    return maxNumerator


if __name__ == "__main__":
    print(f"The numerator of the fraction immediately to the left of 3/7 is: {run()}")
