from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

# Generiraj par ECC ključeva
private_key = ec.generate_private_key(ec.SECP384R1())
public_key = private_key.public_key()
# Serializacija javnog ključ za djeljenje/pohranu
pem_public_key = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
# Šifriranje poruke pomoču javnog ključa (ECC koristi zajedničku tajnu za  šifriranje)
shared_secret = private_key.exchange(ec.ECDH(), public_key)
derived_key = hashes.Hash(hashes.SHA256())
derived_key.update(shared_secret)
encrypted_message = derived_key.finalize() # Pojednostavljenje encripcije
# Dešifriranje poruke pomoču privatnog ključa 
decrypted_message = encrypted_message # Pojednostavljeno dešifriranje
print(f"Public Key:\n{pem_public_key.decode('utf-8')}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted_message}")