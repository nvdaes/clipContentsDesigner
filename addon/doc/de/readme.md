# Designer für die Zwischenablage #

*	Autoren: Noelia Ruiz Martínez, Abdel.
*	NVDA-Kompatibilität: 2018.4 bis 2019.2.
*	[Stabile Version herunterladen][1]
*	[Entwicklerversion herunterladen][2]

Diese Erweiterung kann verwendet werden, um Text zur Zwischenablage
hinzuzufügen. Dies kann beispielsweise beim Zusammenfügen von verschiedenen
Textabschnitten nützlich sein. Der Inhalt der Zwischenablage kann auch
gelöscht werden.

## Tastenkombinationen ##
*	NVDA+Windows+C: Fügt den ausgewählten Text, MathML-Objekte als
  Unicode-Punktschriftzeichen oder die Zeichenkette, die mit dem Lese-Cursor
  markiert wurde, in die Zwischenablage hinzu.
*	NVDA+windows+X: Löscht die Zwischenablage.
*	NVDA+Windows+F9: Markiert die aktuelle Position des Lese-Cursors als Anfang des Textes, der in die Zwischenablage eingefügt werden soll. Wenn Sie nvda+F9 verwenden, wird der Text nicht hinzugefügt.
*	Nicht zugeordnet: Kopien in die Zwischenablage (oder Ausschnitte aus der Zwischenablage) mit einer Bestätigungsabfrage einfügen oder entfernen.

Anmerkung: Die obigen Befehle können im NVDA-Menü unter Einstellungen /
Eingaben... in der Kategorie "Befehle zum Text betrachten" geändert werden.

## Einstellungen ##
*	Einstellungen des Designers für den inhalt der Zwischenablage: hier kann ein Trennzeichen zum leichteren Auffinden von Textsegmenten gesetzt werden, sobald der gesamte Text zur Zwischenablage eingefügt wurde. Es kann auch gewählt werden, ob der hinzugefügte Text angehängt oder vorangestellt wird, ob verfügbare Aktionen (Hinzufügen, Löschen der Zwischenablage, Kopieren und Ausschneiden emulieren) sofort oder nach Bestätigung ausgeführt werden sollen und ob Bestätigungen nur bei vorhandenem Text in der Zwischenablage ausgegeben werden.

Anmerkungen:

*	Der obige Befehl kann im NVDA-Menü unter Einstellungen / Eingaben in der
  Kategorie "Konfiguration" geändert werden.
*	Bestätigungen werden nicht angefordert, wenn ein Meldungsfenster von NVDA
  noch geöffnet ist. In diesem Fall werden die Aktionen sofort ausgeführt

## Änderungen in 10.0
* Es wurde ein Fehler in dem Dialog behoben, der verwendet wurde, um den
  Text der Zwischenablage anzuzeigen, wenn sein Titel nicht-lateinische
  Zeichen enthält.
* Ein Fehler wurde behoben, der bei der Verwendung der emulierten Funktionen
  zum Ausschneiden und Kopieren mit einem arabischen Tastaturlayout
  auftrat. Dies wurde von Abdel behoben, der als zusätzlichen Autor dieser
  Erweiterung nun hinzugefügt wurde.

## Änderungen in 9.0

* Es wurde die Möglichkeit hinzugefügt, den Text der Zwischenablage im
  Lesemodus anzuzeigen.
* Es wurde eine Option hinzugefügt, um zu wählen, ob Bestätigungen
  erforderlich sind, wenn die Zwischenablage nicht leer ist, z.B. wenn
  Dateien oder Ordner kopiert wurden.
* Benötigt NVDA 2018.4 oder höher.

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
*	Erstveröffentlichung.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ccd

[2]: https://addons.nvda-project.org/files/get.php?file=ccd-dev

[3]: https://addons.nvda-project.org/files/get.php?file=ccd-o
