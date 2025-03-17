from Crypto.Cipher import AES
import os

def decrypt_file(file_path, key):
    # Postavi blok veličinu
    block_size = 16  # AES koristi blok od 16 bajtova
    
    # Otvori šifriranu datoteku
    with open(file_path, "rb") as encrypted_file:
        iv = encrypted_file.read(block_size)  # Čitaj inicijalizacioni vektor (IV)
        cipher = AES.new(key, AES.MODE_CBC, iv)  # Postavi AES u CBC modu
        encrypted_data = encrypted_file.read()
    
    # Dešifriraj podatke
    decrypted_data = cipher.decrypt(encrypted_data)
    
    # Ukloni padding (ako je dodan tokom šifriranja)
    padding_length = decrypted_data[-1]
    decrypted_data = decrypted_data[:-padding_length]

    # Spremi dešifriranu datoteku
    decrypted_file_path = file_path + ".decrypted"
    with open(decrypted_file_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)
    
    print(f"Dešifrirana datoteka je spremljena u: {decrypted_file_path}")

# Primer ključ (mora imati tačno 16, 24 ili 32 bajta za AES)
key = b"your_16_byte_key"
file_path = "encrypted_file.salt"

decrypt_file(file_path, key)
