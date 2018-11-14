from QuickDemo import *
from MainPage import *
import tkinter as tk
import json

def main():
    #quickDemo()
    root = tk.Tk()

    # eliminate the titlebar
    #root.overrideredirect(1)

    mainpage = MainPage(root)
    mainpage.pack(side="top", fill="both", expand=True)

    root.wm_geometry("1500x1000")
    root.mainloop()

if __name__ == "__main__":
    main()