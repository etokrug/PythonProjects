from tkinter import *

ALL = N+S+W+E

class Application(Frame): 
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)
        
        self.rowconfigure(0, weight=2)
        self.columnconfigure(0, weight=2)
        Frame(self, bg="GREEN").grid(row=0, column=0, columnspan=2, sticky=ALL)
        L1 = Label(self, text="Frame 1", bg="GREEN", padx=20, pady=20)
        L1.grid(row=0, column=0, columnspan=2)
        
        self.rowconfigure(1, weight=2)
        self.columnconfigure(0, weight=2)
        Frame(self, bg="BLUE").grid(row=1, column=0, columnspan=2, sticky=ALL)
        L2 = Label(self, text="Frame 2", bg="BLUE", padx=20, pady=20)
        L2.grid(row=1, column=0, columnspan=2)
        
        self.rowconfigure(0, weight=2)
        self.columnconfigure(2, weight=2)
        Frame(self, bg="red").grid(row=0, column=2, rowspan=2, columnspan=3, sticky=ALL)
        L3 = Label(self, text="Frame 3", bg="RED", padx=20, pady=20)
        L3.grid(row=0, column=2, rowspan=2, columnspan=3)

        for r in range(5):
            self.columnconfigure(r, weight=1)
            Button(self, text="Button {0}".format(r+1)).grid(row=3, column=r, sticky=ALL)
            
root = Tk()
app = Application(master=root)
app.mainloop()