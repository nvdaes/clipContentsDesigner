# Vágólap tartalomtervező #
*   - Készítők: Noelia Ruiz Martínez.  - Letöltés [Stabil verzió][1] -
    Letöltés [Fejlesztői verzió][2]
*   Letöltés [stabil verzió][1]
*   Letöltés [fejlesztői verzió][2]

This add-on is used to add text to the clipboard, which can be useful when
you want to join sections of text together ready for pasting.  The clipboard
content can also be cleared.

## Billentyűparancsok ##
*   NVDA+windows+c: Add selected text, Unicode braille characters which
    represent MathML objects, or the string which has been marked with the
    review cursor, to the clipboard.
*   NVDA+windows+x: Vágólap tartalom törlése.
*   NVDA+windows+f9: Mark the current position of the review cursor as the
    start of the text to be added to the clipboard.  If you use nvda+F9, the
    text will not be added.

- NVDA+control+shift+c: A kijelölt vagy az áttekintő kurzorral megjelölt
szöveg hozzáfűzése a vágólaphoz.  - NVDA+control+shift+x: A vágólap
tartalmának törlése.  - NVDA+control+f9: Beállítja az áttekintő kurzor
aktuális pontját kijelölés kezdetének.

## Beállítások menü ##
*   Clip Contents Designer settings: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
It's also possible to choose if the added text will be appended or prepended.

Megjegyzés: A fenti parancsok megváltoztathatóak az NVDA
menü->Beállítások->Beviteli parancsok ablakában a konfiguráció kategóriát
választva.

## Changes for 4.0 ##
*   Add-on settings are managed from NVDA configuration, so that standard
    profiles can be used to save different separators, and it's not needed
    to copy the settings for importing at reinstallation.
*   Now it's possible to choose if the added text will be appended or
    prepended, using the Add text before clip data check box from the Clip
    Contents Designer settings dialog.

## A 3.0 változásai ##
*   Braille representation of MathML objects can be added to the clipboard
    if MathPlayer is installed.
*   If no separator is set, just a single line will be placed between the
    added text segments.
*   Billentyűparancs került definiálásra a Vágolap tartalomtervező beállítás
    ablakának eléréséhez.
*   Hozzáadásra került egy jelölőnégyzet, mellyel szabályozható hogy az
    elválasztó karakter bemásolásra kerüljön-e a saját beállítások mappájába
    a későbbi importáláshoz.

## A 2.0 változásai ##
*   Hindi characters can be used as the separator between added contents.

## Az 1.0 változásai ##
*   - Első kiadás

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev
