# Vágólap tartalomtervező #
*   - Készítők: Noelia Ruiz Martínez.  - Letöltés [Stabil verzió][1] -
    Letöltés [Fejlesztői verzió][2]
*   [Stabil verzió][1] letöltése
*   [Fejlesztői verzió][2] letöltése

A kiegészítő abban az esetben hasznos, ha több különböző szövegrészt
szeretnénk összefűzni, majd azt a vágólapról beilleszteni. A vágólap
tartalma törölhető.

## Billentyűparancsok ##
*   NVDA+windows+c: A vágólap tartalmához fűzi a kijelölt  vagy az áttekintő
    kurzorral megjelölt szöveget, és az unikód braille MathML objektumot
    reprezentáló karaktereket is.
*   NVDA+windows+x: Vágólap tartalom törlése.
*   NVDA+windows+f9: Megadja az áttekintő kurzor aktuális pozícióját
    kijelölés kezdetének. Az NVDA+f9 használata esetén a szöveg nem kerül
    hozzáfűzésre a vágólaphoz.

- NVDA+control+shift+c: A kijelölt vagy az áttekintő kurzorral megjelölt
szöveg hozzáfűzése a vágólaphoz.  - NVDA+control+shift+x: A vágólap
tartalmának törlése.  - NVDA+control+f9: Beállítja az áttekintő kurzor
aktuális pontját kijelölés kezdetének.

## Beállítások menü ##
Vágólap tartalomtervező beállításai: Lehetőség van megadni egy elválasztó karaktert, mely minden hozzáadott szövegrész után beillesztésre kerül, így könnyen elkülöníthetőek az egyes kijelölések.Lehetősége van a megadott karaktert a saját NVDA beállítások mappába is bemásolni, így ez a kiegészítő újratelepítése esetén beimportálható.

Megjegyzés: A fenti parancsok megváltoztathatóak az NVDA
menü->Beállítások->Beviteli parancsok ablakában a konfiguráció kategóriát
választva.

## A 4.0 változásai ##
*   A bővítmény beállításai az NVDA konfigurációjában kezelhetők, így a
    sztenderd profilokat használhatjuk az elválasztók elmentésére, így a
    beállításokat nem kell újra bemásolni az újratelepítéskor történő
    importáláskor.
*   Most már ki lehet választani, hogy a hozzáadni kívánt szöveget a
    tartalom elé vagy mögé csatoljuk, ha használjuk a "vágólap tartalma elé"
    jelölőnégyzetet a vágólaptartalom-tervező beállítása párbeszédpanelén.

## A 3.0 változásai ##
*   Ha a MathPlayer telepítve van, a MathMl objektumok braille
    reprezentációja kerül hozzáfűzésre a vágólaphoz.
*   Ha nincs megadva elválasztó karakter, egy üres sor kerül beszúrásra a
    két szöveg közé.
*   Billentyűparancsot adtak hozzá a Vágólaptartalom-tervező beállítás
    ablakának eléréséhez.
*   Hozzáadtak egy jelölőnégyzetet, mellyel szabályozható, hogy az
    elválasztó karaktert bemásolja-e a bővítmény a saját beállítások
    mappájába a későbbi importáláshoz.

## A 2.0 változásai ##
*   Hindi karakterek is használhatóak az összefűzött szövegek közötti
    elválasztóként.

## Az 1.0 változásai ##
*   - Első kiadás

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev
