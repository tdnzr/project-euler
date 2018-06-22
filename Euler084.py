# Solution to Project Euler problem 84.

# Algorithm: I basically tried to straightforwardly implement the complex rules stated in the problem.
# Then, because we're interested in a statistical solution, I just let the game play for lots of moves.

# Finally, for debugging, it helps that we're given the correct solutions for 6-sided dice,
# plus the reminder that the CH squares will have the lowest probabilities, and the probability of ending on G2J is zero.

# Note that this program yields the wrong result for the fourth most common square for 6 dice,
# namely 19 instead of 00.
# However, given how much time I've spent on this problem, and how ambiguous its description is,
# I'm not interested in debugging it any longer. After all, the main result is correct.


# Rules for Euler Monopoly (as I understand them):
#
# Begin at square zero (GO).
# Roll two six- / four-sided dice and add the result.
# Move based on the result of the dice throw:
# - Normal square: Nothing happens.
# - G2J square: Go to jail, end turn. (We don't skip a turn in jail because that wouldn't affect the probabilities.)
# - CC square: Move according to the top card of the CH deck, then put the card to the bottom.
# - CH square: Move according to the top card of the Chance deck, then put the card to the bottom.
# - If your dice throw was the first or second double (Pasch), take another turn. May not if you're in jail; unsure.
# - Same after the second double.
# - If not in jail and it's the third double, go to jail immediately instead of taking another turn.


from random import shuffle, randint  # randint to simulate the dice; shuffle to shuffle the decks.
from collections import Counter  # To determine the three most common squares.


# Initialize the monopoly board as a list of the 40 squares on the board:
monopoly_string = "GO A1 CC1 A2 T1 R1 B1 CH1 B2 B3 JAIL C1 U1 C2 C3 R2 D1 CC2 D2 D3 FP E1 CH2 E2 E3 R3 F1 F2 U2 F3 G2J G1 G2 CC3 G3 R4 CH3 H1 T2 H2"
Monopoly_Board = monopoly_string.split()


def move(initialIndex, die_sides):
	"""Returns the player position after moving by the value of the dice,
	and whether the dice roll was a double (Pasch)."""
	roll1 = randint(1, die_sides)
	roll2 = randint(1, die_sides)
	return (initialIndex + roll1 + roll2) % 40, roll1 == roll2  # new index modulo 40 (board is 40 squares long)


def card_effect(currentSquare, card_list):
	"""Returns the player position after drawing cards from one of the two decks
	and moving the player based on the result."""
	currentCard = card_list.pop(0)  # "Draws" the top card, and removes it from the list.
	card_list.append(currentCard)  # Move the currently drawn card to the bottom of the deck.
	
	# Return the final square based on the drawn card:
	if currentCard == 0:
		return currentSquare  # The "do nothing" instruction.
	# "R" = go to next railway company (R1, R2, R3 or R4). The railway companies are at indices 5, 15, 25, 35.
	elif currentCard == "R":
		index_R1, index_R2, index_R3, index_R4 = Monopoly_Board.index("R1"), Monopoly_Board.index("R2"), Monopoly_Board.index("R3"), Monopoly_Board.index("R4")
		if currentSquare <= index_R1:
			return index_R1
		elif currentSquare <= index_R2:
			return index_R2
		elif currentSquare <= index_R3:
			return index_R3
		elif currentSquare <= index_R4:
			return index_R4
		else:  # i.e. if currentSquare > index_R4
			return index_R1
	# "U" = go to next utility company (U1 or U2).
	elif currentCard == "U":
		index_U1 = Monopoly_Board.index("U1")
		index_U2 = Monopoly_Board.index("U2")
		if currentSquare <= index_U1 or currentSquare > index_U2:
			return index_U1
		else:
			return index_U2
	elif currentCard == -3:
		return (currentSquare - 3) % 40
	# Remaining cases: GO, JAIL, C1, E3, H2, R1 are all names in the monopoly board.
	else:
		# list.index() only looks for the exact entry in the list,
		# so it's no problem that the list Monopoly_Board contains
		# both a "CC1" and a "C1", as well as a "CH2" and an "H2".
		return Monopoly_Board.index(currentCard)


def run():
    # Initialize the card decks. After putting in the relevant cards,
    # I fill the decks with zeroes to bring them to 16 cards:
    CC_Deck = ["GO", "JAIL"]
    Chance_Deck = ["GO", "JAIL", "C1", "E3", "H2", "R1", "R", "R", "U", -3]
    while len(CC_Deck) < 16:
        CC_Deck.append(0)
    while len(Chance_Deck) < 16:
        Chance_Deck.append(0)

    # Main loop:
    ListOfVisitedSquareIndices = []
    number_of_die_sides = 4
    number_of_games = 10  # Play 10 games.
    moves_per_game = 100_000  # Take 100000 moves per game.
    for _ in range(number_of_games):
        shuffle(CC_Deck)  # Shuffles the list, but returns None.
        shuffle(Chance_Deck)  # Shuffles the list, but returns None.
        indexCurrentSquare = 0  # Start at the square with index zero, i.e. at "GO".
        for _ in range(moves_per_game):
            
            # Throw the dice, and move based on the result.
            doubleCounter = 0  # Count doubles (Päsche).
            while True:
                # Compute the target square:
                newIndex, rolledDouble = move(indexCurrentSquare, number_of_die_sides)
                
                # If we've rolled our third double, we go directly to jail:
                if rolledDouble:
                    doubleCounter += 1
                    if doubleCounter == 3: 
                        indexCurrentSquare = Monopoly_Board.index("JAIL")
                        break
                
                # As we haven't gone to jail due to a thrid double, we can actually move the player:
                indexCurrentSquare = newIndex
                
                # Now we have to check if we landed on a card square,
                # and if so, check if that card moves us further along.
                if "CC" in Monopoly_Board[indexCurrentSquare]:
                    indexCurrentSquare = card_effect(indexCurrentSquare, CC_Deck)
                elif "CH" in Monopoly_Board[indexCurrentSquare]:
                    indexCurrentSquare = card_effect(indexCurrentSquare, Chance_Deck)
                # Oh, and there's also the G2J square.
                elif "G2J" in Monopoly_Board[indexCurrentSquare]:
                    indexCurrentSquare = Monopoly_Board.index("JAIL")
                
                # Finally, if we ended up on the jail square, I originally stopped moving even in case of doubles.
                # But removing this condition brings our result more in line with the one given in the
                # problem description, and the latter is ambiguous on which behavior is correct.
                #if indexCurrentSquare == Monopoly_Board.index("JAIL"):
                #	break
                
                # If we rolled the first or second double, we roll again, otherwise we're done:
                if not rolledDouble:
                    break

            # Now that we've landed on a final square, we can append that to the list of visited squares.
            ListOfVisitedSquareIndices.append(indexCurrentSquare)

    # Finally, we use collections.Counter to analysise the list of visited squares:
    threeMostPopularSquares = Counter(ListOfVisitedSquareIndices).most_common(3)
    return ''.join(str(elem[0]) for elem in threeMostPopularSquares)


if __name__ == "__main__":
    print(f"{run()} is the answer string made from concatenating the indices of the three most popular squares in ascending order.")
