# Password Manager (Flask)

A simple multi-user password manager built with Python and Flask.
Each user secures their passwords using a master password and encryption.

## Features
- User registration and login
- Master password–based encryption
- Encrypted password storage
- User-isolated vaults
- Web interface (Flask)
- Live deployment (Render)

## How It Works
- Users register with a username and master password
- The master password is used to encrypt/decrypt stored credentials
- Passwords are never stored in plain text
- Each user has a separate encrypted vault

## Security Notes
- Encrypted storage using symmetric encryption
- No password recovery (by design)
- Application cannot read user passwords without master password

## Tech Stack
- Python
- Flask
- Cryptography (Fernet)
- HTML/CSS
- Render

## Run Locally
```bash
pip install -r requirements.txt
python app.py



