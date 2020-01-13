sample_board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

def sudoko_board(b):
	
    for i in range(len(b)):

        if i % 3 == 0 and i != 0:
            print("_ _ _ _ _ _ _ _ _ _ _ _ ")

        for j in range(len(b[0])):

            if j % 3 == 0 and j != 0:
                print(" | ", end = "")  # end="" is just to say that you want a space after the end of the statement instead of a new line character.

            if j == 8:
                print(b[i][j])

            else:
                print(str(b[i][j]) + " ", end = "")
            print(b[0] + "@")

sudoko_board(sample_board)


def empty_squares(b):   #finding empty squares in the given sudoko board

	for i in range(len(b)):
		for j in range(len(b[0])):
			
			if b[i][j] == 0:
				return (i,j)  #ROW, COLUMN


#def valid_board():



