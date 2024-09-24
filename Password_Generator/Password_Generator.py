
from datetime import date
import email
from tkinter import *
from tkinter import messagebox
from Models.Credentials import PasswordGenerator
import json



window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=250, width=250)
load_img = PhotoImage(file="pass_gen.png")
canvas.create_image(125, 100, image=load_img)
canvas.grid(row=0, column=1)


#Class instances
password_generator = PasswordGenerator()






#Labels
web_label = Label(text="Website")
web_label.grid(row=1, column=0)

email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

#Entry
website_entry = Entry(width=25)
website_entry.focus()
website_entry.grid(row=1, column=1)

email_entry = Entry(width=25)
email_entry.insert(0, "email@email.com")
email_entry.grid(row=2, column=1)

password_entry = Entry(width=25)
password_entry.grid(row=3, column=1)

def generate_password_and_insert():
    new_password = password_generator.create_password()
    password_entry.insert(0, new_password)
   


generate_button = Button(text="Generate Password", command=generate_password_and_insert)
generate_button.grid(row=3, column=2)


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    to_json= {website:
        {
            "email" : email,
            "password" :password
        }
        }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:


        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(to_json, data_file, indent=4)
        else:
            data.update(to_json)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

    if website and email and password:
        messagebox.showinfo(title="Confirm", message="Credentials are saved!")



add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

def find_credentials():
    website = website_entry.get()

    with open("data.json", "r") as data_file:
            data = json.load(data_file)

    if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Information", message=f"Website: {website}\nEmail: {email}\nPassword: {password}")
                              
    else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exist.")





find_data = Button(text="Search Data", width=14, command=find_credentials)
find_data.grid(row=1, column=2)



window.mainloop()