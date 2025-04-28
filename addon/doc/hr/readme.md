# Upravljanje sadržajem međuspremnika (Clip Contents Designer)

- Authors: Noelia, Abdel.

This add-on is used to add text to the clipboard, which can be useful when you want to join sections of text together ready for pasting.
The clipboard content can also be cleared an shown in browse mode.

## Tipkovnički prečaci

- NVDA+windows+c: U međuspremnik dodaj označeni tekst, brajične znakove u
  unikodu koji predstavljaju MathML objekte ili znakovni niz koji je označen
  pomoću preglednog kursora.
- NVDA+windows+x: Obriši sadržaj međuspremnika.
- Nije dodijeljeno: Kopira u međuspremnik (ili se reže iz njega), s
  mogućnošću da se prethodno od korisnika traži potvrda.
- Nije dodijeljeno: Prikazuje tekst međuspremnika u modusu čitanja ili
  najavljuje prazno stanje međuspremnika ili sadržaj koji se ne može
  predstaviti u pregledavajućoj poruci, na primjer ako su datoteke ili mape
  kopirane iz Windows Explorera.
- Nije dodijeljeno: Prikazuje tekstualni sadržaj međuspremnika kao običan
  tekst u modusu čitanja ili najavljuje prazno stanje međuspremnika ili
  sadržaj koji se ne može predstaviti u pregledavajućoj poruci, na primjer
  ako su datoteke ili mape kopirane iz Windows Explorer.

## Postavke dodatka „Upravljanje sadržajem međuspremnika”

Ova je ploča dostupna u NVDA izborniku, podizbornik Postavke, dijaloški
okvir Postavke.

Sadrži sljedeće kontrole:

- Upiši znakovni niz koji će se koristiti kao razdjeljivač između sadržaja
  koji su dodani u međuspremnik: Omogućuje postavljanje razdjeljivača koji
  se može koristiti za pronalaženje segmenata teksta nakon što je cijeli
  dodani tekst umetnut.
- Dodaj tekst prije podataka međuspremnika: Također je moguće odabrati, hoće
  li se dodani tekst umetnuti ispred ili iza.
- Select the actions which require previous confirmation: You can choose, for each action available, if it should be performed inmediately or after confirmation. Available actions are: add text, clear clipboard, emulate copy and emulate cut.
- Zatraži potvrdu prije izvođenja odabranih radnji: Možeš odabrati hoće li
  se potvrde zatražiti uvijek, samo ako se tekst nalazi u međuspremniku ili
  ako međuspremnik nije prazan (na primjer ako si kopirao/la datoteku, a ne
  tekst).
- Format to show the clipboard text as HTML in browse mode: If you're learning HTML markup language, you may choose Preformatted text in HTML or HTML as shown in a web browser, to have an idea of how your HTML code will be rendered by NVDA in a browser. The difference between preformatted and conventional HTML is that the first option will preserve consecutive spaces and line breaks, and the second one will compact them.  For example, write some HTML tags like h1, h2, li, pre, etc., select and copy the text to clipboard, and use clipContentsDesigner add-on to show the text in a browseable message.
- Maximum number of characters when showing clipboard text in browse mode: Please, be aware that increasing this limit may produce issues if the clipboard contains large strings of text. The default limit is 100000 characters.
- Obnovi standardne vrijednosti.

Napomene:

- Confirmations won't be requested when a message box of NVDA is still opened. In those cases, actions will be inmediately performed.
- Emulate copy and emulate cut commands mean that, when these features are enabled, the add-on will take control of control+c and control+x. This will allow to select if a confirmation should be requested before performing the actions corresponding to these keystrokes.

## Changes for 46.0.0

- NVDA will sanitize HTML in browseable messages.
- Added a button to close browseable messages, in addition to the Escape key.

## Changes for 40.0.0

- Added support for Hebrew keyboard.

## Promjene u verziji 17.0

- Kompatibilno s NVDA čitačem 2023.1.
- The add-on cannot be run in secure mode.

## Promjene u verziji 16.0

- Zahtijeva NVDA 2022.1 ili noviju verziju.

## Promjene u verziji 15.0

- Naredba za dodavanje teksta u međuspremnik ponovo se prikazuje u
  dijaloškom okviru gesta unosa.

## Promjene u verziji 14.0

- Kompatibilno s NVDA čitačem 2021.1.
- Fixed gestures to copy and cut with Persian keyboard, thanks to Mohammadhosein Ghezelsofla.

## Promjene u verziji 13.0

- Compatible with NVDA 2021.1.

## Promjene u verziji 12.0

- Ispravljene su greške prilikom korištenja emuliranja kopiranja u
  programima poput LibreOffice Writer.
- Improved documentation.
- Added a Clip Contents Designer category to assign input gestures to all commands available for this add-on.
- Fixed bugs when using emulate copy in browsers if focus mode is active.
- You can assign different gestures to show the clipboard textual contents as raw text or formatted in HTML. The Format to show the clipboard text in the settings panel has being modified accordingly, to select the two options available for HTML format.

## Promjene u verziji 11.0

- Fixed bugs when using emulate copy in applications like LibreOffice Writer.

## Promjene u verziji 10.0

- Now it's possible to add text marked with the review cursor using standard commands of NVDA (NVDA+f9 and NVDA+f10). NVDA+windows+f9 is no longer used, for a better integration with the new NVDA+shift+f9 command.
- Requires NVDA 2019.3 or later.

## Promjene u verziji 9.0

- Dodana je mogućnost prikazivanja teksta međuspremnika u modusu čitanja.
- Fixed a bug when using the emulate cut and copy features with an Arabic keyboard layout. This has been fixed by Abdel, added as an add-on author.

## Promjene u verziji 8.0

- Postavke dodatka se prikazuju u odgovarajućoj kategoriji dijaloškog okvira
  za NVDA Postavke.
- Zahtijeva NVDA verziju 2018.2 ili noviju.
- Requires NVDA 2018.4 or later.

## Promjene u verziji 7.0

- Ako se u dijaloškom okviru za konfiguriranje funkcionalnosti „Emuliraj
  kopiranje” i „Emuliraj izrezivanje” odabere „ne”, naredbe za ove funkcije
  će se ukloniti kako bi se omogućio normalni način rada za kontrol+c i
  kontrol+x.
- Requires NVDA 2018.2 or later.

## Promjene u verziji 6.0

- Dodane su opcije s kojima se može odlučiti je li se dostupne radnje
  trebaju izvršiti nakon potvrde.

## Promjene u verziji 5.0

- Vizualni prikaz dijaloških okvira je poboljašn, slično dijaloškim okvirima
  koji su prikazani u programu NVDA.
- Zahtijeva NVDA verziju 2016.4 ili noviju.
- Added a dialog to configure the Emulate copy and Emulate cut functionalities at installation. This allows to add the control+c and control+x commands to copy and cut, and be asked if you want to replace the clipboard contents when pressing these keystrokes.
- Fixed documentation for script_add (Windows+NVDA+c).

## Promjene u verziji 4.0

- Postavkama dodatka se upravlja NVDA konfiguracijom, tako da je moguće
  koristiti standardne profile za spremanje raznih rastavljača te nije
  potrebno kopirati postavke nakon reinstalacije.
- Sad je moguće izabrati, hoće li dodani tekst biti dodan ispred ili iza
  postojećeg teksta, koristeći izborno polje „Dodaj tekst ispred podataka
  međuspremnika” u postavkama dodatka.

## Promjene u verziji 3.0

- Brajičin prikaz MathML objekata se može dodati u privremenu memoriju, ako
  je MathPlayer instaliran.
- Ako nema razdvajača, dodat će se samo jedan redak između dodanih segmenata
  teksta.

## Promjene u verziji 2.0

- Znakovi devanagari pisma se mogu koristiti kao rastavljači između dodanog
  sadržaja.
- If no separator is set, just a single line will be placed between the added text segments.
- A shortcut can be assigned to open the Clip Contents Designer settings dialog.
- Added a check box in the settings dialog, for choosing if the separator should be copied to be imported when reinstalling the add-on.

## Promjene u verziji 1.0

- Prva verzija.

## Changes for 1.0

- Initial version.
