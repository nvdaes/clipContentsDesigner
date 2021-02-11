# Rozšírená schránka #

*	Autori: Noelia, Abdel.
*	Funguje s NVDA od verzie 2019.3
*	Stiahnuť [stabilnú verziu][1]
*	Stiahnuť [vývojovú verziu][2]

Tento doplnok využijete, ak chcete do schránky Windows postupne vkladať
rôzne časti textu a výsledok naraz prilepiť. Doplnok vie tiež vyčistiť obsah
schránky a zobraziť obsah schránky v režime prehliadania.

## Klávesové skratky ##
*	NVDA+windows+c: pripojí k obsahu schránky vybratý text, alebo text, ktorý
  ste označili prezeracím kurzorom. Takto je možné pridať aj znaky unicode,
  MathML.
*	NVDA+windows+x: vymaže obsah schránky.
*	Nepridelené: Skopíruje alebo vystrihne obsah, pričom zobrazí varovanie.
*	Not assigned: Shows the clipboard text as HTML in browse mode, or
  announces if clipboard is empty or has contents which can't be presented
  in a browseable message, for instance if files or folders are been copied
  from Windows Explorer.
*	Not assigned: Shows the textual clipboard contents as plain text in browse
  mode, or announces if clipboard is empty or has contents which can't be
  presented in a browseable message, for instance if files or folders are
  been copied from Windows Explorer.


## Clip Contents Designer settings ##

This panel is available from NVDA's menu, Preferences submenu, Settings
dialog.

It contains the following controls:

* Type the string to be used as a separator between contents added to the
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

Poznámky:

*	Ak je otvorené nejaké okno NVDA, nie je možné zobraziť varovanie. V
  takomto prípade sa varovanie nezobrazí a akcia sa rovno vykoná.
*	Emulate copy and emulate cut commands mean that, when these features are
  enabled, the add-on will take control of control+c and control+x. This
  will allow to select if a confirmation should be requested before
  performing the actions corresponding to these keystrokes.

## Changes for 13.0 
* Fixed an issue in visual layout of the settings panel, thanks to Cyrille
  Bougot.
* Improved documentation.
* Added a Clip Contents Designer category to assign input gestures to all
  commands available for this add-on.
* Fixed bugs when using emulate copy in browsers if focus mode is active.
* You can assign different gestures to show the clipboard textual contents
  as raw text or formatted in HTML. The Format to show the clipboard text in
  the settings panel has being modified accordingly, to select the two
  options available for HTML format.

## Changes for 12.0
* Fixed bugs when using emulate copy in applications like LibreOffice
  Writer.

## Zmeny vo verzii 11.0
* Odteraz je možné do schránky pridať aj reťazce označené štandardnými
  príkazmi na označovanie pomocou prezeracieho kurzora (NVDA+F9,
  NVDA+F10). Nvda+windows+F9 sa už nepoužíva, pre lepšiu integráciu so
  skratkou nvda+shift+F9.
* Vyžaduje NVDA od verzie 2019.3.

## Zmeny vo verzii 10.0
* Opravená chyba, ktorá nastávala pri zobrazení názvu okna so zobrazením
  textu v režime prehliadania, ak boli v názve okna špeciálne znaky.
* Abdel opravil problémy s kopírovaním na Arabskom rozložení klávesnice.

## Zmeny vo verzii 9.0

* Pridané zobrazenie obsahu schránky v režime prehliadania.
* Pridaná možnosť zobraziť varovanie, ak schránka nie je prázdna, napríklad
  ak sú v schránke súbory a priečinky.
* Vyžaduje sa NVDA od verzie 2018.4.

## Zmeny vo verzii 8.0 ##

* Nastavenia doplnku pridané do stromu s nastaveniami NVDA.
* Vyžaduje NVDA od verzie 2018.2.
* Stále si môžete stiahnuť [verziu pre NVDA 2017.3][3].

## Zmeny vo verzii 7.0

* Ak nepovolíte simulovanie kopírovania pri inštalácii, doplnok neupravuje
  klávesové skratky.

## Zmeny vo verzii 6.0

*	 Pridané varovanie pri kopírovaní a vystrihnutí.
*	Pridané skratky, ktoré preberajú kontrolu nad schránkou a dajú sa nastaviť z dialógu Klávesové skratky.
*	 Pridané okno, ktoré sa zobrazí pri prvom spustení doplnku a umožňuje nastaviť prevzatieskratiek na prácu so schránkou. Toto umožňuje následné zobrazovanie varovaní pri kopírovaní a vystrihnutí.
*	Opravená dokumentácia pre skript_add (Windows+NVDA+c).

## Zmeny vo verzii 5.0 ##

*	Opravené vizuálne zobrazenie dialógov doplnku.
*	Vyžaduje NVDA od verzie 2016.4

## Zmeny vo verzii 4.0 ##
*	Nastavenia sa ukladajú podľa pravidiel NVDA, takže je možné použiť
  konfiguračné profily NVDA a nie je potrebné po preinštalovaní doplnku
  nanovo importovať nastavenia.
*	Odteraz je možné v nastaveniach doplnku určiť, či sa bude text vkladať na
  koniec alebo na začiatok obsahu schránky. 

## Zmeny vo verzii 3.0 ##
*	Braillovské znaky pre matematické operátory je takisto možné vkladať do
  schránky, ak je k dispozícii MathPlayer.
*	Ak nezadáte znaky na oddelenie, použije sa jeden prázdny riadok.
*	Nastavenia doplnku je možné vyvolať klávesovou skratkou, ktorú si
  nastavíte v dialógu klávesové skratky.
*	Pridané začiarkávacie políčko, ktoré zaistí importovanie nastavení po
  preinštalovaní doplnku.

## Zmeny vo verzii 2.0 ##
*	Znaky v jazyku Hindi môžu byť použité na oddelenie častí schránky.

## Zmeny vo verzii 1.0 ##
*	prvé vydanie.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ccd

[2]: https://addons.nvda-project.org/files/get.php?file=ccd-dev

[3]: https://addons.nvda-project.org/files/get.php?file=ccd-o
