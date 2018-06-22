# Solution to Project Euler problem 74 by tdnzr.
# Quite efficient solution based on using knowledge about chains.

# This problem is related to various chains-related problems, e.g. 12, 92, 95 (from which I borrowed some code), ...

from math import factorial

def calcDigitFactorialSum(number):
    return sum([factorial(int(digit)) for digit in str(number)])


def run():
    chainsList = []

    for i in range(1_000_000):  # starting numbers *below* one million
        chain = []  # I originally figured turning this into a set might improve efficiency (faster membership testing; no need to preserve order), but the result was slower.
        number = i

        # Construct the chain beginning with "number":
        chain.append(number)  # i is the first element of the chain
        while True:
            number = calcDigitFactorialSum(number)
            # Once we've reached an element < i, we've already computed the corresponding chain,
            # so we can reuse that result. This step saves *a lot* of time.
            # Otherwise, stop the chain once it begins repeating itself.
            # If neither condition holds, append the number to the chain.
            if number < i:
                chain += chainsList[number]  # 1-based index. The chain beginning with the number 1 has the index 1.
                break
            elif number in chain or len(chain) > 60:
                break
            else:
                chain.append(number)
        chainsList.append(chain)

    return sum([1 for chain in chainsList if len(chain) == 60])


if __name__ == "__main__":
    print(f"{run()} digit factorial chains with a starting number below one million contain exactly sixty non-repeating terms.")
