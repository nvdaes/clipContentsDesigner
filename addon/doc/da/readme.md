# Clip Contents Designer #

*	Forfatter: Noelia Ruiz Martínez.
*	Download [stabil version][1]
*	Download [udviklingsversion][2]

This add-on is used to add text to the clipboard, which can be useful when
you want to join sections of text together ready for pasting.  The clipboard
content can also be cleared.

## Tastaturkommandoer ##
*	NVDA+windows+c: Add selected text, Unicode braille characters which
  represent MathML objects, or the string which has been marked with the
  review cursor, to the clipboard.
*	NVDA+Windows+x: Ryd udklipsholderen.
*	NVDA+windows+f9: Mark the current position of the review cursor as the start of the text to be added to the clipboard. If you use nvda+F9, the text will not be added.
*	 Not assigned: Copies to (or cuts from) the clipboard, with the possibility of being asked for a previous confirmation.

Bemærk: Kommandoerne ovenfor kan ændres fra NVDA-menuen / Indstillinger /
Inputbevægelser / kategorien tekstlæsning.

## Indstillinger-menuen ##
*	Clip Contents Designer settings: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
It's also possible to choose if the added text will be appended or prepended, if available actions (add, clear clipboard, emulate copy and emulate cut) should be performed inmediately or after confirmation, and if confirmations will be requested just if text is contained in the clipboard.

Notes:

*	The above command can be changed from NVDA menu, Preferences submenu,
  Input gestures dialog, Configuration category.
*	Confirmations won't be requested when a message box of NVDA is still
  opened. In those cases, actions will be inmediately performed

## Changes for 6.0

*	 Added options to choose if available actions should be performed after confirmation.
*	Added Emulate copy and Emulate cut commands, which could be assigned from the Input gestures dialog.
*	 Added a dialog to configure the Emulate copy and Emulate cut functionalities at installation. This allows to add the control+c and control+x commands to copy and cut, and be asked if you want to replace the clipboard contents when pressing these keystrokes.
*	Fixed documentation for script_add (Windows+NVDA+c).

## Ændringer i 5.0 ##

*	Dialogens visuelle præsentation er blevet forbedret og overholder
  udseendet af de dialoger, der vises i NVDA.
*	Kræver NVDA 2016.4 eller nyere.

## Ændringer for 4.0 ##
*	Tilføjelsesindstillinger administreres fra NVDA-konfiguration, så
  standardprofiler kan bruges til at gemme forskellige separatorer, og det
  er ikke nødvendigt at kopiere indstillingerne til import ved
  geninstallation.
*	Nu er det muligt at vælge, om den tilføjede tekst vil blive tilføjet til
  begyndelsen eller slutningen, ved at markere checkboksen "Tilføj tekst før
  data i udklipsholder" i dialogen Indstillinger for udklipsdesigner.

## Ændringer i 3.0 ##
*	Braille representation of MathML objects can be added to the clipboard if
  MathPlayer is installed.
*	If no separator is set, just a single line will be placed between the
  added text segments.
*	Der kan knyttes en genvejstast til at åbne dialogen Indstillinger for Clip
  Contents Designer.
*	Tilføjede en checkboks i Indstillinger-dialogen til at vælge, om
  separatoren skal kopieres, så den kan importeres, når
  tilføjelsesprogrammet bliver geninstalleret.

## Ændringer i 2.0 ##
*	Hindi characters can be used as the separator between added contents.

## Ændringer i 1.0 ##
*	Første version.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev
