import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = []

        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.address_var = tk.StringVar()
        self.search_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Name").grid(row=0, column=0)
        tk.Entry(self.root, textvariable=self.name_var).grid(row=0, column=1)

        tk.Label(self.root, text="Phone").grid(row=1, column=0)
        tk.Entry(self.root, textvariable=self.phone_var).grid(row=1, column=1)

        tk.Label(self.root, text="Email").grid(row=2, column=0)
        tk.Entry(self.root, textvariable=self.email_var).grid(row=2, column=1)

        tk.Label(self.root, text="Address").grid(row=3, column=0)
        tk.Entry(self.root, textvariable=self.address_var).grid(row=3, column=1)

        tk.Button(self.root, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2)

        tk.Label(self.root, text="Search").grid(row=5, column=0)
        tk.Entry(self.root, textvariable=self.search_var).grid(row=5, column=1)
        tk.Button(self.root, text="Search", command=self.search_contact).grid(row=5, column=2)

        self.contacts_listbox = tk.Listbox(self.root)
        self.contacts_listbox.grid(row=6, column=0, columnspan=3, sticky="nsew")

        tk.Button(self.root, text="View All Contacts", command=self.view_contacts).grid(row=7, column=0, columnspan=3)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact).grid(row=8, column=0, columnspan=3)

    def add_contact(self):
        name = self.name_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()
        address = self.address_var.get()

        if name and phone:
            contact = Contact(name, phone, email, address)
            self.contacts.append(contact)
            self.clear_fields()
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Name and Phone are required!")

    def clear_fields(self):
        self.name_var.set("")
        self.phone_var.set("")
        self.email_var.set("")
        self.address_var.set("")

    def view_contacts(self):
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contacts_listbox.insert(tk.END, f"{contact.name} - {contact.phone}")

    def search_contact(self):
        search_term = self.search_var.get().lower()
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts:
            if search_term in contact.name.lower() or search_term in contact.phone:
                self.contacts_listbox.insert(tk.END, f"{contact.name} - {contact.phone}")

    def delete_contact(self):
        selected_contact = self.contacts_listbox.get(tk.ACTIVE)
        if selected_contact:
            name = selected_contact.split(" - ")[0]
            self.contacts = [contact for contact in self.contacts if contact.name != name]
            self.view_contacts()
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "No contact selected!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
