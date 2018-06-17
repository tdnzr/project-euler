# Solution to Project Euler problem 38.

# Upper limit: We need to obtain a 9-digit number by concatenating the products of a number with 1, 2, ...
# Even if we begin with the smallest possible result from a 5-digit number, namely,
# 10000 concatenated with 10000*2, we still end up with 1000020000, a 10-digit number.
# So there's no need to consider starting numbers with 5 or more digits.


def run():
    listOfValidNumbers = []

    for starter in range(1, 9999 + 1):  # Starting numbers have at most 4 digits.
        concatenatedString = ""
        for factor in range(1, 9 + 1):  # I'll have to multiply by at most 1x...9x.
            # Ensure that the next product we append contains no zeroes:
            new_product = str(starter*factor)
            if "0" in new_product:
                break

            # Append the product and test if the resulting number is pandigital:
            concatenatedString += new_product
            
            if len(concatenatedString) > 9:  # The concatenated number must contain at most 9 digits.
                break
            elif len(set(concatenatedString)) == 9:  # The concatenated number must *exactly* contain each of the digits 1...9 once.
                listOfValidNumbers.append(concatenatedString)
                break
    return max(listOfValidNumbers)


if __name__ == "__main__":
    print(run())
