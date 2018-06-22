# Solution to Project Euler problem 34 by tdnzr.

# I was initially confused how I could possibly do an existence proof / identify *all* the numbers,
# without being given any bounds. However, there is a method to the madness:
# The largest factorial of a digit is 9! = 362 880, so once a number has 7 digits, its value is at least 1 000 000,
# but its factorial sum is at most 7*9! = 2 540 160. In other words, there's no need to check numbers >~ 2.5 million.

from math import factorial


def run():
    listOfValidNumbers = []
    for i in range(10, 2_540_160 + 1):
        factorial_sum = sum([factorial(int(n)) for n in str(i)])
        if i == factorial_sum:
            listOfValidNumbers.append(i)
    return(listOfValidNumbers, sum(listOfValidNumbers))


if __name__ == "__main__":
    factorial_list, factorial_sum = run()
    print(f"The complete list of numbers which are equal to the sum of the factorial of their digits is: {factorial_list}")
    print(f"The sum of all numbers which are equal to the sum of the factorial of their digits is: {factorial_sum}")
