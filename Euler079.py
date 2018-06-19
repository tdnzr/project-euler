# Solution to Project Euler problem 79.

# Because I couldn't come up with an elegant algorithm in time, I settled on a 
# brute force solution instead: we just loop the natural numbers,
# and test whether the given number fulfills the the keylog condition,
# i.e. whether the the number contains the digits given in the keylog, and in the same order.
# This algorithm takes ~70s on my computer.

# I initially thought a better approach would be to generate all permutations of the keylog lines,
# concatenate them, and then remove adjacent duplicate patterns (maybe with a regex),
# and finally return the shortest resulting string.
# However, this is impossibly slow: although there are just 33 unique keylog elements,
# this still corresponds to 33! ~= 8.6 * 10**36 permutations to go through...

# All that said, a far superior algorithm (based on a similar logic to decimating the triangles
# in the problems regarding minimal or maximal path sums) would be to go through the contents
# of the keylog one by one, and try to concatenate them into the actual solution.
# e.g. given 719 and 716, we don't know if the shortest solution will go 7169 or 7196,
# but given 689 and 690, we know the shortest solution looks like 6890,
# so we could replace these two entries in the keylog.
# Once only a single entry is left in the keylog, we're done.


def run():
    # The keylog file consisted of 50 short lines, so I put it here as a multiline string instead.
    keylog = '''319 680 180 690 129 620 762 689 762 318
    368 710 720 710 629 168 160 689 716 731
    736 729 316 729 729 710 769 290 719 680
    318 389 162 289 162 718 729 319 790 680
    890 362 319 760 316 729 380 319 728 716'''

    # Realization: The keylog list contains duplicates, which yield no additional information.
    # We can remove duplicates via set().
    keylog_set = set()
    for line in keylog.splitlines():
        keylog_set.update(line.split())

    # Brute force algorithm: Loop throgh the natural numbers,
    # then through all keys in the keylog,
    # then through the three digit characters in each key.
    # Then, go through the digit_string and test whether each digit in the key is in the digit_string,
    # and in the same order.
    for i in range(100_000_000):
        digit_string = str(i)
        for key in keylog_set:
            position = 0
            for char in key:
                position = digit_string[position:].find(char)
                if position == -1:
                    break
            else:
                continue
            break
        # If the contents of all keys match the contents of i, we're done.
        else:
            return i


if __name__ == "__main__":
    print(f"The shortest number which fulfills all conditions in the keylog is: {run()}.")
