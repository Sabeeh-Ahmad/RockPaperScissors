# 🎲 Import random module for making computer choices
import random

# 🏁 Start the game
print("Rock Paper Scissors Game\n")
# 📌 Main game loop
is_running = True
while is_running:
# 📃 Inside the loop, define variables to store scores and round information
  round = 1
  player_score = 0
  computer_score = 0
# ➰ Use a nested loop for each round. Validate inputs as well.
# Print scores at the end of round.
  while player_score < 2 and computer_score < 2:
    print("This is round number:", round)
    options = ("Rock", "Paper", "Scissors")
    computer = random.choice(options)
    player = input("Rock, Paper, Scissors? (r/p/s): ").lower()
    
    if player == "r":
      player = "Rock"
    elif player == "p":
      player = "Paper"
    elif player == "s":
      player = "Scissors"
    else:
      print("Invalid Input!")
      quit()
    print("Player:", player.capitalize())
    print("Computer:", computer.capitalize())
  # 📔 Inside the appropriate loop (inner or outer), make decision on winner
  # and show final result
    if player == "Rock" and computer == "Scissors" or player == "Paper" and computer == "Rock" or player == "Scissors" and computer == "Paper":
      print("You Win")
      player_score += 1
    elif player == computer:
      print("Tie!")
    else:
      print("You Lose!")
      computer_score += 1
    print("Score:", player_score)
    round += 1

  if player_score > computer_score:
    print("You have won the match")
  else:
    print("Computer has won the match")
# ❓ Inside the appropriate loop, Ask to play again
  play_again = input("Do you want to play again? (y/n): ").lower()
  if play_again != "y" or "yes":
    print("Thanks for playing!")
    break
