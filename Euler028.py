# Solution to Project Euler problem 28 by tdnzr.

# Some thoughts:
# 1) I technically don't actually need to draw the spiral, because I only care about the two diagonals.
# 2) The spiral is created by starting at the center, then moving as follows:
# 1 right, 1 down
# 2 left, 2 up
# 3 right, 3 down
# ...

# Anyway, the solution I've come up with here isn't at all pretty.


def run():
    # Initialize the spiral as a matrix of length and height 1001,
    # with the center at at spiral[500][500].
    spiral = [[0 for _ in range(1001)] for _ in range(1001)]

    # Start drawing the spiral, beginning at the center:
    row, col = 500, 500
    offset = 1
    countdown_to_turn = offset
    direction = 0  # 0 = right, 1 = down, 2 = left, 3 = up

    # The spiral will contain the numbers 1 ... 1001*1001.
    for i in range(1, 1001*1001 + 1):
        # Place a number at the current position,
        # then move one step in direction.
        spiral[row][col] = i

        if   direction % 4 == 0:  # right
            col += 1
        elif direction % 4 == 1:  # down
            row += 1
        elif direction % 4 == 2:  # left
            col -= 1
        elif direction % 4 == 3:  # up
            row -= 1

        # If we've reached a corner in the spiral,
        # we have to change direction.
        countdown_to_turn -= 1
        if countdown_to_turn == 0:
            direction += 1
            direction %= 4
            # Before beginning to move horizontally, we have to increase the offset,
            # (see my notes at the top: 1 right, 1 down, 2 left, 2 up, 3 right, 3 down ...)
            # which affects when we'll change direction next time.
            if direction % 2 == 0:
                offset += 1
            countdown_to_turn = offset

    # Now that we've generated the spiral, we can simply calculate the sum
    # of the diagonals. We just sum up both diagonals, then subtract the center:
    diagSum = 0
    for i in range(1001):
        diagSum += spiral[i][i]  # diagonal from top left to bottom right
        diagSum += spiral[i][1000 - i]  # diagonal from top right to bottom left
    diagSum -= spiral[500][500]  # Mustn't double-count the center.
    return diagSum


if __name__ == "__main__":
    print(f"The sum of the two diagonals of the 1001*1001 spiral is: {run()}")
