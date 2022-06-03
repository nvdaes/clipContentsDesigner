# Clip Contents Designer #

*	Autorzy: Noelia, Abdel.
*	Pobierz [stabilna wersja][1] (kompatybilna z NVDA 2022.1 i nowszymi)
*	Pobierz [wersja rozwojowa][2] (kompatybilna z NVDA 2022.1 i nowszymi)

Ten dodatek służy do dodawania tekstu do schowka, co może być przydatne, gdy
chcesz połączyć sekcje tekstu gotowe do wklejenia.  Zawartość schowka można
również wyczyścić i wyświetlić w trybie przeglądania.

## Skróty klawiszowe ##

* NVDA+windows+c: dodaje oznaczony tekst, znak brajlowski we formacie
  Unicode przedstawiający obiekty MathML, lub ciąg znaków zaznaczony za
  pomocą kursora przeglądu do schowka.
* NVDA+windows+x: wyczyść zawartość schowka.
* Nieprzypisane: Kopiuje do schowka (lub wycina z niego), z możliwością
  poproszenia o wcześniejsze potwierdzenie.
* Nieprzypisane: Wyświetla tekst schowka jako HTML w trybie przeglądania lub
  informuje, czy schowek jest pusty lub zawiera zawartość, której nie można
  przedstawić w wiadomości z możliwością przeglądania, na przykład jeśli
  pliki lub foldery zostały skopiowane z Eksploratora Windows.
* Nieprzypisane: Wyświetla tekstową zawartość schowka jako zwykły tekst w
  trybie przeglądania lub informuje, czy schowek jest pusty lub zawiera
  zawartość, której nie można przedstawić w wiadomości z możliwością
  przeglądania, na przykład jeśli pliki lub foldery zostały skopiowane z
  Eksploratora Windows.


## Ustawienia Projektanta zawartości klipu ##

Ten panel jest dostępny z menu NVDA, podmenu Preferencje, okna dialogowego
Ustawienia.

Zawiera następujące kontrolki:

* Wpisz ciąg, który ma być używany jako separator między zawartością dodaną
  do schowka: Umożliwia ustawienie separatora, który może być używany do
  znajdowania segmentów tekstu po wklejeniu całego dodanego tekstu.
* Dodaj tekst przed danymi klipu: Można również wybrać, czy dodany tekst
  będzie dodawany, czy poprzedzony.
* Wybierz działania, które wymagają wcześniejszego potwierdzenia: Możesz
  wybrać, dla każdej dostępnej akcji, czy ma być wykonana natychmiast, czy
  po potwierdzeniu. Dostępne działania to: dodawanie tekstu, czyszczenie
  schowka, emulowanie kopiowania i emulowanie cięcia.
* Poproś o potwierdzenie przed wykonaniem wybranych czynności, gdy: Możesz
  wybrać, czy potwierdzenia będą zawsze wymagane, tylko jeśli tekst jest
  zawarty w schowku lub jeśli schowek nie jest pusty (na przykład, jeśli
  plik został skopiowany, a nie tekst).
* Format, aby wyświetlić tekst schowka jako HTML w trybie przeglądania:
  Jeśli uczysz się języka znaczników HTML, możesz wybrać Wstępnie
  sformatowany tekst w HTML lub HTML, jak pokazano w przeglądarce
  internetowej, aby mieć pojęcie o tym, jak kod HTML będzie renderowany
  przez NVDA w przeglądarce. Różnica między wstępnie sformatowanym a
  konwencjonalnym HTML polega na tym, że pierwsza opcja zachowa kolejne
  spacje i podziały wierszy, a druga je zgęści.  Na przykład napisz niektóre
  znaczniki HTML, takie jak h1, h2, li, pre itp., Zaznacz i skopiuj tekst do
  schowka i użyj dodatku clipContentsDesigner, aby wyświetlić tekst w
  wiadomości, którą można przeglądać.
* Maksymalna liczba znaków podczas wyświetlania tekstu schowka w trybie
  przeglądania: Należy pamiętać, że zwiększenie tego limitu może powodować
  problemy, jeśli schowek zawiera duże ciągi tekstu. Domyślny limit to
  100000 znaków.

Uwagi:

* Potwierdzenia nie będą wymagane, gdy okno komunikatu NVDA jest nadal
  otwarte. W takich przypadkach działania będą wykonywane natychmiast.
* Polecenia Emuluj kopiowanie i emuluj wycinanie oznaczają, że gdy te
  funkcje są włączone, dodatek przejmie kontrolę nad control+c i
  control+x. Pozwoli to wybrać, czy przed wykonaniem czynności
  odpowiadających tym naciśnięciom należy zażądać potwierdzenia.

## Zmiany w wersji 16.0
* Wymaga NVDA 2022.1 lub nowszego.

## Zmiany w wersji 15.0
* Polecenie dodawania tekstu do schowka jest ponownie wyświetlane w oknie
  dialogowym gestów wprowadzania.
* Naprawiono gesty do kopiowania i cięcia za pomocą perskiej klawiatury,
  dzięki Mohammadhosein Ghezelsofla.

## Zmiany w wersji 14.0
* Kompatybilny z NVDA 2021.1.

## Zmiany w wersji 13.0 
* Naprawiono błąd w układzie wizualnym panelu ustawień, dzięki Cyrille
  Bougot.
* Ulepszona dokumentacja.
* Dodano kategorię Clip Contents Designer, aby przypisać gesty wprowadzania
  do wszystkich poleceń dostępnych dla tego dodatku.
* Naprawiono błędy podczas korzystania z emulacji kopii w przeglądarkach,
  jeśli tryb koncentracji uwagi jest aktywny.
* Możesz przypisać różne gesty, aby wyświetlić zawartość tekstową schowka
  jako tekst surowy lub sformatowany w formacie HTML. Format wyświetlania
  tekstu schowka w panelu ustawień został odpowiednio zmodyfikowany, aby
  wybrać dwie opcje dostępne dla formatu HTML.

## Zmiany w wersji 12.0
* Naprawiono błędy podczas korzystania z emulacji kopii w aplikacjach takich
  jak LibreOffice Writer.

## Zmiany w wersji 11.0
* Teraz możliwe jest dodanie tekstu oznaczonego kursorem recenzji za pomocą
  standardowych poleceń NVDA (NVDA + f9 i NVDA + f10). NVDA+windows+f9 nie
  jest już używany, co zapewnia lepszą integrację z nowym poleceniem
  NVDA+shift+f9.
* Wymaga NVDA 2019.3 lub nowszego.

## Zmiany w wersji 10.0
* Naprawiono błąd w oknie dialogowym używanym do wyświetlania tekstu
  schowka, gdy jego tytuł zawiera znaki inne niż łacińskie.
* Naprawiono błąd podczas korzystania z funkcji emulacji wycinania i
  kopiowania z arabskim układem klawiatury. Zostało to naprawione przez
  Abdela, dodanego jako autor dodatku.

## Zmiany w wersji 9.0

* Dodano możliwość wyświetlania tekstu schowka w trybie przeglądania.
* Dodano opcję wyboru, czy potwierdzenia będą wymagane, jeśli schowek nie
  jest pusty, na przykład, jeśli pliki lub foldery są kopiowane.
* Wymaga NVDA 2018.4 lub nowszej.

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
