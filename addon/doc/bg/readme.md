# Clip Contents Designer (Дизайнер за Съдържанието на Клипборда) #
*   Автори: Noelia Ruiz Martínez.
*   Изтегляне [стабилна версия][1]
*   Изтегляне [работна версия][2]

This add-on is used to add text to the clipboard, which can be useful when
you want to join sections of text together ready for pasting.  The clipboard
content can also be cleared.

## Клавиатурни команди ##
*   NVDA+windows+c: Add selected text, Unicode braille characters which
    represent MathML objects, or the string which has been marked with the
    review cursor, to the clipboard.
*   NVDA+Windows+X: Изчистване на съдържанието на клипборда.
*   NVDA+windows+f9: Mark the current position of the review cursor as the
    start of the text to be added to the clipboard.  If you use nvda+F9, the
    text will not be added.

Забележка: Командите от по-горе може да бъдат променени от менюто на NVDA
подменю Настройки, диалога Жестове на въвеждане, категория Преглед на
текста.

## Меню с настройките ##
*   Clip Contents Designer settings: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
It's also possible to choose if the added text will be appended or prepended.

Забележка: Командата от по-горе може да бъде променена от менюто на NVDA,
подменю Настройки, диалога Жестове на въвеждане, категория Настройки.

## Changes for 4.0 ##
*   Add-on settings are managed from NVDA configuration, so that standard
    profiles can be used to save different separators, and it's not needed
    to copy the settings for importing at reinstallation.
*   Now it's possible to choose if the added text will be appended or
    prepended, using the Add text before clip data check box from the Clip
    Contents Designer settings dialog.

## Промени във версия 3.0 ##
*   Braille representation of MathML objects can be added to the clipboard
    if MathPlayer is installed.
*   If no separator is set, just a single line will be placed between the
    added text segments.
*   Може да бъде зададен бърз клавиш за отваряне на прозореца с настройките
    на Clip Contents Designer.
*   В диалоговия прозорец с настройките е добавено поле за отметка за избор
    дали разделителят да бъде копиран за импортиране при преинсталиране на
    добавката.

## Промени във версия 2.0 ##
*   Hindi characters can be used as the separator between added contents.

## Промени във версия 1.0 ##
*   Първоначално издание.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev
