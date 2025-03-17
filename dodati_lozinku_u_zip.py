import pyzipper
import os

def add_password_to_existing_zip(existing_zip_path, new_zip_path, password):
    """Dodajte lozinku postoječoj ZIP datoteci stvaranjem nove ZIP datoteke zaštičene lozinkom.
    Args:
    existing_zip_path: Put do postoječe ZIP datoteke.
    new_zip_path: Put za novu ZIP datoteku zaštičenu lozinkom.
    password: Lozinka za novu ZIP datoteku."""
    with pyzipper.AESZipFile(new_zip_path, 'w', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as new_zf:
        # postaavite lozinku za novu zip datoteku
        new_zf.setpassword(password.encode('utf-8'))
        # otvorite postojeću zip datoteku
        with pyzipper.ZipFile(existing_zip_path, 'r') as existing_zf:
            # iteracija preko datoteke u postojećoj zip datoteci
            for file_name in existing_zf.namelist():
                # pročitajte datoteku iz postojeće zip datoteke i zapišite je u novu zip datoteku
                with existing_zf.open(file_name) as source_file:
                    new_zf.writestr(file_name, source_file.read())

if __name__ == "__main__":
    import sys
    import getpass
    existing_zip_path = sys.argv[1]
    # neke osnovne provjere
    assert os.path.exists(existing_zip_path), "Priložena ZIP datoteka ne postoji"
    # nova zip staza je postojeća zip staza kojoj je pridodan (-protected)
    new_zip_path = existing_zip_path.split('.')[0] + '-protected.zip'
    # lozinka za novu zip datoteku
    password = getpass.getpass("Unesite lozinku za novu ZIP datoteku: ")
    # dodaj lozinku postojećoj zip datoteci
    add_password_to_existing_zip(existing_zip_path, new_zip_path, password)