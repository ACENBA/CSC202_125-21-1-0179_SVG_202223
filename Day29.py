#password
from tkinter import *
from tkinter import messagebox

#password generator
from random import choice, randint, shuffle

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
              'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
              'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '&', '*', '+', '_']

    password_letters= [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password_list = password_list[:max(8, randint(8, 15))]

    password = " ".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)




def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(password) < 8 or len(password) > 15:
        messagebox.showinfo("Invalid Password", "Password should be between 8 and 15 characters.")
        return

    # messagebox.showinfo(title="Title", message="Personal info")
    messagebox.showinfo("Password Requirements", "The password should be between 8 and 15 characters.")
    messagebox.askquestion(message="Do you want to submit this ?")



    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Fill the empty boxes")
    else:

        is_ok = messagebox.askquestion(title="Ttile", message=f" These are the details entered: \n Email: {email} " f"\n Password: {password} \n Is it ok to save?")

        if is_ok:

            with open("data.txt",  "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

cancvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="password.png")
cancvas.create_image(100, 100, image= logo_img)
cancvas.grid(row=0, column=1)

#labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Enteries
website_entry = Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()
email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, )
email_entry.focus()
email_entry.insert(0, "adewalep096@gmail.com")
password_entry = Entry(width=34,)
password_entry.grid(row=3, columnspan=2)

#button
generate_password_button = Button(text="G/ Passkey", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button =Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1)

window.mainloop()
