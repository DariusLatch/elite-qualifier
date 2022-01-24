

room = [
   'xxxxx',
  'x..ex',
   'x...x',
   'x...x',
   'xxxxx',
 ]

def announce_walls(current_row, current_col):
    if room[current_row - 1][current_col] == 'x':
        print("There is a wall 'up'")
    if room[current_row + 1][current_col] == 'x':
        print("There is a wall 'down'")
    if room[current_row][current_col - 1] == 'x':
        print("There is a wall 'left'")
    if room[current_row][current_col + 1] == 'x':
        print("There is a wall 'right'")

def move(current_row, current_col, direction):
    new_row = current_row
    new_col = current_col

    if direction == "up":
        new_row -= 1
    elif direction == "down":
        new_row += 1
    elif direction == "left":
        new_col -= 1
    elif direction == "right":
        new_col += 1
    else:
        print(f"You can't move {direction}. Try using the commands left,right,up, and down")

    if room[new_row][new_col] == 'x': 
        print("There is a wall blocking your path, you cannot move that way!")
        return current_row, current_col

    return new_row, new_col


player_row = 2
player_col = 2

while room[player_row][player_col] != 'e':
    announce_walls(player_row, player_col)
    direction = input('What direction would you like to move? ')
    
    player_row, player_col = move(player_row, player_col, direction)

print('You have escaped the maze GG!')
