from Tkinter import *

class GUI:

    def __init__(self, master):
        self.frame = Frame(master, background="dark green", highlightbackground="black", highlightcolor="black", highlightthickness=2, bd=0)
        self.frame.pack()
        Btn_Deals = self.Btn_Deal = Button(master, text = "Sup Bro", command = self.Deal)
        Btn_Deals.place(x = 365, y=600, width = 70, height = 25)
        TextBox_Input = self.TextBox_Input = Entry(master, width = 42)
        TextBox_Input.place(x = 15, y = 600, height = 25)

    def Deal(self):
        print("C.A.B.")

    def Input(self):
        question = self.TextBox_Input.text

root = Tk()
root.title("ChatBot")
root.configure(background="green")

root.minsize(height=650, width=450)
root.maxsize(height=650, width =450)


k = GUI(root)
root.mainloop()

