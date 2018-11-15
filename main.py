from QuickDemo import *
from MainApp import *
from FullDemo import *
import tkinter as tk
import json

def main():
    val = input("Type either q, f, a for the QuickDemo, FullDemo, and App respectfully\n")

    if (val == "q"):
        quickDemo()
    elif (val == "f"):
        fullDemo()
    elif (val == "a"):
        MainApp().run()
    else:
        val = input("Incorrect Input!")

if __name__ == "__main__":
    main()