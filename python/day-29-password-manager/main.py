from tkinter import *
from tkinter import messagebox # Not a class hence has to call it separately.
# It's just code written to display a pop-up box
import pyperclip
from random import randint, shuffle, choice
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
               'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    nr_letters = randint(8, 10)
    password_letters = [letter for letter in letters][0:nr_letters] # 2nd '[]' limits
    # by index i.e slicing through the result. Only including the first 'N' items.
    # ###OR
    password_numbers = [choice(numbers) for _ in range(2, 4)]
    password_symbols = [choice(symbols) for _ in range(2, 4)]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list) # Simplifies code above
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get().capitalize()
    email = email_entry.get().capitalize()
    password = password_entry.get()

    new_data = {
        website: {
            "Email" : email,
            "Password" : password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any blanks!")
# DAY 30 UPDATED CODE:
    else:
        try:
            with open("data.json", "r") as data_file:
                # json.dump(new_data, data_file, indent=4) ## Write data to a JSON
                # file reading the old data
                data = json.load(data_file) # loads data from file as a dictionary
                #Updating old data with new data
                data.update(new_data)
                #Saving new data
        except FileNotFoundError: # Gives a json error instead of FileNotFound error
            # for some reason otherwise would've put 'except FileNotFound:'.
            # Although after doing the 'find_password()' function, this error seems to
            # have disappeared.
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

        finally: #Optional
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')

# ---------------------------- SEARCH THROUGH PASSWORDS ----------------------------- #
#ALSO DAY 30
def find_password():
    website = website_entry.get().capitalize()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
            if website in data:
                email = data[website]["Email"]
                password = data[website]["Password"]
                messagebox.showinfo(title=f"{website}", message=f"Email: {email} "
                                                            f"\nPassword: {password}")
            else:
                messagebox.showerror(title="Error!", message="No Details for the "
                                                             "Website Exist!")
    except FileNotFoundError:
        messagebox.showerror(title="Error!", message="No Data File Found!")

# ---------------------------- UI SETUP ------------------------------- #
#CHALLENGE 1 - WORKING WITH IMAGES AND SETTING UP THE CANVAS
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

#CHALLENGE 2 - USE grid() AND COLUMNSPAN TO COMPLETE THE USER INTERFACE

#Labels
website_label = Label(text="Website:")
user_label = Label(text="Email/Username:")
password_label = Label(text="Password:")
add_label = Label(text="Add")

website_label.grid(row=1, column=0)
user_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=21)
website_entry.focus() # function 'focus()' focuses the cursor into that particular
# entry
email_entry = Entry(width=35)
email_entry.insert(0, "your-email@example.com") # function 'insert()'
# inserts string from string argument into entry. The index refers to the character in
# the entry where you wanna insert the text. If at the end, use index 'END' instead of
# 0 (at the beginning)
password_entry = Entry(width=21)

website_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)

#Buttons
gen_pass = Button(text="Generate Password", command=generate_password)
add = Button(text="Add", width=36, command=save)
search = Button(text="Search", width =13, command=find_password)

gen_pass.grid(row=3, column=2)
add.grid(row=4, column=1, columnspan=2)
search.grid(row=1, column=2)

window.mainloop()