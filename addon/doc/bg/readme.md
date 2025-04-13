# Дизайнер за съдържанието на клипборда (Clip Contents Designer)

- Автори: Noelia, Abdel.

This add-on is used to add text to the clipboard, which can be useful when you want to join sections of text together ready for pasting.
The clipboard content can also be cleared an shown in browse mode.

## Клавиатурни команди

- NVDA+Windows+C: Добавяне към клипборда на избрания текст, уникод брайлови
  символи представящи обекти на MathML, или низа маркиран с курсора за
  преглед.
- NVDA+Windows+X: Изчистване на съдържанието на клипборда.
- Не е назначено: Копира в (или изрязва от) клипборда, с възможност за
  запитване за потвърждение.
- Не е назначено: Показва текста на клипборда като HTML в режим на
  разглеждане или съобщава, ако клипбордът е празен или има съдържание,
  което не може да бъде представено в съобщение за преглед, например ако
  файлове или папки са копирани от Windows Explorer.
- Не е назначено: Показва текста на клипборда в режим на разглеждане или
  съобщава, ако клипбордът е празен или има съдържание, което не може да
  бъде представено в съобщение за преглед, например ако файлове или папки са
  копирани от Windows Explorer.

## Настройки на дизайнера за съдържанието на клипборда

Този панел е достъпен от менюто на NVDA -> подменю "Настройки" -> диалоговия
прозорец "Настройки".

Съдържа следните контроли:

- Въвеждане на низа, който да се използва като разделител между
  съдържанието, добавено в клипборда: Позволява задаването на разделител,
  който може да се използва за намиране на текстовите сегменти, след като
  целият добавен текст бъде поставен.
- Добавяне на текст преди данните на клипборда: Възможно е също така да се
  избере дали текстът ще бъде добавен преди или след.
- Select the actions which require previous confirmation: You can choose, for each action available, if it should be performed inmediately or after confirmation. Available actions are: add text, clear clipboard, emulate copy and emulate cut.
- Искане на потвърждение, преди да се извършат избраните действия, когато:
  Може да се избере дали потвържденията ще се изискват винаги, само ако
  текстът се съдържа в клипборда или ако клипборда не е празен (например при
  копиране на файл, а не текст).
- Format to show the clipboard text as HTML in browse mode: If you're learning HTML markup language, you may choose Preformatted text in HTML or HTML as shown in a web browser, to have an idea of how your HTML code will be rendered by NVDA in a browser. The difference between preformatted and conventional HTML is that the first option will preserve consecutive spaces and line breaks, and the second one will compact them.  For example, write some HTML tags like h1, h2, li, pre, etc., select and copy the text to clipboard, and use clipContentsDesigner add-on to show the text in a browseable message.
- Maximum number of characters when showing clipboard text in browse mode: Please, be aware that increasing this limit may produce issues if the clipboard contains large strings of text. The default limit is 100000 characters.
- Възстановяване на настройките по подразбиране.

Забележки:

- Confirmations won't be requested when a message box of NVDA is still opened. In those cases, actions will be inmediately performed.
- Emulate copy and emulate cut commands mean that, when these features are enabled, the add-on will take control of control+c and control+x. This will allow to select if a confirmation should be requested before performing the actions corresponding to these keystrokes.

## Changes for 46.0.0

- NVDA will sanitize HTML in browseable messages.
- Added a button to close browseable messages, in addition to the Escape key.

## Changes for 40.0.0

- Added support for Hebrew keyboard.

## Промени във версия 17.0

- Добавката е съвместима с NVDA 2023.1.
- The add-on cannot be run in secure mode.

## Промени във версия 16.0

- Изисква се NVDA 2022.1 или по-нова версия.

## Промени във версия 15.0

- Командата за добавяне на текст към клипборда отново е налична в диалоговия
  прозорец "Жестове на въвеждане".

## Промени във версия 14.0

- Съвместима с NVDA 2021.1.
- Fixed gestures to copy and cut with Persian keyboard, thanks to Mohammadhosein Ghezelsofla.

## Промени във версия 13.0

- Отстранен проблем с визуалното оформление на панела за настройки
  (благодарности за това към Cyrille Bougot).

## Промени във версия 12.0

- Отстранени грешки при използване на емулирано копиране в приложения като
  LibreOffice Writer.
- Improved documentation.
- Added a Clip Contents Designer category to assign input gestures to all commands available for this add-on.
- Fixed bugs when using emulate copy in browsers if focus mode is active.
- You can assign different gestures to show the clipboard textual contents as raw text or formatted in HTML. The Format to show the clipboard text in the settings panel has being modified accordingly, to select the two options available for HTML format.

## Промени във версия 11.0

- Fixed bugs when using emulate copy in applications like LibreOffice Writer.

## Промени във версия 10.0

- Now it's possible to add text marked with the review cursor using standard commands of NVDA (NVDA+f9 and NVDA+f10). NVDA+windows+f9 is no longer used, for a better integration with the new NVDA+shift+f9 command.
- Requires NVDA 2019.3 or later.

## Промени във версия 9.0

- Добавена е възможност за показване на текста на клипборда в режим на
  разглеждане.
- Fixed a bug when using the emulate cut and copy features with an Arabic keyboard layout. This has been fixed by Abdel, added as an add-on author.

## Промени във версия 8.0

- Настройките на добавката се показват в съответната категория на прозореца
  с настройките на NVDA.
- Изисква NVDA 2018.2 или по-нова.
- Requires NVDA 2018.4 or later.

## Промени във версия 7.0

- При инсталиране, в диалоговия прозорец за конфигуриране на функциите за
  емулиране на копиране и изрязване, ако изберете "Не", командите за тези
  функции ще бъдат премахнати, за да можете да възстановите нормалното
  поведение на Control+C и Control+X.
- Requires NVDA 2018.2 or later.

## Промени във версия 6.0

- Добавени са опции за избор дали наличните действия  ще се извършват след
  потвърждение.

## Промени във версия 5.0

- Визуалното представяне на прозореца е подобрено, придържайки се към
  стандарта за изглед на прозорците, извеждани от NVDA.
- Изисква NVDA 2016.4 или по-нова.
- Added a dialog to configure the Emulate copy and Emulate cut functionalities at installation. This allows to add the control+c and control+x commands to copy and cut, and be asked if you want to replace the clipboard contents when pressing these keystrokes.
- Fixed documentation for script_add (Windows+NVDA+c).

## Промени във версия 4.0

- The visual presentation of the dialog has been enhanced, adhering to the appearance of the dialogs shown in NVDA.
- Сега е възможно да изберете дали добавеният текст ще бъде добавен преди
  или след наличния текст, с помощта на опцията "Добави текста преди данните
  в клипборда" в диалоговия прозорец за настройка на Clip Contents Designer.

## Промени във версия 3.0

- Ако е инсталиран MathPlayer, в клипборда могат да се добавят брайлови
  представяния на обекти на MathML,.
- Ако няма зададен разделител, ще бъде поставен един празен ред между
  добавените текстови сегменти.

## Промени във версия 2.0

- Знаци от хинди може да се използват като разделител между добавеното
  съдържание.
- If no separator is set, just a single line will be placed between the added text segments.
- A shortcut can be assigned to open the Clip Contents Designer settings dialog.
- Added a check box in the settings dialog, for choosing if the separator should be copied to be imported when reinstalling the add-on.

## Промени във версия 1.0

- Първоначално издание.

## Changes for 1.0

- Initial version.
