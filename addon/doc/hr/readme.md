# Clip Contents Designer dodaj tekst u međuspremnik #
*   Autor: Noelia Ruiz Martínez.
*   Preuzmi [stabilnu inačicu][1]
*   Preuzmi [razvojnu inačicu][2]

Ovaj se dodatak koristi kako bi se tekst mogao dodati u međuspremnik, što
može biti korisno kada želite zajedno spojiti dijelove teksta koji su
spremni za lijepljenje. Sadržaj međuspremnika također se može izbrisati.

## Tipkovnički prečaci ##
*   NVDA+windows+c: Append selected text, Unicode braille characters which
    represent MathML objects, or the string which has been marked with the
    review cursor, to the clipboard.
*   NVDA+windows+x: Obriši sadržaj međuspremnika.
*   NVDA+windows+f9: Označi trenutnu poziciju preglednog kursora kao početak
    teksta koji treba biti dodan u međuspremnik. Ako koristite NVDA+F9,
    tekst neće biti dodan.

Napomena: Prečaci iznad mogu se promijeniti iz NVDA izbornika, podizbornika
postavke, dijaloškog okvira ulazne geste kategoria pregled teksta.

## Podizbornik postavke ##
*   Clip Contents Designer settings: Allows to set a separator which can be
    used to find the text segments once the entire appended text is
    pasted. You can also choose if the separator should be copied to your
    personal NVDA's configuration folder, so that it can be imported when
    reinstalling the add-on.

Note: The above command can be changed from NVDA menu, Preferences submenu,
Input gestures dialog, Configuration category.

## Changes for 3.0 ##
*   Braille representation of MathML objects can be appended to the
    clipboard if MathPlayer is installed.
*   If no separator is set, just a single line will be placed between the
    appended text segments.
*   A shortcut can be assigned to open the Clip Contents Designer settings
    dialog.
*   Added a check box in the settings dialog, for choosing if the separator
    should be copied to be imported when reinstalling the add-on.

## izmjene u inačici 2.0 ##
*   znakovi devanagari pisma mogu se koristiti kao rastavljači između
    dodanog sadržaja.

## Promjene u inačici1.0 ##
*   Prva inačica.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev
