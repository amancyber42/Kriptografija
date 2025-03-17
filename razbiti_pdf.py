import fitz
from tqdm import tqdm
import sys

def crack_pdf(pdf_path, password_list):
    """Prevedi PDF lozinku koristeći popis lozinki
    Args:
        pdf_path (str): Put do PDF datoteke
        password_list (list): popis lozinki koje treba isprobati
    Returns:
        [str]: Vraća lozinku ako je pronađena, inače ništa"""
    # otvoriti PDF
    doc = fitz.open(pdf_path)
    # ponoviti lozinke
    for password in tqdm(password_list, "Pogađanje lozinke"):
        # pokušati otvoriti lozinkom
        if doc.authenticate(password):
            # kada je lozinka pronađena, autentikacija vraća različitu od nule 
            # izlazak iz petlje i vračanje lozinke
            return password

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Greška: Nedostaju argumenti. Morate unijeti putanju do PDF datoteke i lozinkarski popis.")
        sys.exit(1)
    
    pdf_filename = sys.argv[1]
    wordlist_filename = sys.argv[2]
    
    # učitaj popis lozinki
    with open(wordlist_filename, "r", errors="replace") as f:
        # čitanje svih lozinki u popisu
        password_list = f.read().splitlines()
    
    # pozvati funkciju za probijanje lozinke
    password = crack_pdf(pdf_filename, password_list)
    
    if password:
        print(f"[+] Lozinka pronađena: {password}")
    else:
        print("[!] Lozinka nije pronađena")
