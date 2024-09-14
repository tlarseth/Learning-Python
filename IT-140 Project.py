#Create library of 8 rooms and directions
#Create library of 7 items
#Create def for actions
#Create item tracker
#Include error handling on actions and item names
#Create Win/Lose parameters

# Move between rooms with error handling

class Items:
    def __init__(self, name, disciption):
        self.name = name
        self.position = disciption


sword = Weapon("Master Sword", "It's dangerous to go alone, take this.")
grenade = Weapon("Holy Hand Grenade of Antioch", "Three shall be the number thou shalt count, and the number of the counting shall be three. Four shalt thou not count, neither count thou two, excepting that thou then proceed to three. Five is right out. Once the number three, being the third number, be reached, then lobbest thou thy Holy Hand Grenade of Antioch towards thy foe, who, being naughty in my sight, shall snuff it")
mushroom = Items("Magic Mushroom", "Why are my pants now shorts?")
game = Items("Hatsune Miku Colorful Stage", "Blame my 15 year old daughter for this one")
doll = Items("Freddy Fazbear Plushy", "Can you survive five nights?")
paimon = Items("Paimon", "Emergency Rations:  Just in case you get hungry")


rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'West': 'Cellar'},
    'Cellar': {'West': 'Exit', 'East': 'Bedroom'},
    'Exit': {'East': 'Cellar'}
}
items = {'Great Hall': 'Sword'}
print ('To navigate type the cardinal direction you want to move in "North, South, East, and West"  Type "Exit" to leave the game')


current_room = "Great Hall"

while current_room != "Exit":
    print("You are in the", current_room)
    print("Which direction will you go?")
    print("The possible directions are:", rooms[current_room])
    print("There is a {} in this room".format(items[current_room]))

    get = input(">>> ").title()
    if get in items[current_room]:
        items.pop("get", None)
    print("There is a {} in this room".format(items[current_room]))
    #direction = input(">>> ").title()

    #if direction in rooms[current_room]:
       # current_room = rooms[current_room][direction]
    #else:
        #print("Can not do that.\nTry another direction.")


#print("Congratulations you made it safely.")