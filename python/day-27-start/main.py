# Creating Windows and Labels with TKinter
from tkinter import *

window = Tk() # Creates a window
window.title("GUI Program")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20) # Adds more space around the program - can also add to
# a specific widget, not just window

# Label - ##components to put inside the window
my_label = Label(text="I am a Label", font=["Arial", 24, "bold"]) #Generate text
# however need to use function '.pack()' to show it
my_label.grid(row=0, column=0)
#my_label.pack() #Actually shows the label and centres it
# # 2 different ways to change the text
# my_label["text"] = "New Text"
# my_label.config(text="New Text")

# Button -  A button that the user can press

def button_clicked():
    my_label["text"] = input.get()

button = Button(text="Click Me", command=button_clicked)
button.grid(row=2, column=2)
#button.pack()

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(row=0, column=3)


# Entry

input = Entry(width=10)
input.grid(row=4, column=4)
#input.pack()

# Tkinter Layout Managers: pack(), place() and grid()
#Widgets will only show up if one of these layout managers are called

# pack(): Packs each of the widgets next to each other in a vaguely logical format from
# top to bottom

# place(): Precise positioning - function parameters are x and y coordinates

# grid(): Imagine your entire window is a grid, you can divide it into any number of
# rows and columns using input parameters 'row' and 'column'






window.mainloop() # Keeps the window open, has to go at end of code
