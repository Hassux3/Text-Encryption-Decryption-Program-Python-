# Encryption-Decryption Program

import string
import time

alphabets = string.ascii_lowercase
alphabets_Upper = string.ascii_uppercase


def encryption(plain_text, shift_key):
    cypher_text = ""
    for char in plain_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position+shift_key) % 26
            cypher_text += alphabets[new_position]
        else:
            cypher_text += char
    print("This is your text key:", cypher_text)

def decryption(cypher_text, shift_key):
    decrypted_text = ""
    for char in cypher_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position-shift_key) % 26
            decrypted_text += alphabets[new_position]
        else:
            decrypted_text += char
    print("This is your message:", decrypted_text)

def closing():
    sure = input("Are you sure? (Yes/No) -> ")
    if sure == "Yes" or sure == "yes" or sure == "Yeah" or sure == "yeah":
        print("Thanks for using our service...\n")
        time.sleep(3)
        exit()
    else:
        print("Okay fine!\n")


is_on = True

print("\tEncoding and Decoding\n")
while is_on:
    choice = input("\nEnter Code or Decode or Quit: ")
    if (choice == "code" or choice == "Code"):
        plain_text = input("Type your message: ")
        shift_key = int(input("Enter your shift key: "))
        encryption(plain_text.lower(), shift_key)
    elif (choice == "decode" or choice == "Decode"):
        cypher_text = input("Enter your text key: ")
        shift_key = int(input("Enter your shift key: "))
        decryption(cypher_text, shift_key)
    elif (choice == "Quit" or choice == "quit"):
        closing()
    else:
        print("Invalid command!\n")