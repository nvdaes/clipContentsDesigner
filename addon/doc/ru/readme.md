# Clip Contents Designer #

*	Авторы: Noelia, Abdel.

Это дополнение используется для добавления текста в буфер обмена, что может
быть полезно, когда вы хотите объединить фрагменты текста, готовые к
вставке.  Содержимое буфера обмена также можно очистить и отобразить в
режиме просмотра.

## Команды клавиш ##
*	NVDA+windows+c: Добавить выделенный текст, символы юникода брайля,
  представляющие объекты в MathML, или строку, которая была отмечена
  просмотровым курсором в буфер обмена.
*	NVDA+windows+x: Очистить содержимое буфера обмена.
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


## Настройки Clip Contents Designer ##

Эта панель доступна из меню NVDA, подменю параметров, диалога настроек.

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
* Restore defaults.

Примечания:

* Confirmations won't be requested when a message box of NVDA is still
  opened. In those cases, actions will be inmediately performed.
* Emulate copy and emulate cut commands mean that, when these features are
  enabled, the add-on will take control of control+c and control+x. This
  will allow to select if a confirmation should be requested before
  performing the actions corresponding to these keystrokes.

## Изменения для 22.0
* Added a button to restore defaults in the add-on settings panel.
* The add-on cannot be run in secure mode.

## Изменения для 17.0
* Compatible with NVDA 2023.1.

## Изменения для 16.0
* Требуется NVDA 2022.1 или позднее.

## Изменения для 15.0
* The command to add text to clipboard is again presented in the input
  gestures dialog.
* Fixed gestures to copy and cut with Persian keyboard, thanks to
  Mohammadhosein Ghezelsofla.

## Изменения для 14.0
* Compatible with NVDA 2021.1.

## Изменения для 13.0 
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

## Изменения для 12.0
* Fixed bugs when using emulate copy in applications like LibreOffice
  Writer.

## Изменения для 11.0
* Now it's possible to add text marked with the review cursor using standard
  commands of NVDA (NVDA+f9 and NVDA+f10). NVDA+windows+f9 is no longer
  used, for a better integration with the new NVDA+shift+f9 command.
* Требуется NVDA 2019.3 или позднее.

## Изменения для 10.0
* Fixed a bug in the dialog used to show the clipboard text, when its title
  contains non latin characters.
* Fixed a bug when using the emulate cut and copy features with an Arabic
  keyboard layout. This has been fixed by Abdel, added as an add-on author.

## Изменения для 9.0

* Added the possibility of showing the clipboard text in browse mode.
* Added an option to choose if confirmations will be required if clipboard
  is not empty, for instance, if files or folders are been copied.
* Требуется NVDA 2018.4 или позднее.

## Изменения для 8.0 ##

* The add-on settings are shown in the corresponding category of the NVDA
  Settings dialog.
* Требуется NVDA 2018.2 или позднее.
* If needed, you can download the [last version compatible with NVDA
  2017.3][3].

## Изменения для 7.0

* In the dialog to configure the Emulate copy and Emulate cut
  functionalities at installation, if you choose no, the commands for these
  features will be removed, so that you can restore the normal behavior for
  control+c and control+x.

## Изменения для 6.0

*	Added options to choose if available actions should be performed after
  confirmation.
*	Added Emulate copy and Emulate cut commands, which could be assigned from
  the Input gestures dialog.
*	Added a dialog to configure the Emulate copy and Emulate cut
  functionalities at installation. This allows to add the control+c and
  control+x commands to copy and cut, and be asked if you want to replace
  the clipboard contents when pressing these keystrokes.
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

[3]: https://www.nvaccess.org/addonStore/legacy?file=ccd-o
