# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.

rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}


def movebetweenrooms(player, direction):

# Returns the new player state after moving into another room


    current_room = player

    # check if there is a room in the specified direction
    if direction in rooms[current_room]:
        current_room = rooms[current_room][direction]

    # error handling
    else:
        print("There is nothing in that direction!")

    # return the player state
    return current_room


def displayinstructions():

# display the starting instructions


    print("Simplified Dragon Text Game\n\n"
          "Collect 6 items to win the game, or be killed by the Dragon.\n"
          "Move commands: go South, go North, go East, go West\n")


def main():
    displayinstructions()
    player = ("Great Hall", [])

    while True:

        current_room = player

        # Player info
        # -----------
        print(f"\nYou are in the {current_room}")

        # Game ending
        # -----------
        if player[0] == "Cellar":

            if len(player[1]) == 0:
                print(f"Congratulations! You have defeated the Dragon!")
            else:
                print("GAME OVER!")

            # greeting and exiting
            print("Thanks for playing the game. Hope you enjoyed it.")
            break

        # input validation and parsing
        # ----------------------------
        # get the player's move
        print("-" * 35)
        move = input("Enter your move:\n")

        # invalid move syntax
        if " " not in move:
            print("Invalid input!")
            continue

        # split the move into an action and an argument
        action, arg = move.split(" ", 1)

        # move into another room
        if action == "go":
            movebetweenrooms(player, arg)

        # invalid action
        else:
            print("Invalid input!")


input("Press ENTER to exit")
if __name__ == '__main__':
        main()