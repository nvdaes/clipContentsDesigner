# Clip Contents Designer #
*	Authors: Noelia, Abdel.
*	NVDA compatibility: 2019.3 or later
*	Download [stable version][1]
*	Download [development version][2]

This add-on is used to add text to the clipboard, which can be useful when you want to join sections of text together ready for pasting.
The clipboard content can also be cleared an shown in browse mode.

## Keyboard commands ##
*	NVDA+windows+c: Add selected text, Unicode braille characters which represent MathML objects, or the string which has been marked with the review cursor, to the clipboard.
*	NVDA+windows+x: Clear clipboard contents.
*	 Not assigned: Copies to (or cuts from) the clipboard, with the possibility of being asked for a previous confirmation.
*	 Not assigned: Shows the clipboard text as HTML in browse mode, or announces if clipboard is empty or has contents which can't be presented in a browseable message, for instance if files or folders are been copied from Windows Explorer.
*	 Not assigned: Shows the textual clipboard contents as plain text in browse mode, or announces if clipboard is empty or has contents which can't be presented in a browseable message, for instance if files or folders are been copied from Windows Explorer.


## Clip Contents Designer settings ##

This panel is available from NVDA's menu, Preferences submenu, Settings dialog.

It contains the following controls:

* Type the string to be used as a separator between contents added to the clipboard: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
* Add text before clip data: It's also possible to choose if the added text will be appended or prepended.
* Select the actions which require previous confirmation: You can choose, for each action available, if it should be performed inmediately or after confirmation. Available actions are: add text, clear clipboard, emulate copy and emulate cut.
* Request confirmation before performing the selected actions when: You can select if confirmations will be requested always, just if text is contained in the clipboard, or if clipboard is not empty (for example if you've copied a file, not text).
* Format to show the clipboard text as HTML in browse mode: If you're learning HTML markup language, you may choose Preformatted text in HTML or HTML as shown in a web browser, to have an idea of how your HTML code will be rendered by NVDA in a browser. The difference between preformatted and conventional HTML is that the first option will preserve consecutive spaces and line breaks, and the second one will compact them.  For example, write some HTML tags like h1, h2, li, pre, etc., select and copy the text to clipboard, and use clipContentsDesigner add-on to show the text in a browseable message.
* Maximum number of characters when showing clipboard text in browse mode: Please, be aware that increasing this limit may produce issues if the clipboard contains large strings of text. The default limit is 100000 characters.

Notes:

*	Confirmations won't be requested when a message box of NVDA is still opened. In those cases, actions will be inmediately performed.
* Emulate copy and emulate cut commands mean that, when these features are enabled, the add-on will take control of control+c and control+x. This will allow to select if a confirmation should be requested before performing the actions corresponding to these keystrokes.

## Changes for 14.0
* Compatible with NVDA 2021.1.

## Changes for 13.0 
* Fixed an issue in visual layout of the settings panel, thanks to Cyrille Bougot.
* Improved documentation.
* Added a Clip Contents Designer category to assign input gestures to all commands available for this add-on.
* Fixed bugs when using emulate copy in browsers if focus mode is active.
* You can assign different gestures to show the clipboard textual contents as raw text or formatted in HTML. The Format to show the clipboard text in the settings panel has being modified accordingly, to select the two options available for HTML format.

## Changes for 12.0
* Fixed bugs when using emulate copy in applications like LibreOffice Writer.

## Changes for 11.0
* Now it's possible to add text marked with the review cursor using standard commands of NVDA (NVDA+f9 and NVDA+f10). NVDA+windows+f9 is no longer used, for a better integration with the new NVDA+shift+f9 command.
* Requires NVDA 2019.3 or later.

## Changes for 10.0
* Fixed a bug in the dialog used to show the clipboard text, when its title contains non latin characters.
* Fixed a bug when using the emulate cut and copy features with an Arabic keyboard layout. This has been fixed by Abdel, added as an add-on author.

## Changes for 9.0

* Added the possibility of showing the clipboard text in browse mode.
* Added an option to choose if confirmations will be required if clipboard is not empty, for instance, if files or folders are been copied.
* Requires NVDA 2018.4 or later.

## Changes for 8.0 ##

* The add-on settings are shown in the corresponding category of the NVDA Settings dialog.
* Requires NVDA 2018.2 or later.
* If needed, you can download the [last version compatible with NVDA 2017.3][3].

## Changes for 7.0

* In the dialog to configure the Emulate copy and Emulate cut functionalities at installation, if you choose no, the commands for these features will be removed, so that you can restore the normal behavior for control+c and control+x.

## Changes for 6.0

*	 Added options to choose if available actions should be performed after confirmation.
*	Added Emulate copy and Emulate cut commands, which could be assigned from the Input gestures dialog.
*	 Added a dialog to configure the Emulate copy and Emulate cut functionalities at installation. This allows to add the control+c and control+x commands to copy and cut, and be asked if you want to replace the clipboard contents when pressing these keystrokes.
*	Fixed documentation for script_add (Windows+NVDA+c).

## Changes for 5.0 ##

*	The visual presentation of the dialog has been enhanced, adhering to the appearance of the dialogs shown in NVDA.
*	Requires NVDA 2016.4 or later.

## Changes for 4.0 ##
*	Add-on settings are managed from NVDA configuration, so that standard profiles can be used to save different separators, and it's not needed to copy the settings for importing at reinstallation.
*	Now it's possible to choose if the added text will be appended or prepended, using the Add text before clip data check box from the Clip Contents Designer settings dialog.

## Changes for 3.0 ##
*	Braille representation of MathML objects can be added to the clipboard if MathPlayer is installed.
*	If no separator is set, just a single line will be placed between the added text segments.
*	A shortcut can be assigned to open the Clip Contents Designer settings dialog.
*	Added a check box in the settings dialog, for choosing if the separator should be copied to be imported when reinstalling the add-on.

## Changes for 2.0 ##
*	Hindi characters can be used as the separator between added contents.

## Changes for 1.0 ##
*	Initial version.

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev

[3]: http://addons.nvda-project.org/files/get.php?file=ccd-o
