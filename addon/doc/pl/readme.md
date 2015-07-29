# Projektant zawartości schowka / Clip Contents Designer #
*   Autorzy: Noelia Ruiz Martínez.
*   Pobierz [wersja stabilna][1]
*   Pobierz [wersja rozwojowa][2]

Ten dodatek pozwala dodawać tekst do schowka, co może być użyteczne, jeśli
chcesz połączyć razem kilka części tekstu w całość gotową do wklejenia.
Zawartość schowka może również być wyczyszczona.

## Skróty klawiszowe ##
*   NVDA+windows+c: Append selected text, Unicode braille characters which
    represent MathML objects, or the string which has been marked with the
    review cursor, to the clipboard.
*   NVDA+windows+x: wyczyść zawartość schowka.
*   NVDA+windows+f9: oznacz bieżącą pozycję kursora przeglądu jako początek
    tekstu, który zostanie dodany do schowka.  Jeśli użyjesz nvda+F9, tekst
    nie zostanie dodany.

Uwaga: powyższe polecenia mogą zostać zmienione z menu NVDA, Podmenu
Ustawienia, okno zdarzenia wejścia, kategoria przegląd tekstu.

## Menu ustawienia ##
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

## Zmiany w wersji 2.0 ##
*   Znaki Hindi mogą być używane jako separator dodawanej treści.

## Zmiany dla 1.0 ##
*   Pierwsze wydanie.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev
