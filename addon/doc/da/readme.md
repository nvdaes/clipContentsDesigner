# Udklipsdesigner (Clip Contents Designer) #

*	Forfattere: Noelia, Abdel.Forfatter: Noelia Ruiz Martinez.
*	NVDA-kompatibilitet: 2019.3 eller nyere
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
*	Ikke tildelt: Kopierer til (eller klipper fra) udklipsholderen med
  mulighed for at blive bedt om en bekræftelse.
*	Ikke tildelt: Viser teksten i udklipsholderen i gennemgynstilstand som
  HTML-indhold. Du vil få besked, hvis udklipsholderen er tom eller hvis
  indholdet ikke kan vises i gennemsynstilstand. Dette kan eksempelvis være,
  hvis du har kopiere filer fra Stifinder.
*	Ikke tildelt: Viser teksten i udklipsholderen i gennemgynstilstand som rå
  tekst. Du vil få besked, hvis udklipsholderen er tom eller hvis indholdet
  ikke kan vises i gennemsynstilstand. Dette kan eksempelvis være, hvis du
  har kopiere filer fra Stifinder.


## Indstillinger for Udklipsdesigner ##

Ovennævnte kommando kan ændres fra NVDAs menu, under "Opsætning".

Den indeholder følgende kontroller:

* Indtast den streng, der skal bruges som separator mellem indhold tilføjet
  til udklipsholderen: Gør det muligt at indstille en separator, som kan
  bruges til at finde tekstsegmenterne, når hele den tilføjede tekst er
  indsat.
* Tilføj tekst før klipdata: Det er også muligt at vælge, om den tilføjede
  tekst skal tilføjes foran eller bagefter tekst, der allerede befinder sig
  ved markøren.
* Vælg de handlinger, der kræver tidligere bekræftelse: Du kan for hver
  tilgængelig handling vælge, om den skal udføres med det samme eller efter
  bekræftelse. Tilgængelige handlinger er: tilføj tekst, ryd
  udklipsholderen, emuler kopi og emuler klip.
* Anmod om bekræftelse, før du udfører de valgte handlinger, når: Du kan
  vælge, om der altid skal anmodes om bekræftelser, hvis der kun er tekst i
  udklipsholderen, eller hvis udklipsholderen ikke er tom (f.eks. Hvis du
  har kopieret en fil, ikke tekst).
* Formatér og vis udklipsholderteksten som HTML i gennemsynstilstand: Hvis
  du er ved at lære HTML, kan du vælge Forformateret tekst i HTML eller HTML
  som vist i en webbrowser for at få en idé om, hvordan din HTML -kode vil
  blive gengivet af NVDA i en browser. Forskellen mellem forformateret og
  konventionel HTML er, at den første mulighed bevarer fortløbende mellemrum
  og linjeskift, og den anden komprimerer dem. Skriv f.eks. Nogle HTML-tags
  som h1, h2, li, pre osv., Vælg og kopier teksten til udklipsholderen, og
  brug tilføjelsen til at vise teksten i en meddelelse, der kan gennemses.
* Maksimalt antal tegn, når udklipsholdertekst vises i gennemsynstilstand:
  Vær opmærksom på, at forhøjelse af denne grænse kan give problemer, hvis
  udklipsholderen indeholder store tekststrenge. Standardgrænsen er 100000
  tegn.

Bemærkninger:

*	Bekræftelse vil ikke blive anmodet, når en meddelelsesdialog fra NVDA
  stadig er åben. I disse situationer vil handlingen straks udføres.
*	Kommandoerne "Emulering af kopier" og "Emulering af klip" betyder, at når
  disse funktioner er aktiveret, overtager tilføjelsen Ctrl+C og
  Ctrl+X. Dette giver mulighed for at vælge, om der skal anmodes om en
  bekræftelse, før de handlinger, der svarer til disse tastetryk, udføres.

## Ændringer for 13.0
* Rettet et problem i det visuelle layout for indstillingspanelet takket
  være Cyrille Bougot.
* Forbedret dokumentationen.
* Tilføjede en Udklipsdesigner-kategori for at tildele inputbevægelser til
  alle kommandoer, der er tilgængelige for denne tilføjelse.
* Rettede fejl ved brug af "Emuler kopi" i browsere, hvis fokustilstand er
  aktiv.
* Du kan tildele forskellige kommandoer til visning af udklipsholderens
  tekstlige indhold. Indholdet kan vises som rå tekst eller formateret i
  HTML. Formatet til visning af udklipsholderteksten i indstillingspanelet
  er blevet ændret i overensstemmelse hermed, så du kan vælge de to mulige
  indstillinger.

## Ændringer for 12.0
* Rettede fejl ved brug af "Emuler kopi" i applikationer som LibreOffice
  Writer.

## Ændringer i 11.0
* Nu er det muligt at tilføje tekst markeret med læsemarkøren ved hjælp af
  standardkommandoer for NVDA (NVDA+f9 og NVDA+f10). NVDA+windows+f9 bruges
  ikke længere til, således tilføjelsen fungerer i overensstemmelse med
  NVDA+Shift+F9.
* Kræver NVDA 2019.3 eller nyere.

## Ændringer i 10.0
* Rettet en fejl i den dialog, der blev brugt til at vise teksten i
  udklipsholderen, når dens titel indeholdte ikke-latinske tegn.
* Rettet en fejl ved brug af emuleringen af klip/kopier og
  kopieringsfunktioner med et arabisk tastaturlayout. Dette er rettet af
  Abdel, nu tilføjet som en forfatter.

## Ændringer for 9.0

* Tilføjet mulighed for at vise udklipsholderens aktuelle tekstindhold i
  gennemsynstilstand.
* Tilføjet en mulighed for at vælge, om der skal kræves bekræftelse, hvis
  udklipsholderen ikke er tom, hvis der f.eks. Er kopieret filer eller
  mapper.
* Kræver NVDA 2018.4 eller nyere.

## Ændringer i 8.0 ##

* Tilføjelsens indstillinger vises i den tilsvarende kategori NVDA
  indstillinger i dialogboksen.
* Kræver NVDA 2018.2 eller nyere.
* Hvis nødvendigt, kan du hente [sidste version kompatibel med NVDA
  2017.3][3].

## Ændringer i7.0

* Hvis du vælger "nej" i dialogen, hvor du kan konfigurere funktionaliteten
  til at emulere kopi og klip under installationen, vil kommandoerne for
  disse funktioner blive deaktiveret. Dette gendanner den sædvanlige adfærd
  for Ctrl+C og Ctrl+X.

## Ændringer i 6.0

*	 Tilføjede indstilling der lader dig vælge, om tilgængelige handlinger skal bekræftes, før de udføres.
*	 Tilføjede tastetryk for emuler kopi og emuler klip, der kan tildeles under dialogen "Inputbevægelser".
*	 Tilføjede en dialog, der lader dig konfigure emuler klip og emuler klip under installationen. Dette tilføjer handlingerne Kopi og Klip til kommandoerne Ctrl+C og Ctrl+X, og spørger om du vil erstatte udklipsholderens indhold, når du benytter disse taster.
*	 rettede dokumentation for script_add (Windows+NVDA+c).

## ændringer i 5.0 ##

*	Dialogens visuelle præsentation er blevet forbedret og overholder
  udseendet af de dialoger, der vises i NVDA.
*	Kræver NVDA 2016.4 eller nyere.

## Ændringer i 4.0 ##
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
