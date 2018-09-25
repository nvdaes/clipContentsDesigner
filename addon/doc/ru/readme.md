# Clip Contents Designer #

*	Авторы: Noelia Ruiz Martínez.
*	Загрузить [стабильную версию][1]
*	Загрузить [разрабатываемую версию][2]

Это дополнение используется для соединения текста в буфере обмена, которое
может быть полезно, если вы хотите объединить разделы вставляемого текста.
Содержимое буфера обмена также можно очищать.

## Команды клавиш ##
*	NVDA+windows+c: Добавить выделенный текст, символы юникода брайля,
  представляющие объекты в MathML, или строку, которая была отмечена
  просмотровым курсором в буфер обмена.
*	NVDA+windows+x: Очистить содержимое буфера обмена.
*	NVDA+windows+f9: Mark the current position of the review cursor as the start of the text to be added to the clipboard. If you use nvda+F9, the text will not be added.
*	 Not assigned: Copies to (or cuts from) the clipboard, with the possibility of being asked for a previous confirmation.

Примечание: Эти команды могут быть изменены в меню NVDA, подменю Параметры,
диалог Жесты ввода, категория просмотр текста.

## Меню Настроек ##
*	Clip Contents Designer settings: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
It's also possible to choose if the added text will be appended or prepended, if available actions (add, clear clipboard, emulate copy and emulate cut) should be performed inmediately or after confirmation, and if confirmations will be requested just if text is contained in the clipboard.

Примечания:

*	Приведенная выше команда может быть изменена из меню NVDA, подменю
  параметры, диалог жесты ввода, категория конфигурация.
*	Confirmations won't be requested when a message box of NVDA is still
  opened. In those cases, actions will be inmediately performed

## Changes for 8.0 ##

* The add-on settings are shown in the corresponding category of the NVDA
  Settings dialog.
* Requires NVDA 2018.2 or later.
* If needed, you can download the [last version compatible with NVDA
  2017.3][3].

## Changes for 7.0

* In the dialog to configure the Emulate copy and Emulate cut
  functionalities at installation, if you choose no, the commands for these
  features will be removed, so that you can restore the normal behavior for
  control+c and control+x.

## Изменения для 6.0

*	 Added options to choose if available actions should be performed after confirmation.
*	Added Emulate copy and Emulate cut commands, which could be assigned from the Input gestures dialog.
*	 Added a dialog to configure the Emulate copy and Emulate cut functionalities at installation. This allows to add the control+c and control+x commands to copy and cut, and be asked if you want to replace the clipboard contents when pressing these keystrokes.
*	Fixed documentation for script_add (Windows+NVDA+c).

## Изменения для 5.0 ##

*	Визуальное представление диалогов было модифицировано, придерживаясь
  внешнего вида диалогов, отображаемых в NVDA.
*	Требуется NVDA 2016.4 или позднее.

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
*	Если разделитель не выбран, между фрагментами текста будет добавляться
  одна пустая строка.
*	A shortcut can be assigned to open the Clip Contents Designer settings
  dialog.
*	Added a check box in the settings dialog, for choosing if the separator
  should be copied to be imported when reinstalling the add-on.

## Изменения для 2.0 ##
*	Символы хинди могут использоваться в качестве разделителя между
  добавляемым содержимым.

## Изменения для 1.0 ##
*	Первоначальная версия.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ccd

[2]: https://addons.nvda-project.org/files/get.php?file=ccd-dev

[3]: https://addons.nvda-project.org/files/get.php?file=ccd-o
