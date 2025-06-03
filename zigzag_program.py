# Press ctrl + c to stop the program

from sys import exit
from time import sleep

indent = 0
indentation = True

try:
    while True:
        print(" " * indent + "*****")
        sleep(0.1)

        if indentation:
            indent += 1

        if indent >= 20:
            indentation = False

        if indentation == False:
            indent -= 1
            print(" " * indent + "*****")

        if indent == 1:
            indentation = True

except KeyboardInterrupt:
    print("\nStopping the program!")
    exit()