# Fantasy Text Game
# Created by Kyle Mann
# Created for SNHU IT-140
# Almost done

# Dictionary of rooms, items, and directions
rooms = {'Training Camp': {'name': 'the Training Camp', 'North': 'Clearing', 'item': 'None'},
         'Clearing': {'name': 'Clearing', 'South': 'Training Camp', 'North': 'Forest Maze', 'East': 'Cave', 'item': 'Master Sword', 'description': 'A mysterious sword that somehow shoots laser beams'},
         'Cave': {'name': 'Cave', 'West': 'Clearing', 'item': 'Holy Hand Grenade of Antioch', 'description': 'And the number you count to is three, no more no less'},
         'Forest Maze': {'name': 'Forest Maze', 'South': 'Clearing', 'East': 'Camp Site', 'item': 'Needler', 'description': 'An alien device that somehow shoots needles at rapid speeds'},
         'Camp Site': {'name': 'Camp Site', 'West': 'Forest Maze', 'East': 'Graveyard', 'item': 'Project Sekai Game', 'description': 'Why do I all of a sudden want to tap the screen rapidly in beat'},
         'Graveyard': {'name': 'Graveyard', 'South': 'Mysterious Room', 'West': 'Camp Site', 'item': 'Magic Mushroom', 'description': 'Hopefully this is not deadly'},
         'Mysterious Room': {'name': 'Mysterious Room', 'South': 'Exit', 'North': 'Graveyard', 'item': 'Dragon Balls', 'description': 'What is your wish, I do not have all day'},
         'Exit': {'name': 'Exit', 'item': 'None'}
}

# Begin adventure with instructions
print('Magical Text Adventure Game\n')
print('Collect 6 items to win the game, or be defeated by the Darkness.')
print('Move commands: Go South, Go North, Go East, Go West')
print('Add to Inventory: Get Item')

# Get user's name
user_name = input('Enter your name: \n').title()

# Setting up variables
current_room = rooms['Training Camp']
directions = ['North', 'South', 'East', 'West']
Inventory = {}
user_inv = list(Inventory.values())

# Display current information
while current_room != 'Exit':
    print('-' * 42)
    print('You are in the {}'.format(current_room['name']))
    print("{}'s current inventory: {}".format (user_name, list(Inventory.values())))
# Output current possible directions to move
    rooms_directions = list(current_room.keys())
    rooms_directions1 = rooms_directions[1:-2]
    print ('\nCurrent directions you can go')
    print (rooms_directions1)
    print()

# Check for item in current room
    if current_room['item'] != 'None':
        print('There is a treasure chest in this room...Hopefully it is not a mimic...')
    else:
        print('There is nothing worth taking in this room...You kleptomaniac!!!')

    user_command = input('Enter your move: \n>>> ').title()
    user_direction = user_command.split()
    user_move = user_direction[-1]
    user_command_move = user_move.title()

# Movement handling
    if user_command_move in directions:
        if user_command_move in current_room and user_direction[0] == 'Go':
            current_room = rooms[current_room[user_command_move]]

# Win scenario
            if (current_room['name'] == 'Mysterious Room') and (len(Inventory.keys()) != 5):
                print('You lose {}, but unfortunately the Darkness took the cake with it.'.format (user_name))
                break


# Error handling of direction input that is invalid
        else:
            print('\nA mysterious force prevents you from going that way.')

            # Win scenario
        if current_room['name'] == 'Exit' and (len(Inventory.keys()) == 6):
            print ("Congratulations on defeating the darkness {}, you didn't even have to cast magic missile to do it".format(user_name))
            break
        elif current_room['name'] == 'Exit' and (len(Inventory.keys()) != 6):
            print ("\nA mysterious force prevents you from leaving, perhaps you forgot an item?")
            current_room = rooms['Training Camp']

# Item management
    elif user_command == 'Get Item':
        if current_room['item'] != 'none':
            Inventory['Item' + str(len(Inventory.keys()) + 1)] = current_room['item']
            print("You acquired : ", current_room['item'])
            print(current_room['description'])
            print ()
            print ('Current Inventory:')
            print(user_inv)
            current_room['item'] = 'None'
        else:
            print("No items to collect in this room")

# Player decides to quit game
    elif user_command == 'Quit':
        print('Thanks for playing {}!'.format(user_name))
        break

# Error handling of wrong input entered
    else:
        print('Invalid input')