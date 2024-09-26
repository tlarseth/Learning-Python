def main():
    x = input('Greetings mortal!!! : ').replace(" ", "").lower()
    if x.find("hello") != -1:
        print('$0')
    elif x[0] == "h":
        print('$20')
    else :
        print('$100')
main()