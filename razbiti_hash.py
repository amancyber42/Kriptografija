# Razbijanje hashova
import hashlib
from tqdm import tqdm

# Popis podržanih tipova raspršivanja
hash_names = [
    'blake2b', 'blake2s', 'md5', 'sha1',
    'sha224', 'sha256', 'sha384', 'sha512',
    'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512',
]

def crack_hash(hash, wordlist, hash_type):
    """Crack a hash using a wordlist.
    Args:
    hash (str): The hash to crack.
    wordlist (str): The path to the wordlist.
    hash_type (str): The hash algorithm to use.
    
    Returns:
    str: Krekirani hash ili None ako nije pronađen.
    """
    hash_fn = getattr(hashlib, hash_type, None)
    if hash_fn is None or hash_type not in hash_names:
        # Nije podržana vrsta raspršivanja
        raise ValueError(f'[!] Invalid hash type: {hash_type}, supported are {hash_names}')
    
    # Izbroji broj redaka u popisu riječi kako bi se postavio ukupan iznos
    with open(wordlist, 'r', encoding='latin1') as f:
        total_lines = sum(1 for line in f)
    print(f"[*] Cracking hash {hash} using {hash_type} with a list of {total_lines} words.")
    
    # Otvori popis riječi s istim enkodiranjem
    with open(wordlist, 'r', encoding='latin1') as f:
        # Ponavljanje preko svake linije
        for line in tqdm(f, desc='Cracking hash', total=total_lines):
            if hash_fn(line.strip().encode()).hexdigest() == hash:
                return line.strip()  # Uklanja višak razmaka
            
    # Ako lozinka nije pronađena
    print("[!] Password not found in the wordlist.")
    return None

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Crack a hash using a wordlist.')
    parser.add_argument('hash', help='The hash to crack.')
    parser.add_argument('wordlist', help='The path to the wordlist.')
    parser.add_argument('--hash-type', help='The hash type to use.', default='sha256')
    args = parser.parse_args()
    print()
    # Pokušaj krekanja hasha i ispisi rezultat
    result = crack_hash(args.hash, args.wordlist, args.hash_type)
    if result:
        print("[+] Found Password:", result)
    else:
        print("[!] Password not found.")
