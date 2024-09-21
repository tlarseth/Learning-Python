# Fantasy Text Game
# Created by Kyle "Dae'Loki" Mann
# Created for SNHU IT-140



rooms = {'Training Camp': {'name': 'the Training Camp', 'Go North': 'Clearing', 'item': 'None'},
         'Clearing': {'name': 'Clearing', 'Go South': 'Training Camp', 'Go North': 'Forest Maze', 'Go East': 'Cave', 'item': 'Master Sword'},
         'Cave': {'name': 'Cave', 'Go West': 'Clearing', 'item': 'Holy Hand Grenade of Antioch'},
         'Forest Maze': {'name': 'Forest Maze', 'Go South': 'Clearing', 'Go East': 'Camp Site', 'item': 'Needler'},
         'Camp Site': {'name': 'Camp Site', 'Go West': 'Forest Maze', 'Go East': 'Graveyard', 'item': 'Project Sekai Game'},
         'Graveyard': {'name': 'Graveyard', 'Go South': 'Mysterious Room', 'item': 'Magic Mushroom'},
         'Mysterious Room': {'name': 'Mysterious Room', 'Go South': 'Exit', 'item': 'Dragon Balls'},
         'Exit': {'name': 'Exit', 'item': 'None'}
}


print('Magical Text Adventure Game\n')
print('Collect 6 items to win the game, or be defeated by the Darkness.')
print('Move commands: Go South, Go North, Go East, Go West')
print('Add to Inventory: Get Item')

current_room = rooms['Training Camp']
directions = ['Go North', 'Go South', 'Go East', 'Go West']
Item = ['Master Sword', 'Holy Hand Grenade of Antioch', 'Needler', 'Project Sekai Game', 'Magic Mushroom', 'Dragon Balls']
Inventory = {}
user_inv = list(Inventory.values())
while current_room != 'Exit':
    print('-' * 42)
    print('You are in the {}'.format(current_room['name']))
    print('Your current inventory: {}'.format (list(Inventory.values())))
    if current_room['item']:
        print('Item in room: {}'.format(''.join(current_room['item'])))
        print('')

    user_command = input('Enter your move: \n>>> ').title()

    if user_command in directions:
        if user_command in current_room:
            current_room = rooms[current_room[user_command]]
            if (current_room['name'] == 'Mysterious Room') and (len(Inventory.keys()) != 5):
                print('You lose, but unfortunately the Darkness took the cake with it.')
                break
            else:
                print('You see an item that is up for grabs...hopefully it is not a mimic...')
        else:
            print('\nA mysterious force prevents you from going that way.')
        if current_room['name'] == 'Exit':
            print ("Congradulations on defeating the darkness, you didn't even have to cast magic missile to do it")
            break
    elif user_command == 'Get Item':
        if current_room['item'] != 'none':
            Inventory['Item' + str(len(Inventory.keys()) + 1)] = current_room['item']
            # Inventory.append(current_room['item'])

            print("You acquired : ", current_room['item'])
            print ()
            print ('Current Inventory:')
            print(user_inv)
            current_room['item'] = 'none'
        else:
            print("No items to collect in this room")


    elif user_command == 'Quit':
        print('Thanks for playing!')
        break

    else:
        print('Invalid input')
