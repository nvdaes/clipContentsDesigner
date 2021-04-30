# Upravljanje sadržajem međuspremnika (Clip Contents Designer) #

*	Authors: Noelia, Abdel.
*	NVDA kompatibilnost: 2019.3 i novija
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
*	Nije dodijeljeno: Kopira u međuspremnik (ili se reže iz njega), s
  mogućnošću da se prethodno od korisnika traži potvrda.
*	Nije dodijeljeno: Prikazuje tekst međuspremnika u modusu pregledavanja ili
  najavljuje prazno stanje međuspremnika ili sadržaj koji se ne može
  predstaviti u pregledavajućoj poruci, na primjer ako su datoteke ili mape
  kopirane iz Windows Explorera.
*	Nije dodijeljeno: Prikazuje tekstualni sadržaj međuspremnika kao običan
  tekst u modusu pregledavanja ili najavljuje prazno stanje međuspremnika
  ili sadržaj koji se ne može predstaviti u pregledavajućoj poruci, na
  primjer ako su datoteke ili mape kopirane iz Windows Explorer.


## Upravljanje sadržajem međuspremnika, postavke ##

Ova je ploča dostupna u NVDA izborniku, podizbornik Postavke, dijaloški
okvir Postavke.

It contains the following controls:

* Type the string to be used as a separator between contents added to the
  clipboard: Allows to set a separator which can be used to find the text
  segments once the entire added text is pasted.
* Add text before clip data: It's also possible to choose if the added text
  will be appended or prepended.
* Select the actions which require previous confirmation: You can choose,
  for each action available, if it should be performed inmediately or after
  confirmation. Available actions are: add text, clear clipboard, emulate
  copy and emulate cut.
* Request confirmation before performing the selected actions when: You can
  select if confirmations will be requested always, just if text is
  contained in the clipboard, or if clipboard is not empty (for example if
  you've copied a file, not text).
* Format to show the clipboard text as HTML in browse mode: If you're
  learning HTML markup language, you may choose Preformatted text in HTML or
  HTML as shown in a web browser, to have an idea of how your HTML code will
  be rendered by NVDA in a browser. The difference between preformatted and
  conventional HTML is that the first option will preserve consecutive
  spaces and line breaks, and the second one will compact them.  For
  example, write some HTML tags like h1, h2, li, pre, etc., select and copy
  the text to clipboard, and use clipContentsDesigner add-on to show the
  text in a browseable message.
* Maximum number of characters when showing clipboard text in browse mode:
  Please, be aware that increasing this limit may produce issues if the
  clipboard contains large strings of text. The default limit is 100000
  characters.

Napomene:

*	Neće biti potrebno potvrditi, ako se neka NVDA poruka još uvijek
  prikazuje. U tim će se slučajevima radnje izvršavati odmah.
*	Emulate copy and emulate cut commands mean that, when these features are
  enabled, the add-on will take control of control+c and control+x. This
  will allow to select if a confirmation should be requested before
  performing the actions corresponding to these keystrokes.

## Promjene u verziji 13.0
* Fixed an issue in visual layout of the settings panel, thanks to Cyrille
  Bougot.
* Improved documentation.
* Added a Clip Contents Designer category to assign input gestures to all
  commands available for this add-on.
* Ispravljene su greške prilikom korištenja emulirajuće kopije u
  preglednicima ako je modus fokusa aktiviran.
* You can assign different gestures to show the clipboard textual contents
  as raw text or formatted in HTML. The Format to show the clipboard text in
  the settings panel has being modified accordingly, to select the two
  options available for HTML format.

## Promjene u verziji 12.0
* Ispravljene su greške prilikom korištenja emulirajuće kopije u programima
  poput LibreOffice Writer.

## Promjene u verziji 11.0
* Sada je moguće dodati tekst koji je označen preglednim kursorom, pomoću
  standardnih naredbi NVDA (NVDA+f9 i NVDA+f10). NVDA+windows+f9 se više ne
  koristi, radi boljw integracijw s novom naredbom NVDA+šift+f9.
* Zahtijeva NVDA verziju 2019.3 ili noviju.

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
  kontrol+c i kontrol+x.

## Promjene u verziji 6.0

*	Dodana je mogućnost za odluku o izvršavanju dostupnih radnji nakon potvrde.
*	Dodane su naredbe Simuliraj kopiranje i Simuliraj izrezivanje, koje je moguće dodijeliti u dijaloškom okviru Ulazne geste.
*	Dodan je dijaloški okvir za podešavanje naredbi Simuliraj kopiranje i Simuliraj izrezivanje, tijekom instaliranja. Ovo dozvoljava dodavanje naredbi kontrol+c i kontrol+x za kopiranje i izrezivanje, te postavljanjem pitanja, želiš li zamijeniti sadržaj međuspremnika pri korištenju ovih tipkovničkih prečaca.
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
