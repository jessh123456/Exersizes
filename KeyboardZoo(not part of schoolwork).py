def leave_or_not(Animal):
    yn = input("Thanks for visiting Harold! Would you like to visit another "
               "animal? Press [Y] to to continue visiting or press [N] to "
               "leave.\n:").upper()
    if yn == "Y":
        Animal = input("Which animal would you like to see? Press [G] to visit"
                       " the giraffe, press[B] to visit the birds.\n:").upper()
    else:
        print("Thankyou for visiting the keyboard zoo! Come again soon!")
        quit()
    return Animal

def giraffe():
    print("Welcome to the Giraffe enclosure! this is Harold the giraffe!")
    print("  /)ii/)")
    print("(u '' )")
    print("   |  |")
    print("   |o |")
    print("   |  |")
    print("   |  |___________||")
    print("   |      o        |")
    print("   |_o_________o___|")
    print("   || ||       || ||")
    print("   || ||       || ||")
    print("   || ||       || ||")



yn = "Y"


print("Hello! Welcome to the keyboard zoo!")
print("Here we have a range of different animal. There are giraffes,.")
Animal = input("If you would like to see an animal press these letters: For a "
               "giraffe press [G].\n:").upper()
while yn != "N":
    if Animal == "G":
        print("Welcome to the Giraffe enclosure! this is Harold the giraffe!")
        print("  /)ii/)")
        print("(u '' )")
        print("   |  |")
        print("   |o |")
        print("   |  |")
        print("   |  |___________||")
        print("   |      o        |")
        print("   |_o_________o___|")
        print("   || ||       || ||")
        print("   || ||       || ||")
        print("   || ||       || ||")
        Animal = leave_or_not(Animal)
    elif Animal == "B":
        print("Welcome to the Bird enclosure")


