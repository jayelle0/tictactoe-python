# display board 
def display_board(board): 
    print( board[7] + '|' +board[8]+ '|' + board[9])
    print ('-----')
    print( board[4] + '|' +board[5]+ '|' + board[6])
    print ('-----')
    print( board[1] + '|' +board[2]+ '|' + board[3])


board = ['#',' ',' ',' ',' ',' ' ,' ',' ',' ',' ' ]
# test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(board)
# display_board(test_board)


# Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer.
def player_input(): 
    marker = ""
    while marker != "O" and marker != "X": 
        marker = input("Player 1 - Please choose X or O: ")
    player1 = marker

    if player1 == "X": 
        player2 = "O"
    else: 
        player2= "X"
    return player1, player2

# to unpack tuples for use 
# player1marker, player2marker = player_input()

# print ('Player 1 Marker:' +player1marker + ' ' +'Player 2 Marker:' +player2marker)

# Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
def place_marker(board, marker, position):
    if board[position] == " ":
       board[position] = marker
    else: 
        print ('Please choose different position')

place_marker(board,'$',8)
display_board(board)

# **Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won. **
def win_check(board, mark):

# Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.

# **Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.**

# **Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.**

# Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.

# **Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.**

# **Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!**