# Solution to Project Euler problem 81.

# Solution based on decimating the matrix, in analogy to problem 18.
# For some reason, I decided to decimate the matrix one diagonal at a time,
# which resulted in some weird code.


def run():
    # Initialize the matrix:
    with open('Euler081_matrix.txt', 'r') as inputFile:
        matrix = []
        for line in inputFile.read().splitlines():  # Result: 80 lines of strings like "1234,1234,4321,1234,4312".
            matrix_row = [int(s) for s in line.split(',')]
            matrix.append(matrix_row)
        matrixLength = len(matrix)

    # Decimate the matrix one diagonal at a time, beginning with the top left.
    # Which row, col pairs describe a specific diagonal? Answer: those with 
    # row + col + 1 = constant (I call this constant the "diagonalNumber").
    for diagonalNumber in range(2, matrixLength * 2):
        # While we're still in the upper left half of the matrix, plus the diagonal,
        # the row index lies between these limits:
        if diagonalNumber < matrixLength + 1:  # 
            rowStart = 0
            rowEnd = diagonalNumber
        # Once we're in the lower right half of the matrix, the row index
        # lies between these limits, instead:
        # (I suspect this part could be simplified by using or allowing negative indices.)
        else:
            rowStart = diagonalNumber - matrixLength
            rowEnd = matrixLength
        
        for row in range(rowStart, rowEnd): 
            col = (diagonalNumber - 1) - row  # row + col = diagonalNumber - 1
            
            # Decimate the diagonal by adding to the current cell
            # the minimum of the cells to the top and to the left:
            if row == 0:
                matrix[row][col] += matrix[row][col - 1]
            elif col == 0:
                matrix[row][col] += matrix[row - 1][col]
            else:
                matrixUp = matrix[row - 1][col]
                matrixLeft = matrix[row][col - 1]
                matrix[row][col] += min(matrixUp, matrixLeft)

    return matrix[-1][-1]


if __name__ == "__main__":
    print(f"The minimal path sum in the 80x80 matrix is: {run()}")
