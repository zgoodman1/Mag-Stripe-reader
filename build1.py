import tkinter as tk
import os
from tkinter import Frame, CENTER, Label, BOTH
from PIL import Image, ImageTk

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb   


def thanks():
        thanksLabel = tk.Label(root, bg=_from_rgb((104, 155, 202)), width=int(screenWidth/5), height=int(screenHeight/5), text="Thank You")
        thanksLabel.place(x=int(screenWidth/2.5), rely=.6)
        
def askFor():
        entryFrame = Frame(root, bg=_from_rgb((104, 155, 202)), width=int(screenWidth/4.5), height=int(screenHeight/5))
        entryFrame.place(x=int(screenWidth/2.5), rely=.6)

        entryText = tk.Label(entryFrame, bg=_from_rgb((104, 155, 202)),text="Swipe One Card then click Submit, or type 'Exit'")
        entryText.place(relx=.5, rely=.4, anchor=CENTER)

        def get():
                global pw
                pw = entry.get()
                entry.delete(0, 'end')

        entry = tk.Entry(entryFrame)
        entry.focus_set()
        entry.place(relx=.5, rely=.6, anchor=CENTER)
        entry.bind("<Return>", get())
                
        entryButton = tk.Button(entryFrame, text="Submit", command=get())
        entryButton.place(relx=.5, rely=.8, anchor=CENTER)
        entryButton.bind("<Return>", get())

# create a new root window
root = tk.Tk()
inputs = []
pw = ''
# get screen width and height to fill screen with picture when needed
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
# make unc background
path = str(os.getcwd()) + "/UNC_card_bg.jpg"
img = Image.open(path)
img = img.resize((int(screenWidth), int(screenHeight)))
img = ImageTk.PhotoImage(img)
# imgL as soon as it becomes a label object
imgL = tk.Label(root, image=img)
imgL.pack()


askFor()









input = pw

if (input != 'Exit' and (input not in inputs)):
        thanks()
        inputs.append(input)
        #root.after(4000, askFor())
elif input == 'Exit':
        root.destroy()
#elif input in inputs:
        #root.after(1000, askFor())


root.mainloop()
