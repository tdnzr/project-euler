# Solution to Project Euler problem 9.


def run():
    a, b, c = 0, 0, 0
    for a in range(1, 333):  # a < b < c < 1000, so a < 333
        for b in range(a + 1, 500):  # b < c < 1000, so b < 500
            c = 1000-a-b
            if a**2 + b**2 == c**2:
                return (a, b, c, a * b * c)


if __name__ == "__main__":
    a, b, c, product = run()
    print(f"The three numbers are: {a}, {b} and {c}")
    print(f"The product of the three numbers is: {product}")
