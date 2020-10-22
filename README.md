# Opis rješenja:
Moje rješenje se sastoji od 2 aplikacije. Za izradu aplikacija koristio sam flask biblioteku. Za svaku aplikaciju postoji po jedan dockerfile i testna skripta.

## Service1.py
Aplikacija zatraži json file iz kojeg uzme string, a zatim taj string hashira te ga vrati.

- lib: flask i hashlib
- napravi instancu Flask klase za web aplikaciju
- definira se funkcija te joj se dodjeli putanja i metoda koju će izvršavati u ovom slučaju POST
- unutar funkcije dohvaća se json koji mora sadržavati varijablu rawValue
- dohvaća se i hashFunc koja je defaultno postavljena na sha256 ta varijabla govori koji način hashiranja će se koristiti
- metoda getHash vrača izračunatu hash vrijednost stringa dobivenog iz rawValue

## Service2.py
- lib: flask, requests, json, os
- definira se funkcija getHtmlHash
- ova funkcija najprije dohvaća json u kojem je zapisan url s tog url-a pokupi cijeli HTML 
- HTML se proslijedi preko varijable rawValue u prvu aplikaciju koja hashira taj tekst

## config.yml
- najprije pokreće instalaciju biblioteke pytest
- Nakon instalacije pokreće test za Service1.py a zatim za Service2.py

## Testovi
- Testovi su napisani samo kako bi se mogao bolje demonstrirati rad CircleCi
  
# Poboljšanja:

- Umjesto md5 koristio sam sha256. Tijekom vremena otkriveni su nedostatci md5 hash algoritma.
National Institute of Standards and Technology preporučuje korištenje SHA-256.

- Izbacio sam watchdog.

- Pošto 2 kontejnera moraju komunicirati napravio sam docker network, te sam ga morao dodijeliti kontejnerima.

- Push na master trigera build na CircleCI koji pokreče testove za oba servisa.
