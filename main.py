from manager_utils import generate_key, encrypt_password, decrypt_password, load_data, save_data

def main():
    print("=== Secure Password Manager ===")
    master_password = input("Enter your master password: ")
    key = generate_key(master_password)

    data = load_data()

    while True:
        print("\nMenu:")
        print("1. Add new credential")
        print("2. Retrieve credential")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            site = input("Website/Service name: ")
            username = input("Username: ")
            password = input("Password: ")

            encrypted = encrypt_password(password, key)
            data[site] = {"username": username, "password": encrypted}
            save_data(data)
            print(f"Credential for {site} saved successfully!")

        elif choice == "2":
            site = input("Website/Service name to retrieve: ")
            if site in data:
                username = data[site]["username"]
                encrypted = data[site]["password"]
                password = decrypt_password(encrypted, key)
                print(f"\nCredentials for {site}:")
                print(f"Username: {username}")
                print(f"Password: {password}")
            else:
                print(f"No credentials found for {site}.")

        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
