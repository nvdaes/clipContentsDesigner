# Zwischenablagenverwalter #

*	Autoren: Noelia, Abdel.
*	[Stabile Version herunterladen][1] (kompatibel mit NVDA 2022.1 und neuer)
*	[Entwicklerversion herunterladen][2] (kompatibel mit NVDA 2022.1 und
  neuer)

Diese Erweiterung kann verwendet werden, um Text zur Zwischenablage
hinzuzufügen. Dies kann beispielsweise beim Zusammenfügen von verschiedenen
Textabschnitten nützlich sein. Der Inhalt der Zwischenablage kann auch
gelöscht werden.

## Tastenkombinationen ##

* NVDA+Windows+C: Fügt den ausgewählten Text, MathML-Objekte als
  Unicode-Punktschriftzeichen oder die Zeichenkette, die mit dem NVDA-Cursor
  markiert wurde, zur Zwischenablage hinzu.
* NVDA+Windows+X: Leert die Zwischenablage.
* Nicht zugeordnet: Kopieren (oder Ausschneiden) in die Zwischenablage, mit
  der Möglichkeit, um eine vorherige Bestätigung gebeten zu werden.
* Nicht zugewiesen: Zeigt den Text der Zwischenablage im Lesemodus als HTML
  an oder benachrichtigt, wenn die Zwischenablage leer ist oder Inhalte
  enthält, die nicht in einer darstellbaren Nachricht angezeigt werden
  können, z. B. wenn Dateien oder Ordner im Windows Explorer kopiert wurden.
* Nicht zugewiesen: Zeigt den Text-Inhalt der Zwischenablage im Lesemodus
  als einfachen Text an oder gibt aus, ob die Zwischenablage leer ist oder
  Inhalte enthält, die nicht in einer darstellbaren Nachricht angezeigt
  werden können, z. B. wenn Dateien oder Ordner im dem Windows Explorer
  kopiert wurden.


## Einstellungen für den Zwischenablagenverwalter ##

Diese Kategorie finden Sie im NVDA_Menü, unter Optionen und Einstellungen.

Folgende Einstellungen sind verfügbar:

* Geben Sie die Zeichenfolge ein, die als Trennzeichen zwischen Inhalten
  verwendet werden soll, die der Zwischenablage hinzugefügt wurden:
  Ermöglicht das Festlegen eines Trennzeichens, mit dem die Textsegmente
  gefunden werden können, sobald der gesamte hinzugefügte Text eingefügt
  wurde.
* Text vor Daten der Zwischenablage hinzufügen: Sie können auch auswählen,
  ob der hinzugefügte Text angehängt oder vorangestellt werden soll.
* Wählen Sie die Aktionen aus, für die eine vorherige Bestätigung
  erforderlich ist: Sie können für jede verfügbare Aktion auswählen, ob sie
  sofort oder nach der Bestätigung ausgeführt werden soll. Verfügbare
  Aktionen sind: Text hinzufügen, Zwischenablage löschen, Kopieren emulieren
  und Ausschneiden emulieren.
* Fordern Sie eine Bestätigung an, bevor Sie die ausgewählten Aktionen
  ausführen, wenn: Sie können wählen, ob immer Bestätigungen angefordert
  werden sollen, nur wenn Text in der Zwischenablage enthalten ist oder wenn
  die Zwischenablage nicht leer ist z. B. wenn Sie eine Datei (kein Text)
  kopiert haben.
* Legen Sie fest, wie der Text in der Zwischenablage als HTML im Lesemodus
  dargestellt wird: Wenn Sie die HTML-Auszeichnungssprache lernen, können
  Sie vorformatierten Text in HTML oder HTML wie im Internetbrowser
  auswählen, damit Sie eine Vorstellung bekommen, wie Ihr HTML-Code in einem
  Internetbrowser von NVDA dargestellt wird. Der Unterschied zwischen
  vorformatiertem und herkömmlichem HTML besteht darin, dass bei der ersten
  Option aufeinanderfolgende Leerzeichen und Zeilenumbrüche beibehalten und
  bei der zweiten Option komprimiert werden. Schreiben Sie beispielsweise
  einige HTML-Tags wie h1, h2, li, pre etc.., wählen Sie den Text aus und
  kopieren Sie diesen in die Zwischenablage. Verwenden Sie die Erweiterung,
  um den Text in einer Fenster anzuzeigen.
* Maximale Anzahl von Zeichen beim Anzeigen von Text in der Zwischenablage
  im Lesemodus: Beachten Sie, dass das Erhöhen dieser Grenze zu Problemen
  führen kann, wenn die Zwischenablage große Textzeichenfolgen enthält. Das
  Standardlimit beträgt 100000 Zeichen.

Anmerkungen:

* Bestätigungen werden nicht angefordert, wenn ein Meldungsfenster von NVDA
  geöffnet ist. In diesem Fall werden die Aktionen sofort ausgeführt.
* Die Befehle "Kopieren" und "Ausschneiden" emulieren bedeutet, dass die
  Erweiterung die Kontrolle über Strg+C und Strg+X übernimmt, sobald diese
  Funktionen verwendet werden. So können Sie auswählen, ob eine Bestätigung
  angefordert werden soll, bevor die diesen Tastenkombinationen
  entsprechenden Aktionen ausgeführt werden.

## Änderungen in 16.0
* Benötigt NVDA 2022.1 oder neuer.

## Änderungen in 15.0
* Der Befehl zum Hinzufügen von Text in die Zwischenablage wird wieder im
  Dialogfeld für die Tastenbefehle angezeigt.
* Tastenkombinationen zum Kopieren und Ausschneiden mit persischer Tastatur
  behoben, dank Mohammad Hosein Ghezelsofla.

## Änderungen in 14.0
* Kompatibel mit NVDA 2021.1.

## Änderungen in 13.0 
* Dank Cyrille Bougot wurde ein Problem im visuellen Layout des
  Einstellungsfelds behoben.
* Verbesserte Dokumentation.
* Es wurde eine Kategorie "Zwischenablagenverwalter" hinzugefügt, damit
  allen verfügbaren Befehlen Tastenkombinationen zugewiesen werden können.
* Fehler bei der Verwendung der Emulationskopie im Lesemodus behoben, wenn
  der Fokusmodus aktiv ist.
* Sie können verschiedene Gesten zuweisen, um den Textinhalt der
  Zwischenablage als Rohtext oder in HTML formatiert anzuzeigen. Das Format
  zum Anzeigen des Textes in der Zwischenablage im Einstellungsfeld wurde
  entsprechend geändert, um die beiden für das HTML-Format verfügbaren
  Optionen auszuwählen.

## Änderungen in 12.0
* Fehler bei der Verwendung von Emulationskopien in Anwendungen wie
  LibreOffice Writer behoben.

## Änderungen in 11.0
* Jetzt ist es möglich, Text mit den Standardbefehlen des NVDA-Cursors
  (NVDA+f9 und NVDA+f10) zu markieren und in die Zwischenablage zu
  kopieren. NVDA+Windows+f9 wird nicht mehr verwendet, um dem neuen Befehl
  NVDA+shift+f9  besser zu integrieren.
* Erfordert NVDA 2019.3 oder höher.

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
  MathPlayer zur Zwischenablage hinzugefügt werden.
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
