# Zwischenablagendesigner #

*	Autor: Noelia Ruiz Martínez
*	NVDA-Kompatibilität: 2018.2 bis 2019.1
*	[Stabile Version herunterladen][1]
*	[Entwicklerversion herunterladen][2]

This add-on is used to add text to the clipboard, which can be useful when
you want to join sections of text together ready for pasting.  The clipboard
content can also be cleared an shown in browse mode.

## Tastenkombinationen ##
*	NVDA+Windows+C: Fügt den ausgewählten Text, MathML-Objekte als
  Unicode-Punktschriftzeichen oder die Zeichenkette, die mit dem Lese-Cursor
  markiert wurde, in die Zwischenablage hinzu.
*	NVDA+windows+X: Löscht die Zwischenablage.
*	NVDA+windows+f9: Mark the current position of the review cursor as the start of the text to be added to the clipboard. If you use nvda+F9, the text will not be added.
*	 Not assigned: Copies to (or cuts from) the clipboard, with the possibility of being asked for a previous confirmation.
*	 Not assigned: Shows the clipboard text in browse mode, or announces if clipboard is empty or has contents which can't be presented in a browseable message, for instance if files or folders are been copied from Windows Explorer..

Anmerkung: Die obigen Befehle können im NVDA-Menü unter Einstellungen /
Eingaben... in der Kategorie "Befehle zum Text betrachten" geändert werden.

## Einstellungen ##
*	Clip Contents Designer settings: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
It's also possible to choose if the added text will be appended or prepended, if available actions (add, clear clipboard, emulate copy and emulate cut) should be performed inmediately or after confirmation, and if confirmations will be requested always, just if text is contained in the clipboard, or if clipboard is not empty.
Furthermore, it's possible to change the format and maximum number of characters of the clipboard text which will be shown in browse mode. Please, be aware that increasing this limit may produce issues if the clipboard contains large strings of text. The default limit is 100000 characters.

Anmerkungen:

*	Der obige Befehl kann im NVDA-Menü unter Einstellungen / Eingaben in der
  Kategorie "Konfiguration" geändert werden.
*	Bestätigungen werden nicht angefordert, wenn ein Meldungsfenster von NVDA
  noch geöffnet ist. In diesem Fall werden die Aktionen sofort ausgeführt.

## Changes for 9.0

* Added the possibility of showing the clipboard text in browse mode.
* Added an option to choose if confirmations will be required if clipboard
  is not empty, for instance, if files or folders are been copied.
* Requires NVDA 2018.4 or later.

## Änderungen in 8.0 ##

* Die Einstellungen für die Erweiterung werden in der entsprechenden
  Kategorie der Einstellungen von NVDA angezeigt.
* Benötigt NVDA 2018.2 oder höher.
* Bei Bedarf können Sie die [letzte Version, die mit NVDA 2017.3 kompatibel
  ist][3] herunterladen.

## Änderungen in 7.0

* Die Befehle im Dialog zum Konfigurieren der Funktionen für das Emulieren
  der Kopier- und Ausschneide-Funktion  werden bei der Installation
  entfernt, so dass das normale Verhalten von Strg+C und Strg+X
  wiederhergestellt werden kann.

## Änderungen in 6.0

*	Optionen für verfügbare Aktionen nach der Ausführung einer Bestätigung  wurden hinzugefügt.
*	Befehle für das Kopieren und Ausschneiden emulieren sind nun vorhanden. Diese können im NVDA-Menü im Bereich "Eingaben..." angepasst werden.
*	Es wurde ein Dialog hinzugefügt, um die Funktionen Kopieren und Ausschneiden emulieren bei der Installation anzupassen. Dies erlaubt es, die Befehle Strg+C und Strg+X zum Kopieren und Ausschneiden hinzuzufügen. Die Bestätigungsmeldung, ob Sie den Inhalt der Zwischenablage ersetzen möchten, kann hier umgeschaltet werden.
*	Die Dokumentation für script_add (Windows+NVDA+C) wurde korrigiert.

## Änderungen in 5.0 ##

*	Die visuelle Darstellung des Dialogs wurde verbessert und entspricht dem
  Erscheinungsbild der Dialoge in NVDA.
*	Benötigt NVDA 2016.4 oder höher.

## Änderungen in 4.0 ##
*	Erweiterungseinstellungen werden von der NVDA-Konfiguration verwaltet, so
  dass Standardprofile verwendet werden können, um verschiedene Trennlinien
  zu speichern. Es ist nicht erforderlich, die Einstellungen für den Import
  bei der Neuinstallation zu kopieren.
*	Es kann nun gewählt werden, ob der hinzugefügte Text angehängt oder
  vorangestellt werden soll, indem Sie das Kontrollkästchen Text vor den
  Daten der Zwischenablage hinzufügen im Einstellungsdialog der Erweiterung
  verwenden.

## Änderungen in 3.0 ##
*	Braille-Darstellung von MathML-Objekten können bei installiertem
  MathPlayer zur Zwischenablage kopiert oder ausgeschnitten werden.
*	Wenn kein Trennzeichen gesetzt ist, wird nur eine einzige Linie zwischen
  den angehängten Textsegmenten platziert.
*	Sie können ein Tastenkürzel zum Öffnen des Einstellungsdialogs zuweisen.
*	Es wurde ein Kontrollkästchen im Einstellungsdialog hinzugefügt, mit dem
  festgelegt wird, ob die Trennlinie beim erneuten Installieren der
  Erweiterung für den Import kopiert werden soll.

## Änderungen in 2.0 ##
*	Indische Zeichen können nun als Trennzeichen zwischen kopierten Inhalten
  verwendet werden.

## Änderungen in 1.0 ##
*	Erstveröffentlichung



[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ccd

[2]: https://addons.nvda-project.org/files/get.php?file=ccd-dev

[3]: https://addons.nvda-project.org/files/get.php?file=ccd-o
