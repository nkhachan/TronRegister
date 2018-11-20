import sys
import os
sys.path.append("/home/noopur/kivy")
sys.path.append(os.getcwd() + "/src")
sys.path.append(os.getcwd() + "/src/APIs")
sys.path.append(os.getcwd() + "/src/demos")
sys.path.append(os.getcwd() + "/kivy_stuff")
sys.path.append(os.getcwd() + "/tkinter")
print(sys.path)

from runApp import runApp
from TransactionPage import *
from MainApp import *
from QuickDemo import quickDemo
from FullDemo import fullDemo

def main():
    val = input("Type either q, f, a for the QuickDemo, FullDemo, and App respectfully\n")

    if (val == "q"):
        quickDemo()
    elif (val == "f"):
        fullDemo()
    elif (val == "a"):
        MainApp().run()
        #runApp()
    else:
        val = input("Incorrect Input!")

if __name__ == "__main__":
    main()
