# Solution to Project Euler problem 59.

# cipher.txt is a text file in which the bytes were converted to ASCII,
# then each byte was XORed "with a given value, taken from a secret key".


from string import ascii_lowercase


def run():
    # Load the cipher file and save it as a list of ordinals:
    with open("Euler059_cipher.txt", 'r') as cipher_text:
        cipher = [int(s) for s in cipher_text.read().split(',')]

    # Generate all possible keys. The key consists of three
    # lower-case characters. (Here, I directly convert to their ASCII codes.)
    keys = ((ord(a), ord(b), ord(c))
            for a in ascii_lowercase
            for b in ascii_lowercase
            for c in ascii_lowercase)

    for key in keys:
        # Decrypt the message with the key:
        decrypted = ""
        for index, elem in enumerate(cipher):
            # ^ = bitwise XOR; index % 3 because I'm supposed to cycle through the key.
            decryptedNum = elem ^ key[index % 3]
            decryptedChar = chr(decryptedNum)
            decrypted += decryptedChar  # Concatenate string

        # Now test whether the decrypted message is correct, i.e.
        # whether it contains some common English words like the ones below.
        # Note: string.find() returns -1 if a string is not found, and "if -1" returns True.
        # That cost me a few minutes in debugging...
        if decrypted.find("and") >= 0 and decrypted.find("the") >= 0 and decrypted.find("was") >= 0:
            # print(decrypted)
            break

    ascii_sum = sum([ord(char) for char in decrypted])
    return ascii_sum

if __name__ == "__main__":
    print(f"The sum of the ASCII values in the original text is: {run()}")
