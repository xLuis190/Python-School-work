from tkinter import *

def main():
    root = Tk()
    buttonList = []
    for x in range(0,100):
        buttonList.append(Button(root,text ="Button {}".format(x)))
    
    for index in range(len(buttonList)):
        
        if(index < 50):
            buttonList[index].pack(side = BOTTOM)

        elif(index > 50):
            buttonList[index].pack(side = RIGHT)
        
    root.mainloop()
