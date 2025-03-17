# Što je kriptografija?

Kriptografija  je  složena  znanost  i  umjetnost  osiguravanja  informacija
matematičke  tehnike  i  algoritmi.  U  svojoj  srži,  to  uključuje  transformaciju
čitljive  podatke,  poznate  kao  čisti  tekst,  u  nerazumljiv  format  tzv
šifrirani  tekst.  Ova  se  transformacija  postiže  primjenom  kriptografskih
algoritmi,  u  biti  skupovi  pravila  i  procedura.
 
- Pokretanje koda simetricna_kriptografija.py
Ispis rezultat koda:

Plain Text: b'Pozdrav iz Zagreba'
Generated key: b'WGo3UxvVvrgldqmP7QlpCVqmGSFTSgJCXsLhgf1q5XY='
Encrypted Message: b'gAAAAABn1a7uEX4ecHL-EpbT4jFEeGNKIGqvDEFHxMOpO3PocQNp4W6Y-ZNBCV9uU-dN1jAEMFMiKfgd8CNC3mGE3HXTHJATxG3h-vJlufCEAteUGpS5w8o='

Decrypted message: Pozdrav iz Zagreba


## RSA  šifriranje  i  dešifriranje

RSA (Rivest-Shamir-Adleman) je jedan od najpoznatijih asimetričnih kriptografskih algoritama koji se koristi za sigurno šifriranje i dešifriranje podataka, kao i za digitalne potpise. Osnovna ideja RSA algoritma zasniva se na matematičkoj složenosti faktorizacije velikih brojeva.

# Kako funkcioniše RSA?
RSA koristi par ključeva:
- Javni ključ (koristi se za šifriranje)
- Privatni ključ (koristi se za dešifriranje)
 
- Generiranje ključeva:
Pokretanje koda RSA.py
Ispis rezultata koda:

Generating key pair..
Public key: (65537, 114603808306014838892670147249690380561)
Private key: (25843869614944127800718767261207582973, 114603808306014838892670147249690380561)
Orginal poruka: Pozdrav RSA!
Encrypted message: 34797249570900936653989204567541729947556136678217209979432949254561859230308272399716464090049630512484909786106510488765274964695744430023693886359268718627229783529562996065978592728950304733990428940708551422508767224108718761662107391380070048724943711295153781235385501717996477418415963593918821010113068296362438143750019734735971130492393197447730946287016124489047929049032666626560971369915269322279288356750090813778170537211451386464755893863294
Decrypted message: Pozdrav RSA!


# Asimetrična kriptografija
Asimetrična kriptografija (poznata i kao kriptografija sa javnim ključem) je vrsta enkripcije u kojoj se koriste dva različita ključa:

Javni ključ – koristi se za šifriranje podataka. Može se slobodno djeliti sa svima.
Privatni ključ – koristi se za dešifriranje podataka. Mora ostati tajan.
Glavna prednost asimetrične kriptografije je što omogućava sigurnu komunikaciju između strana koje se ne poznaju, bez potrebe za prethodnom razmenom tajnog ključa (što je problem kod simetrične kriptografije).

Kako funkcionira?
Šifriranje

Pošiljatelj koristi javni ključ primatelja da šifrira poruku.
Šifrirana poruka može biti poslana preko nesigurnih kanala.
Dešifriranje

Primatelj koristi privatni ključ da dešifrira poruku i dobije originalan sadržaj.
🔑 Važno:
Podaci šifrirani javnim ključem mogu se dešifrirati samo privatnim ključem, što znači da čak ni pošiljatelj ne može kasnije dešifrirati poruku.

Prednosti i mane
✅ Prednosti
✔ Sigurna komunikacija bez potrebe za prethodnim djljenjem tajnih ključeva
✔ Omogućava digitalne potpise (provjera autentičnosti i integriteta podataka)
✔ Koristi se za SSL/TLS (HTTPS), elektronsku trgovinu, VPN, e-mail enkripciju

❌ Nedostaci
❌ Sporije od simetrične kriptografije (npr. AES), jer koristi složene matematičke operacije
❌ Ako privatni ključ bude ukraden, sigurnost sistema je ugrožena
 
- Pokretanje koda asimetricna_kriptografija.py
Ispis rezultata koda:

Orginal Message: b'Kriptografija je kull'
Encrypted Message: b'b]\xef!\xb8\xe4\x9c\x8e\x9eq;\x08\xecv\xd0\x0f\x19\xb4a6p\xc1;8\xcb9\xb4\xf5\xc2\xa0\xa9!j\xe1L\xf8\xbd\x98?\x0ez\xb1M,\xb3\xb6\xca\xff\x91\xd0\xe3\xa44m\x04CT2\xf8\xbd\x7f\x0cy\x13\x82\x15X\xf0\x03\xd8\xef\xf5eJ\xb0mV}Lo\xe7\x85Gp\xdbB^\x90U\x15*"\xdd\x17.$\xd7{\x17\xd8+CM\xc7\xf2\xfaN\x95\xe3\xb7]\xa6{\xc9j\x8a}\xd4R\xac\xf0\xc7\x15+g\xcd\x95(\xcda\x862\xc6\xb5\xe7\xdd_\xa9\xadO\xb5\x8a\xc56$\xf5\x92c\xdb\xb9Z%\xec\x8c^y\xb3\x02\xf2\xe8G\xe3\xc1\xafX\t\xe0@\x11\x98\x88yP\xc2\xa5\x86}rh\x8c\xcd[\xebCv\x15\x07\'\x89\xa82\xa2\xf20=\x80a3F\xcd\xe0\x8c\x97\xfc\xbf\x85\t\x9cIP:\xcd\x80nW\x7f0\x0e1\x14\x06\x84\x0f\x90]\x9eOt\r\xa3\xae\x15\xfe\xb6\x19\xdbq((\xf8;\xccf\x11\x11a\xb5:\xb3\xd3\x0c@"\x07\x0b\xad'  b'b]\xef!\xb8\xe4\x9c\x8e\x9eq;\x08\xecv\xd0\x0f\x19\xb4a6p\xc1;8\xcb9\xb4\xf5\xc2\xa0\xa9!j\xe1L\xf8\xbd\x98?\x0ez\xb1M,\xb3\xb6\xca\xff\x91\xd0\xe3\xa44m\x04CT2\xf8\xbd\x7f\x0cy\x13\x82\x15X\xf0\x03\xd8\xef\xf5eJ\xb0mV}Lo\xe7\x85Gp\xdbB^\x90U\x15*"\xdd\x17.$\xd7{\x17\xd8+CM\xc7\xf2\xfaN\x95\xe3\xb7]\xa6{\xc9j\x8a}\xd4R\xac\xf0\xc7\x15+g\xcd\x95(\xcda\x862\xc6\xb5\xe7\xdd_\xa9\xadO\xb5\x8a\xc56$\xf5\x92c\xdb\xb9Z%\xec\x8c^y\xb3\x02\xf2\xe8G\xe3\xc1\xafX\t\xe0@\x11\x98\x88yP\xc2\xa5\x86}rh\x8c\xcd[\xebCv\x15\x07\'\x89\xa82\xa2\xf20=\x80a3F\xcd\xe0\x8c\x97\xfc\xbf\x85\t\x9cIP:\xcd\x80nW\x7f0\x0e1\x14\x06\x84\x0f\x90]\x9eOt\r\xa3\xae\x15\xfe\xb6\x19\xdbq((\xf8;\xccf\x11\x11a\xb5:\xb3\xd3\x0c@"\x07\x0b\xad'
Decrypted Message: Kriptografija je kull


# Eliptične krivulje u kriptografiji
Eliptična krivulja je posebna matematička kriva koja se koristi u kriptografiji eliptičnih krivulja (ECC - Elliptic Curve Cryptography).
Ova tehnika je sigurnija i efikasnija od klasičnih metoda kao što je RSA, jer pruža istu sigurnost sa mnogo manjim ključevima.

Prednosti ECC u odnosu na RSA
✅ Jača sigurnost sa manjim ključem (256-bitni ECC ključ nudi istu sigurnost kao 3072-bitni RSA ključ).
✅ Brža obrada i manja potrošnja resursa (pogodno za mobilne uređaje i IoT).
✅ Manja veličina ključeva i digitalnih potpisa, što smanjuje potrebu za memorijom.

❌ Mane
🔹 Matematički složeniji od RSA.
🔹 Teža implementacija i verifikacija, što može dovesti do sigurnosnih grešaka.

- Pokretanje koda elipticna_krivulja.py
Ispis rezultata koda:

Public Key:
-----BEGIN PUBLIC KEY-----
MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEuJLjrOnX+ovexi7hl+WwZUPHs90JKasB
KLi8FuT7HuD0oPR+4tD55VlwKQWJ42khyMhb5hvI21+vCscdsybbN60bSfJLt8Pu
Ta4TNAdZcMzcqyGI2Wh+Cf9e4/B4G52E
-----END PUBLIC KEY-----

Encrypted Message: b'\xd8\xee\xa9\xe8\xba*\xce\xdd\x9c\x15\xber\xeb\x00\xdd!\\{\xdf\xd5\xe2y=)#*&\x8f>\xef\xbaP'
Decrypted Message: b'\xd8\xee\xa9\xe8\xba*\xce\xdd\x9c\x15\xber\xeb\x00\xdd!\\{\xdf\xd5\xe2y=)#*&\x8f>\xef\xbaP'

# Čemu služe digitalni potpisi i za što se koriste?
Digitalni potpisi služe za provjeru autentičnosti, integriteta i neporecivosti digitalnih podataka. Koriste se kako bi se osiguralo da dokument ili poruka nije mijenjana te da dolazi od provjerenog pošiljatelja.

Glavne primjene digitalnih potpisa:
Sigurna elektronička komunikacija

Digitalni potpisi osiguravaju da e-mailovi, poruke i datoteke dolaze od legitimnog pošiljatelja i nisu mijenjani u prijenosu.
Koristi se u protokolima kao što su PGP (Pretty Good Privacy) i S/MIME.
Potpisivanje dokumenata

Digitalni potpisi zamjenjuju ručne potpise u pravnim i poslovnim dokumentima.
Primjeri: PDF digitalni potpisi (Adobe Sign, DocuSign), potpisivanje ugovora, faktura i službenih dopisa.
Sigurnost softvera i ažuriranja

Programeri koriste digitalne potpise za potpisivanje aplikacija kako bi osigurali da ih korisnici preuzimaju iz pouzdanih izvora.
Primjeri: Microsoft, Apple i Linux potpisuju softver kako bi spriječili instalaciju zlonamjernih programa.
Autentifikacija korisnika i uređaja

Koristi se u dvofaktorskoj autentifikaciji (2FA) i autentifikaciji servera u web komunikaciji (TLS/SSL certifikati).
Omogućuje sigurno prijavljivanje na sustave bez korištenja lozinki.
Blockchain i kriptovalute

U Bitcoin i drugim kriptovalutama digitalni potpisi se koriste za potvrdu transakcija.
Svaka transakcija je potpisana privatnim ključem kako bi se dokazalo vlasništvo nad sredstvima.
Elektroničke osobne iskaznice i e-Government

Vlade koriste digitalne potpise u e-osobnim iskaznicama, e-porezima i drugim e-uslugama.
Primjer: Hrvatska e-osobna iskaznica omogućava potpisivanje dokumenata putem sustava e-Građani.
Zaštita integriteta podataka

Digitalni potpisi osiguravaju da podaci nisu mijenjani ili kompromitirani tijekom prijenosa.
Koristi se u osjetljivim industrijama poput bankarstva, zdravstva i financijskih transakcija.

Zaključak
Digitalni potpisi su ključni alat za sigurnost u digitalnom svijetu. Pružaju autentičnost, integritet i neporecivost, čime omogućuju sigurno poslovanje, komunikaciju i upravljanje podacima u digitalnom okruženju.

- Pokretanje koda kreirati_i_provjeriti_potpise.py
Ispis rezultata koda:

Signature verified: The message is authentic.

# Cezarova šifra – Osnovna Substitucijska Šifra
Cezarova šifra (poznata i kao Caesar cipher) jedna je od najstarijih i najjednostavnijih metoda šifriranja. Ime je dobila po Gaju Juliju Cezaru, koji ju je koristio za sigurnu vojnu komunikaciju.

Kako radi Cezarova šifra?
Cezarova šifra je substitucijska šifra, što znači da zamjenjuje svako slovo u poruci drugim slovom pomaknutim za određeni broj mjesta u abecedi.

Primjer s pomakom od 3 mjesta:

Originalni tekst: HELLO
Pomak za 3 mjesta: KHOOR
H → K, E → H, L → O, L → O, O → R

- Pokretanje koda cezarova_sifra.py
Ispis rezultata koda:

[?] Molimo unesite svoj tekst/poruku: Kriptografija u pythonu
[?] Navedite duljinu smjene (0-25): 7
[+] 'Kriptografija u pythonu' je šifriran kao Rypwavnyhmpqh b wfaovub

# Razbiti cezarovu šifru
  
- Pokretanje koda cezarova_sifra_razbiti.py
Šifru dobijete "[?] Navedite duljinu smjene (0-25): 7" (koji broj odaberete 0-25)
Ispis rezultata koda:

[?] Unesi tekst/poruku za dešifriranje: Rypwavnyhmpqh b wfaovub
Key 0: Rypwavnyhmpqh b wfaovub
Key 1: Qxovzumxglopg a veznuta
Key 2: Pwnuytlwfknof z udymtsz
Key 3: Ovmtxskvejmne y tcxlsry
Key 4: Nulswrjudilmd x sbwkrqx
Key 5: Mtkrvqitchklc w ravjqpw
Key 6: Lsjquphsbgjkb v qzuipov
Key 7: Kriptografija u pythonu
Key 8: Jqhosnfqzehiz t oxsgnmt
Key 9: Ipgnrmepydghy s nwrfmls
Key 10: Hofmqldoxcfgx r mvqelkr
Key 11: Gnelpkcnwbefw q lupdkjq
Key 12: Fmdkojbmvadev p ktocjip
Key 13: Elcjnialuzcdu o jsnbiho
Key 14: Dkbimhzktybct n irmahgn
Key 15: Cjahlgyjsxabs m hqlzgfm
Key 16: Bizgkfxirwzar l gpkyfel
Key 17: Ahyfjewhqvyzq k fojxedk
Key 18: Zgxeidvgpuxyp j eniwdcj
Key 19: Yfwdhcufotwxo i dmhvcbi
Key 20: Xevcgbtensvwn h clgubah
Key 21: Wdubfasdmruvm g bkftazg
Key 22: Vctaezrclqtul f ajeszyf
Key 23: Ubszdyqbkpstk e zidryxe
Key 24: Tarycxpajorsj d yhcqxwd
Key 25: Szqxbwozinqri c xgbpwvc

# Afina šifra – Poboljšana verzija Cezarove šifre
Afina šifra je modificirana verzija Cezarove šifre, ali s dodatnim matematičkim elementom kako bi se povećala sigurnost. Pripada skupini monoalfabetskih substitucijskih šifri, što znači da svako slovo ulaznog teksta uvijek postaje isto šifrirano slovo.

Kako radi afina šifra?

Afina šifra koristi matematičku funkciju za pretvorbu svakog slova u šifrirani oblik.
x – indeks slova u abecedi (npr. A=0, B=1, C=2… Z=25),
a – multiplikativni ključ (mora biti relativno prost s 26, tj. gcd(a, 26) = 1),
b – aditivni ključ (pomak, slično Cezarovoj šifri),
mod 26 – kako bi se osiguralo da rezultat ostane unutar abecede.
Za dešifriranje koristimo multiplikativni inverz broja a, označen s a⁻¹, kako bismo dobili izvorni tekst. 

Za što se koristi afina šifra?
Kriptografska edukacija – koristi se u obrazovanju za učenje osnova kriptografije i modularne aritmetike.
Poboljšana verzija Cezarove šifre – pruža veću sigurnost od jednostavne zamjene jer koristi i multiplikaciju, ne samo pomak.
Povijesne enkripcije – prije pojave modernih šifriranih sustava koristila se za kodiranje poruka u vojne i privatne svrhe.
Osnovne enkripcije u aplikacijama – može se koristiti u jednostavnim programima i igrama gdje nije potrebna visoka sigurnost.

- Pokrenite kod afina_sifra.py
Ispis rezultata koda:

[?] Unesite tekst za šifriranje: KRIPTOGRAFIJA
[+] Plaintext: KRIPTOGRAFIJA
[+] Šifrirani tekst: OJIDPACJKZILK

# Razbijanje afine šifre
Afina šifra, iako jača od Cezarove šifre, još uvijek je lako probijena jer je riječ o monoalfabetskoj substitucijskoj šifri. To znači da svako slovo u originalnom tekstu uvijek postaje isto slovo u šifriranom tekstu, što omogućava napade poput analize učestalosti i brutalne sile.

- Pokrenite kod afina_sifra_dekriptirati.py
U afinoj šifri se koristi za ključ a = 3, b = 10
Ispis rezultata koda:

[?] Unesi poruku za dešifriranje:OJIDPACJKZILK
Key (a=3, b=7): LSJQUPHSBGJKB
Key (a=3, b=8): CJAHLGYJSXABS
Key (a=3, b=9): TARYCXPAJORSJ
Key (a=3, b=10): KRIPTOGRAFIJA
Key (a=3, b=11): BIZGKFXIRWZAR

# Zaključati PDF datoteka – Sigurnosne Metode i Primjena
Zaključavanje PDF datoteke omogućava zaštitu dokumenata lozinkom ili ograničenjima pristupa, čime se sprječava neovlašteno otvaranje, uređivanje ili ispisivanje. To se često koristi za zaštitu povjerljivih informacija, pravnih dokumenata i ugovora.

Vrste zaštite PDF-a
Postoji nekoliko metoda zaštite PDF-a:

Zaštita lozinkom ("User Password") – Korisnik mora unijeti lozinku kako bi otvorio PDF.
Zaštita od uređivanja ("Owner Password") – PDF se može otvoriti, ali nije dopušteno mijenjanje, ispis ili kopiranje teksta.
Šifriranje PDF-a – PDF se enkriptira kako bi se osigurala potpuna zaštita sadržaja.
Digitalni potpisi – Osiguravaju autentičnost i integritet dokumenta.
 
- Umetnite pdf datoteku u direktori gdje vam je pisan kod.
Pokrenite kod zakljucati_pdf.py
Ispis rezultata koda:

Unesi stazu do PDF datoteke: Recept.pdf
Unesi lozinku za zaključavanje PDF: 
[!] Molim pričekajte nekoliko secundi...
[+] PDF uspješno zaključan.

Kada pokušavate pokrenuti pdf datoteku pomoču preglednika morate upisati lozinku koju ste naveli.

# Razbiti PDF
Morate napraviti datoteku password.txt i napitati neke  lozinke koje če se koristiti u kriptografiji

- Pokretanje koda: python razbiti_pdf.py Recept.pdf password.txt
Ispis rezultata koda:

Dokumenti\Python File\Kriptografija> python razbiti_pdf.py Recept.pdf password.txt
Pogađanje lozinke:  98%|████████████████████████████████████████████████████████████████████████████████████████████████████▉  | 50/51 [00:00<00:00, 18253.56it/s]
[+] Lozinka pronađena: 1234

# Stvaranje Zip datoteke i zaključavanje zip datoteke
ZIP datoteke su popularne za kompresiju i arhiviranje više datoteka u jedinstveni paket. Također, možete dodati lozinku za šifriranje i zaštitu tih datoteka. Python nudi različite biblioteke za rad s ZIP datotekama.
 
- Pokretanje koda: python zakljucati_zip_datoteku.py --zipfile new_test.zip --addfile kriptografija.txt
Ispis rezultata koda:

Kriptografija> python zakljucati_zip_datoteku.py --zipfile new_test.zip --addfile kriptografija.txt
[?] Unesite svoju lozinku > 
[+] Zip datoteka je zaključana jakom lozinkom.

kreirali smo datoteku new_test.zip

# Dodavanje lozinke u zip (-protected)

- Pokretanje koda: python dodati_lozinku_u_zip.py Nova.zip
unesete lozinku i mapa je kreirana

# Razbijannje zip lozinke
 
- Pokrenuti kod: python razbiti_zip.py new_test.zip password.txt
Ispis rješenje koda:

Kriptografija> python razbiti_zip.py new_test.zip password.txt
Ukupan broj lozinki za testiranje: 52
  0%|                                                                                                                                    | 0/52 [00:00<?, ?word/s][+] Lozinka pronađena: Mery123$
 98%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▋  | 51/52 [00:00<00:00, 1094.06word/s]

# Upravitelj lozinki

-  Pokretanje koda: python upravitelj_lozinki.py
Kada se prijavite dobite (user_data.json)
Ispis rješenje koda:

1. Registracija
2. Prijava
3. Izlaz
Unesite svoj izbor: 1 
Unesite korisničko ime: Lara
Unesite lozinku: 
[+] Registracija uspješna.

1. Registracija
2. Prijava
3. Izlaz
Unesite svoj izbor: 2
Unesite korisničko ime: Lara
Unesite lozinku: 
[+] Prijava uspješna.

1. Dodaj web stranicu
2. Dohvati lozinku
3. Pogledaj spremljene web stranice
4. Odjava
Unesite svoj izbor: 4
[+] Odjavljeni ste.

1. Registracija
2. Prijava
3. Izlaz
Unesite svoj izbor: 3
Izlaz iz programa...

# Program za šifriranje datoteka
 
- Pokretanje koda:
Ispis rješenja koda:

[?] ] Želite li šifrirati ili dekriptirati datoteku?

Odaberite opciju 1 za šifriranje i 2 za dešifriranje: 1
Unesite stazu do ulazne datoteke: C:\Users\Krunoslav\OneDrive\Dokumenti\Python File\Kriptografija\kriptografija.txt
[+] C:\Users\Krunoslav\OneDrive\Dokumenti\Python File\Kriptografija\kriptografija.txt Šifriranje uspješno.

šifrirana datoteka:
gAAAAABn2G-NDnblp3wJMcwe9wcpjQsN1Qm09HlPyQznPgJsz6qttJqYmBwo3k2gGkINRPjkJ2YZOaKXCN8LFfIwdLSEXnHPJQGHmV1Vgd8VsP_OI99b4Sr-j937gnyuhb6RwFqQB7vGkJxewzOyxEvbdIBC701_sLWMBfLzSvXwAE6MdYjkdAyIQo0xLmdoHbnxBKplQm9gEfIxwnRN1OH_nNIcQrv--obRuaU31xp0EkcK1-tgxhfeAvrdD7iDbnPDb2XoKo366F3lVdp3EZRZ7zdqXI8j1wbWZ38rvtVRIwc289_eg0tPrt8j9o0Q60OsISup0Me6bOuS7wWBIqb9TRuZZgAEdCGikz35bKgBXzh6UPyX1QxMKA7Le142EtJlHc_2WDrNHr50V8p0rQGQNN9SrxA2I_kjuU7wmRz2_yWo6J__l9IUMyogdoLiH19YbPyLpbKeDlRQtLcugpiX54fvID3dxC7BBp8M8jxv85m3JwppnpZt1892gVg8eX1e2H6YkNWxGwbxWszj51XAPtUO9Z694dDh3ibyyC2yjdB233q-SJVShpGsKlUxhB8LZExTY7yg6B83_wV8000d6OxmufTz6uK15W2c_8tCLbjAfdsOVpY=
za dešifriranje:
[?] ] Želite li šifrirati ili dekriptirati datoteku?

Odaberite opciju 1 za šifriranje i 2 za dešifriranje: 2
Unesite stazu do ulazne datoteke: C:\Users\Krunoslav\OneDrive\Dokumenti\Python File\Kriptografija\kriptografija.txt
[+] Uspješno dešifrirano

# Validator datoteka
Ovo je jednostavna, ali močna skripta koju možemo koristiti za provjeru naših preuzimanja  kako  bismo  osigurali  integritet.
Sada,  testirajmo  naš  kod.  Za  ovu  demonstraciju  koristit  ću  VLC media  player.  Koristim  ovo  jer  je  VLC  prilično  popularan  media  player.
Kada odete na stranicu za preuzimanje VLC i preuzmete, odmah ispod Downloading VLC možete vidjeti SHA-256, kopirajte ga i pokrenite skriptu i nakon riječi --hash zaljepite SHA-255 i stisnete enter.

- Pokrenuti kod: python validator_datoteka.py -f C:\Users\Krunoslav\Downloads\vlc-3.0.21-win32.exe --hash  4bd03202b6633f9611b3fc8757880a9b2b38c7c0c40ed6bcbefec71c0099d493
Ispis:

[+] Hash provjera uspješna. Softver je autentičan.

