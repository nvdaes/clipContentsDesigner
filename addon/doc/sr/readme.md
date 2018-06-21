# Dizajner sadržaja privremene memorije #

*	Autor: Noelia Ruiz Martínez.
*	preuzmi [stabilnu verziju][1]
*	preuzmi [verziju u razvoju][2]

Ovaj dodatak se koristi za dodavanje odvojenih delova teksta u privremenu
memoriju, što može biti korisno kada želite da pridružite više delova
teksta. a može i da ukloni sadržaj privremene memorije.

## Prečice ##
*	NVDA+Windows+c: Dodaje označeni tekst, brajevo predstavljanje MathML
  objekata ili tekst označen preglednim kursorom u privremenu memoriju.
*	NVDA+Windows+x: Uklanja sadržaj privremene memorije.
*	NVDA+windows+f9: Mark the current position of the review cursor as the start of the text to be added to the clipboard. If you use nvda+F9, the text will not be added.
*	 Not assigned: Copies to (or cuts from) the clipboard, with the possibility of being asked for a previous confirmation.

Napomena: Navedene komande možete pronaći i izmeniti kroz NVDA meni >
Podešavanja > Ulazne komande, pa zatim pronađite sekciju Pregled teksta.

## Podešavanja ##
*	Clip Contents Designer settings: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
It's also possible to choose if the added text will be appended or prepended, if available actions (add, clear clipboard, emulate copy and emulate cut) should be performed inmediately or after confirmation, and if confirmations will be requested just if text is contained in the clipboard.

Notes:

*	The above command can be changed from NVDA menu, Preferences submenu,
  Input gestures dialog, Configuration category.
*	Confirmations won't be requested when a message box of NVDA is still
  opened. In those cases, actions will be inmediately performed

## Changes for 8.0 ##

* The add-on settings are shown in the corresponding category of the NVDA
  Settings dialog.
* Requires NVDA 2018.2 or later.
* If needed, you can download the [last version compatible with NVDA
  2017.3][3].

## Changes for 7.0

* In the dialog to configure the Emulate copy and Emulate cut
  functionalities at installation, if you choose no, the commands for these
  features will be removed, so that you can restore the normal behavior for
  control+c and control+x.

## Changes for 6.0

*	 Added options to choose if available actions should be performed after confirmation.
*	Added Emulate copy and Emulate cut commands, which could be assigned from the Input gestures dialog.
*	 Added a dialog to configure the Emulate copy and Emulate cut functionalities at installation. This allows to add the control+c and control+x commands to copy and cut, and be asked if you want to replace the clipboard contents when pressing these keystrokes.
*	Fixed documentation for script_add (Windows+NVDA+c).

## Promene u 5.0 ##

*	Vizuelno predstavljanje dijaloga je poboljšano, slično dijalozima koji su
  prikazani u programu NVDA.
*	Zahteva NVDA 2016.4 ili noviji.

## Promene u 4.0 ##
*	Podešavanja dodatka upravljaju NVDA konfiguracijom, tako da možete
  koristiti standardne profile za čuvanje podešavanja, i ne morate da
  kopirate podešavanja nakon reinstalacije.
*	Sada je moguće izabrati da li će dodat tekst biti spojen ili prespojen,
  koristeći dodaj deo teksta pre podataka izborno polje u podešavanjima
  dodatka.

## Promene u 3.0 ##
*	Brajevo predstavljanje MathML objekata se može dodati u privremenu
  memoriju ako je MathPlayer instaliran.
*	Ako nema udvajača, samo jedan red će biti između dodatih segmenata.
*	‚Prečica može biti podešena za otvaranje dijaloga za podešavanja dodatka.
*	Dodat izborni okvir u dijalogu sa podešavanjima, za izbor da li će udvajač
  biti kopiran za ponovni uvoz nakon reinstalacije dodatka.

## Promene u 2.0 ##
*	Indijski karakteri mogu da se koriste kao odvajanje između dodatih delova
  teksta.

## Promene u 1.0 ##
*	Prva verzija.


[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev

[3]:
https://github.com/nvdaes/clipContentsDesigner/releases/download/7.2/clipContentsDesigner-7.2.nvda-addon
