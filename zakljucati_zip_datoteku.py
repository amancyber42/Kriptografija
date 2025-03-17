import pyzipper, argparse, sys, re, getpass
from colorama import Fore, init

init()
# Definirati funkciju za dobivanje CLI naredbe
def get_cli_aruments():
    parser = argparse.ArgumentParser(description="Program za zaključavanje ZIP datoteke")
    # Prikupiti korisničke argumente
    parser.add_argument('--zipfile', dest='zip_file', help='Navedite ZIP datoteku za izradu ili ažuriranje.')
    parser.add_argument('--addfile', '-a', dest='add_files', nargs='+', help='Navedite jednu ili više datoteka za dodavanjeu ZIP datoteku.')
    # Razčlanite prikupljene argumente.
    args = parser.parse_args()
    # Provjerite nedostaju li argumenti, ispišite odgovarajuće poruke i izađite iz programa
    if not args.zip_file:
        parser.print_help()
        sys.exit()
    if not args.add_files:
        parser.print_help()
        sys.exit()
    return args

# Funkcija za provjeru snage lozinke
def check_password_strength(password):
    # Provjerite minimalnu duljinu. U ovom slučaju 8.
    if len(password) < 8:
        return False
    
    # Provjeriti postoji barem jedno veliko slovo, jedno malo slovo i jedna znamenka
    if not (re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'\d', password)):
        return False
    return True

# Pozovite funkciju argumenata
arguments = get_cli_aruments()
# Dobiti korisničku lozinku
password = getpass.getpass("[?] Unesite svoju lozinku > ")
# Ako je lozinka slaba, recite korisniku i izađite iz programa.
if not check_password_strength(password):
    print(f"{Fore.RED}[-] Lozinka nije dovoljno jaka. Trebala bi biti najmanje 8 znakova i sadžavati najmanje jedno veliko slovo, jedno malo slovo i jednu znamenku.")
    sys.exit()

# Napravite ZIP datoteku zaštičenom lozinkom
with pyzipper.AESZipFile(arguments.zip_file, 'w', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as zf:
    zf.setpassword(password.encode())
    # Dodajte datoteku u ZIP datoteku
    for file_to_add in arguments.add_files:
        zf.write(file_to_add)
# Ispišite poruku o uspjehu
print(f"{Fore.GREEN}[+] Zip datoteka je zaključana jakom lozinkom.")