# Clip Contents Designer #

*	Autor: Noelia Ruiz Martínez.
*	[stabile Version herunterladen][1]
*	[Entwicklerversion herunterladen][2]

Diese Erweiterung kann verwendet werden, um Text zur Zwischenablage
hinzuzufügen. Dies kann beispielsweise beim Zusammenfügen von verschiedenen
Textabschnitten nützlich sein.  Der Inhalt der Zwischenablage kann auch
gelöscht werden.

## Tastenkombinationen ##
*	NVDA+Windows+c: Fügt den ausgewählten Text, MathML-Objekte als
  Unicode-Punktschriftzeichen oder die Zeichenkette, die mit dem Lese-Cursor
  markiert wurde, in die Zwischenablage ein.
*	NVDA+windows+x: löscht die Zwischenablage
*	NVDA+Windows+f9: Markiert die aktuelle Position des Lese-Cursors als Anfang des Textes, der in die Zwischenablage eingefügt werden soll. Wenn Sie nvda+F9 verwenden, wird der Text nicht hinzugefügt. 
*	 Nicht zugeordnet: Kopien in die Zwischenablage (oder Ausschnitte aus der Zwischenablage) mit einer Bestätigungsabfrage einfügen oder entfernen. 

Anmerkung: die obigen Befehle können im NVDA-Menü unter
Einstellungen/eingaben in der Kategorie Befehle zum Betrachten von Text
geändert werden.

## Einstellungen ##
*	 Einstellungen des Designers für den inhalt der Zwischenablage: hier kann ein Trennzeichen zum leichteren Auffinden von Textsegmenten gesetzt werden, sobald der gesamte Text zur Zwischenablage eingefügt wurde. Es kann auch gewählt werden, ob der hinzugefügte Text angehängt oder vorangestellt wird, ob verfügbare Aktionen (Hinzufügen, Löschen der Zwischenablage, Kopieren und Ausschneiden emulieren) sofort oder nach Bestätigung ausgeführt werden sollen und ob Bestätigungen nur bei vorhandenem Text in der Zwischenablage ausgegeben werden. 

Anmerkungen:

*	Der obige Befehl kann im NVDA-Menü unter Einstellungen/eingaben in der
  Kategorie Konfiguration geändert werden.
*	Bestätigungen werden nicht angefordert, wenn ein Meldungsfenster von NVDA
  noch geöffnet ist. In diesen Fällen werden die Aktionen sofort ausgeführt

## Änderungen für 8.0 ##

* Die Einstellungen für die Erweiterung werden in der entsprechenden
  Kategorie des NVDA-Einstellungensdialog angezeigt.
* Benötigt NVDA 2018.2 oder höher.
* Bei Bedarf können Sie die [letzte Version, die mit NVDA 2017.3 kompatibel
  ist][3] herunterladen.

## Änderungen in Version 7.0

* Die Befehle im Dialog zum Konfigurieren der Funktionen für das Emulieren
  der Kopier- und Ausschneide-Funktion  werden bei der Installation
  entfernt, so dass das normale Verhalten von STRG+c und STRG+x
  wiederhergestellt werden kann.

## Änderungen in Version 6.0

*	 Optionen für verfügbare Aktionen nach der Ausführung einer Bestätigung  wurden hinzugefügt. 
*	 Befehle für das Kopieren und Ausschneiden emulieren sind nun vorhanden. Diese können im NVDA-Menü im Bereich Eingaben angepasst werden. 
*	 Es wurde ein Dialog hinzugefügt, um die Funktionen Kopieren und Ausschneiden emulieren bei der Installation anzupassen. Dies erlaubt es, die Befehle control+c und control+x zum Kopieren und Ausschneiden hinzuzufügen. Die Bestätigungsmeldung, ob Sie den Inhalt der Zwischenablage ersetzen möchten, kann hier aus und eingeschaltet werden. 
*	 Die Dokumentation für script_add (Windows+NVDA+c) wurde korrigiert. 

## Änderungen in Version 5.0 ##

*	Die visuelle Darstellung des Dialogs wurde verbessert und entspricht dem
  Erscheinungsbild der Dialoge in NVDA.
*	Benötigt NVDA 2016.4 oder höher.

## Änderungen in Version 4.0 ##
*	Erweiterungseinstellungen werden von der NVDA-Konfiguration verwaltet, so
  dass Standardprofile verwendet werden können, um verschiedene Separatoren
  zu speichern. Es ist nicht erforderlich, die Einstellungen für den Import
  bei der Neuinstallation zu kopieren.
*	Es kann nun gewählt werden, ob der hinzugefügte Text angehängt oder
  vorangestellt wird, indem Sie das Kontrollkästchen Text vor den Daten der
  Zwischenablage hinzufügen im Einstellungsdialog des Clip Contents Designer
  verwenden.

## Änderungen in Version 3.0 ##
*	Brailledarstellung von MathML-Objekten können bei installiertem MathPlayer
  zur Zwischenablage kopiert oder ausgeschnitten werden.
*	Wenn kein Trennzeichen gesetzt ist, wird nur eine einzige Linie zwischen
  den angehängten Textsegmenten platziert werden.
*	Sie können eine Tastenkürzel zum Öffnen des Einstellungsdialogs zuweisen.
*	Es wurde ein Kontrollkästchen im Einstellungsdialog hinzugefügt, mit dem
  festgelegt werden kann, ob der Separator beim erneuten Installieren der
  Erweiterung für den Import kopiert werden soll.

## Änderungen in Version 2.0 ##
*	Indische Zeichen können nun als Trennzeichen zwischen kopierten Inhalten
  verwendet werden.

## Änderungen in Version 1.0 ##
*	anfängliche Version


[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev

[3]:
https://github.com/nvdaes/clipContentsDesigner/releases/download/7.2/clipContentsDesigner-7.2.nvda-addon
