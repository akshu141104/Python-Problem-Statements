
"""
Project 3 "Mini Password Manager using OOP"
Problem Statement:
Build a CLI password manager. A user can store passwords for websites, retrieve them by site name, update them, and delete them. Passwords should be stored encoded (not plain text) using base64.
Stack: Python OOP, base64 module, file I/O
Input: Website name + password (via terminal)
Output: Encoded stored password, decoded on retrieval
Think about:
How do you design a PasswordManager class with add/get/update/delete methods?
What's the difference between encoding and encrypting?
How do you use __str__ and __repr__ for clean output?
What happens when someone tries to retrieve a site that doesn't exist?"""


import base64
import json
import os

class PasswordManager:
    def __init__(self, filename="passwords.json"):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return {}

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.data, file, indent=4)

    def encode_password(self, password):
        return base64.b64encode(password.encode()).decode()

    def decode_password(self, encoded_password):
        return base64.b64decode(encoded_password.encode()).decode()

    def add_password(self, site, password):
        self.data[site] = self.encode_password(password)
        self.save_data()
        print("Password added successfully!")

    def get_password(self, site):
        if site in self.data:
            decoded = self.decode_password(self.data[site])
            print(f"Password for {site}: {decoded}")
        else:
            print("Site not found!")

    def update_password(self, site, new_password):
        if site in self.data:
            self.data[site] = self.encode_password(new_password)
            self.save_data()
            print("Password updated!")
        else:
            print("Site not found!")

    def delete_password(self, site):
        if site in self.data:
            del self.data[site]
            self.save_data()
            print("Password deleted!")
        else:
            print("Site not found!")

    def __str__(self):
        return f"Stored sites: {list(self.data.keys())}"

    def __repr__(self):
        return f"PasswordManager({self.filename})"


# -------- CLI Menu --------
pm = PasswordManager()

while True:
    print("\n1. Add\n2. Get\n3. Update\n4. Delete\n5. Show All\n6. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        site = input("Enter site: ")
        password = input("Enter password: ")
        pm.add_password(site, password)

    elif choice == "2":
        site = input("Enter site: ")
        pm.get_password(site)

    elif choice == "3":
        site = input("Enter site: ")
        password = input("Enter new password: ")
        pm.update_password(site, password)

    elif choice == "4":
        site = input("Enter site: ")
        pm.delete_password(site)

    elif choice == "5":
        print(pm)

    elif choice == "6":
        break

    else:
        print("Invalid choice!")