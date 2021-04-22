import random 

# step1 - display board 
def display_board(board): 
    print( board[7] + '|' +board[8]+ '|' + board[9])
    print ('-----')
    print( board[4] + '|' +board[5]+ '|' + board[6])
    print ('-----')
    print( board[1] + '|' +board[2]+ '|' + board[3])


# test_board = ['#',' ',' ',' ',' ',' ' ,' ',' ',' ',' ' ]
# test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(board)
# display_board(test_board)


# step 2 - Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer.
def player_input(): 
    marker = ""
    while marker != "O" and marker != "X": 
        marker = input("Player 1 - Please choose X or O: ").upper()
    player1 = marker

    if player1 == "X": 
        player2 = "O"
    else: 
        player2= "X"
    return player1, player2

# to unpack tuples for use 
# player1marker, player2marker = player_input()
# print ('Player 1 Marker:' +player1marker + ' ' +'Player 2 Marker:' +player2marker)

# player_input()

# Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
def place_marker(board, marker, position):
       board[position] = marker



# **Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won. **
def win_check(board, mark):
    # true if mark has won 
    # winning_combo = [[1,2,3],[4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [3,5,7], [1,5,9]]
    return ( (board[1] == mark and  board[2]== mark and board[3] == mark) or 
    (board[4]== mark and  board[5]== mark and board[6]== mark) or 
    (board[7]== mark and  board[8]== mark and board[9]== mark) or 
    (board[1]== mark and  board[4]== mark and board[7]== mark) or 
    (board[2]== mark and  board[5]== mark and board[8]== mark) or  
    (board[3]== mark and  board[6]== mark and board[9]== mark) or  
    (board[3]== mark and  board[5]== mark and board[7]== mark) or  
    (board[1]== mark and  board[5]== mark and board[9]) == mark)

# board[1] = TRUE; need to be more specific with statement within and/or 

# place_marker(test_board,'x',1)
# place_marker(test_board,'x',2)
# place_marker(test_board,'x',3)
# place_marker(test_board,'x',4)
# place_marker(test_board,'x',5)
# place_marker(test_board,'x',6)
# place_marker(test_board,'x',7)
# place_marker(test_board,'x',8)
# place_marker(test_board,'x',9)
# display_board(test_board)
# win_check(test_board, 'x')

# Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.
def first_player(): 
    selected= random.randint(1,2)
    # print(f'Player {selected} will go first')
    return selected 

# first_player()

# **Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.**
# return true if space is blank 
def check_space(board, position):
    # print ( board[position] == ' ')
    return  board[position] == ' '

# check_space(test_board,1)

# **Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.**
def check_full(board): 
    for x in range(1,10): 
        if check_space(board, x):
            return False
    return True 

# check_full(test_board)

# Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.

def next_position( board ): 
    position = 0 
    while position not in range (1,10) or not check_space(board, position):
        position = int(input("Please choose a position (1-9): ")) 
    # print(position)
    return position 

# Use OR instead of AND because if we want function to keep running if either are false. If we use AND, then the function will stop running if one of the statements are true 
    
# next_position(test_board)


# **Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.**
def play_again(): 
    choice = '' 
    while choice != "Y" and choice != "N":
        choice = input('Would you like to play again? (Y or N)').upper() 
    if choice == "Y": 
        return True 
    else:
        return False 


# **Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!**

print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    game_board = [" "]*10
    player1_marker, player2_marker= player_input()
    turn= first_player()
    print(f'Player {turn} will go first')
    #pass

    play_game = '' 
    while play_game != "Y" and play_game != "N":
        play_game= input('Ready to play? (Y or N)').upper() 

    if play_game == "Y": 
        game_on =True
    else: 
        game_on = False
    while game_on:
        #Player 1 Turn
        if turn == 1: 
            display_board(game_board)
            position = next_position(game_board)
            place_marker(game_board, player1_marker, position)
            display_board(game_board)
            if win_check(game_board, player1_marker):
                print('You won!')
                game_on= False 
            else: 
                if not check_full(game_board):
                    turn = 2
                    print(f'It is now player {turn} turn')
                else: 
                    print('It is a tie')
                    game_on= False 

        # Player2's turn.
        else: 
            display_board(game_board)
            position = next_position(game_board)
            place_marker(game_board, player2_marker, position)
            display_board(game_board)
            if win_check(game_board, player2_marker):
                print('You won!')
                game_on= False 
            else: 
                if not check_full(game_board):
                    turn = 1
                    print(f'It is now player {turn} turn')
                else: 
                    print('It is a tie')
                    game_on= False 
            
            #pass

    if not play_again():
        break