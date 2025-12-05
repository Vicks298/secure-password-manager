import json
from cryptography.fernet import Fernet
import base64
import hashlib

DATA_FILE = "data.json"

# Generate a key from the master password
def generate_key(master_password):
    # Hash master password and encode
    key = hashlib.sha256(master_password.encode()).digest()
    return base64.urlsafe_b64encode(key)

# Encrypt a password
def encrypt_password(password, key):
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()

# Decrypt a password
def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    return f.decrypt(encrypted_password.encode()).decode()

# Load stored data
def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Save data
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
