# Solution to Project Euler problem 6 by tdnzr.


def run():
    squareOfSum = sum(i for i in range(1, 101))**2
    sumOfSquares = sum(i**2 for i in range(1, 101))
    return squareOfSum - sumOfSquares


if __name__ == "__main__":
    print(f'The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is: {run()}')
