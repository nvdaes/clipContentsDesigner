# Designer für den Inhalt der Zwischenablage  #
*   Autoren: Noelia Ruiz Martínez.
*   [stabile Version herunterladen][1]
*   [Entwicklerversion herunterladen][2]

Diese Erweiterung kann verwendet werden, um mehrere Textteile
zusammenzufügen und in der Zwischenablage zu speichern. Das Löschen der
Zwischenablage ist ebenfalls möglich.

## Tastenkombinationen ##
*   NVDA+windows+c: Append selected text, Unicode braille characters which
    represent MathML objects, or the string which has been marked with the
    review cursor, to the clipboard.
*   NVDA+windows+x: löscht die Zwischenablage
*   NVDA+windows+f9: Setzt eine Startmarke an der aktuellen Position des
    NVDA-Cursors. Wenn Sie nvda+f9 zum Setzen der Startmarke verwenden, wird
    kein Text an die Zwischenablage angefügt.

Anmerkung: die obigen Befehle können im NVDA-Menü unter
Einstellungen/eingaben in der Kategorie Befehle zum Betrachten von Text
geändert werden.

## Einstellungen ##
*   Einstellungen für den Designer des Zwischenablagen-Inhaltes: Hier können
    Sie ein Trennzeichen einstellen, das verwendet wird, um die einzelnen
    Segmente voneinander zu trennen, wenn Sie den Inhalt der Zwischenablage
    in ein Dokument einfügen. Sie können auch festlegen, dass das
    Trennzeichen in Ihre persönlichen Einstellungsverzeichnis von NVDA
    kopiert werden soll, so dass es wieder importiert werden kann, wenn die
    Erweiterung neu installiert wird.

Anmerkung: der obige Befehl kann im NVDA-Menü unter Einstellungen/eingaben
in der Kategorie Konfiguration geändert werden.

## Änderungen in Version 3.0 ##
*   Braille representation of MathML objects can be appended to the
    clipboard if MathPlayer is installed.
*   Wenn kein Trennzeichen gesetzt ist, wird nur eine einzige Linie zwischen
    den angehängten Textsegmente platziert werden.
*   A shortcut can be assigned to open the Clip Contents Designer settings
    dialog.
*   Added a check box in the settings dialog, for choosing if the separator
    should be copied to be imported when reinstalling the add-on.

## Änderungen in Version 2.0 ##
*   Indische Zeichen können nun als Trennzeichen zwischen kopierten Inhalten
    verwendet werden.

## Änderungen in Version 1.0 ##
*   anfängliche Version

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev
