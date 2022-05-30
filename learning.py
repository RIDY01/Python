#libraries
import time
import random

#output
print("Python learning script")
print("-----------------------------")

#functions
def getAge():
    age = input("What is your age?: ")

    if age.isdigit():
         print("Your age is " + age)

         if int(age) < 18:
            print("underage)
         else:
            print("adult")

         favNumber(age)
    else:
        print("Please enter a positive number")
        getAge()

def favNumber(age):
    print("-----------------------------")
    print("Lets check your favorite number...")

    time.sleep(3)

    favNumber = random.randint(1, 100)

    print("Your favorite number is " + str(favNumber))
    print("-----------------------------")
    print("Lets play a quick game:")
    ranNum = random.randint(0,20)
    game(ranNum)


def game(ranNum):

    int(ranNum)

    iptNr = input("Guess a number between 0 and 20: ")


    if iptNr.isdigit():
        while ranNum != int(iptNr):
            iptNr = input("Guess a number between 0 and 20: ")

            if iptNr.isdigit():
                if int(iptNr) < 0 or int(iptNr) > 20:
                    print("Please try again: ")

                else:
                    print("Wrong number. try again: ")

            else:
                print("Please enter a number between 0 and 20!!")
    else:
        print("Please enter a number between 0 and 20!!")
        game(ranNum)


def end():
    print("")
    print("You won. Goodbye.")
    input("Press enter to exit")


#start
getAge()
end()
