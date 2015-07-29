# Samensteller voor klembordinhoud #
*   Auteurs: Noelia Ruiz Martínez.
*   Download [stabiele versie][1]
*   Download [ontwikkelversie][2]

Deze add-on kan gebruikt worden om tekst toe te voegen achteraan het
klembord, wat handig kan zijn als u bepaalde tekstgedeelten vòòr het plakken
samen wilt voegen. De inhoud van het klembord kan daarnaast ook gewist
worden.

## Toetsenbordsneltoetsen ##
*   NVDA+windows+c: Append selected text, Unicode braille characters which
    represent MathML objects, or the string which has been marked with the
    review cursor, to the clipboard.
*   NVDA+windows+x: Inhoud van klembord wissen.
*   NVDA+windows+F9: Markeer de huidige positie van de leescursor als het
    begin van de tekst die achteraan het klembord moet worden
    toegevoegd. Als u NVDA+F9 gebruikt, wordt de tekst niet achteraan
    toegevoegd maar wordt de bestaande inhoud van het klembord eerst gewist.

Opmerking: De bovenstaande commando's kunnen worden gewijzigd via het
NVDA-menu, Opties submenu, Invoerhandelingen koppelen dialoogvenster,
Leesoverzicht categorie.

## Menu opties ##
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

## Veranderingen in 2.0 ##
*   Tekens uit het Hindi kunnen nu gebruikt worden als scheidingsteken
    tussen toegevoegde inhoud.

## Veranderingen in 1.0 ##
*   Eerste versie.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev
