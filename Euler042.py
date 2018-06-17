# Solution to Project Euler problem 42.

# As in problem 22, this problem involved dealing with a text file,
# so I borrowed and adapted some code.
# I also took the check_tri function from problem 45.

from math import sqrt


def check_tri(t):
    # Inverse function of Tn = n(n + 1)/2
    check = (-1 + sqrt(1 + 8*t))/2
    return check.is_integer()


def run():
    with open("Euler042_words.txt", 'r') as word_file:
        word_string = word_file.read()
    # Remove the leading and trailing character of the string, then remove the remaining nonsense via split:
    word_list = word_string[1:-1].split('","')

    counter = 0
    for word in word_list:
        charSum = sum([ord(char)-64 for char in word])  # ord("A") = 65, ..., ord("Z") = 90, so 1 = ord("A")-64 etc.
        if check_tri(charSum):
            counter += 1
    return counter


if __name__ == "__main__":
    print(f"words.txt contains {run()} triangle words.")
