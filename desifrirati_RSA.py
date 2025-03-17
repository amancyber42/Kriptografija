from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def decrypt_rsa(file_path, private_key_path):
    # Učitaj privatni ključ
    with open(private_key_path, "rb") as key_file:
        private_key = RSA.import_key(key_file.read())
    
    # Postavi dekriptor
    cipher = PKCS1_OAEP.new(private_key)
    
    # Učitaj šifrirane podatke
    with open(file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
    
    # Dešifriraj podatke
    decrypted_data = cipher.decrypt(encrypted_data)

    # Spremi dešifriranu datoteku
    decrypted_file_path = file_path + ".decrypted"
    with open(decrypted_file_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)
    
    print(f"Dešifrirana datoteka je spremljena u: {decrypted_file_path}")

file_path = "encrypted_file.salt"
private_key_path = "private_key.pem"

decrypt_rsa(file_path, private_key_path)
