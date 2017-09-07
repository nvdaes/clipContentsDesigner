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
*	NVDA+Windows+F9: Marker læsemarkørens aktuelle position som starten af den tekst, der skal tilføjes til udklipsholderen.
Hvis du bruger NVDA+F9, vil teksten ikke blive tilføjet.

Bemærk: Kommandoerne ovenfor kan ændres fra NVDA-menuen / Indstillinger /
Inputbevægelser / kategorien tekstlæsning.

## Indstillinger-menuen ##
Indstillinger for Udklipsdesigner: Her kan du indstille en separator, som kan bruge til at finde de enkelte tekstsegmenter, når først hele den tilføjede tekst er blevet indsat.
Her kan du også vælge om den tilføjede tekst skal indsættes før eller efter eksisterende tekst.

Bemærk: Denne kommando kan ændres under NVDA-menu / Indstillinger /
Inputbevægelser / kategorien Indstillinger.

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

[1]: https://addons.nvda-project.org/files/get.php?file=ccd

[2]: https://addons.nvda-project.org/files/get.php?file=ccd-dev
