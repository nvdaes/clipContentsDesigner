# Vágólap tartalomtervező #

*	- Készítők: Noelia Ruiz Martínez.  - Letöltés [Stabil verzió][1] -
  Letöltés [Fejlesztői verzió][2]
*	[Stabil verzió][1] letöltése
*	[Fejlesztői verzió][2] letöltése

A kiegészítő abban az esetben hasznos, ha több különböző szövegrészt
szeretnénk összefűzni, majd azt a vágólapról beilleszteni. A vágólap
tartalma törölhető.

## Billentyűparancsok ##
*	NVDA+windows+c: A vágólap tartalmához fűzi a kijelölt  vagy az áttekintő
  kurzorral megjelölt szöveget, és az unikód braille MathML objektumot
  reprezentáló karaktereket is.
*	NVDA+windows+x: Vágólap tartalom törlése.
*	NVDA+windows+f9: Mark the current position of the review cursor as the start of the text to be added to the clipboard. If you use nvda+F9, the text will not be added.
*	 Not assigned: Copies to (or cuts from) the clipboard, with the possibility of being asked for a previous confirmation.

- NVDA+control+shift+c: A kijelölt vagy az áttekintő kurzorral megjelölt
szöveg hozzáfűzése a vágólaphoz.  - NVDA+control+shift+x: A vágólap
tartalmának törlése.  - NVDA+control+f9: Beállítja az áttekintő kurzor
aktuális pontját kijelölés kezdetének.

## Beállítások menü ##
*	Clip Contents Designer settings: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
It's also possible to choose if the added text will be appended or prepended, if available actions (add, clear clipboard, emulate copy and emulate cut) should be performed inmediately or after confirmation, and if confirmations will be requested just if text is contained in the clipboard.

Notes:

*	The above command can be changed from NVDA menu, Preferences submenu,
  Input gestures dialog, Configuration category.
*	Confirmations won't be requested when a message box of NVDA is still
  opened. In those cases, actions will be inmediately performed

## Changes for 8.0 ##

* The add-on settings are shown in the corresponding category of the NVDA
  Settings dialog.
* Requires NVDA 2018.2 or later.
* If needed, you can download the [last version compatible with NVDA
  2017.3][3].

## Changes for 7.0

* In the dialog to configure the Emulate copy and Emulate cut
  functionalities at installation, if you choose no, the commands for these
  features will be removed, so that you can restore the normal behavior for
  control+c and control+x.

## Changes for 6.0

*	 Added options to choose if available actions should be performed after confirmation.
*	Added Emulate copy and Emulate cut commands, which could be assigned from the Input gestures dialog.
*	 Added a dialog to configure the Emulate copy and Emulate cut functionalities at installation. This allows to add the control+c and control+x commands to copy and cut, and be asked if you want to replace the clipboard contents when pressing these keystrokes.
*	Fixed documentation for script_add (Windows+NVDA+c).

## Changes for 5.0 ##

*	The visual presentation of the dialog has been enhanced, adhering to the
  appearance of the dialogs shown in NVDA.
*	Requires NVDA 2016.4 or later.

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

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev

[3]:
https://github.com/nvdaes/clipContentsDesigner/releases/download/7.2/clipContentsDesigner-7.2.nvda-addon
