'''TASK 5

Contact Information: Store name, phone number, email, and address for each contact.

Add Contact: Allow users to add new contacts with their details.

View Contact List: Display a list of all saved contacts with names and phone numbers.

Search Contact: Implement a search function to find contacts by name or phone number.

Update Contact: Enable users to update contact details.

Delete Contact: Provide an option to delete a contact.

User Interface: Design a user-friendly interface for easy interaction.'''


import tkinter as tk

# Initialize an empty list to store contacts
contacts = []

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    if name and phone:
        contact = {'Name': name, 'Phone': phone, 'Email': email, 'Address': address}
        contacts.append(contact)
        contact_listbox.insert(tk.END, name)
        clear_fields()

# Function to display contact details
def show_contact(event):
    selected_contact = contact_listbox.get(contact_listbox.curselection())
    for contact in contacts:
        if contact['Name'] == selected_contact:
            details_label.config(text=f"Name: {contact['Name']}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\nAddress: {contact['Address']}")

# Function to clear the input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Function to delete a contact
def delete_contact():
    selected_contact = contact_listbox.get(contact_listbox.curselection())
    for contact in contacts:
        if contact['Name'] == selected_contact:
            contacts.remove(contact)
            contact_listbox.delete(contact_listbox.curselection())
            clear_fields()
            details_label.config(text="Contact Details")

# Create the main window
app = tk.Tk()
app.title("Contact Management System")

# Create and configure input fields for contact details
name_label = tk.Label(app, text="Name:")
name_entry = tk.Entry(app)
phone_label = tk.Label(app, text="Phone:")
phone_entry = tk.Entry(app)
email_label = tk.Label(app, text="Email:")
email_entry = tk.Entry(app)
address_label = tk.Label(app, text="Address:")
address_entry = tk.Entry(app)

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
phone_label.grid(row=1, column=0)
phone_entry.grid(row=1, column=1)
email_label.grid(row=2, column=0)
email_entry.grid(row=2, column=1)
address_label.grid(row=3, column=0)
address_entry.grid(row=3, column=1)

# Create and configure buttons for adding and deleting contacts
add_button = tk.Button(app, text="Add Contact", command=add_contact)
delete_button = tk.Button(app, text="Delete Contact", command=delete_contact)

add_button.grid(row=4, column=0)
delete_button.grid(row=4, column=1)

# Create and configure a listbox for displaying contact names
contact_listbox = tk.Listbox(app)
contact_listbox.grid(row=0, column=2, rowspan=5, padx=10)

# Bind the listbox to show contact details on selection
contact_listbox.bind("<<ListboxSelect>>", show_contact)

# Create and configure a label for displaying contact details
details_label = tk.Label(app, text="Contact Details")
details_label.grid(row=5, column=0, columnspan=3)

# Run the application
app.mainloop()
