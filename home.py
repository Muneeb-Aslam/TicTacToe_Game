from argparse import Action
from cProfile import label
from cgitb import text
from tkinter import *
from turtle import *
def centeredscreen(root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - 200)
    center_y = int(screen_height/2 - 200)

    # set the position of the window to the center of the screen
    root.geometry(f'400x400+{center_x}+{center_y}')

if __name__=="__main__":
    root = Tk()
    root.title("TicTaeToe")
    centeredscreen(root)
    root.resizable(False,False)
    root.configure(bg="darkgrey")

    choice = Label(root,text="Choose the Numbers of Players")
    players = Button(root,text="Two Players",command=Action)
    player = Button(root,text="One Players",command=Action)



    root.mainloop()