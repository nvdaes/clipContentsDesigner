# Udklipsdesigner #

*	Authors: Noelia, Abdel.
*	NVDA compatibility: 2018.4 to 2019.2.
*	Download [stabil version][1]
*	Download [udviklingsversion][2]

Denne tilføjelse bruges til at tilføje tekst til udklipsholderen, hvilket
kan være nyttigt, når du vil tilslutte tekstafsnit sammen klar til
indsætning. Udklipsholderens indhold kan også ryddes og vises i
gennemsynstilstand.

## Tastaturkommandoer ##
*	NVDA+Windows+c: Tilføj tekst, Unicode-Braille-tegn, som repræsenterer
  MathML-objekter, eller den tekststreng, som er blevet markeret med
  læsemarkøren, til udklipsholderen.
*	NVDA+Windows+x: Ryd udklipsholderen.
*	NVDA+Windows+F9: Marker læsemarkørens aktuelle position som starten af den tekst, der skal tilføjes til udklipsholderen. Hvis du bruger NVDA+F9, vil teksten ikke blive tilføjet.
*	 Ikke tildelt; Tilføjede mulighed for at kopiere test til eller klippe tekst fra udklipsholderen, med mulighed for at få dette bekræftet.
*	 Ikke tildelt: Viser teksten i udklipsholderen i gennemsynstilstand, eller meddeler hvis udklipsholderen er tom eller indeholder tekst, der ikke kan vises i gennemsynstilstand. Dette kan f.eks. være, hvis filer eller mapper er blevet kopieret fra Windows Stifinder..

Bemærk: Kommandoerne ovenfor kan ændres fra NVDA-menuen / Præferencer/
Inputbevægelser / kategorien tekstlæsning.

## Indstillinger-menuen ##
Indstillinger for Udklipsdesigner: Her kan du indstille en separator, som kan bruge til at finde de enkelte tekstsegmenter, når først hele den tilføjede tekst er blevet indsat.
Her kan du også vælge om den tilføjede tekst skal indsættes før eller efter eksisterende tekst, om tilgængelige handlinger (tilføj, ryd udklipsholder, emuler kopi og emuler klip) skal udføres straks eller efter handlingen bekræftes, og om der kun skal anmodes om bekræftelse, hvis udklipsholderen indeholder tekst.
Yderligere kan du ændre formatet og max antal af tegn, der skal vises i gennemsynstilstand, når du får udklipsholderens indhold vist i gennemsynstilstand. Det højeste tal er 100000 tegn.

Bemærkninger:

*	Ovennævnte kommando kan ændres fra NVDAs menu, under Præferencer. Herunder
  gå til Inputbevægelser og vælg kategorien "Configuration".
*	Bekræftelse vil ikke blive anmodet, når en meddelelsesdialog fra NVDA
  stadig er åben. I disse situationer vil handlingen straks udføres.

## Changes for 10.0
* Fixed a bug in the dialog used to show the clipboard text, when its title
  contains non latin characters.
* Fixed a bug when using the emulate cut and copy features with an Arabic
  keyboard layout. This has been fixed by Abdel, added as an add-on author.

## Ændringer for 9.0

* Tilføjet mulighed for at vise udklipsholderens aktuelle tekstindhold i
  gennemsynstilstand.
* Tilføjet en mulighed for at vælge, om der skal kræves bekræftelse, hvis
  udklipsholderen ikke er tom, hvis der f.eks. Er kopieret filer eller
  mapper.
* Kræver NVDA 2018.4 eller nyere.

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
