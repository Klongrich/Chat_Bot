from Tkinter import *

class GUI:

    def __init__(self, master):
        self.frame = Frame(master, background="dark green", highlightbackground="black", highlightcolor="black", highlightthickness=2, bd=0)
        self.frame.pack()

        self.my_message = Label(root)
        self.input_box = Text(master, height=2, width=34)
        self.input_box.place(x=0, y=388)

        self.send_button = Button(master, text = "---->", command = self.send_message)
        self.send_button.place(x=245, y=388)

    def send_message(self):
        input = self.input_box.get("1.0", END)
        self.input_box.delete('1.0', END)
        self.my_message.config(text=input)
        self.my_message.place(x=15, y=345)
        print(input)

root = Tk()
root.title("ChatBot")
root.configure(background="green")

root.minsize(height=417, width=300)
root.maxsize(height=417, width=300)


k = GUI(root)
root.mainloop()

