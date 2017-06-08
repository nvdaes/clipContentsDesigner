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
*	NVDA+windows+f9: Mark the current position of the review cursor as the start of the text to be added to the clipboard.
    If you use nvda+F9, the text will not be added.

- NVDA+control+shift+c: A kijelölt vagy az áttekintő kurzorral megjelölt
szöveg hozzáfűzése a vágólaphoz.  - NVDA+control+shift+x: A vágólap
tartalmának törlése.  - NVDA+control+f9: Beállítja az áttekintő kurzor
aktuális pontját kijelölés kezdetének.

## Beállítások menü ##
*	Clip Contents Designer settings: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
It's also possible to choose if the added text will be appended or prepended.

Megjegyzés: A fenti parancsok megváltoztathatóak az NVDA
menü->Beállítások->Beviteli parancsok ablakában a konfiguráció kategóriát
választva.

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

[1]: https://addons.nvda-project.org/files/get.php?file=ccd

[2]: https://addons.nvda-project.org/files/get.php?file=ccd-dev
