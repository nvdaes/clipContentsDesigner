# Udklipsdesigner (Clip Contents Designer) #

*	Forfattere: Noelia, Abdel.Forfatter: Noelia Ruiz Martinez.

Denne tilføjelse bruges til at tilføje tekst til udklipsholderen, hvilket
kan være nyttigt, når du vil tilslutte tekstafsnit sammen klar til
indsætning. Udklipsholderens indhold kan også ryddes og vises i
gennemsynstilstand.

## Tastaturkommandoer ##

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
* Restore defaults.

Bemærkninger:

*	Bekræftelse vil ikke blive anmodet, når en meddelelsesdialog fra NVDA
  stadig er åben. I disse situationer vil handlingen straks udføres.
*	Emulate copy and emulate cut commands mean that, when these features are
  enabled, the add-on will take control of control+c and control+x. This
  will allow to select if a confirmation should be requested before
  performing the actions corresponding to these keystrokes.

## Changes for 46.0.0

## Changes for 40.0.0

## Ændringer for 16.0

* Rettede kommandoer til at kopiere og klippe med persisk tastatur, takket

  være Cyrille Bougot.
* Forbedret dokumentationen.

* Du kan tildele forskellige kommandoer til visning af udklipsholderens

  indstillinger.

  Writer.

* Nu er det muligt at tilføje tekst markeret med læsemarkøren ved hjælp af
  standardkommandoer for NVDA (NVDA+f9 og NVDA+f10). NVDA+windows+f9 bruges

  ikke længere til, således tilføjelsen fungerer i overensstemmelse med

  NVDA+Shift+F9.

## Ændringer i 10.0

* Rettet en fejl i den dialog, der blev brugt til at vise teksten i
  udklipsholderen, når dens titel indeholdte ikke-latinske tegn.
* Rettet en fejl ved brug af emuleringen af klip/kopier og
  Abdel, nu tilføjet som en forfatter.

## Ændringer for 9.0

* Tilføjet mulighed for at vise udklipsholderens aktuelle tekstindhold i
  gennemsynstilstand.
  udklipsholderen ikke er tom, hvis der f.eks. Er kopieret filer eller
  mapper.
* Kræver NVDA 2018.4 eller nyere.

## Ændringer i 8.0 ##

  indstillinger i dialogboksen.

* Kræver NVDA 2018.2 eller nyere.

## Ændringer i7.0

* Hvis du vælger "nej" i dialogen, hvor du kan konfigurere funktionaliteten
  til at emulere kopi og klip under installationen, vil kommandoerne for
  disse funktioner blive deaktiveret. Dette gendanner den sædvanlige adfærd

  for Ctrl+C og Ctrl+X.

## Ændringer i 6.0

*	Added options to choose if available actions should be performed after
  confirmation.
*	Added Emulate copy and Emulate cut commands, which could be assigned from

  the Input gestures dialog.
*	Added a dialog to configure the Emulate copy and Emulate cut
  functionalities at installation. This allows to add the control+c and
  control+x commands to copy and cut, and be asked if you want to replace

  the clipboard contents when pressing these keystrokes.


*	Fixed documentation for script_add (Windows+NVDA+c).

## ændringer i 5.0 ##

*	Dialogens visuelle præsentation er blevet forbedret og overholder
  udseendet af de dialoger, der vises i NVDA.

*	Kræver NVDA 2016.4 eller nyere.

## Ændringer i 4.0 ##

*	Tilføjelsesindstillinger administreres fra NVDA-konfiguration, så
  standardprofiler kan bruges til at gemme forskellige separatorer, og det

  er ikke nødvendigt at kopiere indstillingerne til import ved
  geninstallation.
  begyndelsen eller slutningen, ved at markere checkboksen "Tilføj tekst før
  data i udklipsholder" i dialogen Indstillinger for udklipsdesigner.

## ændringer i 3.0 ##

*	Punktskriftrepræsentation af MathML-objekter kan tilføjes til

*	Hvis der ikke er indstillet nogen separator, vil der blot blive indsat en
  enkelt linje mellem de tilføjede tekstsegmenter.
*	Der kan knyttes en genvejstast til at åbne dialogen Indstillinger for

  Udklipsdesigner.

## ændringer i 2.0 ##

*	Hindi-tegn kan nu bruges som separator mellem tilføjet indhold.

[[!tag dev stable]]
