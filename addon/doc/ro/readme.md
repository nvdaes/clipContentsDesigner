# Clip Contents Designer #

*	Autori: Noelia Ruiz Martínez.
*	Compatibilitate NVDA: 2018.2 - 2019.1.
*	Descarcă [versiunea stabilă][1]
*	Descarcă [versiunea în dezvoltare][2]

This add-on is used to add text to the clipboard, which can be useful when
you want to join sections of text together ready for pasting.  The clipboard
content can also be cleared an shown in browse mode.

## Comenzi de taste ##
*	NVDA+Windows+C: Adaugă textul selectat, caracterele Unicode braille care
  reprezintă obiectele MathML, sau string-ul care a fost marcat cu cursorul
  de vizualizare, pe planșetă.
*	NVDA+Windows+X: Curăță contentul de pe planșetă.
*	NVDA+windows+f9: Mark the current position of the review cursor as the start of the text to be added to the clipboard. If you use nvda+F9, the text will not be added.
*	 Not assigned: Copies to (or cuts from) the clipboard, with the possibility of being asked for a previous confirmation.
*	 Not assigned: Shows the clipboard text in browse mode, or announces if clipboard is empty or has contents which can't be presented in a browseable message, for instance if files or folders are been copied from Windows Explorer..

Notă: Comenzile de mai sus pot fi modificate din meniul NVDA, Preferințe,
Gesturi de intrare, Categoria de vizualizare a textului.

## Meniul de preferințe ##
*	Clip Contents Designer settings: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
It's also possible to choose if the added text will be appended or prepended, if available actions (add, clear clipboard, emulate copy and emulate cut) should be performed inmediately or after confirmation, and if confirmations will be requested always, just if text is contained in the clipboard, or if clipboard is not empty.
Furthermore, it's possible to change the format and maximum number of characters of the clipboard text which will be shown in browse mode. Please, be aware that increasing this limit may produce issues if the clipboard contains large strings of text. The default limit is 100000 characters.

Note:

*	Comanda de mai sus poate fi modificată din meniul NVDA, Preferințe,
  Gesturi de intrare, Categoria de configurare.
*	Confirmările nu vor fi solicitate dacă o casetă de mesaj a NVDA-ului e
  încă deschisă. În aceste cazuri, acțiunile vor fi efectuate imediat

## Changes for 9.0

* Added the possibility of showing the clipboard text in browse mode.
* Added an option to choose if confirmations will be required if clipboard
  is not empty, for instance, if files or folders are been copied.
* Requires NVDA 2018.4 or later.

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
