from Tkinter import *

class GUI:

    def __init__(self, master):
        self.frame = Frame(master, background="dark green", highlightbackground="black", highlightcolor="black", highlightthickness=2, bd=0)
        self.frame.pack()
        Btn_Deals = self.Btn_Deal = Button(self.frame, text = "Sup Bro", command = self.Deal)
        Btn_Deals.place(x = 20, y=30, width = 120, height = 25)
        Btn_Deals.pack()
    def Deal(self):
        print("C.A.B.")



root = Tk()
root.title("ChatBot")
root.configure(background="green")

root.minsize(height=750, width=600)
root.maxsize(height=750, width =600)


k = GUI(root)
root.mainloop()

