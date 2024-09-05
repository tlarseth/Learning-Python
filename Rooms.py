rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'West': 'Cellar'},
    'Cellar': {'West': 'Exit', 'East': 'Bedroom'},
    'Exit': {'East': 'Cellar'}
}

print ('To navigate type the cardinal direction you want to move in "North, South, East, and West"  Type "Exit" to leave the game')


current_room = "Great Hall"

while current_room != "Exit":
    print("You are in the", current_room)
    print("Which direction will you go?")

    direction = input(">>> ").title()

    if direction in rooms[current_room]:
        current_room = rooms[current_room][direction]
    else:
        print("Can not do that.\nTry another direction.")

print("Congratulations you made it safely.")