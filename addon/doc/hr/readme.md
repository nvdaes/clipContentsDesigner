# Upravljanje sadržajem međuspremnika (Clip Contents Designer) #

*	Authors: Noelia, Abdel.
*	NVDA kompatibilnost: 2018.4 do 2019.2.
*	Preuzmi [stabilnu verziju][1]
*	Preuzmi [razvojnu verziju][2]

Ovaj se dodatak koristi za dodavanje teksta u međuspremnik, što može biti
korisno kad se žele spojiti dijelovi teksta, koji su spremni za
lijepljenje. Sadržaj međuspremnika se može i izbrisati te prikazati u modusu
za čitanje.

## Tipkovnički prečaci ##
*	NVDA+windows+c: U međuspremnik dodaj označeni tekst, brajične znakove u
  unikodu koji predstavljaju MathML objekte ili znakovni niz koji je označen
  pomoću preglednog kursora.
*	NVDA+windows+x: Obriši sadržaj međuspremnika.
*	NVDA+windows+f9: Označi trenutačni položaj pokazivača kao početak teksta koji se dodaje u međuspremnik. Ako koristiš NVDA+F9, tekst se neće dodati.
*	Nije dodijeljeno: Kopira u međuspremnik (ili se reže iz njega), s mogućnošću da se prethodno od korisnika traži potvrda.
*	Nije dodijeljeno: Prikazuje tekst međuspremnika u modusu pregledavanja ili najavljuje prazno stanje međuspremnika ili sadržaj koji se ne može predstaviti u pregledavajućoj poruci, na primjer ako su datoteke ili mape kopirane iz Windows Explorer.

Napomena: Gore navedeni prečaci se mogu promijeniti u NVDA izborniku,
podizbornik Postavke, dijaloški okvir Ulazne geste, kategorija Pregled
teksta.

## Izbornik za Postavke ##
*	Postavke za „Upravljanje sadržajem međuspremnika”: Omogućuje postavljanje rastavljača koji se može koristiti za traženje segmenata teksta, nakon što je cjelokupni tekst zalijepljen.
Također je moguće odabrati hoće li se tekst dodati ispred ili iza postojećeg teksta, ako se raspoložive radnje (dodaj, izbriši međuspremnik, simuliraj kopiranje i simuliraj izrezivanje) trebaju izvesti odmah ili nakon potvrde, a ako će se potvrde uvijek tražiti, samo ako se u međuspremniku nalazi tekst ili ako međuspremnik nije prazan.
Nadalje je moguće promijeniti format i maksimalni broj znakova teksta u međuspremniku, koji će biti prikazan u modusu pregledavanja. Povećanje ograničenja može stvoriti probleme, ako međuspremnik sadrži veliki broj tekstualnih nizova. Zadana granica je 100000 znakova.

Napomene:

*	Gore navedeni prečaci se mogu promijeniti u NVDA izborniku, podizbornik
  Postavke, dijaloški okvir Ulazne geste, kategorija Konfiguracija.
*	Neće biti potrebno potvrditi, ako se neka NVDA poruka još uvijek
  prikazuje. U tim slučajevima će se radnje izvršavati odmah

## Promjene u verziji 10.0
* Ispravljana je greška u dijaloškom okviru za prikaz teksta međuspremnika,
  kad naslov sadrži ne-latinične znakove.
* Ispravljena je greška kad se koriste funkcije simuliranja izrezivanja i
  kopiranja s arapskim rasporedom tipkovnice. To je ispravio Abdel, dodan je
  kao autor dodatka.

## Promjene u verziji 9.0

* Dodana je mogućnost prikazivanja teksta međuspremnika u modusu čitanja.
* Dodana je opcija za potrebu potvrđivanja ako međuspremnik nije prazan, na
  primjer, ako su kopirane datoteke ili mape.
* Zahtijeva NVDA verziju 2018.4 ili noviju.

## Promjene u verziji 8.0 ##

* Postavke dodatka se prikazuju u odgovarajućoj kategoriji dijaloškog okvira
  za NVDA Postavke.
* Zahtijeva NVDA verziju 2018.2 ili noviju.
* Ako treba, moguće je preuzeti [zadnju verziju kompatibilnu s NVDA
  2017.3][3].

## Promjene u verziji 7.0

* U dijaloškom okviru za konfiguriranje funkcionalnosti Simuliraj kopiranje
  i Simuliraj izrezivanje, ako se odabere „ne”, uklonit će se naredbe za ove
  funkcije, tako da će biti moguće koristiti normalni način rada za
  control+c i control+x.

## Promjene u verziji 6.0

*	Dodana je mogućnost za odluku o izvršavanju dostupnih radnji nakon potvrde.
*	Dodane su naredbe Simuliraj kopiranje i Simuliraj izrezivanje, koje je moguće dodijeliti u dijaloškom okviru Ulazne geste.
*	Dodan je dijaloški okvir za podešavanje naredbi Simuliraj kopiranje i Simuliraj izrezivanje, tijekom instaliranja. Ovo dozvoljava dodavanje naredbi control+c i control+x za kopiranje i izrezivanje, te postavljanjem pitanja, želiš li zamijeniti sadržaj međuspremnika pri korištenju ovih tipkovničkih prečaca.
*	Riješena dokumentacija za script_add (Windows+NVDA+c).

## Promjene u verziji 5.0 ##

*	Vizualni prikaz dijaloških okvira je poboljašn, slično dijaloškim okvirima
  koji su prikazani u programu NVDA.
*	Zahtijeva NVDA verziju 2016.4 ili noviju.

## Promjene u verziji 4.0 ##
*	Postavkama dodatka se upravlja NVDA konfiguracijom, tako da je moguće
  koristiti standardne profile za spremanje raznih rastavljača te nije
  potrebno kopirati postavke nakon reinstalacije.
*	Sad je moguće izabrati, hoće li dodani tekst biti dodan ispred ili iza
  postojećeg teksta, koristeći izborno polje „Dodaj tekst ispred podataka
  međuspremnika” u postavkama dodatka.

## Promjene u verziji 3.0 ##
*	Brajičin prikaz MathML objekata se može dodati u privremenu memoriju, ako
  je MathPlayer instaliran.
*	Ako nema razdvajača, dodat će se samo jedan redak između dodanih segmenata
  teksta.
*	Moguće je odrediti prečac za otvaranje dijaloškog okvira za postavke
  dodatka.
*	U dijaloškom okviru za postavke je dodan potvrdni okvir, kojim se odlučuje
  o tome, treba li razdvajač kopirati za uvoz nakon ponovnog instaliranja
  dodatka.

## Promjene u verziji 2.0 ##
*	Znakovi devanagari pisma se mogu koristiti kao rastavljači između dodanog
  sadržaja.

## Promjene u verziji 1.0 ##
*	Prva verzija.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ccd

[2]: https://addons.nvda-project.org/files/get.php?file=ccd-dev

[3]: https://addons.nvda-project.org/files/get.php?file=ccd-o
