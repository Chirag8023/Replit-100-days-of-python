import random  # Added to generate random moves for the computer player

player1Score = 0
player2Score = 0
totalGames = 0
print("EPIC BATTLE!")
Moves = ["rock", "paper", "scissor"]

while totalGames < 3:
    totalGames += 1
    print("Round", totalGames)  # Use totalGames instead of 1 to display the correct round number
    print("Select your moves")
    player1move = input("Player1, what is your move? ").lower()  # Convert input to lowercase for consistency
    player2move = random.choice(Moves)  # Generate a random move for player 2 (computer)
    
    print("Player2 chose:", player2move)  # Display the computer's choice
    
    if player1move not in Moves:
        print("Invalid move. Please choose from 'rock', 'paper', or 'scissor'.")
        totalGames -= 1  # Decrement totalGames if the input was invalid
        continue

    if player1move == player2move:
        print("It's a tie")
    elif (
        (player1move == "rock" and player2move == "scissor")
        or
        (player1move == "paper" and player2move == "rock")
        or
        (player1move == "scissor" and player2move == "paper")
    ):
        print("Player1 wins!")
        player1Score += 1
    else:
        print("Player2 wins!")
        player2Score += 1

# Determine the overall winner
if player1Score > player2Score:
    print("Player1 is the overall winner")
elif player2Score > player1Score:
    print("Player2 is the overall winner")
else:
    print("It's a tie. No overall winner")