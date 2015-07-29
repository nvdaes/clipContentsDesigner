# Dizajner sadržaja privremene memorije #
*   Autor: Noelia Ruiz Martínez.
*   preuzmi [stabilnu verziju][1]
*   preuzmi [verziju u razvoju][2]

Ovaj dodatak se koristi za dodavanje odvojenih delova teksta u privremenu
memoriju, a može i da ukloni sadržaj privremene memorije.

## Prečice ##
*   NVDA+windows+c: Append selected text, Unicode braille characters which
    represent MathML objects, or the string which has been marked with the
    review cursor, to the clipboard.
*   NVDA+Windows+x: Uklanja sadržaj privremene memorije.
*   NVDA+Windows+F9: Označava trenutnu poziciju preglednog kursora kao
    početak teksta za kopiranje u privremenu memoriju.  Ako upotrebite
    NVDA+F9, tekst neće biti dodat.

Napomena: Navedene komande možete pronaći i izmeniti kroz NVDA meni >
Podešavanja > Ulazne komande, pa zatim pronađite sekciju Pregled teksta.

## Podešavanja ##
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

## Promene u 2.0 ##
*   Hindi karakteri mogu da se koriste kao odvajanje između dodatih delova
    teksta.

## Promene u 1.0 ##
*   Prva verzija.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev
