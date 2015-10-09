from tkinter import *
import os

ALL = N+S+W+E

root = Tk()

def color_handler(arg):
    Frame.T1.config(fg=arg)
    Frame.L31.config(fg=arg)
    
def handler1(event):
    print("Frame 1 clicked at ", event.x, event.y)

def handler2(event):
    print("Frame 2 was clicked at ", event.x, event.y)

def handler3():
    filename = Frame.E1.get()
    Frame.T1.config(state=NORMAL)
    Frame.T1.delete(1.0, END)
    try:
        prefile = open(filename, 'r')
        opened = prefile.readlines()
        for sentence in opened:
            Frame.T1.insert(END, sentence)
        Frame.T1.config(state=DISABLED)
    except IOError:
        Frame.T1.insert(END, "FILE NOT FOUND AT {0}".format(os.getcwd()))
        Frame.T1.config(state=DISABLED)

class Applcation(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.configure(height=50, width=50)

    rootFrame = Frame(root)
    rootFrame.master.rowconfigure(0, weight=1)
    rootFrame.master.columnconfigure(0, weight=1)
    rootFrame.grid(sticky=ALL)
    
    #First internal frame
    Frame.F1 = Frame(rootFrame, bg="Green")
    rootFrame.rowconfigure(0, weight=2)
    rootFrame.columnconfigure(0, weight=2)
    Frame.F1.bind("<Button-1>", handler1)
    Frame.F1.grid(row=0, columnspan=2, sticky=ALL)
    #First internal frame button
    Frame.L1 = Label(Frame.F1, text="Frame 1", bg="GREEN", padx=10, pady=30)
    Frame.L1.bind("<Button-1>", handler1)
    Frame.L1.grid(row=0, columnspan=2, sticky=ALL)
    
    #Second internal frame
    Frame.F2 = Frame(rootFrame, bg="BLUE", padx=10, pady=30)
    rootFrame.rowconfigure(1, weight=2)
    rootFrame.columnconfigure(0, weight=2)
    Frame.F2.bind("<Button-1>", handler2)
    Frame.F2.grid(row=1, columnspan=2, sticky=ALL)
    #Second internal label
    Frame.L2 = Label(Frame.F2, text="Frame 2", bg="BLUE")
    Frame.L2.bind("<Button-1>", handler2)
    Frame.L2.grid(row=1, columnspan=2, sticky=ALL)
    
    #Third internal frame
    Frame.F3 = Frame(rootFrame, bg="grey")
    rootFrame.rowconfigure(0, weight=2)
    rootFrame.columnconfigure(2, weight=2)
    Frame.F3.grid(row=0, column=2, rowspan=2, columnspan=3, sticky=ALL)
    
    #Third internal frame label for entry widget
    Frame.L31 = Label(Frame.F3, text="File Name...", bg="grey", font=18)
    Frame.L31.grid(row=0, column=0, padx=20, pady=20)
    
    #third internal frame entry widget
    rootFrame.rowconfigure(0, weight=2)
    rootFrame.columnconfigure(3, weight=2)
    Frame.F3.rowconfigure(0, weight=2)
    Frame.F3.columnconfigure(1, weight=2)
    Frame.E1 = Entry(Frame.F3, bg="grey", font=16)
    Frame.E1.grid(row=0, column=1, columnspan=2, ipadx=4, ipady=4, sticky=ALL)
    
    #Third internal frame text widget
    Frame.F3.rowconfigure(1, weight=1)
    Frame.F3.columnconfigure(0, weight=1)
    Frame.T1 = Text(Frame.F3, bg="grey", font=16)
    Frame.T1.grid(row=1, column=0, columnspan=3, sticky=ALL)
    Frame.T1.insert(END, "Awaiting file name...")
    Frame.T1.config(state=DISABLED)
    
    #Red button
    rootFrame.columnconfigure(0, weight=1)
    redB = Button(rootFrame, text="Red", command=lambda arg="red": color_handler(arg), width=25)
    redB.grid(row=3, column=0, sticky=ALL)
     
    #Blue button
    rootFrame.columnconfigure(1, weight=1)
    blueB = Button(rootFrame, text="blue", command=lambda arg="blue": color_handler(arg), width=25)
    blueB.grid(row=3, column=1, sticky=ALL)
     
    #Green button
    rootFrame.columnconfigure(2, weight=1)
    blueB = Button(rootFrame, text="Green", command=lambda arg="green": color_handler(arg), width=25)
    blueB.grid(row=3, column=2, sticky=ALL)
     
    #Black button
    rootFrame.columnconfigure(3, weight=1)
    blueB = Button(rootFrame, text="Black", command=lambda arg="black": color_handler(arg), width=25)
    blueB.grid(row=3, column=3, sticky=ALL)
     
    #Open button
    rootFrame.columnconfigure(4, weight=1)
    openB = Button(rootFrame, text="Open", command=handler3)
    openB.grid(row=3, column=4, sticky=ALL)

root.mainloop()