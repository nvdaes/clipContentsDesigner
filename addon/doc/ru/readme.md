# Clip Contents Designer #

*	Авторы: Noelia Ruiz Martínez.
*	Загрузить [стабильную версию][1]
*	Загрузить [разрабатываемую версию][2]

This add-on is used to add text to the clipboard, which can be useful when
you want to join sections of text together ready for pasting.  The clipboard
content can also be cleared.

## Команды клавиш ##
*	NVDA+windows+c: Add selected text, Unicode braille characters which
  represent MathML objects, or the string which has been marked with the
  review cursor, to the clipboard.
*	NVDA+windows+x: Очистить содержимое буфера обмена.
*	NVDA+windows+f9: Mark the current position of the review cursor as the start of the text to be added to the clipboard.
    If you use nvda+F9, the text will not be added.

Примечание: Эти команды могут быть изменены в меню NVDA, подменю Параметры,
диалог Жесты ввода, категория просмотр текста.

## Меню Настроек ##
*	Clip Contents Designer settings: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
It's also possible to choose if the added text will be appended or prepended.

Note: The above command can be changed from NVDA menu, Preferences submenu,
Input gestures dialog, Configuration category.

## Изменения для 5.0 ##

*	The visual presentation of the dialog has been enhanced, adhering to the
  appearance of the dialogs shown in NVDA.
*	Requires NVDA 2016.4 or later.

## Изменения для 4.0 ##
*	Add-on settings are managed from NVDA configuration, so that standard
  profiles can be used to save different separators, and it's not needed to
  copy the settings for importing at reinstallation.
*	Now it's possible to choose if the added text will be appended or
  prepended, using the Add text before clip data check box from the Clip
  Contents Designer settings dialog.

## Изменения для 3.0 ##
*	Braille representation of MathML objects can be added to the clipboard if
  MathPlayer is installed.
*	If no separator is set, just a single line will be placed between the
  added text segments.
*	A shortcut can be assigned to open the Clip Contents Designer settings
  dialog.
*	Added a check box in the settings dialog, for choosing if the separator
  should be copied to be imported when reinstalling the add-on.

## Изменения для 2.0 ##
*	Hindi characters can be used as the separator between added contents.

## Изменения для 1.0 ##
*	Первоначальная версия.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ccd

[2]: https://addons.nvda-project.org/files/get.php?file=ccd-dev
