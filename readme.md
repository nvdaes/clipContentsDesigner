# Clip Contents Designer #

## Keyboard commands ##

* VDA+windows+c: Add selected text, Unicode braille characters which represent MathML objects, or the string which has been marked with the review cursor, to the clipboard.
* ot assigned: Copies to (or cuts from) the clipboard, with the possibility of being asked for a previous confirmation.

This panel is available from NVDA's menu, Preferences submenu, Settings dialog.

It contains the following controls:

* Type the string to be used as a separator between contents added to the clipboard: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
* Add text before clip data: It's also possible to choose if the added text will be appended or prepended.
* Select the actions which require previous confirmation: You can choose, for each action available, if it should be performed inmediately or after confirmation. Available actions are: add text, clear clipboard, emulate copy and emulate cut.
* Request confirmation before performing the selected actions when: You can select if confirmations will be requested always, just if text is contained in the clipboard, or if clipboard is not empty (for example if you've copied a file, not text).
* Format to show the clipboard text as HTML in browse mode: If you're learning HTML markup language, you may choose Preformatted text in HTML or HTML as shown in a web browser, to have an idea of how your HTML code will be rendered by NVDA in a browser. The difference between preformatted and conventional HTML is that the first option will preserve consecutive spaces and line breaks, and the second one will compact them.  For example, write some HTML tags like h1, h2, li, pre, etc., select and copy the text to clipboard, and use clipContentsDesigner add-on to show the text in a browseable message.
* Maximum number of characters when showing clipboard text in browse mode: Please, be aware that increasing this limit may produce issues if the clipboard contains large strings of text. The default limit is 100000 characters.
* Show configuration dialog when updating: Uncheck this if you don't want to see a dialog to configure emulate copy and cut when updating the add-on.
* Restore defaults.

Notes:

*	Confirmations won't be requested when a message box of NVDA is still opened. In those cases, actions will be inmediately performed.
* Emulate copy and emulate cut commands mean that, when these features are enabled, the add-on will take control of control+c and control+x. This will allow to select if a confirmation should be requested before performing the actions corresponding to these keystrokes.

## Changes for 49.0.0

* Added a checkbox to decide if a configuration dialog should be shown when the add-on is updated.

## Changes for 46.0.0

* NVDA will sanitize HTML in browseable messages.

## Changes for 22.0.0

* The add-on cannot be run in secure mode.

* The command to add text to clipboard is again presented in the input gestures dialog.

## Changes for 14.0

* Compatible with NVDA 2021.1.

## Changes for 13.0

* Added a Clip Contents Designer category to assign input gestures to all commands available for this add-on.
* Fixed bugs when using emulate copy in browsers if focus mode is active.

## Changes for 11.0

* Now it's possible to add text marked with the review cursor using standard commands of NVDA (NVDA+f9 and NVDA+f10). NVDA+windows+f9 is no longer used, for a better integration with the new NVDA+shift+f9 command.

* Fixed a bug when using the emulate cut and copy features with an Arabic keyboard layout. This has been fixed by Abdel, added as an add-on author.

## Changes for 9.0

* Added the possibility of showing the clipboard text in browse mode.
* Requires NVDA 2018.4 or later.

* The add-on settings are shown in the corresponding category of the NVDA Settings dialog.

## Changes for 7.0

* In the dialog to configure the Emulate copy and Emulate cut functionalities at installation, if you choose no, the commands for these features will be removed, so that you can restore the normal behavior for control+c and control+x.

## Changes for 6.0

*	Added Emulate copy and Emulate cut commands, which could be assigned from the Input gestures dialog.
* Added a dialog to configure the Emulate copy and Emulate cut functionalities at installation. This allows to add the control+c and control+x commands to copy and cut, and be asked if you want to replace the clipboard contents when pressing these keystrokes.
*	Fixed documentation for script_add (Windows+NVDA+c).

## Changes for 5.0 ##

*	The visual presentation of the dialog has been enhanced, adhering to the appearance of the dialogs shown in NVDA.
*	Requires NVDA 2016.4 or later.

## Changes for 4.0 ##

*	Add-on settings are managed from NVDA configuration, so that standard profiles can be used to save different separators, and it's not needed to copy the settings for importing at reinstallation.
*	Now it's possible to choose if the added text will be appended or prepended, using the Add text before clip data check box from the Clip Contents Designer settings dialog.

*	Braille representation of MathML objects can be added to the clipboard if MathPlayer is installed.
*	If no separator is set, just a single line will be placed between the added text segments.
*	A shortcut can be assigned to open the Clip Contents Designer settings dialog.
*	Added a check box in the settings dialog, for choosing if the separator should be copied to be imported when reinstalling the add-on.

## Changes for 2.0 ##

*	Hindi characters can be used as the separator between added contents.

## Changes for 1.0 ##
