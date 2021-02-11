# Clip Contents Designer #

*	Autorzy: Noelia, Abdel.
*	NVDA compatibility: 2019.3 or later
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
*	Not assigned: Copies to (or cuts from) the clipboard, with the possibility
  of being asked for a previous confirmation.
*	Not assigned: Shows the clipboard text as HTML in browse mode, or
  announces if clipboard is empty or has contents which can't be presented
  in a browseable message, for instance if files or folders are been copied
  from Windows Explorer.
*	Not assigned: Shows the textual clipboard contents as plain text in browse
  mode, or announces if clipboard is empty or has contents which can't be
  presented in a browseable message, for instance if files or folders are
  been copied from Windows Explorer.


## Clip Contents Designer settings ##

This panel is available from NVDA's menu, Preferences submenu, Settings
dialog.

It contains the following controls:

* Type the string to be used as a separator between contents added to the
  clipboard: Allows to set a separator which can be used to find the text
  segments once the entire added text is pasted.
* Add text before clip data: It's also possible to choose if the added text
  will be appended or prepended.
* Select the actions which require previous confirmation: You can choose,
  for each action available, if it should be performed inmediately or after
  confirmation. Available actions are: add text, clear clipboard, emulate
  copy and emulate cut.
* Request confirmation before performing the selected actions when: You can
  select if confirmations will be requested always, just if text is
  contained in the clipboard, or if clipboard is not empty (for example if
  you've copied a file, not text).
* Format to show the clipboard text as HTML in browse mode: If you're
  learning HTML markup language, you may choose Preformatted text in HTML or
  HTML as shown in a web browser, to have an idea of how your HTML code will
  be rendered by NVDA in a browser. The difference between preformatted and
  conventional HTML is that the first option will preserve consecutive
  spaces and line breaks, and the second one will compact them.  For
  example, write some HTML tags like h1, h2, li, pre, etc., select and copy
  the text to clipboard, and use clipContentsDesigner add-on to show the
  text in a browseable message.
* Maximum number of characters when showing clipboard text in browse mode:
  Please, be aware that increasing this limit may produce issues if the
  clipboard contains large strings of text. The default limit is 100000
  characters.

Uwagi:

*	Confirmations won't be requested when a message box of NVDA is still
  opened. In those cases, actions will be inmediately performed.
*	Emulate copy and emulate cut commands mean that, when these features are
  enabled, the add-on will take control of control+c and control+x. This
  will allow to select if a confirmation should be requested before
  performing the actions corresponding to these keystrokes.

## Changes for 13.0 
* Fixed an issue in visual layout of the settings panel, thanks to Cyrille
  Bougot.
* Improved documentation.
* Added a Clip Contents Designer category to assign input gestures to all
  commands available for this add-on.
* Fixed bugs when using emulate copy in browsers if focus mode is active.
* You can assign different gestures to show the clipboard textual contents
  as raw text or formatted in HTML. The Format to show the clipboard text in
  the settings panel has being modified accordingly, to select the two
  options available for HTML format.

## Changes for 12.0
* Fixed bugs when using emulate copy in applications like LibreOffice
  Writer.

## Changes for 11.0
* Now it's possible to add text marked with the review cursor using standard
  commands of NVDA (NVDA+f9 and NVDA+f10). NVDA+windows+f9 is no longer
  used, for a better integration with the new NVDA+shift+f9 command.
* Requires NVDA 2019.3 or later.

## Zmiany w wersji 10.0
* Fixed a bug in the dialog used to show the clipboard text, when its title
  contains non latin characters.
* Fixed a bug when using the emulate cut and copy features with an Arabic
  keyboard layout. This has been fixed by Abdel, added as an add-on author.

## Zmiany w wersji 9.0

* Added the possibility of showing the clipboard text in browse mode.
* Added an option to choose if confirmations will be required if clipboard
  is not empty, for instance, if files or folders are been copied.
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
