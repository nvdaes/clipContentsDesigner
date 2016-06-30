# Clip Contents Designer #
*   Autori: Noelia Ruiz Martínez.
*   Download [stable version][1]
*   Download [development version][2]

This add-on is used to add text to the clipboard, which can be useful when
you want to join sections of text together ready for pasting.  The clipboard
content can also be cleared.

## Comandi rapidi ##
*   NVDA+windows+c: Add selected text, Unicode braille characters which
    represent MathML objects, or the string which has been marked with the
    review cursor, to the clipboard.
*   NVDA + Windows + x: Cancella contenuto degli appunti.
*   NVDA+windows+f9: Mark the current position of the review cursor as the
    start of the text to be added to the clipboard.  If you use nvda+F9, the
    text will not be added.

Nota: I comandi di cui sopra possono essere modificati dal menu di NVDA,
sottomenu Preferenze, gesti di immissione, categoria revisione del testo.

## Menu preferenze ##
*   Clip Contents Designer settings: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
It's also possible to choose if the added text will be appended or prepended.

Nota: Il comando di cui sopra può essere modificato dal menu di NVDA,
sottomenu Preferenze, gesti di immissione, categoria Configurazione

## Changes for 4.0 ##
*   Add-on settings are managed from NVDA configuration, so that standard
    profiles can be used to save different separators, and it's not needed
    to copy the settings for importing at reinstallation.
*   Now it's possible to choose if the added text will be appended or
    prepended, using the Add text before clip data check box from the Clip
    Contents Designer settings dialog.

## Cambiamenti per 3.0 ##
*   Braille representation of MathML objects can be added to the clipboard
    if MathPlayer is installed.
*   If no separator is set, just a single line will be placed between the
    added text segments.
*   Può essere assegnato un tasto caldo per aprire la finestra impostazioni
    di Clip Contents Designer 
*   Aggiunta una casella di controllo nella finestra di dialogo, per
    selezionare se il separatore debba essere copiato per poi essere
    importato in caso di nuova installazione del componente aggiuntivo.

## Cambiamenti per 2.0 ##
*   Hindi characters can be used as the separator between added contents.

## Cambiamenti per 1.0 ##
*   Versione iniziale

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev
