import random

board = []
snakes = { 16: 6, 48: 30, 64: 60 }
ladders = { 1: 38, 4: 14, 9: 31 }

for i in range(1, 101):
    if i in snakes:
        board.append('🐍 ')
    elif i in ladders:
        board.append('🪜 ')
    else:
        board.append(str(i))

def roll_dice():
    dice_value = random.randint(1, 6)
    return dice_value

def check_snake_or_ladder(position):
    if position in snakes:
        print("Ouch! Here's a snake 🐍. Going down to", snakes[position])
        return snakes[position]
    elif position in ladders:
        print("Yay! Found a ladder. Going up to", ladders[position])
        return ladders[position]
    else:
        return position
    
def player_turn(current_position):
    input("Press Enter to roll the dice...")
    dice_value = roll_dice()
    print("You rolled a", dice_value,"🎲")
    current_position += dice_value
    if current_position > 100:
        print("Position exceeds 100! Try again next turn.")
        return current_position - dice_value  
    current_position = check_snake_or_ladder(current_position)
    print("You're now at position", current_position)
    return current_position

def is_winner(position):
    if position == 100:
        return True
    
def switch_player(current_player, total_players):
    current_player = (current_player + 1) % total_players
    return current_player

def play_game():
    print("Welcome to snakes and ladders! 🐍🪜")
    print("Board: ",board)
    n = int(input("How many players? "))
    curr_pos_player = []
    for i in range(n):
        curr_pos_player.append(0)
    current_player = 0
    while True:
        print("Player",current_player + 1,"'s turn.")
        current_position = player_turn(curr_pos_player[current_player])
        curr_pos_player[current_player] = current_position
        if is_winner(current_position):
            print("Player",current_player + 1," wins! 🎉")
            break
        current_player = switch_player(current_player, n)


play_game()
