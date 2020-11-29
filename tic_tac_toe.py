board = {'1': ' ', '2': ' ', '3': ' ',
        '4': ' ', '5': ' ', '6': ' ',
        '7': ' ', '8': ' ', '9': ' '}

keys = []

for key in board:
    keys.append(key)

# function to print the board after every move
def boardAfterEveryMove(sampleBoard):
    print(sampleBoard['1'] + '|' + sampleBoard['2'] + '|' + sampleBoard['3'])
    print('-+-+-')
    print(sampleBoard['4'] + '|' + sampleBoard['5'] + '|' + sampleBoard['6'])
    print('-+-+-')
    print(sampleBoard['7'] + '|' + sampleBoard['8'] + '|' + sampleBoard['9'])

def mainGame():

    turn = 'X'
    count = 0

    for i in range(10):
        boardAfterEveryMove(board)
        print("'Your turn now '" + turn + "' where do you wanna move?'")

        move = input()

        if board[move] == ' ':
            board[move] = turn
            count += 1
        else:
            print("Sorry, this space is already filled.\ntry again")
            continue

        #check if player X or O has won,for every move after 5 moves

        if count >= 5:
            if board['1'] == board['2'] == board['3'] != ' ': 
                boardAfterEveryMove(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif board['4'] == board['5'] == board['6'] != ' ':
                boardAfterEveryMove(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif board['7'] == board['8'] == board['9'] != ' ':
                boardAfterEveryMove(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif board['1'] == board['4'] == board['7'] != ' ': # down the left side
                boardAfterEveryMove(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif board['2'] == board['5'] == board['8'] != ' ': # down the middle
                boardAfterEveryMove(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif board['3'] == board['6'] == board['9'] != ' ': # down the right side
                boardAfterEveryMove(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif board['7'] == board['5'] == board['3'] != ' ': # diagonal
                boardAfterEveryMove(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif board['1'] == board['5'] == board['9'] != ' ': # diagonal
                boardAfterEveryMove(board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
        # when the board is full, we'll declare the result as 'tie'
        if count == 9:
            print("\nGame Over\n")
            print("It was a tie !!!")

        #to change the player after every move

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
            
    # now asking if the player wants to restart the game

    askToReplay = input("Do you wanna play again? (y/n)")
    if askToReplay == "y" or askToReplay == "Y":
        for key in keys:
            board[key] = " "
        mainGame()

if __name__ == "__main__":
    mainGame() 
