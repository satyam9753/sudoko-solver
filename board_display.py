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

#sudoko_board(sample_board)


def empty_squares(b):   #finding empty squares in the given sudoko board

	for i in range(len(b)):
		for j in range(len(b[0])):
			
			if b[i][j] == 0:
				return (i,j)  #ROW, COLUMN
	return None


def validNumberBoard(b, num, pos):

    # FOR ROW-WISE CHECKING...
    for i in range(len(b[0])):
        
        if b[pos[0]][i] == num and pos[1] != i:  
            return False

    # FOR COLUMN-WISE CHECKING...
    for i in range(len(b)):
        
        if b[i][pos[1]] == num and pos[0] != i:
            return False

    # CHECKING WHICH BOX WE ARE CURRENTLY DEALING WITH...
    box_horizontal = pos[1] // 3
    box_vertical = pos[0] // 3


    for i in range(box_vertical*3, box_vertical*3 + 3):
        for j in range(box_horizontal * 3, box_horizontal*3 + 3):

            if b[i][j] == num and (i,j) != pos:
                return False

    return True


def backtrackSolve(b):

    find = empty_squares(b)# go looking for empty squares till each square is filled
    if not find:
        return True
    else:
        row, col =  find

    for i in range(1,10): # since SUDOKO BOARD has numbers from 1 to 9.
        if validNumberBoard(b, i, (row,col)):
            b[row][col] = i   #if valid number is found, we add that to our board

            if backtrackSolve(b):
                return True

            b[row][col] = 0   #reset the element to 0
    return False



#sudoko_board(sample_board) #before solving
backtrackSolve(sample_board)
sudoko_board(sample_board)  #after solving


