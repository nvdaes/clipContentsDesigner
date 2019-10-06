# Clip Contents Designer #

*	Authors: Noelia, Abdel.
*	NVDA compatibility: 2018.4 to 2019.2.
*	Pobierz [wersja stabilna][1]
*	Pobierz [wersja rozwojowa][2]

This add-on is used to add text to the clipboard, which can be useful when
you want to join sections of text together ready for pasting.  The clipboard
content can also be cleared an shown in browse mode.

## Skróty klawiszowe ##
*	NVDA+windows+c: dodaje oznaczony tekst, znak brajlowski we formacie
  Unicode przedstawiający obiekty MathML, lub ciąg znaków zaznaczony za
  pomocą kursora przeglądu do schowka.
*	NVDA+windows+x: wyczyść zawartość schowka.
*	NVDA+windows+f9: Mark the current position of the review cursor as the start of the text to be added to the clipboard. If you use nvda+F9, the text will not be added.
*	 Not assigned: Copies to (or cuts from) the clipboard, with the possibility of being asked for a previous confirmation.
*	 Not assigned: Shows the clipboard text in browse mode, or announces if clipboard is empty or has contents which can't be presented in a browseable message, for instance if files or folders are been copied from Windows Explorer..

Uwaga: powyższe polecenia mogą zostać zmienione z menu NVDA, Podmenu
Ustawienia, okno zdarzenia wejścia, kategoria przegląd tekstu.

## Menu ustawienia ##
*	Clip Contents Designer settings: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
It's also possible to choose if the added text will be appended or prepended, if available actions (add, clear clipboard, emulate copy and emulate cut) should be performed inmediately or after confirmation, and if confirmations will be requested always, just if text is contained in the clipboard, or if clipboard is not empty.
Furthermore, it's possible to change the format and maximum number of characters of the clipboard text which will be shown in browse mode. Please, be aware that increasing this limit may produce issues if the clipboard contains large strings of text. The default limit is 100000 characters.

Uwagi:

*	Powyższy skrót można zmienić w menu NVDA, podmenu Ustawienia, Zdarzenia
  wejścia, Panel Konfiguracji.
*	Jeśli okno dialogowe NVDA jest nadal otwarte, dodatek nie będzie prosił o
  potwierdzenie. W takim wypadku, czynności zostaną natychmiastowo wykonane.

## Changes for 10.0
* Fixed a bug in the dialog used to show the clipboard text, when its title
  contains non latin characters.
* Fixed a bug when using the emulate cut and copy features with an Arabic
  keyboard layout. This has been fixed by Abdel, added as an add-on author.

## Changes for 9.0

* Added the possibility of showing the clipboard text in browse mode.
* Added an option to choose if confirmations will be required if clipboard
  is not empty, for instance, if files or folders are been copied.
* Requires NVDA 2018.4 or later.

## Zmiany w wersji 8.0 ##

* Ustawienia dodatku są wyświetlane w odpowiedniej kategorii dialogu
  ustawień NVDA.
* Wymaga NVDA 2018.2 lub nowszej.
* W razie potrzeby, można pobrać [najnowszą wersję zgodną z NVDA 2017.3][3].

## Zmiany w wersji 7.0

* In the dialog to configure the Emulate copy and Emulate cut
  functionalities at installation, if you choose no, the commands for these
  features will be removed, so that you can restore the normal behavior for
  control+c and control+x.

## Zmiany w wersji 6.0

*	 Dodano opcje pozwalające wybrać, czy dostępne czynności mają być wykonane dopiero po ich potwierdzeniu.
*	Dodano skróty emulowania kopiowania i emulowania wycinania, które można przypisać w oknie dialogowym Zdarzeń wejścia.
*	 Dodano okno dialogowe służące do ustawiania funkcji emulowania kopiowania i emulowania wycinania podczas instalacji dodatku. Pozwala to na dodawanie skrótów control+c i control+x do kopiowania i wycinania, oraz wywołania pytania, czy zawartość schowka ma zostać zastąpiona po naciśnięciu tych skrótów.
*	Poprawiono dokumentację dla skryptu_add (Windows+NVDA+c).

## Zmiany w wersji 5.0 ##

*	Wizualna prezentacja dialogów została ulepszona, aby była zgodna z
  wyświetlanymi dialogami w NVDA.
*	Wymaga NVDA 2016.4 lub nowszą wersje.

## Zmiany w wersji 4.0 ##
*	Ustawieniami dodatku teraz można zarządzać z samej konfiguracji NVDA, i z
  tego powodu teraz profile konfiguracyjne mogą być użyte do zachowywania
  różnych separatorów, a właściwie, teraz staje się niepotrzebnym kopiowanie
  ustawień separatora podczas reinstalacji.
*	Teraz można wybrać, czy tekst kopiowany ma być dodawany na końcu lub na
  początku, używając pola wyboru Dodaj tekst przed danymi Clip z dialogu
  ustawień projektanta zawartości schowka.

## Zmiany w wersji 3.0 ##
*	Wyświetlony brajl z MathML mogą być dodany do schowka, jeżeli MathPlayer
  jest zainstalowany.
*	Jeżeli separator nie jest ustawiony, będzie wstawiona pojedyńcza linia
  pomiędzy odcinkami dodanego tekstu.
*	Teraz można przydzielić skrót do otwierania dialogu ustawień Projektanta
  zawartości schowka.
*	Dodane pole wyboru, dla wybierania czy separator musi być importowany
  podczas reinstalacji dodatku.

## Zmiany w wersji 2.0 ##
*	Znaki Dewanagari mogą być używane jako separator dodawanej treści.

## Zmiany dla 1.0 ##
*	Pierwsze wydanie.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ccd

[2]: https://addons.nvda-project.org/files/get.php?file=ccd-dev

[3]: https://addons.nvda-project.org/files/get.php?file=ccd-o
