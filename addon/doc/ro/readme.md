# Clip Contents Designer #

*	Autori: Noelia și Abdel.
*	Compatibilitate NVDA: 2018.4 - 2019.2.
*	Descarcă [versiunea stabilă][1]
*	Descarcă [versiunea în dezvoltare][2]

Acest supliment este utilizat pentru a adăuga text pe planșetă, care poate
fi folositor când dorești să accesezi secțiuni de text împreună gata pentru
a fi lipit. Conținutul de pe planșetă poate, deasemenea, fi curățat și
afișat în modul de navigare.

## Comenzi de taste ##
*	NVDA+Windows+C: Adaugă textul selectat, caracterele Unicode braille care
  reprezintă obiectele MathML, sau string-ul care a fost marcat cu cursorul
  de vizualizare, pe planșetă.
*	NVDA+Windows+X: Curăță contentul de pe planșetă.
*	NVDA+Windows+F9: Marchează poziția de vizualizare curentă din examinarea cursorului ca începutul textului pentru a fi adăugat pe planșetă. Dacă utilizați NVDA+F9, textul nu va fi adăugat.
*	 Neatribuită: Copiază, cu posibilitatea de a fi întrebat pentru o confirmare anterioară.
*	 Neatribuită: Afișează textul de pe planșetă în modul de navigare sau anunță dacă planșeta este goală ori are conținut care nu poate fi prezentat într-un mesaj de navigare, un bun exemplu fiind copierea fișierelor sau a folderelor din Windows Explorer..

Notă: Comenzile de mai sus pot fi modificate din meniul NVDA, Preferințe,
Gesturi de intrare, Categoria de vizualizare a textului.

## Meniul de preferințe ##
*\TSetări Contents Clip Designer: Permite setarea unui separator care poate fi utilizat pentru a găsi segmente de text odată ce întregul text adăugat este lipit.
Este de asemenea posibil să se aleagă dacă textul adăugat va fi anexat sau prefixat, dacă există opțiuni disponibile (adaugă, curăță planșeta, simulează copia și simulează tăierea) ar trebui să fie efectuate imediat sau după confirmare și dacă confirmările vor fi solicitate doar dacă textul este conținut pe planșetă.
În plus, puteți modifica formatul și numărul maxim de caractere pe care textul de pe planșetă care va fi afișat în modul de navigare trebuie să îl aibă. Vă rugăm să aveți în vedere faptul că, cu cât e mai mare limita, cu atât mai mult sunt șanse să apară probleme. Limita implicită este de 100000 de caractere.

Note:

*	Comanda de mai sus poate fi modificată din meniul NVDA, Preferințe,
  Gesturi de intrare, Categoria de configurare.
*	Confirmările nu vor fi solicitate dacă o casetă de mesaj a NVDA-ului e
  încă deschisă. În aceste cazuri, acțiunile vor fi efectuate imediat

## Modificări în 10.0
* S-a rezolvat o problemă în dialog care făcea să se afișeze textul de pe
  planșetă când titlul său conținea caractere nelatine.
* S-a rezolvat o problemă întâmpinată la utilizarea copierii și a tăierii
  simulate cu o tastatură arabă. A fost rezolvată de Abdel, care acum are
  statutul de autor al suplimentului.

## Modificări în 9.0

* Acum, este posibilă afișarea textului aflat pe planșetă în modul de
  navigare.
* S-a adăugat o opțiune care vă permite să alegeți dacă vor fi sau nu
  necesare confirmările îb cazul în care planșeta nu este goală, un bun
  exemplu fiind copierea fișierelor sau a folderelor.
* Necesită NVDA 2018.4 sau mai nou.

## Modificări în 8.0 ##

* Setările suplimentului sunt afișate în categoria corespunzătoare a
  dialogului setărilor NVDA..
* Necesită NVDA 2018.2 sau mai nou.
* Dacă e musai, puteți să descărcați [ultima versiune compatibilă cu NVDA
  2017.3][3].

## Modificări în 7.0

* În dialogul pentru configurarea copierii și tăierii simulate la instalare,
  dacă alegeți nu, comenzile pentru aceste caracteristici vor fi șterse,
  astfel încât să puteți restaura comportamentul normal pentru control+c și
  control+x.

## Modificări în 6.0

*	 Au fost adăugate opțiuni pentru a alege dacă opțiunile disponibile ar trebui efectuate după confirmare.
*	 Au fost adăugate comenzile de simulare a copiei și a tăierii, care pot fi atribuite din dialogul gesturilor de intrare.
*	 A fost adăugat un dialog pentru configurarea funcționalităților de simulare a copiei și a tăierii la instalare. Aceasta permite adăugarea comenzii control+c și control+x pentru copiere și tăiere. Veți fi întrebat dacă vreți să înlocuiți conținuturile planșetei la apăsarea acestor combinații de taste.
*	A fost reparată documentația pentru script_add (Windows+NVDA+c).

## Modificări în 5.0 ##

*	Prezentarea vizuală a dialogului a fost îmbunătățită, aderând la aspectul
  dialogurilor afișate în NVDA.
*	Necesită NVDA 2016.4 sau mai nou.

## Modificări din 4.0 ##
*	Setările suplimentului sunt gestionate din configurarea NVDA, deci
  profilurile implicite pot fi folosite pentru a salva diferite separatoare,
  și nu este nevoie să copiezi setările pentru a le importa la reinstalare.
*	Acum este posibilă selectarea dacă textul adăugat va fi anexat sau
  prefixat, utilizând căsuța Adăugare text din dialogul de setări al Clip
  Contents Designer-ului.

## Modificări din 3.0 ##
*	Reprezentarea Braille din obiectele MathML poate fi adăugat pe planșetă
  dacă MathPlayer este instalat.
*	Dacă niciun separator nu este setat, o singură linie va fi adăugată între
  segmentele textului adăugat.
*	O scurtătură poate fi definită pentru a deschide setările Clip Contents
  Designer-ului.
*	A fost adăugată o căsuță în dialogul de setări, pentru a selecta dacă
  separatorul trebuie să fie copiat pentru a fi immportat când reinstalezi
  add-on-ul.

## Modificări din 2.0 ##
*	Caracterele indiene pot fi folosite ca separator între content-ul adăugat.

## Modificări din 1.0 ##
*	Versiunea inițială.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ccd

[2]: https://addons.nvda-project.org/files/get.php?file=ccd-dev

[3]: https://addons.nvda-project.org/files/get.php?file=ccd-o
