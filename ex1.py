board = [[],[],[]]

def fill_board():
	for row in board:
		for i in range(0, 3):
			row.append("|_|")

def print_board():
	for row in board:
		for col in row:
			print col,
		print

print "Welcome towards Tic Tac Toe!"
print "Enter whether you want to be player X or player O."
player_choice = raw_input()

def player_symbol():
	if player_choice == 'x':
		return "|X|"
	return "|O|"	

def ai_symbol():
	if player_choice == 'x':
		return "|O|"
	return "|X|"
	
fill_board()
print_board()
print "Enter row, col (e.g. 2,1) to place an " + player_choice + "."
print "Or enter 'quit' to quit the game."

placement_coordinates = raw_input()

def parse_input(placement_coordinates):
	coordinate_list = placement_coordinates.split(",", 2)
	row = int(coordinate_list[0])
	col = int(coordinate_list[1])
	return [row,col]
	
def make_move(coordinates, player):
	board[coordinates[0]][coordinates[1]] = player

def ai_horizontal_tail_move(player, scanned_player):
	for row in board:
		for i in range(0, 2):
			if row[i] == row[i + 1] and row[i] == scanned_player:
				if i == 0 and row[i + 2] == "|_|":
					row[i + 2] = player
					return True
				elif row[i - 1] == "|_|":
					row[i - 1] = player
					return True
	return False

def ai_vertical_tail_move(player, scanned_player):
	for j in range(0, 3):
		for i in range(0, 2):
			if board[i][j] == board[i + 1][j] and board[i][j] == scanned_player:
				if i == 0 and board[i + 2][j] == "|_|":
					board[i + 2][j] = player
					return True 
				elif board[i - 1][j] == "|_|":
					board[i - 1][j] = player
					return True
	return False
	
def ai_diagonal_tail_move(player, scanned_player):
	for i in range(0, 2):
		if board[i][i] == board[i + 1][i + 1] and board[i][i] == scanned_player:
			if i == 0 and board[i + 2][i + 2] == "|_|":
				board[i + 2][i + 2] = player
				return True
			elif board[i - 1][i - 1] == "|_|":
				board[i - 1][i - 1] = player
				return True
	if board[2][0] == board[1][1] and board[2][0] == scanned_player:
		if board[0][2] == "|_|":
			board[0][2] = player
			return True
	elif board[0][2] == board[1][1] and board[0][2] == scanned_player:
		if board[2][0] == "|_|":
			board[2][0] = player
			return True
	return False
	
def ai_horizontal_sandwich_move(player, scanned_player):
	for row in board:
		if row[0] == row[2] and row[0] == scanned_player:
			if row[1] == "|_|":
				row[1] = player
				return True
	return False
	
def ai_vertical_sandwich_move(player, scanned_player):
	for j in range(0, 3):
		if board[0][j] == board[2][j] and board[0][j] == scanned_player:
			if board[1][j] == "|_|":
				board[1][j] = player
				return True
	return False

def ai_diagonal_sandwich_move(player, scanned_player):
	if board[1][1] == "|_|":
		if board[0][0] == board[2][2] and board[0][0] == scanned_player:
			board[1][1] = player
			return True
		elif board[2][0] == board[0][2] and board[2][0] == scanned_player:
			board[1][1] = player
			return True
	return False 

def ai_center_move(player):
	if board[1][1] == "|_|":
		board[1][1] = player
		return True
	return False

def ai_corner_move(player):
	if board[0][0] == "|_|":
		board[0][0] = player
		return True
	elif board[0][2] == "|_|":
		board[0][2] = player 
		return True
	elif board[2][0] == "|_|":
		board[2][0] = player 
		return True
	elif board[2][2] == "|_|":
		board[2][2] = player 
		return True
	return False

def ai_side_move(player):
	if board[1][0] == "|_|":
		board[1][0] = player
		return True
	elif board[2][1] == "|_|":
		board[2][1] = player
		return True
	elif board[1][2] == "|_|":
		board[1][2] = player
		return True
	elif board[0][1] == "|_|":
		board[0][1] = player
		return True
	return False
	
def ai_tails_check():
	if not ai_horizontal_tail_move(ai_symbol(), ai_symbol()):
		if not ai_horizontal_tail_move(ai_symbol(), player_symbol()):
			if not ai_vertical_tail_move(ai_symbol(), ai_symbol()):
				if not ai_vertical_tail_move(ai_symbol(), player_symbol()):
					if not ai_diagonal_tail_move(ai_symbol(), ai_symbol()):
						if not ai_diagonal_tail_move(ai_symbol(), player_symbol()):
							return False
	return True
	
def ai_sandwich_check():
	if not ai_horizontal_sandwich_move(ai_symbol(), ai_symbol()):
		if not ai_horizontal_sandwich_move(ai_symbol(), player_symbol()):
			if not ai_vertical_sandwich_move(ai_symbol(), ai_symbol()):
				if not ai_vertical_sandwich_move(ai_symbol(), player_symbol()):
					if not ai_diagonal_sandwich_move(ai_symbol(), ai_symbol()):
						if not ai_diagonal_sandwich_move(ai_symbol(), player_symbol()):
							return False
	return True
	
def ai_last_moves():
	if not ai_center_move(ai_symbol()):
		if not ai_corner_move(ai_symbol()):
			if not ai_side_move(ai_symbol()):
				return False
	return True
	
def ai_turn():
	if not ai_tails_check():
		if not ai_sandwich_check():
			if not ai_last_moves():
				return False
	return True
	
def check_for_horizontal_win():
	for row in board:
		if row[0] == row[1] and row[1] == row[2]:
			if row[0] != "|_|":
				return True
	return False

def check_for_vertical_win():
	for j in range(0, 3):
		if board[0][j] == board[1][j] and board[1][j] == board[2][j]:
			if board[0][j] != "|_|":
				return True
	return False
	
def check_for_diagonal_win():
	if board[1][1] != "|_|":
		if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
			return True
		elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
			return True
	return False
	
def check_for_win():
	if not check_for_horizontal_win():
		if not check_for_vertical_win():
			if not check_for_diagonal_win():
				return False
	return True
			
while(placement_coordinates != "quit"):
	coordinates = parse_input(placement_coordinates)
	if board[coordinates[0]][coordinates[1]] != "|_|":
		print "That spot is taken, try again."
	else:
		make_move(coordinates, player_symbol())
		if check_for_win():
			print_board()
			print "You won!!! Game over."
			break
		elif not ai_turn():
			print_board()
			print "Game over. It was a tie."
			break
		elif check_for_win():
			print_board()
			print "You lost. Game over."
			break
		else:
			print_board()
		
	print "Enter row, col (e.g. 2,1) to place an " + player_choice + "."
	print "Or enter 'quit' to quit the game."
	placement_coordinates = raw_input()

 
	