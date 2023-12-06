
import random
def agin():
    try :
        d = input("\n\n\n\t\t\t\t\t\t\tdo you wanna play agin ( write (yes) or (no) ) : ")
    except:
        print("you have entered a wrong imput , please try agin ")
        d = input("\n\n\n\t\t\t\t\t\t\tdo you wanna play agin ( write (yes) or (no) ) : ")
    if d == "yes":
        print("\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
        game()
    else:
        print("\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tgoodbye ")
def game():
    # making python guess a random number
    try:
        f = int(input("set the first number : "))
    except:
        print("you have entered a wrong imput , please try agin ")
        f = int(input("set the first number : "))
    try:
       s = int(input("set the second number : "))
    except:
        print("you have entered a wrong imput , please try agin ")
        s = int(input("set the second number : "))
    num = random.randint(f, s)
    # make the user guess that number

    # set a number of tries of guessings for the user
    t = 5
    # make a loop
    while t != 0:
        try:
            g = int(input(" guess a number between " + str(f) + " to " + str(s) + " : "))
        except:
            print("you have entered a wrong imput , please try agin ")
            g = int(input(" guess a number between " + str(f) + " to " + str(s) + " : "))

        # if the number was right say congratulations and end the program
        if num == g:
            print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tcongratulations")
            break
        # if the number was wrong say try agin and make the user try agin
        if num != g:
            print("wrong guess , please try agin \n\n")
            t -= 1
    if t == 0:
        print("you lose ")
        print("the right number was " + str(num))
    agin()
game()
