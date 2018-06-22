# Solution to Project Euler problem 5 by tdnzr.
# Alternative solution.

# Algorithm: Start with the initial product 1*...*20, then divide by factors until I get the minimal viable (number) product. Pun intended.


def run():
    highLimit = 20
    startProd = 1
    for i in range(2, highLimit+1):
        startProd *= i  # Result: 2432902008176640000

    i = 2  # initial factor to test by.
    while i <= highLimit:
        test = startProd // i
        for j in range(2, highLimit+1):
            if test % j != 0:
                i += 1
                break  # Exit the current for-loop.
        else:  # Triggers if the for-loop was successfully concluded, i.e. if test is still divisible by 1...20.
            startProd = test

    return startProd


if __name__ == "__main__":
    print(run())
