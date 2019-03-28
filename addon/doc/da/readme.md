# Udklipsdesigner #

*	Forfatter: Noelia Ruiz Martinez.
*	NVDA-kompatibilitet: 2018.2 til 2019.1
*	Download [stabil version][1]
*	Download [udviklingsversion][2]

This add-on is used to add text to the clipboard, which can be useful when
you want to join sections of text together ready for pasting.  The clipboard
content can also be cleared an shown in browse mode.

## Tastaturkommandoer ##
*	NVDA+Windows+c: Tilføj tekst, Unicode-Braille-tegn, som repræsenterer
  MathML-objekter, eller den tekststreng, som er blevet markeret med
  læsemarkøren, til udklipsholderen.
*	NVDA+Windows+x: Ryd udklipsholderen.
*	NVDA+windows+f9: Mark the current position of the review cursor as the start of the text to be added to the clipboard. If you use nvda+F9, the text will not be added.
*	 Not assigned: Copies to (or cuts from) the clipboard, with the possibility of being asked for a previous confirmation.
*	 Not assigned: Shows the clipboard text in browse mode, or announces if clipboard is empty or has contents which can't be presented in a browseable message, for instance if files or folders are been copied from Windows Explorer..

Bemærk: Kommandoerne ovenfor kan ændres fra NVDA-menuen / Præferencer/
Inputbevægelser / kategorien tekstlæsning.

## Indstillinger-menuen ##
*	Clip Contents Designer settings: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
It's also possible to choose if the added text will be appended or prepended, if available actions (add, clear clipboard, emulate copy and emulate cut) should be performed inmediately or after confirmation, and if confirmations will be requested always, just if text is contained in the clipboard, or if clipboard is not empty.
Furthermore, it's possible to change the format and maximum number of characters of the clipboard text which will be shown in browse mode. Please, be aware that increasing this limit may produce issues if the clipboard contains large strings of text. The default limit is 100000 characters.

Bemærkninger:

*	Ovennævnte kommando kan ændres fra NVDAs menu, under Præferencer. Herunder
  gå til Inputbevægelser og vælg kategorien "Configuration".
*	Bekræftelse vil ikke blive anmodet, når en meddelelsesdialog fra NVDA
  stadig er åben. I disse situationer vil handlingen straks udføres.

## Changes for 9.0

* Added the possibility of showing the clipboard text in browse mode.
* Added an option to choose if confirmations will be required if clipboard
  is not empty, for instance, if files or folders are been copied.
* Requires NVDA 2018.4 or later.

## ændringer i 8.0 ##

* Tilføjelsens indstillinger vises i den tilsvarende kategori NVDA
  indstillinger i dialogboksen.
* Kræver NVDA 2018.2 eller nyere.
* Hvis nødvendigt, kan du hente [sidste version kompatibel med NVDA
  2017.3][3].

## ændringer i 7.0

* Hvis du vælger "nej" i dialogen, hvor du kan konfigurere funktionaliteten
  til at emulere kopi og klip under installationen, vil kommandoerne for
  disse funktioner blive deaktiveret. Dette gendanner den sædvanlige adfærd
  for Ctrl+C og Ctrl+X.

## ændringer i 6.0

*	 Tilføjede indstilling der lader dig vælge, om tilgængelige handlinger skal bekræftes, før de udføres.
*	 Tilføjede tastetryk for emuler kopi og emuler klip, der kan tildeles under dialogen "Inputbevægelser".
*	 Tilføjede en dialog, der lader dig konfigure emuler klip og emuler klip under installationen. Dette tilføjer handlingerne Kopi og Klip til kommandoerne Ctrl+C og Ctrl+X, og spørger om du vil erstatte udklipsholderens indhold, når du benytter disse taster.
*	 rettede dokumentation for script_add (Windows+NVDA+c).

## ændringer i 5.0 ##

*	Dialogens visuelle præsentation er blevet forbedret og overholder
  udseendet af de dialoger, der vises i NVDA.
*	Kræver NVDA 2016.4 eller nyere.

## ændringer for 4.0 ##
*	Tilføjelsesindstillinger administreres fra NVDA-konfiguration, så
  standardprofiler kan bruges til at gemme forskellige separatorer, og det
  er ikke nødvendigt at kopiere indstillingerne til import ved
  geninstallation.
*	Nu er det muligt at vælge, om den tilføjede tekst vil blive tilføjet til
  begyndelsen eller slutningen, ved at markere checkboksen "Tilføj tekst før
  data i udklipsholder" i dialogen Indstillinger for udklipsdesigner.

## ændringer i 3.0 ##
*	Punktskriftrepræsentation af MathML-objekter kan tilføjes til
  udklipsholderen, hvis MathPlayer er installeret.
*	Hvis der ikke er indstillet nogen separator, vil der blot blive indsat en
  enkelt linje mellem de tilføjede tekstsegmenter.
*	Der kan knyttes en genvejstast til at åbne dialogen Indstillinger for
  Udklipsdesigner.
*	Tilføjede en checkboks i dialogen Indstillinger til at vælge, om
  separatoren skal kopieres, så den kan importeres, når
  tilføjelsesprogrammet bliver geninstalleret.

## ændringer i 2.0 ##
*	Hindi-tegn kan nu bruges som separator mellem tilføjet indhold.

## ændringer i 1.0 ##
*	Første version.



[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ccd

[2]: https://addons.nvda-project.org/files/get.php?file=ccd-dev

[3]: https://addons.nvda-project.org/files/get.php?file=ccd-o[1]:
https://addons.nvda-project.org/files/get.php?file=ccd
