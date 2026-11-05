#Encrypt a message 

#The idea is that we will use both Greek and English letters and
#we will combine them to create a unique encryption method.
#If you keep only the english letters, you will get the original message back.


import random

def encrypt_message(message):
    greek_letters = list("ΑΒΕΖΗΙΚΜΝΟΡΤΥ")

    encrypted_message = ""
    for i in range(random.randint(1, 5)):
        random_greek = random.choice(greek_letters)
        encrypted_message += random_greek

    for char in message:
        if char == " ":
            encrypted_message += "Χ"  # Use the Greek letter Chi (Χ) to represent spaces
        else:
            encrypted_message += char
        for i in range(random.randint(1, 5)):
            random_greek = random.choice(greek_letters)
            encrypted_message += random_greek
        
    return encrypted_message

def decrypt_message(encrypted_message):
    greek_letters = set("ΑΒΕΖΗΙΚΜΝΟΡΤΥ")
    decrypted_message = ""
    
    for char in encrypted_message:
        if char not in greek_letters:
            if char == "Χ":
                decrypted_message += " "  # Convert Chi (Χ) back to space
            else:
                decrypted_message += char
    return decrypted_message
            
def main():
    while True:
        print("Welcome to the Secret Messager!")
        print("Option 1: Encrypt a message")
        print("Option 2: Decrypt a message")
        while True:
            input_option = input("Enter your option (1 or 2): ")
            if input_option in ["1", "2"]:
                break
            else:
                print("Invalid option. Please enter 1 or 2.")
            
        if input_option == "1":
            input_message = input("Enter the message to encrypt(in English): ")
            input_message = input_message.upper()  # Convert the input message to uppercase
    
            if not input_message:
                print("No message entered. Exiting.")
                return
            encrypted_message = encrypt_message(input_message)
            print()
            print(f"Encrypted message: {encrypted_message}")
        elif input_option == "2":
            input_message = input("Enter the message to decrypt: ")
            decrypted_message = decrypt_message(input_message)
            print()
            print(f"Decrypted message: {decrypted_message}")
            
        print()
        print("Do you want to continue? (y/n)")
        continue_option = input().lower()
        if continue_option != "y":
            print("Exiting the program.")
            break
        
if __name__ == "__main__":
    main()