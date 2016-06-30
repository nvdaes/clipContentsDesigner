# Clip Contents Designer #
*   Forfattere: Noelia Ruiz Martínez.
*   Download [stabil version][1]
*   Download [udviklingsversion][2]

This add-on is used to add text to the clipboard, which can be useful when
you want to join sections of text together ready for pasting.  The clipboard
content can also be cleared.

## Tastaturkommandoer ##
*   NVDA+windows+c: Add selected text, Unicode braille characters which
    represent MathML objects, or the string which has been marked with the
    review cursor, to the clipboard.
*   NVDA+Windows+x: Ryd udklipsholderen.
*   NVDA+windows+f9: Mark the current position of the review cursor as the
    start of the text to be added to the clipboard.  If you use nvda+F9, the
    text will not be added.

Bemærk: Kommandoerne ovenfor kan ændres fra NVDA-menuen / Indstillinger /
Inputbevægelser / kategorien tekstlæsning.

## Indstillinger-menuen ##
*   Clip Contents Designer settings: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
It's also possible to choose if the added text will be appended or prepended.

Bemærk: Denne kommando kan ændres under NVDA-menu / Indstillinger /
Inputbevægelser / kategorien Indstillinger.

## Changes for 4.0 ##
*   Add-on settings are managed from NVDA configuration, so that standard
    profiles can be used to save different separators, and it's not needed
    to copy the settings for importing at reinstallation.
*   Now it's possible to choose if the added text will be appended or
    prepended, using the Add text before clip data check box from the Clip
    Contents Designer settings dialog.

## Ændringer i 3.0 ##
*   Braille representation of MathML objects can be added to the clipboard
    if MathPlayer is installed.
*   If no separator is set, just a single line will be placed between the
    added text segments.
*   Der kan knyttes en genvejstast til at åbne dialogen Indstillinger for
    Clip Contents Designer.
*   Tilføjede en checkboks i Indstillinger-dialogen til at vælge, om
    separatoren skal kopieres, så den kan importeres, når
    tilføjelsesprogrammet bliver geninstalleret.

## Ændringer i 2.0 ##
*   Hindi characters can be used as the separator between added contents.

## Ændringer i 1.0 ##
*   Første version.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev
