# Clip Contents Designer #
*   Autori: Noelia Ruiz Martínez.
*   Download [stable version][1]
*   Download [development version][2]

Questo componente aggiuntivo viene utilizzato per aggiungere il testo agli
appunti, il che può essere utile quando si desidera unire sezioni di testo
insieme per poi incollarlo. Il contenuto degli appunti può essere
cancellato.

## Comandi rapidi ##
*   NVDA+windows+c: Append selected text, Unicode braille characters which
    represent MathML objects, or the string which has been marked with the
    review cursor, to the clipboard.
*   NVDA + Windows + x: Cancella contenuto degli appunti.
*   NVDA + Windows + f9: Marca la posizione corrente del cursore di
    controllo come l'inizio del testo da aggiungere negli Appunti. Se si
    utilizza NVDA + F9, il testo non verrà aggiunto.

Nota: I comandi di cui sopra possono essere modificati dal menu di NVDA,
sottomenu Preferenze, gesti di immissione, categoria revisione del testo.

## Menu preferenze ##
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

## Changes for 2.0 ##
*   Hindi characters can be used as the separator between appended contents.

## Cambiamenti per 1.0 ##
*   Versione iniziale

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev
