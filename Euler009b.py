# Solution to Project Euler problem 9.
# Solution with list comprehension.
# This solution shows some of their limitations (in comparison to the for-loops in 009a):
# One, I can't conveniently declare "c = 1000 - a - b".
# Two, I can't stop the computation once I've found a result.


def run():
    result = [
        (a, b, 1000 - a - b)
        for a in range(1, 333)  # a < b < c < 1000, so a < 333
        for b in range(a + 1, 500)  # b < c < 1000, so b < 500
        if a**2 + b**2 == (1000 - a - b)**2
    ]
    a, b, c = result[0]
    return (a, b, c, a * b * c)


if __name__ == "__main__":
    a, b, c, product = run()
    print(f"The three numbers are: {a}, {b} and {c}")
    print(f"The product of the three numbers is: {product}")
