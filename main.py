import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '&']

    password_l = [choice(letters) for _ in range(randint(8, 10))]
    password_n = [choice(numbers) for _ in range(randint(2, 4))]
    password_s = [choice(symbols) for _ in range(randint(2, 4))]

    password_lst = password_l + password_n + password_s
    password = "".join(password_lst)

    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get().title()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "PASSWORD": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please don't leave any field empty!")
    else:
        ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                           f"\nPassword: {password} \nIs it ok to save?")

        if ok:
            try:
                with open("password_manager.json", "r") as file:
                    # Reading old weather_data
                    data = json.load(file)
            except FileNotFoundError:
                with open("password_manager.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                # Updating old weather_data with new weather_data
                data.update(new_data)

                with open("password_manager.json", "w") as file:
                    # Saving updated weather_data
                    json.dump(data, file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)
                messagebox.showinfo(message="Your weather_data was saved successfully")


# ---------------------------- SEARCH ------------------------------- #
def find_password():
    website = website_input.get().title()
    try:
        with open("password_manager.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No weather_data file found.")
    else:
        if website in data:
            messagebox.showinfo(message=f"Website: {website}\n"
                                        f"Email: {data[website]['email']}\n"
                                        f"Password: {data[website]['PASSWORD']}")
        else:
            messagebox.showinfo(title="Error", message="There are no details saved for this website.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

# Image
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Website Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_label.config(padx=5, pady=5)

# Website Entry

website_input = Entry()
website_input.focus()
website_input.grid(column=1, row=1, sticky="EW")

# Search Button
search = Button(text="Search", command=find_password)
search.grid(column=2, row=1, sticky="EW")

# Email/Username Label
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_label.config(padx=5, pady=5)

# Email/Username Entry
email_input = Entry()
email_input.insert(END, "andreea.dmt20@gmail.com")
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")

# Password Label

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_label.config(padx=5, pady=5)

# Password Entry

password_input = Entry()
password_input.grid(column=1, row=3, sticky="EW")

# Generate Button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky="EW")

# Add Button
add_button = Button(text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
