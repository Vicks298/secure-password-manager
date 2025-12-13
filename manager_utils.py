import json, os
from cryptography.fernet import Fernet
import base64, hashlib

USERS_FILE = "users.json"
VAULTS_FOLDER = "vaults"

# -----------------------------
# User account functions
# -----------------------------
def hash_password(master):
    return hashlib.sha256(master.encode()).hexdigest()

def register_user(username, master):
    if not os.path.exists(USERS_FILE):
        users = {}
    else:
        with open(USERS_FILE) as f:
            users = json.load(f)
    if username in users:
        raise Exception("Username already exists")
    users[username] = hash_password(master)
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)
    # create empty vault for this user
    if not os.path.exists(VAULTS_FOLDER):
        os.makedirs(VAULTS_FOLDER)
    with open(f"{VAULTS_FOLDER}/{username}.json", "w") as f:
        json.dump({}, f)

def check_login(username, master):
    if not os.path.exists(USERS_FILE):
        return False
    with open(USERS_FILE) as f:
        users = json.load(f)
    if username not in users:
        return False
    return users[username] == hash_password(master)

# -----------------------------
# Vault functions
# -----------------------------
def get_cipher(master):
    key = hashlib.sha256(master.encode()).digest()
    return Fernet(base64.urlsafe_b64encode(key))

def add_password(username, master, service, username_pw, password):
    cipher = get_cipher(master)
    vault_file = f"{VAULTS_FOLDER}/{username}.json"
    data = {}
    if os.path.exists(vault_file):
        with open(vault_file) as f:
            data = json.load(f)
    encrypted = cipher.encrypt(password.encode()).decode()
    data[service] = {"username": username_pw, "password": encrypted}
    with open(vault_file, "w") as f:
        json.dump(data, f, indent=4)

def get_password(username, master, service):
    cipher = get_cipher(master)
    vault_file = f"{VAULTS_FOLDER}/{username}.json"
    if not os.path.exists(vault_file):
        raise Exception("Vault not found")
    with open(vault_file) as f:
        data = json.load(f)
    if service not in data:
        raise Exception("Service not found")
    encrypted_pw = data[service]["password"]
    return cipher.decrypt(encrypted_pw.encode()).decode()



