# Clip Contents Designer #
*   Авторы: Noelia Ruiz Martínez.
*   Загрузить [стабильную версию][1]
*   Загрузить [разрабатываемую версию][2]

Это дополнение используется для соединения текста в буфере обмена, которое
может быть полезно, если вы хотите объединить разделы вставляемого текста.
Содержимое буфера обмена также можно очищать.

## Команды клавиш ##
*   NVDA+windows+c: Append selected text, Unicode braille characters which
    represent MathML objects, or the string which has been marked with the
    review cursor, to the clipboard.
*   NVDA+windows+x: Очистить содержимое буфера обмена.
*   NVDA+windows+f9: Отметить текущую позицию курсора обзора как начало
    текста, который будет добавлен в буфер обмена.  Если вы используете
    nvda+F9, текст не будет добавлен.

Примечание: Эти команды могут быть изменены в меню NVDA, подменю Параметры,
диалог Жесты ввода, категория просмотр текста.

## Меню Настроек ##
*   Clip Contents Designer settings: Allows to set a separator which can be
    used to find the text segments once the entire appended text is
    pasted. You can also choose if the separator should be copied to your
    personal NVDA's configuration folder, so that it can be imported when
    reinstalling the add-on.

Note: The above command can be changed from NVDA menu, Preferences submenu,
Input gestures dialog, Configuration category.

## Changes for 3.0 ##
*   Braille representation of MathML objects can be appended to the
    clipboard if MathPlayer is installed.
*   If no separator is set, just a single line will be placed between the
    appended text segments.
*   A shortcut can be assigned to open the Clip Contents Designer settings
    dialog.
*   Added a check box in the settings dialog, for choosing if the separator
    should be copied to be imported when reinstalling the add-on.

## Changes for 2.0 ##
*   Hindi characters can be used as the separator between appended contents.

## Изменения для 1.0 ##
*   Первоначальная версия.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev
