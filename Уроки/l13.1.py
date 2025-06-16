from cryptography.fernet import Fernet

def write_key(filename="secret.key"): # Создает ключ
    key = Fernet.generate_key()
    # read write
    with open(filename, "wb") as key_file: # Читання запис дозапис (второе)
        key_file.write(key)
    return key

def load_key(filename="secret.key"):
    with open(filename, "read") as key_file:
        return key_file.read()
    
def encrypt_message(message, key):
    cipher = Fernet(key)
    encrypted = cipher.encrypt(message.encode())
    return encrypted

def decrypt_message(encrypted_message, key):
    cipher = Fernet(key)
    decrypted = cipher.decrypt(encrypted_message).decode()
    return decrypted

key = write_key()

# text = "123123"
text = r"C:\asd"

encrypted = encrypt_message(text, key)
print(f"Message: {encrypted}")

decrypted = decrypt_message(encrypted, key)
print(f"Message final: {decrypted}")