# Vágólap tartalomtervező #

*	Készítők: Noelia, Abdel.
*	Támogatott NVDA kiadások: 2019.3 és újabb
*	[Stabil verzió][1] letöltése
*	[Fejlesztői verzió][2] letöltése

A kiegészítő abban az esetben hasznos, ha több különböző szövegrészt
szeretnénk összefűzni, majd azt a vágólapról beilleszteni. A vágólap
tartalma törölhető, illetve megjeleníthető böngésző módban.

## Billentyűparancsok ##
*	NVDA+windows+c: A vágólap tartalmához fűzi a kijelölt  vagy az áttekintő
  kurzorral megjelölt szöveget, és az unikód braille MathML objektumot
  reprezentáló karaktereket is.
*	NVDA+windows+x: Vágólap tartalom törlése.
*	Alapértelmezés szerint nincs billentyűparancs hozzárendelve: Másolás a
  vágólapra vagy kivágás onnan a végrehajtás előtt megerősítés kérésével.
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

Megjegyzések:

*	Amikor az NVDA egy másik üzenetablaka is nyitva van a bővítmény nem kér
  megerősítést a vágólapműveletek előtt, de attól még végrehajtja azokat.
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

## A 11.0 változásai
* Most már hozzáfűzhető az áttekintőkurzorral kijelölt szöveg is az NVDA+F9
  és NVDA+F10 billentyűparancsok használatával. A korábban használt
  NVDA+Windows+F9 parancs már nem használható.
* Az NVDA 2019.3 vagy újabb kiadására van szükség.

## A 10.0 változásai
* Hiba elhárítva: ha a vágólap tartalmát megjelenítő párbeszédablak címe nem
  latin betűket tartalmaz
* Hiba elhárítva: problémát okozott az emulált másolás és kivágás arab
  kiosztású billentyűzeteken

## A 9.0 változásai

* A vágólap tartalma már megjeleníthető böngészőmódban is
* Megerősítés kérhető olyan esetben, ha a vágólap nem üres, de tartalma nem
  szöveges, pl. ha egy fájlt vagy mappát másoltunk rá.
* Az NVDA 2018.4 vagy újabb kiadása szükséges

## A 8.0 változásai ##

* A bővítmény beállításai az NVDA beállításai közt jelennek meg külön
  kategóriában
* Az NVDA 2018.2 vagy újabb kiadása szükséges
* Ha szükséges, letöltheti a [legutolsó verziót][3], ami még támogatja az
  NVDA 2017.3 kiadását.

## A 7.0 változásai

* Amennyiben a bővítmény telepítése során nem állítja be az emulált másolást
  és kivágást, akkor nem változik meg a Ctrl+C és Ctrl+X parancsok
  hagyományos viselkedése.

## A 6.0 változásai

*	 Beállítható, hogy mely vágólapműveletek végrehajtása előtt kérjen megerősítést.
*	Az NVDA beviteli parancsai között billentyűparancs rendelhető az emulált másoláshoz és az emulált kivágáshoz.
*	 A telepítésnél beállítható a Ctrl+C és Ctrl+X billentyűparancs az emulált másoláshoz és kivágáshoz. Ekkor megerősítést kér a parancsok végrehajtása előtt.
*	 Javították a hozzáfűzés szkriptjének (Windows+NVDA+c) dokumentációját.

## Az 5.0 változásai ##

*	Javították a bővítmény párbeszédablakának vizuális megjelenítését.
*	Az NVDA 2016.4 vagy újabb kiadása szükséges

## A 4.0 változásai ##
*	A bővítmény beállításai az NVDA konfigurációjában kezelhetők, így a
  sztenderd profilokat használhatjuk az elválasztók elmentésére, így a
  beállításokat nem kell újra bemásolni az újratelepítéskor történő
  importáláskor.
*	Most már ki lehet választani, hogy a hozzáadni kívánt szöveget a tartalom
  elé vagy mögé csatoljuk, ha használjuk a "vágólap tartalma elé"
  jelölőnégyzetet a vágólaptartalom-tervező beállítása párbeszédpanelén.

## A 3.0 változásai ##
*	Ha a MathPlayer telepítve van, a MathMl objektumok braille reprezentációja
  kerül hozzáfűzésre a vágólaphoz.
*	Ha nincs megadva elválasztó karakter, egy üres sor kerül beszúrásra a két
  szöveg közé.
*	Billentyűparancsot adtak hozzá a Vágólaptartalom-tervező beállítás
  ablakának eléréséhez.
*	Hozzáadtak egy jelölőnégyzetet, mellyel szabályozható, hogy az elválasztó
  karaktert bemásolja-e a bővítmény a saját beállítások mappájába a későbbi
  importáláshoz.

## A 2.0 változásai ##
*	Hindi karakterek is használhatóak az összefűzött szövegek közötti
  elválasztóként.

## Az 1.0 változásai ##
*	- Első kiadás

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ccd

[2]: https://addons.nvda-project.org/files/get.php?file=ccd-dev

[3]: https://addons.nvda-project.org/files/get.php?file=ccd-o[1]:
https://addons.nvda-project.org/files/get.php?file=ccd
