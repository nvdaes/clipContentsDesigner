# Clip Contents Designer #

*	Autorzy: Noelia Ruiz Martínez.
*	Pobierz [wersja stabilna][1]
*	Pobierz [wersja rozwojowa][2]

Ten dodatek pozwala dodawać tekst do schowka, co może być użyteczne, jeśli
chcesz połączyć razem kilka części tekstu w całość gotową do wklejenia.
Zawartość schowka może również być wyczyszczona.

## Skróty klawiszowe ##
*	NVDA+windows+c: dodaje oznaczony tekst, znak brajlowski we formacie
  Unicode przedstawiający obiekty MathML, lub ciąg znaków zaznaczony za
  pomocą kursora przeglądu do schowka.
*	NVDA+windows+x: wyczyść zawartość schowka.
*	NVDA+windows+f9: Zaznacza obecne położenie kursora przeglądu, kiedy początek tekstu ma być dodany do schowka. Po naciśnięciu nvda+F9, tekst nie zostanie dodany do schowka.
*	 Nieprzypisano: Kopiuje do schowka lub wycina z niego, może wystąpić zapytanie o potwierdzenie.

Uwaga: powyższe polecenia mogą zostać zmienione z menu NVDA, Podmenu
Ustawienia, okno zdarzenia wejścia, kategoria przegląd tekstu.

## Menu ustawienia ##
*	Ustawienia Clip Contents Designer: Można ustawić specjalny separator, który pomaga znaleźć fragmenty tekstu gdy cała zawartość schowka została już wklejona.
Można tam też określić, czy dodany tekst będzie czymś poprzedzony, czy nowy tekst znajdzie się za nim. Oprócz tego, można zdecydować, czy dostępne opcje (dodawanie, wyczyszczenie schowka, emulowanie kopiowania i emulowanie wycinania) mają być wykonane od razu, czy po potwierdzeniu oraz czy dodatek będzie prosił o potwierdzenia wtedy, gdy tekst jest w schowku.

Uwagi:

*	Powyższy skrót można zmienić w menu NVDA, podmenu Ustawienia, Zdarzenia
  wejścia, Panel Konfiguracji.
*	Jeśli okno dialogowe NVDA jest nadal otwarte, dodatek nie będzie prosił o
  potwierdzenie. W takim wypadku, czynności zostaną natychmiastowo wykonane.

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

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev

[3]:
https://github.com/nvdaes/clipContentsDesigner/releases/download/7.2/clipContentsDesigner-7.2.nvda-addon
