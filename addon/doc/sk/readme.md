# Rozšírená schránka #

*	Autori: Noelia, Abdel.

Tento doplnok využijete, ak chcete do schránky Windows postupne vkladať
rôzne časti textu a výsledok naraz prilepiť. Doplnok vie tiež vyčistiť obsah
schránky a zobraziť obsah schránky v režime prehliadania.

## Klávesové skratky ##

*	Nepridelené: Skopíruje alebo vystrihne obsah, pričom zobrazí varovanie.
*	Not assigned: Shows the clipboard text as HTML in browse mode, or
  announces if clipboard is empty or has contents which can't be presented
  in a browseable message, for instance if files or folders are been copied
  from Windows Explorer.
*	Not assigned: Shows the textual clipboard contents as plain text in browse
  mode, or announces if clipboard is empty or has contents which can't be
  presented in a browseable message, for instance if files or folders are
  been copied from Windows Explorer.

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

Poznámky:

*	Ak je otvorené nejaké okno NVDA, nie je možné zobraziť varovanie. V
  takomto prípade sa varovanie nezobrazí a akcia sa rovno vykoná.
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
* You can assign different gestures to show the clipboard textual contents
  as raw text or formatted in HTML. The Format to show the clipboard text in


## Changes for 12.0
## Zmeny vo verzii 11.0


  NVDA+F10). Nvda+windows+F9 sa už nepoužíva, pre lepšiu integráciu so
  skratkou nvda+shift+F9.
## Zmeny vo verzii 10.0


## Zmeny vo verzii 9.0

* Pridané zobrazenie obsahu schránky v režime prehliadania.

* Pridaná možnosť zobraziť varovanie, ak schránka nie je prázdna, napríklad
  ak sú v schránke súbory a priečinky.
* Vyžaduje sa NVDA od verzie 2018.4.

## Zmeny vo verzii 8.0 ##

* Nastavenia doplnku pridané do stromu s nastaveniami NVDA.

* Vyžaduje NVDA od verzie 2018.2.

## Zmeny vo verzii 7.0

* Ak nepovolíte simulovanie kopírovania pri inštalácii, doplnok neupravuje
  klávesové skratky.

*	Added options to choose if available actions should be performed after
  confirmation.
*	Added Emulate copy and Emulate cut commands, which could be assigned from
  the Input gestures dialog.

  control+x commands to copy and cut, and be asked if you want to replace
  the clipboard contents when pressing these keystrokes.

*	Fixed documentation for script_add (Windows+NVDA+c).


*	Opravené vizuálne zobrazenie dialógov doplnku.

*	Vyžaduje NVDA od verzie 2016.4


*	Nastavenia sa ukladajú podľa pravidiel NVDA, takže je možné použiť

  nanovo importovať nastavenia.

*	Odteraz je možné v nastaveniach doplnku určiť, či sa bude text vkladať na
  koniec alebo na začiatok obsahu schránky.

## Zmeny vo verzii 3.0 ##

*	Braillovské znaky pre matematické operátory je takisto možné vkladať do
  schránky, ak je k dispozícii MathPlayer.
*	Nastavenia doplnku je možné vyvolať klávesovou skratkou, ktorú si
*	Pridané začiarkávacie políčko, ktoré zaistí importovanie nastavení po

## Zmeny vo verzii 2.0 ##


*	Znaky v jazyku Hindi môžu byť použité na oddelenie častí schránky.
[[!tag dev stable]]
