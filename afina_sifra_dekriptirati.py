import string
from colorama import Fore, init

init()

# Funkcija za dobivanje euklidskog algoritma
def extended_gcd(a, b):
    """Prošireni euklidski algoritam za pronalaženje največeg zajedničkog djeljitelja i kofecijenata 
    x, y tako da je ax + by = gcd(a, b)."""
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)
    
# Funkcija za dobivanje modularne inverzne
def modular_inverse(a, m):
    """Izračunaj modularni multiplikativni inverz modulam.
    Pokreće iznimku ako modularni inverz ne postoji."""
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modularni inverz ne postoji')
    else:
        return x % m
    
# Funkcija za dešifriranje naše poruke
def affine_decrypt(ciphertext, a, b):
    """Dešifriraj poruku šifriranu pomoču affline cipher koristeći
    zadane ključne komponente a i b."""
    alphabet = string.ascii_uppercase
    m = len(alphabet)
    plaintext = ''
    # izračunaj modularni multiplikativni inverz od a
    a_inv = modular_inverse(a, m)
    # iteriraj kroz svaki znak u šifriranom tekstu
    for char in ciphertext:
        # Provjerite jeli znak u abecedi
        if char in alphabet:
            # Ako je slovo abecede, dešifriraj ga.
            # Pronađite indeks znaka u abecedi.
            c = alphabet.index(char)
            # Primjeniti formulu za dešifriranje: a_inv*(c-b) mod m.
            p = (a_inv * (c - b)) % m
            # Dodavanje dešifriranog znaka otvorenom tekstu.
            plaintext += alphabet[p]
        else:
            # Ako znak nije u abecedi, ostavite ga nepromijenjenim.
            plaintext += char
    # Vrati dešifrirani otvoreni tekst.
    return plaintext
    
# Funkcija za izvod brute force napada
def affine_brute_force(ciphertext):
    """Napad brute-force za pronalaženje mogućih ključeva za afinu šifru i ispis
    potecijalnih dešifriranja za ručnu provjeru."""
    alphabet = string.ascii_uppercase
    m = len(alphabet)
    # iteracija kroz moguće vrijednosti za a
    for a in range(1, m):
        # osigurati dasu a i m međusobno prosti
        if extended_gcd(a, m)[0] == 1:
            # iterirati kroz moguće vrijednosti za b
            for b in range(0, m):
                # dešifriranje pomoču trenutnog ključa
                decrypted_text = affine_decrypt(ciphertext, a, b)
                # ispis moguče dešifriranja za ručnu provjeru
                print(f"Key (a={a}, b={b}): {decrypted_text}")

ciphertext = input(f"{Fore.GREEN}[?] Unesi poruku za dešifriranje:")
# Ivesti brute-force napad kako biste pronašli potencijalno dešifriranu poruku
affine_brute_force(ciphertext)