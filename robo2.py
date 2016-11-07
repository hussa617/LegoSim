import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Frame(master, width=800, height=600)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self,width=70,height=20)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",width=20,height=2,
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("Hi there, Earthlings!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
exit()
