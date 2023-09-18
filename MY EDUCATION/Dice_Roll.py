import random

def roll_dice():
    # Generate a random number between 1 and 6 (inclusive) to simulate rolling a dice
    dice_result = random.randint(1, 6)
    
    # Print the result of the dice roll
    print(f"You rolled a {dice_result}")

# Call the roll_dice function to roll the dice
roll_dice()
