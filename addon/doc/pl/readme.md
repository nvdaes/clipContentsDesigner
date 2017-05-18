# Projektant zawartości schowka / Clip Contents Designer #

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
NVDA+windows+f9: oznacz bieżącą pozycję kursora przeglądu jako początek tekstu, który zostanie dodany do schowka.  Jeśli użyjesz nvda+F9, tekst nie zostanie dodany.    Jeśli użyjesz nvda+F9, tekst nie będzie dodany.

Uwaga: powyższe polecenia mogą zostać zmienione z menu NVDA, Podmenu
Ustawienia, okno zdarzenia wejścia, kategoria przegląd tekstu.

## Menu ustawienia ##
*	Ustawienia projektanta zawartości schowka: pozwala ustawić separator, umożliwiający znalezienie segmentów tekstu, gdy cały tekst zostanie wklejony.
Jest także możliwe ustalenie, czy dany tekst będzie dodany na początku lub na końcu.

Uwaga: powyższe polecenie może zostać zmienione z menu NVDA, Podmenu
Ustawienia, okno zdarzenia wejścia, kategoria przegląd tekstu.

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
