from Tkinter import *

class GUI:

    def __init__(self, master):
        self.frame = Frame(master, background="dark green", highlightbackground="black", highlightcolor="black", highlightthickness=2, bd=0)
        self.frame.pack()

root = Tk()
root.title("ChatBot")
root.configure(background="brown")

root.minsize(height=417, width=467)
root.maxsize(height=417, width=467)

k = GUI(root)
root.mainloop()