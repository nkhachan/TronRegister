
def printWelcome():
    print("Welcome to the CommandLine Register! \n",
          "Please enter one of the following options : \n",
          "\"Login\" to log in to your account \n",
          "\"Register\" to register for an account \n",
          "\"Exit\" to exit this program\n",
          "\"Quick\" to run the quick wallet")

def runProgram():
    printWelcome()
    while (1):
        var = input()

        if (var == "Exit"):
            break

        elif (var == "Quick"):
            quickDemo();

