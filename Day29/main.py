from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Opps", message="Error!! You have to fill the field first") 

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail : {email} \nPassword:{password} \nIs it okay to save?" )
        if is_ok:
            with open("./Day29/data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="./Day29/logo.png") 
canvas.create_image(100, 100,image = logo_img)
canvas.grid(row=0, column=1)


# Lables 
website_label = Label(text="Website:")
website_label.grid(row= 1, column=0)

email_label = Label(text="Emain/ Username:")
email_label.grid(row= 2, column=0)

password_label = Label(text="Password:")
password_label.grid(row= 3, column=0)


# Entries
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=3)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=3)
email_entry.insert(0, "HarshDodiya@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)


# Generate password button
generate_password = Button(text="Generate Password")
generate_password.grid(row= 3, column= 2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=3)

window.mainloop()