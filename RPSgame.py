import random

CHOICES = {"1": "Rock", "2": "Paper", "3": "Scissors"}
BEATS = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
TARGET = 3

print("=== Rock - Paper - Scissors ===")
print(f"First to {TARGET} points wins!\n")

player_score = 0
computer_score = 0

while player_score < TARGET and computer_score < TARGET:
    print("1) Rock   2) Paper   3) Scissors")
    pick = input("Your choice: ").strip()

    if pick not in CHOICES:
        print("Invalid input! Enter 1, 2 or 3.\n")
        continue

    player = CHOICES[pick]
    computer = random.choice(list(CHOICES.values()))
    print(f"You: {player} | Computer: {computer}")

    if player == computer:
        print("It's a draw! Play again.")
    elif BEATS[player] == computer:
        player_score += 1
        print("You win this round!")
    else:
        computer_score += 1
        print("Computer wins this round!")

    print(f"Score -> You: {player_score} | Computer: {computer_score}\n")

if player_score == TARGET:
    print("Congratulations! You won the game!")
else:
    print("Computer wins the game. Better luck next time!")

