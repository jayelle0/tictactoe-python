# display board 
def display_board(board): 
    print( board[7] + '|' +board[8]+ '|' + board[9])
    print ('-----')
    print( board[4] + '|' +board[5]+ '|' + board[6])
    print ('-----')
    print( board[1] + '|' +board[2]+ '|' + board[3])


# board = ['#',' ',' ',' ',' ',' ' ,' ',' ',' ',' ' ]
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

player_input()