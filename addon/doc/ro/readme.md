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





* Add text before clip data: It's also possible to choose if the added text
  will be appended or prepended.
* Select the actions which require previous confirmation: You can choose,
  for each action available, if it should be performed inmediately or after
  confirmation. Available actions are: add text, clear clipboard, emulate
  copy and emulate cut.
* Request confirmation before performing the selected actions when: You can
  select if confirmations will be requested always, just if text is
  contained in the clipboard, or if clipboard is not empty (for example if
  you've copied a file, not text).
* Format to show the clipboard text as HTML in browse mode: If you're
  learning HTML markup language, you may choose Preformatted text in HTML or
  HTML as shown in a web browser, to have an idea of how your HTML code will
  be rendered by NVDA in a browser. The difference between preformatted and
  conventional HTML is that the first option will preserve consecutive
  spaces and line breaks, and the second one will compact them.  For
  example, write some HTML tags like h1, h2, li, pre, etc., select and copy
  the text to clipboard, and use clipContentsDesigner add-on to show the
  text in a browseable message.
* Maximum number of characters when showing clipboard text in browse mode:
  Please, be aware that increasing this limit may produce issues if the
  clipboard contains large strings of text. The default limit is 100000
  characters.
* Restore defaults.

Note:

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
* S-a adăugat o opțiune care vă permite să alegeți dacă vor fi sau nu
* Necesită NVDA 2018.4 sau mai nou.


* În dialogul pentru configurarea copierii și tăierii simulate la instalare,
  dacă alegeți nu, comenzile pentru aceste caracteristici vor fi șterse,
  astfel încât să puteți restaura comportamentul normal pentru control+c și
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
