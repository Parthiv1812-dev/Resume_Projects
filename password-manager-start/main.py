from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def store_value():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    new_data = {website:
                    {"email": email,
                     "password": password
                     }
                }

    if len(website) == 0 or len(email) == 0:
        messagebox.showerror(title="Error", message="Please fill all the fields")

    else:
        try:
            f = open("password.json","r")
           #Reading the old data
            data = json.load(f)
        except FileNotFoundError:
            with open("password.json", "w") as f:
                json.dump(new_data, f, indent=4)

        else:
           #Updating the old data with new data
            data.update(new_data)
            with open("password.json","w") as f:
                # Saving the updated data
                json.dump(data, f, indent=4)

        finally:

            website_entry.delete(0, END)
            password_entry.delete(0, END)
            f.close()

        # except FileNotFoundError:
        #     with open("password.json","w") as f:
        #         json.dump(new_data, f, indent=4)
        #         website_entry.delete(0, END)
        #         password_entry.delete(0, END)


def search_value():
    website = website_entry.get()
    try:
        content = json.load(open("password.json","r"))
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found")
    try:
        messagebox.showinfo(title=website, message=f"Email: {content[website]['email']}\nPassword: {content[website]['password']}")
    except KeyError:
        messagebox.showerror(title="Error", message="No data File Found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(200, 200)
window.config(padx=50, pady=50)

password_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=password_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()


email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "parthiv.bharat@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)


add_button = Button(text="Add", width=36, command=store_value)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=13, command=search_value)
search_button.grid(column=2, row=1)

window.mainloop()