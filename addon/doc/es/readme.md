# Clip Contents Designer #
*   Autores: Noelia Ruiz Martínez.
*   Descargar [versión estable][1]
*   Descargar [versión de desarrollo][2]

This add-on is used to add text to the clipboard, which can be useful when
you want to join sections of text together ready for pasting.  The clipboard
content can also be cleared.

## Órdenes de teclado ##
*   NVDA+windows+c: Add selected text, Unicode braille characters which
    represent MathML objects, or the string which has been marked with the
    review cursor, to the clipboard.
*   NVDA+windows+x: Limpia el contenido del portapapeles.
*   NVDA+windows+f9: Mark the current position of the review cursor as the
    start of the text to be added to the clipboard.  If you use nvda+F9, the
    text will not be added.

Nota: Las órdenes anteriores se pueden cambiar desde el menú NVDA, submenú
Preferencias, Diálogo Gestos de Entrada, Categoría Revisión de Texto.

## Menú Preferencias ##
*   Clip Contents Designer settings: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
It's also possible to choose if the added text will be appended or prepended.

Nota: La orden anterior puede cambiarse desde el menú NVDA, submenú
Preferencias, diálogo Gestos de Entrada, Categoría Configuración.

## Changes for 4.0 ##
*   Add-on settings are managed from NVDA configuration, so that standard
    profiles can be used to save different separators, and it's not needed
    to copy the settings for importing at reinstallation.
*   Now it's possible to choose if the added text will be appended or
    prepended, using the Add text before clip data check box from the Clip
    Contents Designer settings dialog.

## Cambios para 3.0 ##
*   Braille representation of MathML objects can be added to the clipboard
    if MathPlayer is installed.
*   If no separator is set, just a single line will be placed between the
    added text segments.
*   Se puede asignar un atajo de teclado para abrir el diálogo de Opciones
    de Clip Contents Designer.
*   Añadida una casilla de verificación en el diálogho de opciones, para
    elegir si el separador debería copiarse para importarse cuando se
    reinstale el complemento.

## Cambios para 2.0 ##
*   Hindi characters can be used as the separator between added contents.

## Cambios para 1.0 ##
*   Versión inicial.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev
