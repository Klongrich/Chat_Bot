from Tkinter import *

class GUI:

    def __init__(self, master):
        self.frame = Frame(master, background="dark green", highlightbackground="black", highlightcolor="black", highlightthickness=2, bd=0)
        self.frame.pack()

        self.my_message = Label(master)
        Btn_Deals = self.Btn_Deal = Button(master, text = "Sup Bro", command = self.send_message)
        Btn_Deals.place(x = 365, y=600, width = 70, height = 25)

        self.TextBox_Input = Text(master, width = 42)
        self.TextBox_Input.place(x = 15, y = 600, height = 25)

    def send_message(self):
        input = self.TextBox_Input.get("1.0", END)
        self.TextBox_Input.delete('1.0', END)
        self.my_message.config(text=input)
        self.my_message.place(x=15, y=545)
        print(input)

root = Tk()
root.title("ChatBot")
root.configure(background="green")

root.minsize(height=650, width=450)
root.maxsize(height=650, width =450)


k = GUI(root)
root.mainloop()

