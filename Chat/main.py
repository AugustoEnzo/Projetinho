from client import Client

import cryptography.fernet

global encrypted_text
global message
global other_person_decrypted_message
global other_message

client: Client = Client()

secret_key = "Choose a best key"
# Making the key random
key = client.generate_fernet_key(secret_key.encode('utf-8'))
fernet = cryptography.fernet.Fernet(key)

person: str = "Alice"
other_person: str = "Bob"

print(f"You're connected as {person}")
print(f"To send a message to {other_person}, insert 1, To read {other_person} messages, insert 2")
choice = input("Choice: ")
if choice == "1":
    message = input(f"{person}: Insert your message and I'll cryptography that: ")
    inserted_secret_key = input(f"Insert the secret key combined with {other_person}: ")
    if inserted_secret_key == secret_key:
        encrypted_text: bytes = fernet.encrypt(message.encode('utf-8'))
        print(f"{person}'s encrypted text: {encrypted_text}")
        client.insert_messages_to_collection(person, other_person, False, encrypted_text)
    else:
        print("Wrong key")
elif choice == "2":
    collection_to_operate = client.read_from_collection(other_person, person, False)\
        .collection
    other_person_encrypted_message: bytes = collection_to_operate.find("message")
    other_person_decrypted_message: str = fernet.decrypt(other_person_encrypted_message).decode('utf-8')

    print(f"{other_person} decrypted text: {other_person_decrypted_message}")
    collection_to_operate.update_one(
        {"from": other_person, "to": person, "readStatus": False},
        {"$set": {"readStatus": True}}
    )
else:
    print(f"insert a valid value!")

print(f"You've logged as {other_person}")
print(f"To send a message to {person}, insert 1, To read {person} messages, insert 2")
other_choice = input("Choice: ")
if other_choice == "1":
    other_message = input(f"{other_person}: Insert your message and I'll cryptography that: ")
    other_person_encrypted_message = fernet.encrypt(other_message.encode('utf-8'))
    print(f"encrypted text from {other_person}: {other_person_encrypted_message}")
elif other_choice == "2":
    person_decrypted_message = fernet.decrypt(encrypted_text).decode('utf-8')
    print(f"{other_person}'s encrypted text: {other_person_decrypted_message}")
else:
    print(f"insert a valid value!")

# results
print(f"String to generate the key: {secret_key}")
print(f"Person message: {message}")
print(f"Other person message: {other_message}")
print(f"Message in bytes: {key}")
print(f"Secret key: {key.decode()}")
