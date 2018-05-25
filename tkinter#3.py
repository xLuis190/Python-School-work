# Problem1
from tkinter import *
def prob1():
    

    win = Tk()

    B = Button(win,text="Left Click me!")
    B.bind('<Button-1>',toggle)
    B.pack()
    win.mainloop()

def main():
    prob1()
    

if __name__ == "__main__":
    main()
