# Clip Contents Designer #

*	Autori: Noelia și Abdel.

Acest supliment este utilizat pentru a adăuga text pe planșetă, care poate
fi folositor când dorești să accesezi secțiuni de text împreună gata pentru
a fi lipit. Conținutul de pe planșetă poate, deasemenea, fi curățat și
afișat în modul de navigare.

## Comenzi de taste ##

*	Not assigned: Copies to (or cuts from) the clipboard, with the possibility
  of being asked for a previous confirmation.
*	Not assigned: Shows the clipboard text as HTML in browse mode, or
  announces if clipboard is empty or has contents which can't be presented
  in a browseable message, for instance if files or folders are been copied
  from Windows Explorer.
*	Not assigned: Shows the textual clipboard contents as plain text in browse
  mode, or announces if clipboard is empty or has contents which can't be
  presented in a browseable message, for instance if files or folders are
  been copied from Windows Explorer.

  clipboard: Allows to set a separator which can be used to find the text
  segments once the entire added text is pasted.

  confirmation. Available actions are: add text, clear clipboard, emulate
  copy and emulate cut.


*	Confirmations won't be requested when a message box of NVDA is still
  opened. In those cases, actions will be inmediately performed.
*	Emulate copy and emulate cut commands mean that, when these features are
  enabled, the add-on will take control of control+c and control+x. This
  will allow to select if a confirmation should be requested before
  performing the actions corresponding to these keystrokes.

## Changes for 46.0.0

## Changes for 40.0.0

## Changes for 16.0

* Fixed gestures to copy and cut with Persian keyboard, thanks to

  Bougot.
* Improved documentation.
* Added a Clip Contents Designer category to assign input gestures to all

* Fixed bugs when using emulate copy in browsers if focus mode is active.

* You can assign different gestures to show the clipboard textual contents
  as raw text or formatted in HTML. The Format to show the clipboard text in
  the settings panel has being modified accordingly, to select the two

## Changes for 12.0

* Fixed bugs when using emulate copy in applications like LibreOffice
  Writer.

## Changes for 11.0

* Now it's possible to add text marked with the review cursor using standard
  used, for a better integration with the new NVDA+shift+f9 command.
* Requires NVDA 2019.3 or later.

## Modificări în 10.0

  navigare.

* În dialogul pentru configurarea copierii și tăierii simulate la instalare,
  dacă alegeți nu, comenzile pentru aceste caracteristici vor fi șterse,
  control+x.


## Modificări în 6.0

*	Added options to choose if available actions should be performed after
  confirmation.

*	Added Emulate copy and Emulate cut commands, which could be assigned from
  the Input gestures dialog.
*	Added a dialog to configure the Emulate copy and Emulate cut
  functionalities at installation. This allows to add the control+c and

  control+x commands to copy and cut, and be asked if you want to replace

  the clipboard contents when pressing these keystrokes.


*	Fixed documentation for script_add (Windows+NVDA+c).

## Modificări în 5.0 ##

*	Prezentarea vizuală a dialogului a fost îmbunătățită, aderând la aspectul
  dialogurilor afișate în NVDA.

*	Necesită NVDA 2016.4 sau mai nou.

## Modificări din 4.0 ##

*	Setările suplimentului sunt gestionate din configurarea NVDA, deci
  profilurile implicite pot fi folosite pentru a salva diferite separatoare,

  și nu este nevoie să copiezi setările pentru a le importa la reinstalare.

*	Acum este posibilă selectarea dacă textul adăugat va fi anexat sau
  Contents Designer-ului.

## Modificări din 3.0 ##

*	Reprezentarea Braille din obiectele MathML poate fi adăugat pe planșetă

  dacă MathPlayer este instalat.

*	Dacă niciun separator nu este setat, o singură linie va fi adăugată între
  segmentele textului adăugat.

*	O scurtătură poate fi definită pentru a deschide setările Clip Contents
  Designer-ului.

  separatorul trebuie să fie copiat pentru a fi immportat când reinstalezi
  add-on-ul.

## Modificări din 2.0 ##

*	Caracterele indiene pot fi folosite ca separator între content-ul adăugat.
*	Versiunea inițială.
