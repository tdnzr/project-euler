# Solution to Project Euler problem 22.


def run():
    with open("Euler022_names.txt", 'r') as name_file:
        name_string = name_file.read()

    # Remove the leading and trailing character of the string, then remove the remaining nonsense via split:
    name_list = name_string[1:-1].split('","')
    name_list.sort()  # Sort the list alphabetically.

    score = 0
    for word in name_list:
        charSum = sum([ord(char)-64 for char in word])  # ord("A") = 65, ..., ord("Z") = 90, so 1 = ord("A")-64 etc.
        index = name_list.index(word) + 1  # +1 because I'm interested in the alphabetical position (1-based), not the list position (0-based index).
        score += (charSum * index)
    return score


if __name__ == "__main__":
    print(run())
