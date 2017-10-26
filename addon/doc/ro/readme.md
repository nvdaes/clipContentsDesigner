# Clip Contents Designer #

*	Autori: Noelia Ruiz Martinez.
*	Descarcă [versiunea stabilă][1]
*	Descarcă [versiunea în dezvoltare][2]

Acest supliment este utilizat pentru a adăuga text pe planșetă, care poate
fi folositor când dorești să accesezi secțiuni de text împreună gata pentru
a fi lipit. Conținutul de pe planșetă poate, deasemenea, fi curățat.

## Comenzi de taste ##
*	NVDA+Windows+C: Adaugă textul selectat, caracterele Unicode braille care
  reprezintă obiectele MathML, sau string-ul care a fost marcat cu cursorul
  de vizualizare, pe planșetă.
*	NVDA+Windows+X: Curăță contentul de pe planșetă.
*	NVDA+Windows+F9: Marchează poziția de vizualizare curentă din examinarea cursorului ca începutul textului pentru a fi adăugat pe planșetă. Dacă utilizați nvda+F9, textul nu va fi adăugat.
*	 Neatribuită: Copiază, cu posibilitatea de a fi întrebat pentru o confirmare anterioară.

Notă: Comenzile de mai sus pot fi modificate din meniul NVDA, Preferințe,
Gesturi de intrare, Categoria de vizualizare a textului.

## Meniul de preferințe ##
*\TSetări Contents Clip Designer: Permite setarea unui separator care poate fi utilizat pentru a găsi segmente de text odată ce întregul text adăugat este lipit.
Este de asemenea posibil să se aleagă dacă textul adăugat va fi anexat sau prefixat, dacă există opțiuni disponibile (adaugă, curăță planșeta, simulează copia și simulează tăierea) ar trebui să fie efectuate imediat sau după confirmare și dacă confirmările vor fi solicitate doar dacă textul este conținut pe planșetă.

Note:

*	Comanda de mai sus poate fi modificată din meniul NVDA, Preferințe,
  Gesturi de intrare, Categoria de configurare.
*	Confirmările nu vor fi solicitate dacă o casetă de mesaj a NVDA-ului e
  încă deschisă. În aceste cazuri, acțiunile vor fi efectuate imediat

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

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev
