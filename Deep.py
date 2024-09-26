def main():
    y = str(input("What is the answer to the great question of life, the universe, and everything?"))
    x = y.strip()
    if x == ("42"):
        print ("Yes")
    elif x == ("Fourty Two"):
        print ("Yes")
    elif x == ("forty-two"):
        print ("Yes")
    elif x == ("FoRty TwO"):
        print ("Yes")
    elif x == ("forty two"):
        print ("Yes")
    else:
        print ("No")


main()