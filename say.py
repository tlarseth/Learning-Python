import cowsay
import sys
import fortune

name = input('What is your name?')
cowsay.trex('Hello, ' + name)
#if len(sys.argv) == 2:
    #cowsay.trex("Hello, " + sys.argv[1])