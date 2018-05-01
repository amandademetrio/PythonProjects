#Tic Tac Toe

#Possible grid positions. Format is row,column numbers. Tuples.
grid_positions = [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3)]

grid_status = { 
    (1,1):" ",
    (1,2):" ",
    (1,3):" ",
    (2,1):" ",
    (2,2):" ",
    (2,3):" ",
    (3,1):" ",
    (3,2):" ",
    (3,3):" "
}

def onboarding_instructions():
    """Function that prints onboarding instructions on the screen. Also prints the grid where game will be played"""

    print "Hi! This is a game of Tic Tac Toe. The goal is to get three of the same item (x or o) on the same row or column (including diagonals!). The game is played on a three by three game board like this one:"
    print ""
    print "   |   |   "
    print " " + grid_status[(1,1)] + " | " + grid_status[(1,2)] + " | " + grid_status[(1,3)]
    print "___|___|___"
    print "   |   |   "
    print " " + grid_status[(2,1)] + " | " + grid_status[(2,2)] + " | " + grid_status[(2,3)]
    print "___|___|___"
    print "   |   |   "
    print " " + grid_status[(3,1)] + " | " + grid_status[(3,2)] + " | " + grid_status[(3,3)]
    print "   |   |   "
    print ""

def print_board():
    """Just prints the current status of the board in the formatting required by tic tac toe"""
    
    print ""
    print "   |   |   "
    print " " + grid_status[(1,1)] + " | " + grid_status[(1,2)] + " | " + grid_status[(1,3)]
    print "___|___|___"
    print "   |   |   "
    print " " + grid_status[(2,1)] + " | " + grid_status[(2,2)] + " | " + grid_status[(2,3)]
    print "___|___|___"
    print "   |   |   "
    print " " + grid_status[(3,1)] + " | " + grid_status[(3,2)] + " | " + grid_status[(3,3)]
    print "   |   |   "
    print ""

def make_a_move(board):
    """Game asks for user name (and stores it), game asks for row number, game asks for column number"""
    
    #Need to add later: check if user input is valid
    player_number = int(raw_input("Which player are you? 1 or 2? > "))
    
    #Need to add later: check if user input is valid
    row_number = int(raw_input("Which row would you like to pick? > "))
    
    #Need to add later: check if user input is valid
    column_number = int(raw_input("Which column would you like to pick? > "))
    
    #Check if choice was already made
    user_choice = board[(row_number,column_number)]
    if user_choice != " ":
        print "This position was already filled; please pick another one"
        make_a_move(board)
    else:
        #Updating the board
        if player_number == 1:
            board[(row_number,column_number)] = "x"
            return board
        elif player_number == 2:
            board[(row_number,column_number)] = "o"
            return board

def check_for_win(board):
    """Checks board for row, column and diagonal wins; returns True if there was no win. Returns False if there was a win"""
    
    #Checking for matches in rows
    if board[(1,1)] == board [(1,2)] == board [(1,3)] == "x":
        winner = 1
        return winner
    elif board[(2,1)] == board [(2,2)] == board [(2,3)] == "x":
        winner = 1
        return winner
    elif board[(3,1)] == board [(3,2)] == board [(3,3)] == "x":
        winner = 1
        return winner
        
    elif board[(1,1)] == board [(1,2)] == board [(1,3)] == "o":
        winner = 2
        return winner
    elif board[(2,1)] == board [(2,2)] == board [(2,3)] == "o":
        winner = 2
        return winner
    elif board[(3,1)] == board [(3,2)] == board [(3,3)] == "o":
        winner = 2
        return winner
        
    #Checking for matches in columns
    if board[(1,1)] == board [(2,1)] == board [(3,1)] == "x":
        winner = 1
        return winner
    elif board[(1,2)] == board [(2,2)] == board [(3,2)] == "x":
        winner = 1
        return winner
    elif board[(1,3)] == board [(2,3)] == board [(3,3)] == "x":
        winner = 1
        return winner
        
    elif board[(1,1)] == board [(2,1)] == board [(3,1)] == "o":
        winner = 2
        return winner
    elif board[(1,2)] == board [(2,2)] == board [(3,2)] == "o":
        winner = 2
        return winner
    elif board[(1,3)] == board [(2,3)] == board [(3,3)] == "o":
        winner = 2
        return winner
        
    #Checking for diagonals
    if board[(1,1)] == board[(2,2)] == board[(3,3)] == "x":
        winner = 1
        return winner
    elif board [(3,1)] == board[(2,2)] == board[(1,3)] == "x":
        winner = 1
        return winner
    
    elif board[(1,1)] == board[(2,2)] == board[(3,3)] == "o":
        winner = 2
        return winner
        
    elif board [(3,1)] == board[(2,2)] == board[(1,3)] == "o":
        winner = 2
        return winner

def check_for_tie(board):
    """Checks if there was a tie, which is no empty positions on the board. Tie is True means there's a tie. Tie is False means there's not a tie"""
    
    tie_status = True
    
    while tie_status:
        for key in board:
            if board[key] == " ":
                tie_status = False

	return tie_status
  
def play_game(board):
    #First, prints the board and instructions
    onboarding_instructions()
    
    playing = True
    
    while playing:
        make_a_move(board)
        print_board()
    
        winner = check_for_win(board)
        tie = check_for_tie(board)
        
        if tie == True:
            print "It's a tie! Start over, please"
            break
        elif winner == None:
             playing = True
        elif winner == 1:
            print "Player 1 has won!"
            break
        elif winner == 2:
            print "Player 2 has won!"
            break
            
play_game(grid_status)