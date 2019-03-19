import tkinter as tk
import os
from tkinter import Frame, CENTER, Label, BOTH
from PIL import Image, ImageTk
import csv
import datetime

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb   

root = tk.Tk()
entries = []
pw = ''
# get screen width and height to fill screen with picture when needed
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
def get(entry):
        pw = entry.get() 
        if (pw != 'Exit' and (pw not in entries) and pw != ''):
                entry.delete(0, 'end')
                entries.append(pw)
                entryText.config(text="Thanks! Who's next?")
        elif (pw == 'Exit'):
                # writes num of people that swiped into event on certain day when UI is closed
                with open('attendance.csv', 'w', newline='') as file:
                        writer = csv.writer(file)
                        now = datetime.datetime.now()
                        writer.writerow(['{} people swiped in for event on {}'.format(len(entries)-1, now.strftime("%m/%d/%Y")) ])
                root.destroy()
        elif pw in entries:
                # not exit but has been used already
                entry.delete(0, 'end')
                entryText.config(text="Already swiped in, who's next?")

# make unc background
path = str(os.getcwd()) + "/UNC_card_bg.jpg"
img = Image.open(path)
img = img.resize((int(screenWidth), int(screenHeight)))
img = ImageTk.PhotoImage(img)

# make background img a label
imgL = tk.Label(root, image=img)
imgL.pack()

# frame of text entry
entryFrame = Frame(root, bg=_from_rgb((104, 155, 202)), width=int(screenWidth/4.5), height=int(screenHeight/5))
entryFrame.place(x=int(screenWidth/2.5), rely=.6)

# entry message
entryText = tk.Label(entryFrame, bg=_from_rgb((104, 155, 202)),text="Swipe One Card then click Submit, or type 'Exit'")
entryText.place(relx=.5, rely=.4, anchor=CENTER)

# set focus to entry widget and bind it to return button of keyboard
entry = tk.Entry(entryFrame)
entry.focus_set()
entry.place(relx=.5, rely=.6, anchor=CENTER)
entry.bind("<Return>", lambda event, name='get': get(entry))

# submit button
entryButton = tk.Button(entryFrame, text="Submit", command= lambda: get(entry))
entryButton.place(relx=.5, rely=.8, anchor=CENTER)

root.mainloop()