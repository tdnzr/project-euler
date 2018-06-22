# Solution to Project Euler problem 98 by tdnzr.


from math import sqrt
from itertools import permutations  # combinations returns r length subsequences of elements from the input iterable.


def is_square(n):
    """Returns True if n is a perfect square, False otherwise."""
    return sqrt(n).is_integer()


def largest_square(wordOne, wordTwo):
    """Returns the largest square which can be constructed by replacing the letters in wordOne and wordTwo with digits,
    where same letters correspond to same digits, different letters correspond to different digits,
    and leading zeroes are not permitted."""
    
    # Determine how many unique characters are in each word.
    # Because the two words are anagrams, I only have to check wordOne.
    uniqueCharsSet = set(wordOne)  # Beware: Sets are unordered. This can cause problems.
    unique_char_count = len(uniqueCharsSet)
    uniqueChars = list(uniqueCharsSet)  # Necessary later on because one cannot access elements of a set by index.
    
    maxSquare = 0
    
    # Convert the given pair of anagrams into all possible numbers:
    # I originally used a nested for-loop of itertools.combinations and itertools.permutations here,
    # but by giving permutations a second argument, a single for-loop is enough.
    # Also, by generating permutations of a number string, rather than of range(10),
    # we don't have to do so many string conversions later on.
    for perm in permutations("0123456789", unique_char_count):
        # Generate a key to convert words into digits. Dictionaries are great for this.
        translate_dict = {uniqueChars[i]: perm[i] for i in range(unique_char_count)}

        # Skip the current for-loop if wordOne or wordTwo would begin with a zero.
        if translate_dict[wordOne[0]] == "0" or translate_dict[wordTwo[0]] == "0":
            continue

        # Now we translate the words into numbers:
        numberOne = int(''.join(translate_dict[char] for char in wordOne))
        numberTwo = int(''.join(translate_dict[char] for char in wordTwo))

        # Finally, we check if the generated numbers are both square,
        # and if so, whether either square is larger than the largest we've found so far.
        if not (is_square(numberOne) and is_square(numberTwo)):
            continue
        if maxSquare < numberOne or maxSquare < numberTwo:
            maxSquare = max(numberOne, numberTwo)
    return maxSquare


def run():
    # Process the file of words and turn it into a list:
    with open("Euler098_words.txt", 'r') as inputFile:
        # [1:-1] removes the leading and trailing quotation marks; and the remaining nonsense is removed via the split function.
        listOfWords = inputFile.read()[1:-1].split('","')

    # Step 1: Find all anagrams in the list of words:
    # a) Sort the letters in the words alphabetically.
    sorted_words = [sorted(word) for word in listOfWords]

    # b) Find all anagrams via this convoluted list comprehension.
    pairsOfAnagrams = [(listOfWords[i], listOfWords[j])
                        for i in range(len(listOfWords))
                        for j in range(len(listOfWords))
                        if i < j and sorted_words[i] == sorted_words[j]]

    # The problem only asks us to find the largest square number which can be formed.
    # So as a speedup, I order the pairsOfAnagrams by word length in reverse order.
    # So I begin at the largest possible pairs, and stop once I've found a valid square number
    # as well as exhausted all words of the same length:
    pairsOfAnagrams.sort(key=lambda x: len(x[0]), reverse=True)  # Sort the list of lists by the length of their first elements.


    # Step 2: For each pair of anagrams, find the largest square number
    # that can be constructed from them, if any.
    global_max_square = 0
    minimal_word_length = 0 
    for word_one, word_two in pairsOfAnagrams:
        # Because we've sorted pairsOfAnagrams by length in descending order,
        # once we've found a valid square number,
        # we can stop once we've exhausted all words of the same length.
        if len(word_one) < minimal_word_length:
            break

        # Otherwise, we try to find the largest square number
        # that can be constructed from this pair of words.
        current_max_square = largest_square(word_one, word_two)
        if current_max_square > global_max_square:
            global_max_square = current_max_square
            minimal_word_length = len(word_one)
    return global_max_square


if __name__ == "__main__":
    print(f"The largest square number which can be formed by any member of an anagram pair in the word file is: {run()}")
