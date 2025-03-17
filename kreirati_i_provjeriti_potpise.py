# Generiranje i provjera digitalnih potpisa u Pythonu
from cryptography.hazmat.primitives import hashes # Uvoz funkcije hash
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from colorama import init, Fore

init()
# Generiranje privatnih i javnih ključeva pomoću RSA algoritma
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# Definiranje poruke koje će se potpisivati i koristiti za provjeru
message = b"Secret message to be signed" # Prva poruka za potpisivanje 
message2 = b"Second message that is not signed" # Druga poruka koja nije potpisana

# Potpisati poruku privatnim ključem
signature = private_key.sign( # poruku koju treba potpisati
    message,
    padding.PSS( #koristiti PSS shemu padding-a sa sha256 raspršivanjem
        mgf=padding.MGF1(hashes.SHA256()), # navesti generirane maske
        salt_length=padding.PSS.MAX_LENGTH # definirati duljinu soli za padding
    ),
    hashes.SHA256() # navesti hash algoritam kao SHA-256
)

# Provjeriti popis pomoću javnog ključa
try:
    public_key.verify(
        signature,  # potpis koji treba provjeriti
        message,    # poruku koju treba provjeriti # message2
        padding.PSS(  # koristiti isti algoritam za paddingi raspršavanje
            mgf=padding.MGF1(hashes.SHA256()), # odrediti masku
            salt_length=padding.PSS.MAX_LENGTH  # definirati duljinu soli
        ),
        hashes.SHA256() # navesti hash kao sha256
    )
    print(f"{Fore.GREEN}Signature verified: The message is authentic.") # poruka je autentična
except Exception:
    print(f"{Fore.RED}Signature verification failed: The message may have been tampered width.") # neovlaštena poruka ili greška