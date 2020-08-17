from time import sleep

def happy_birthday(who="you"):
    if who == "you":
        print("Happy birthday to you")
    if who != "you":
        print("Happy birthday dear", who)


# Main looop

name = input("What is your name?")

for a in range (0,2):
    happy_birthday()
    sleep(1)

happy_birthday(name)
sleep(1)
happy_birthday()
sleep(1)

for a in range (0,3):
    print ("Hip hip... ", end = '')
    sleep(1)
    print ("hooray!")
    sleep(1)
