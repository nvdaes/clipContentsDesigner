# Clip Contents Designer #
*   Autor: Noelia Ruiz Martínez.
*   Stiahnuť [stabilná verzia][1]
*   Stiahnuť [vývojovú verziu][2]

Tento doplnok využijete, ak chcete do schránky Windows postupne vkladať
rôzne časti textu a výsledok naraz prilepiť. Doplnok vie tiež vyčistiť obsah
schránky.

## Klávesové skratky ##
*   NVDA+windows+c: Append selected text, Unicode braille characters which
    represent MathML objects, or the string which has been marked with the
    review cursor, to the clipboard.
*   NVDA+windows+x: vymaže obsah schránky.
*   NVDA+windows+F9: označí aktuálnu pozíciu prezeracieho kurzora ako
    začiatok textu, ktorý bude pripojený do schránky. Ak namiesto toho
    použijete nvda+F9, text nebude pripojený, ale nahradí aktuálny obsah
    schránky.

Tieto skratky môžete zmeniť z menu NVDA >možnosti > klávesové skratky,
kategória prezeranie textu.

## Možnosti ##
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

## Zmeny vo verzii 2.0 ##
*   Znaky v jazyku Hindi môžu byť použité na oddelenie častí schránky.

## Zmeny vo verzii 1.0 ##
*   prvé vydanie.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev
