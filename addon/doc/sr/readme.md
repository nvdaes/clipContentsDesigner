# Dizajner sadržaja privremene memorije #

*	Authors: Noelia, Abdel.
*	NVDA compatibility: 2019.3 or later
*	preuzmi [stabilnu verziju][1]
*	preuzmi [verziju u razvoju][2]


This add-on is used to add text to the clipboard, which can be useful when
you want to join sections of text together ready for pasting.  The clipboard
content can also be cleared an shown in browse mode.

## Prečice ##

* NVDA+Windows+c: Dodaje označeni tekst, brajevo predstavljanje MathML
  objekata ili tekst označen preglednim kursorom u privremenu memoriju.
* NVDA+Windows+x: Uklanja sadržaj privremene memorije.
* Not assigned: Copies to (or cuts from) the clipboard, with the possibility
  of being asked for a previous confirmation.
* Not assigned: Shows the clipboard text in browse mode, or announces if
  clipboard is empty or has contents which can't be presented in a
  browseable message, for instance if files or folders are been copied from
  Windows Explorer.

Napomena: Navedene komande možete pronaći i izmeniti kroz NVDA meni >
Podešavanja > Ulazne komande, pa zatim pronađite sekciju Pregled teksta.

## Podešavanja ##
*	Clip Contents Designer settings: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
It's also possible to choose if the added text will be appended or prepended, if available actions (add, clear clipboard, emulate copy and emulate cut) should be performed inmediately or after confirmation, and if confirmations will be requested always, just if text is contained in the clipboard, or if clipboard is not empty.
Furthermore, it's possible to change the format and maximum number of characters of the clipboard text which will be shown in browse mode. Please, be aware that increasing this limit may produce issues if the clipboard contains large strings of text. The default limit is 100000 characters.

Notes:

*	The above command can be changed from NVDA menu, Preferences submenu,
  Input gestures dialog, Configuration category.
*	Confirmations won't be requested when a message box of NVDA is still
  opened. In those cases, actions will be inmediately performed.

## Changes for 12.0
* Fixed bugs when using emulate copy in applications like LibreOffice
  Writer.

## Changes for 11.0
* Now it's possible to add text marked with the review cursor using standard
  commands of NVDA (NVDA+f9 and NVDA+f10). NVDA+windows+f9 is no longer
  used, for a better integration with the new NVDA+shift+f9 command.
* Requires NVDA 2019.3 or later.

## Changes for 10.0
* Fixed a bug in the dialog used to show the clipboard text, when its title
  contains non latin characters.
* Fixed a bug when using the emulate cut and copy features with an Arabic
  keyboard layout. This has been fixed by Abdel, added as an add-on author.

## Changes for 9.0

* Added the possibility of showing the clipboard text in browse mode.
* Added an option to choose if confirmations will be required if clipboard
  is not empty, for instance, if files or folders are been copied.
* Requires NVDA 2018.4 or later.

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

[1]: https://addons.nvda-project.org/files/get.php?file=ccd

[2]: https://addons.nvda-project.org/files/get.php?file=ccd-dev

[3]: https://addons.nvda-project.org/files/get.php?file=ccd-o
