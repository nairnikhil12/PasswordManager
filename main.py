import tkinter as tk
from tkinter import messagebox, ttk

from GeneratePassword import *
import db

# Event handler for Generate Password button
def event_generate_password():
    ent_password.delete(0, tk.END)
    ent_password.insert(0, generate_password())

# Event handler for Create Record button
def event_create_record():
    app_name = ent_app_name.get()
    url = ent_url.get()
    email = ent_email.get()
    password = ent_password.get()

    if app_name == '' or url == '' or email == '' or password == '':
        messagebox.showinfo("Alert", "All details must be filled!")
        return

    # add the record into the database
    db.insert_record((app_name, url, email, password))

    # clear all the inputs
    event_reset()

    update_view('')

# Event handler for Reset Button
def event_reset():
    ent_app_name.delete(0, tk.END)
    ent_url.delete(0, tk.END)
    ent_email.delete(0, tk.END)
    ent_password.delete(0, tk.END)

# Event handler for Search Button
def event_search():
    update_view(ent_search.get())

# Update the view of records
def update_view(pattern):
    queries = db.fetch_records(pattern)

    name = ""
    url = ""
    email = ""
    password = ""
    for i, record in enumerate(queries):
        name = name + str(i+1) + ") " + record[0] + "\n"
        url = url + record[1] + "\n"
        email = email + record[2] + "\n"
        password = password + record[3] + "\n"

    lbl_query_name['text'] = name
    lbl_query_url['text'] = url
    lbl_query_email['text'] = email
    lbl_query_password['text'] = password

# Program constants
HORIZONTAL_PADDING = 5
VERTICAL_PADDING = 10

window = tk.Tk()

window.title('Password Manager')

#Set Background image
bg = tk.PhotoImage(file='image.png')
bgimage = ttk.Label(window, image=bg)
bgimage.place(x=0, y=0)

# Widgets for Application Name
lbl_app_name = ttk.Label(window, text='Application Name: ')
lbl_app_name.grid(row=0, column=0, padx=HORIZONTAL_PADDING, pady=VERTICAL_PADDING)
ent_app_name = ttk.Entry(window)
ent_app_name.grid(row=0, column=1, pady=VERTICAL_PADDING)

# Widgets for URL
lbl_url = ttk.Label(window, text='URL: ')
lbl_url.grid(row=0, column=2, padx=HORIZONTAL_PADDING, pady=VERTICAL_PADDING)
ent_url = ttk.Entry(window)
ent_url.grid(row=0, column=3, pady=VERTICAL_PADDING)

# Widgets for Email Id
lbl_email = ttk.Label(window, text='Email ID: ')
lbl_email.grid(row=1, column=0, padx=HORIZONTAL_PADDING, pady=VERTICAL_PADDING)
ent_email = ttk.Entry(window)
ent_email.grid(row=1, column=1, pady=VERTICAL_PADDING)

# Widgets for password
lbl_password = ttk.Label(window, text='Password: ')
lbl_password.grid(row=1, column=2, padx=HORIZONTAL_PADDING, pady=VERTICAL_PADDING)
ent_password = ttk.Entry(window)
ent_password.grid(row=1, column=3, pady=VERTICAL_PADDING)

# Generate Password Button
btn_generate_password = ttk.Button(window, text='Generate Password', command=event_generate_password)
btn_generate_password.grid(row=1, column=4, padx=HORIZONTAL_PADDING)

# Create Record Button
btn_create_record = ttk.Button(window, text='Create', command=event_create_record)
btn_create_record.grid(row=3, column=1, pady=2*VERTICAL_PADDING)

# Reset Button
btn_reset = ttk.Button(window, text='Reset', command=event_reset)
btn_reset.grid(row=3, column=3, pady=2*VERTICAL_PADDING)

# Widgets for search
lbl_search = ttk.Label(window, text='Search: ')
lbl_search.grid(row=4, column=0, padx=HORIZONTAL_PADDING, pady=2*VERTICAL_PADDING)
ent_search = ttk.Entry(window)
ent_search.grid(row=4, column=1, padx=HORIZONTAL_PADDING, pady=2*VERTICAL_PADDING)
btn_search = ttk.Button(window, text='Search', command=event_search)
btn_search.grid(row=4, column=2, padx=HORIZONTAL_PADDING, pady=2*VERTICAL_PADDING)

# Widgets for displaying the records
lbl_query_name = ttk.Label(window)
lbl_query_name.grid(row=5, column=0)
lbl_query_url = ttk.Label(window)
lbl_query_url.grid(row=5, column=1)
lbl_query_email = ttk.Label(window)
lbl_query_email.grid(row=5, column=2)
lbl_query_password = ttk.Label(window)
lbl_query_password.grid(row=5, column=3)

# initialize the program to display all passwords
update_view('')

window.grid_rowconfigure(5, weight=2)
window.grid_columnconfigure(5, weight=2)
window.mainloop()