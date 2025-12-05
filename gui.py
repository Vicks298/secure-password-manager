import tkinter as tk
from tkinter import messagebox
from manager_utils import generate_key, encrypt_password, decrypt_password, load_data, save_data

# --- Master password ---
MASTER_PASSWORD = "your_master_password_here"
key = generate_key(MASTER_PASSWORD)

data = load_data()

# --- Functions ---
def add_credential():
    site = entry_site.get()
    username = entry_username.get()
    password = entry_password.get()
    
    if site and username and password:
        encrypted = encrypt_password(password, key)
        data[site] = {"username": username, "password": encrypted}
        save_data(data)
        messagebox.showinfo("Success", f"Credential for {site} saved!")
        entry_site.delete(0, tk.END)
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "All fields are required!")

def retrieve_credential():
    site = entry_site.get()
    if site in data:
        username = data[site]["username"]
        password = decrypt_password(data[site]["password"], key)
        messagebox.showinfo(f"Credentials for {site}", f"Username: {username}\nPassword: {password}")
    else:
        messagebox.showwarning("Error", f"No credentials found for {site}.")

# --- GUI ---
root = tk.Tk()
root.title("Secure Password Manager")

tk.Label(root, text="Website/Service:").grid(row=0, column=0, pady=5)
entry_site = tk.Entry(root, width=30)
entry_site.grid(row=0, column=1, pady=5)

tk.Label(root, text="Username:").grid(row=1, column=0, pady=5)
entry_username = tk.Entry(root, width=30)
entry_username.grid(row=1, column=1, pady=5)

tk.Label(root, text="Password:").grid(row=2, column=0, pady=5)
entry_password = tk.Entry(root, width=30, show="*")
entry_password.grid(row=2, column=1, pady=5)

tk.Button(root, text="Add Credential", command=add_credential, width=20).grid(row=3, column=0, pady=10)
tk.Button(root, text="Retrieve Credential", command=retrieve_credential, width=20).grid(row=3, column=1, pady=10)

root.mainloop()
