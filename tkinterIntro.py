from tkinter import *
timesClicked = 0
def printClick(event):
    print("CLICKED {} times".format(timesClicked))
    timesClicked = timesClicked +1
root = Tk()
'''
B1 = Button(root)
B1.configure(text="I am button 1")
B1.bind("%f",printClick)
B1.pack()
'''
C_red = Canvas(root,width=100,height=100)
C_red.create_oval(2,2,98,98, fill="#FF5733")
C_red.pack()

root.mainloop()
