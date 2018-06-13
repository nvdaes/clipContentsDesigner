# Clip Contents Designer dodaj tekst u međuspremnik #

*	Autor: Noelia Ruiz Martínez.
*	Preuzmi [stabilnu inačicu][1]
*	Preuzmi [razvojnu inačicu][2]

Ovaj se dodatak koristi kako bi se tekst mogao dodati u međuspremnik, što
može biti korisno kada želite zajedno spojiti dijelove teksta koji su
spremni za lijepljenje. Sadržaj međuspremnika također se može izbrisati.

## Tipkovnički prečaci ##
*	NVDA+windows+c: dodaj označeni tekst, ili niz označen uz pomoć preglednog
  kursora, u međuspremnik.
*	NVDA+windows+x: Obriši sadržaj međuspremnika.
*	NVDA+windows+f9: Mark the current position of the review cursor as the start of the text to be added to the clipboard. If you use nvda+F9, the text will not be added.
*	 Not assigned: Copies to (or cuts from) the clipboard, with the possibility of being asked for a previous confirmation.

Napomena: Prečaci iznad mogu se promijeniti iz NVDA izbornika, podizbornika
postavke, dijaloškog okvira ulazne geste kategoria pregled teksta.

## Podizbornik postavke ##
*	Clip Contents Designer settings: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
It's also possible to choose if the added text will be appended or prepended, if available actions (add, clear clipboard, emulate copy and emulate cut) should be performed inmediately or after confirmation, and if confirmations will be requested just if text is contained in the clipboard.

Napomene: 

*	The above command can be changed from NVDA menu, Preferences submenu,
  Input gestures dialog, Configuration category.
*	Potvrde neće biti zatražene ako se neka poruka u vezi NVDA još uvijek
  prikazuje. U tim slučajevima, akcije će se odmah izvršavati

## Changes for 7.0

* U dijaloškom okviru za konfiguriranje funkcionalnosti Simulirano kopiranje
  i Simulirano rezanje, ako odaberete ne, naredbe za ove značajke će se
  ukloniti, te ćete za iste naredbe koristiti naredbe control+c I control+x.

## Changes for 6.0

*	 Dodane mogućnosti izbora hoće li se dostupne akcije izvršavati nakon potvrde.
*	Dodane komande Kopiraj i Izreži, koje možete odabrati u dijaloškom okviru Ulazne geste.
*	 Dodane komande Kopiraj i Izreži, koje možete odabrati u dijaloškom okviru Ulazne geste*	Dodan dijaloški okvir za podešavanje naredbi Kopiraj i Izreži pri instalaciji. Ovo dozvoljava dodavanje kratica control+c i control+x za naredbe kopiraj i izreži, te pitanje želite li zamijeniti sadržaj međuspremnika dok koristite ove tipkovničke kratice.
*	Riješena dokumentacija za script_add (Windows+NVDA+c).

## izmjene u inačici 5.0 ##

*	Vizualno predstavljanje dijaloških okvira je poboljašno, slično dijaloškim
  okvirima koji su prikazani u programu NVDA.
*	Zahtjeva NVDA inačicu 2016.4 ili noviju.

## izmjene u inačici 4.0 ##
*	Podešavanja dodatka upravljaju NVDA konfiguracijom, tako da možete
  koristiti standardne profile za čuvanje podešavanja i ne morate kopirati
  podešavanja nakon reinstalacije.
*	Sada je moguće izabrati hoće li dodani tekst biti spojen ili prespojen,
  koristeći izborno polje dodaj dio teksta prije podataka u postavkama
  dodatka.

## izmjene u inačici 3.0 ##
*	Brajev prikaz MathML objekata se može dodati u privremenu memoriju ako je
  MathPlayer instaliran.
*	Ako nema razdvajača, bit će samo jedan red između dodanih segmenata.
*	Prečica može biti podešena za otvaranje dijaloškog okvira postavki
  dodatka.
*	Dodan izborni okvir u postavkama za izbor da li če razdvajač biti kopiran
  za ponovni uvoz nakon reinstalacije dodatka.

## izmjene u inačici 2.0 ##
*	znakovi devanagari pisma mogu se koristiti kao rastavljači između dodanog
  sadržaja.

## Promjene u inačici1.0 ##
*	Prva inačica.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev
