from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
import json

FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password(length=14):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "Email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.askokcancel(title="filed Empty", message="Don't leave any of filed Empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# -----------------------------Find Password-------------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Data Not Found In File.")
    else:
        if website in data:
            email = data[website]["Email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Detail", message=f"Email : {email} \n Password : {password}")
        else:
            messagebox.showinfo(title="Error", message=f"Data for {website} doesn't exist")


# ---------------------------- UI SETUP ------------------------------- #
# window created
window = Tk()
window.title("PASSWORD MANAGER ")
window.config(padx=50, pady=50)
# canvas
canvas = Canvas(height=200, width=200)
lock_image = PhotoImage(file="E:/Python Coding/Day29/logo.png")
canvas.create_image(110, 110, image=lock_image)
canvas.grid(column=1, row=0)
# label
label = Label(text="Website :", font=(FONT_NAME, 12, "bold", "italic"))
label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", font=(FONT_NAME, 12, "bold", "italic"))
email_label.grid(column=0, row=2)
pass_label = Label(text="Password:", font=(FONT_NAME, 12, "bold", "italic"))
pass_label.grid(column=0, row=3)
# entry
website_entry = Entry(width=33)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "hanzalawaleed6@gmail.com")
password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)
# button
button = Button(text="Generate Password", width=13, command=generate_password)
button.grid(column=2, row=3)
add = Button(text="Add", width=36, command=save)
add.grid(column=1, row=4, columnspan=2)
search = Button(text="Search", width=13, command=find_password)
search.grid(column=2, row=1)

window.mainloop()
