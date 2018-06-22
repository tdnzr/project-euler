# Solution to Project Euler problem 54 by tdnzr.

# My solution straightforwardly determines the 'rank' of each hand,
# plus the highest card involved in this rank,
# then compares the two hands.
# It's by no means efficient (in particular, I'm repeating some calculations, sorts or comparisons unnecessarily,
# use linked lists when I don't necessarily need to, etc), but it works.

# I initially got a wrong result. Luckily, someone posted a trace of their program,
# which helped me debug mine. It turned out I'd gotten close to the correct results
# despite several independent errors. But now they're all fixed.


from collections import Counter


def card_value(s):
    """Returns the integer value of a card."""
    value_dict = {
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14,
    }
    first_char = s[0]
    if first_char in value_dict:
        return value_dict[first_char]
    else:
        return int(first_char)


# Check whether all cards in the hand have the same suit.
# This Poker problem only cares about suit in this binary manner,
# specifically in case of Royal Flush, Straight Flush, and Flush.
def single_suit(l):
    """Returns True if all cards in the hand have the same suit, False otherwise."""
    first_suit = l[0][1]  # suit of the first card
    for card in l[1:]:
        suit_other = card[1]
        if first_suit != suit_other:
            return False
    else:
        return True


# Check whether all cards in the hand are consecutive.
# This is necessary for Royal Flush, Straight Flush, and Straight.
def is_consecutive(descending_list):
    """Returns True if all cards in the hand are consecutive, False otherwise."""
    for i in range(len(descending_list) - 1):
        if descending_list[i] != descending_list[i + 1] + 1:
            return False
    else:
        return True


# Evaluate the rank of a hand:
def evaluate_hand(l):
    """This function evaluates a Poker hand and returns both the rank of the hand, as well as the highest card involved in this rank."""
    rank_dict = {
        'High Card': 0,
        'One Pair': 1,
        'Two Pairs': 2,
        'Three of a Kind': 3,
        'Straight': 4,
        'Flush': 5,
        'Full House': 6,
        'Four of a Kind': 7,
        'Straight Flush': 8,
        'Royal Flush': 9
    }

    one_suit = single_suit(l)
    card_values = [card_value(card) for card in l]  # This list is still sorted.
    consecutive = is_consecutive(card_values)

    if one_suit and consecutive and card_values[0] == 14:
        return rank_dict['Royal Flush'], card_values[0]
    # Else, check if one suit and consecutive:
    elif one_suit and consecutive:
        return rank_dict['Straight Flush'], card_values[0]

    # From this point on, we need to determine how many pairs etc. are in the hand.
    # For this, we use the Counter module. it returns stuff like this:
    # c = Counter([1, 3, 4, 5, 2, 2, 2]) -> print(c) becomes: Counter({2: 3, 3: 2, 1: 1, 4: 1, 5: 1})
    # c.most_common(2) becomes: [(2, 3), (3, 2)]
    # So we use tuple unpacking:
    (highest_card_involved, highest_count), (other_highest_card_involved, second_highest_count) = Counter(card_values).most_common(2)

    if highest_count == 4:
        return rank_dict['Four of a Kind'], highest_card_involved
    elif highest_count == 3 and second_highest_count == 2:
        return rank_dict['Full House'], highest_card_involved
    elif one_suit:
        return rank_dict['Flush'], card_values[0]
    elif consecutive:
        return rank_dict['Straight'], card_values[0]
    elif highest_count == 3:
        return rank_dict['Three of a Kind'], highest_card_involved
    elif highest_count == 2 and second_highest_count == 2:
        # "Elements with equal counts are ordered arbitrarily" by the Counter class.
        # i.e. the Counter.most_common(2) might arbitrarily return [(2, 2), (10, 2)] or [(10, 2), (2, 2)].
        # So we have to return the maximum.
        return rank_dict['Two Pairs'], max(highest_card_involved, other_highest_card_involved)
    elif highest_count == 2 and second_highest_count == 1:  # The second check is technically redundant.
        return rank_dict['One Pair'], highest_card_involved
    elif highest_count == 1:
        return rank_dict['High Card'], card_values[0]
    else:
        raise AssertionError("Couldn't determine the rank of a hand. This should never happen.")


def run():
    # Evaluate how many hands are won by player one (= hand_one)
    with open('Euler054_poker.txt', 'r') as file_of_hands:
        hands_won = 0
        for line in file_of_hands:  # Returns lines including linebreaks ('\n')
            # Split each line in the file into two hands.
            # Then sort each hand in descending order; this helps a lot in the later stages.
            hand_list = line.rstrip('\n').split()
            hand_one = hand_list[0:5]
            hand_two = hand_list[5:10]
            hand_one.sort(key=card_value, reverse=True)
            hand_two.sort(key=card_value, reverse=True)

            rank_one, highest_involved_one = evaluate_hand(hand_one)
            rank_two, highest_involved_two = evaluate_hand(hand_two)

            # Now, compare both hands:
            if rank_one > rank_two:
                hands_won += 1
            elif rank_one == rank_two:
                # "If two players have the same ranked hands then the rank made up of the highest value wins;
                # for example, a pair of eights beats a pair of fives [...]."
                if highest_involved_one > highest_involved_two:
                    hands_won += 1
                # "But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared;
                # if the highest cards tie then the next highest cards are compared, and so on."
                elif highest_involved_one == highest_involved_two:
                    # These two lists are still sorted by construction:
                    cards_one = [card_value(card) for card in hand_one]
                    cards_two = [card_value(card) for card in hand_two]
                    # "In each hand there is a clear winner."
                    # Otherwise, there could be an ambiguity if hands were identical except for suit.
                    for i in range(5):
                        if cards_one[i] > cards_two[i]:
                            hands_won += 1
                            break
                        # If player two has a higher card, they win instead:
                        elif cards_two[i] > cards_one[i]:
                            break
                    else:
                        raise AssertionError("Couldn't determine a clear winner for this hand. This should never happen.")

    return hands_won


if __name__ == "__main__":
    print(f"Of all the Poker hands contained in the provided file, player one won {run()} of them.")
