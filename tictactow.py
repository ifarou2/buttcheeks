

"""
1|2|3
4|5|6
7|8|9
"""

board = "1|2|3\n4|5|6\n7|8|9"
turn = "x"
while True:
	print(board)
	move = input("Move: ")
	if move in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
		board = board.replace(move, turn)
		if turn == "x":
			turn = "o"
		elif turn == "o":
			turn = "x"
	
