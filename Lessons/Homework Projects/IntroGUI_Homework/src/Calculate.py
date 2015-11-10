from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    
    def createWidgets(self):
        #1st frame
        king_frame = Frame(self)
        #king_frame objects
        self.first_label = Label(king_frame, text="Number:")
        self.input1 = Entry(king_frame)
        #object builds
        self.first_label.pack(side=LEFT)
        self.input1.pack()
        #king_frame build
        king_frame.pack(padx=3, pady=3)
        
        #second frame
        queen_frame = Frame(self)
        #queen_frame objects
        self.second_label = Label(queen_frame, text="Number:")
        self.input2 = Entry(queen_frame)
        #object builds
        self.second_label.pack(side=LEFT)
        self.input2.pack()
        #queen_frame build
        queen_frame.pack(padx=3, pady=3)
        
        #output frame
        output_frame = Frame(self)
        #objects
        self.output_label = Label(output_frame, text="Spitfire")
        #object builds
        self.output_label.pack()
        #output_frame build
        output_frame.pack(padx=3, pady=3)
        
        #peasant_frame
        peasant_frame = Frame(self)
        #objects
        self.QUIT = Button(peasant_frame, text="Quit", command=self.quit)
        self.get_coin = Button(peasant_frame, text="Calculate", command=self.handle)
        #object builds
        self.QUIT.pack(side=LEFT)
        self.get_coin.pack(side=LEFT)
        #peasant_frame build
        peasant_frame.pack(padx=3, pady=3)

    def handle(self):
        entry1 = self.input1.get()
        entry2 = self.input2.get()
        try:
            calc1 = float(entry1)
            calc2 = float(entry2)
            final_calc = calc1 + calc2
            self.output_label.config(text=final_calc)
        except ValueError:
            self.output_label.config(text="***ERROR***""")

    
root= Tk()
app = Application(master=root)
app.mainloop()
        
        