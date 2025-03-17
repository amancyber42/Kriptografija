import random
from sympy import isprime, mod_inverse

def generate_prime_candidate(length):
    """Generiraj nesumićni neparan cijeli broj određene duljine bita.
    
    Args:
    length: Duljina bita primarnog kandidata.
    Returns:
    Neparni cijeli broj s navedenom duljinom bita."""
    p = random.getrandbits(length)
    # Mora se osigurati da je broj neparan i ima postaavljen najviši bit (za održavanje duljina)
    p |= (1 << length -1) | 1
    return p

def generate_large_prime(lenght):
    """Generiraj veliki prosti broj određene duljine bita.
    Args:
    length: Duljina bita primarnog broja za generiranje.
    Returns:
    Prosti broj s navedenom duljinom bita."""
    p = 4
    # Nastavite generirati proste kandidate dok se ne pronađe prosti broj
    while not isprime(p):
        p = generate_prime_candidate(lenght)
    return p

def generate_keypair(keysize):
    """Generiraj javni i privatni par ključeva za RSA enkripciju.
    Args:
    keysize: Duljina ključeva ta generiranje
    Returns:
    Torka koja sadrži parove javnog i privatnog ključa."""
    # Generiraj dva velika prosta broja
    p = generate_large_prime(keysize)
    q = generate_large_prime(keysize)
    # Izračunaj modul za javni i privatni kjluč
    n = p * q
    # Izrečunajte Eulerovu tocijentnu funkciju (phi)
    phi = (p-1) * (q-1)
    # Odabrati javni eksponent
    e = 65537
    # Izračunaj privatni eksponent 
    d = mod_inverse(e, phi)
    # Vrati javni i privatni par ključeva
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    """Šifrira niz (plaintext) pomoču javnog ključa (pk).
    Args:
    pk: Torka koja sadrži javni ključ i modul (e, n).
    plaintext: Niz koji pretstavlja poruku koju treba šifrirati.
    Returns:
    Popis cijelih brojeva koji predstavljaju šifriranu poruku."""
    key, n = pk
    # Pretvorite svako slovo u otvorenom tekstu u brojeve koristeći učinkovitije modularno stepenovanje
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    """Dekriptira popis cijelih brojeva (ciohertext) korištenjem privatnog ključa (pk).
    Args:
    pk: Torka koja sadrži privatni ključ i modul (d, n).
    ciphertext: Popis cijelih brojeva koji prestavljaju šifriranu poruku.
    Returns:
    Niz koji pretstavlja dekriptiranu poruku."""
    key, n = pk
    # Dešifriraj svaki broj u šifriranom tekstu i pretvoriti ga natrag u znakove
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)

if __name__ == '__main__':
    # Veličina ključa mora biti velika (npr. 2048 bita) za stvarne aplikacije
    keysize = 64 # Manja veličina korištena radi jednostavnosti
    print("Generating key pair..")
    public, private = generate_keypair(keysize)
    print("Public key:", public)
    print("Private key:", private)

    message = "Pozdrav RSA!"
    print("Orginal poruka:", message)
    encrypted_msg = encrypt(public, message)
    print("Encrypted message:", ''.join(map(lambda x: str(x), encrypted_msg)))
    decrypted_msg = decrypt(private, encrypted_msg)
    print("Decrypted message:", decrypted_msg)