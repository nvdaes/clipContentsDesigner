# Clip Contents Designer #

*	Autoren: Noelia und Abdel.

Diese Erweiterung kann verwendet werden, um Text zur Zwischenablage
hinzuzufügen. Dies kann beispielsweise beim Zusammenfügen von verschiedenen
Textabschnitten nützlich sein. Der Inhalt der Zwischenablage kann auch
gelöscht werden.

## Tastenkombinationen ##

*	Nicht zugeordnet: Kopieren (oder Ausschneiden) in die Zwischenablage, mit
  der Möglichkeit, um eine vorherige Bestätigung gebeten zu werden.
*	Nicht zugewiesen: Zeigt den Text der Zwischenablage im Lesemodus als HTML
  an oder benachrichtigt, wenn die Zwischenablage leer ist oder Inhalte
  enthält, die nicht in einer darstellbaren Nachricht angezeigt werden
  können, z. B. wenn Dateien oder Ordner im Windows Explorer kopiert wurden.
*	Nicht zugewiesen: Zeigt den Text-Inhalt der Zwischenablage im Lesemodus
  als einfachen Text an oder gibt aus, ob die Zwischenablage leer ist oder
  Inhalte enthält, die nicht in einer darstellbaren Nachricht angezeigt
  werden können, z. B. wenn Dateien oder Ordner im dem Windows Explorer
  kopiert wurden.

  Aktionen sind: Text hinzufügen, Zwischenablage löschen, Kopieren emulieren
  und Ausschneiden emulieren.

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
* Restore defaults.

Anmerkungen:

*	Bestätigungen werden nicht angefordert, wenn ein Meldungsfenster von NVDA
  geöffnet ist. In diesem Fall werden die Aktionen sofort ausgeführt.
*	Emulate copy and emulate cut commands mean that, when these features are
  enabled, the add-on will take control of control+c and control+x. This
  will allow to select if a confirmation should be requested before
  performing the actions corresponding to these keystrokes.

## Changes for 46.0.0

## Changes for 40.0.0

* Die NVDA-Erweiterung läuft nicht im geschützten Modus.

## Änderungen in 15.0

  Dialogfeld für die Tastenbefehle angezeigt.

* Dank Cyrille Bougot wurde ein Problem im visuellen Layout des

  Optionen auszuwählen.

## Änderungen in 12.0

## Änderungen in 11.0









  NVDA+shift+f9  besser zu integrieren.


## Änderungen in 9.0

  Lesemodus anzuzeigen.

* Es wurde eine Option hinzugefügt, um zu wählen, ob Bestätigungen
  erforderlich sind, wenn die Zwischenablage nicht leer ist, z.B. wenn
  Dateien oder Ordner kopiert wurden.
* Benötigt NVDA 2018.4 oder höher.

* Die Einstellungen für die Erweiterung werden in der entsprechenden
  Kategorie der Einstellungen von NVDA angezeigt.
* Benötigt NVDA 2018.2 oder höher.

* Die Befehle im Dialog zum Konfigurieren der Funktionen für das Emulieren
  der Kopier- und Ausschneide-Funktion  werden bei der Installation
  entfernt, so dass das normale Verhalten von Strg+C und Strg+X

## Änderungen in 6.0

  the Input gestures dialog.





*	Added a dialog to configure the Emulate copy and Emulate cut

  the clipboard contents when pressing these keystrokes.

*	Fixed documentation for script_add (Windows+NVDA+c).
*	Die visuelle Darstellung des Dialogs wurde verbessert und entspricht dem
  Erscheinungsbild der Dialoge in NVDA.

*	Benötigt NVDA 2016.4 oder höher.

## Änderungen in 4.0 ##

  dass Standardprofile verwendet werden können, um verschiedene Trennlinien

  zu speichern. Es ist nicht erforderlich, die Einstellungen für den Import
  bei der Neuinstallation zu kopieren.

*	Es kann nun gewählt werden, ob der hinzugefügte Text angehängt oder
  vorangestellt werden soll, indem Sie das Kontrollkästchen Text vor den
  verwenden.

## Änderungen in 3.0 ##

*	Braille-Darstellung von MathML-Objekten können bei installiertem
  MathPlayer zur Zwischenablage hinzugefügt werden.

  den angehängten Textsegmenten platziert.

*	Es wurde ein Kontrollkästchen im Einstellungsdialog hinzugefügt, mit dem
  festgelegt wird, ob die Trennlinie beim erneuten Installieren der
