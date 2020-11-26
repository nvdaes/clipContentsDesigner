# Vágólap tartalomtervező #

*	Készítők: Noelia, Abdel.
*	Támogatott NVDA kiadások: 2019.3 és újabb
*	[Stabil verzió][1] letöltése
*	[Fejlesztői verzió][2] letöltése

A kiegészítő abban az esetben hasznos, ha több különböző szövegrészt
szeretnénk összefűzni, majd azt a vágólapról beilleszteni. A vágólap
tartalma törölhető, illetve megjeleníthető böngésző módban.

## Billentyűparancsok ##

* NVDA+windows+c: A vágólap tartalmához fűzi a kijelölt  vagy az áttekintő
  kurzorral megjelölt szöveget, és az unikód braille MathML objektumot
  reprezentáló karaktereket is.
* NVDA+windows+x: Vágólap tartalom törlése.
* Alapértelmezés szerint nincs billentyűparancs hozzárendelve: Másolás a
  vágólapra vagy kivágás onnan a végrehajtás előtt megerősítés kérésével.
* Alapértelmezés szerint nincs billentyűparancs hozzárendelve: A vágólap
  tartalmának megjelenítése böngészőmódú ablakban. Amennyiben nincs
  böngészőmódban megjeleníthető tartalom a vágólapon a program
  figyelmeztet. Akkor is, ha a vágólap üres, és akkor is, ha nincs rajta
  szövegesen megjeleníthető tartalom. Ez utóbbi olyan esetben lehetséges, ha
  pl. fájlokat másoltunk a vágólapra.

Megjegyzés: A fenti parancsok megváltoztathatók az NVDA
menü->Beállítások->Beviteli parancsok ablakában a Szövegáttekintés
kategóriát választva.

## Beállítások menü ##
*	Vágólap tartalomtervező beállításai: Lehetőség van megadni egy elválasztó karaktert, mely minden hozzáadott szövegrész után beillesztésre kerül, így a végén elkülöníthetőek lesznek a különböző helyről hozzáfűzött részek.
Beállítható, hogy a hozzáfűzni kívánt szöveg a vágólap tartalma elé vagy mögé kerüljön. Megadható, hogy mely vágólap műveletek végrehajtása előtt kérjen a program megerősítést. Az is, hogy megerősítést mindig, csak szöveges tartalom esetén vagy csak akkor kérjen, ha a vágólap nem üres.
Megadható továbbá a vágólap tartalmának böngészőmódú megjelenítési formátuma és a megjeleníthető karakterek maximális száma. A limit megadásánál figyelembe kell venni, hogy a nagy mennyiségű szövegek megjelenítése problémákat okozhat. A limit alapértelmezés szerint 100000 karakter.

Megjegyzések:

*	A fenti parancs megváltoztatható az NVDA menü->Beállítások->Beviteli
  parancsok ablakában a konfiguráció kategóriát választva.
*	Amikor az NVDA egy másik üzenetablaka is nyitva van a bővítmény nem kér
  megerősítést a vágólapműveletek előtt, de attól még végrehajtja azokat.

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
