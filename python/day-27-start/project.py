from tkinter import *
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=800, height=300)
font=("Arial", 48, "normal")
he= 32

def converter():
    num = float(input.get())
    num *= 1.609
    return num

def on_click():
    calculation = Label(text=f"{converter()}",font=("Arial", 20, "normal"))
    calculation.grid(row=1, column=1)

# Entry
input = Entry(width=20)
input.grid(row=0, column=1)

#Label
text1 = Label(text="Miles",font=font)
text1.grid(row=0, column=2)
text2 = Label(text="is equal to", font=font)
text2.grid(row=1, column=0)
text3 = Label(text="Km", font=font)
text3.grid(row=1, column=2)

#Button
button = Button(text="Calculate", command=on_click,font=font)
button.grid(row=2, column=1)







window.mainloop()