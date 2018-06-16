# Solution to Project Euler problem 25.


from fibonacci import fibonacci  # generator function from problem 2


def run():
    counter = 0
    for n in fibonacci():
        counter += 1
        if n >= 10**999:  # 1000 digits = 999 zeroes. And this is somehow faster than checking len(str(n)) >= 1000.
            return counter


if __name__ == "__main__":
    print(f"The index of the first term in the Fibonacci sequence to contain 1000 digits is: {run()}")
