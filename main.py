from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    n_website = website_entry.get()
    n_email_user = email_entry.get()
    n_password = password_entry.get()

    is_ok = messagebox.askokcancel(title=n_website,
                                   message=f"These are the details entered: \n Email:{n_email_user}\nPassword: {n_password}")
    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{n_website} | {n_email_user} | {n_password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)
canvas.config(bg="white", highlightthickness=0)

website_label = Label(text="Website:", font=("Arial", 10, "bold"), bg="white")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_label = Label(text="Email/Username:", font=("Arial", 10, "bold"), bg="white")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2)
email_entry.insert(0, "abdallahadam130@gmail.com")

password_label = Label(text="Password:", font=("Arial", 10, "bold"), bg="white")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, columnspan=1)

generate_button = Button(text="Generate Password", bg="white", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, bg="white", highlightthickness=0, bd=0, command=add_data)
add_button.grid(column=1, row=4)

window.mainloop()
