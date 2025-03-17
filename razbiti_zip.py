from tqdm import tqdm
import pyzipper
import sys

# staza popisa zaporki koje želite koristiti
wordlist = sys.argv[2]
# zip datoteka kojoj želite razbiti lozinku
zip_file = sys.argv[1]

# Inicijalizirajte pyzipper
with pyzipper.AESZipFile(zip_file, 'r') as zf:
    n_words = len(list(open(wordlist, "rb")))
    print("Ukupan broj lozinki za testiranje:", n_words)
    
    with open(wordlist, "rb") as wordlist_file:
        for word in tqdm(wordlist_file, total=n_words, unit="word"):
            try:
                zf.extractall(pwd=word.strip())
            except:
                continue
            else:
                print("[+] Lozinka pronađena:", word.decode().strip())
                exit(0)

print("[!] Lozinka nije pronađena, pokušajte s drugim popisom riječi.")