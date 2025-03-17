import PyPDF2, getpass
from colorama import Fore, init

init()

# funkcija za zaključavanje pdf
def lock_pdf(input_file, password):
    with open(input_file, 'rb') as file:
        # Stvoriti objekt pdf čitača
        pdf_reader = PyPDF2.PdfReader(file)
        # Stvoriti objekt za pisanje pdf-a
        pdf_writer = PyPDF2.PdfWriter()
        # Dodati sve stranice pisaču
        for page_run in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_run])
        # Šifrirati pdf s naveddnom lozinkom
        pdf_writer.encrypt(password)
        # Napisati šifrirani sadržaj natrag u izvornu datoteku
        with open(input_file, 'wb') as output_file:
            pdf_writer.write(output_file)
# Dobiti korisnički unos
input_pdf = input("Unesi stazu do PDF datoteke: ")
password = getpass.getpass("Unesi lozinku za zaključavanje PDF: ")
# Zaključaj PDF koristeči PyPDF2
print(f"{Fore.GREEN}[!] Molim pričekajte nekoliko secundi...")
lock_pdf(input_pdf, password)
# Daje korisniku do znanja da je gotovo
print(f"{Fore.GREEN}[+] PDF uspješno zaključan.")
