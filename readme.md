# Clip Contents Designer #
*	Authors: Noelia Ruiz Martínez.
*	Download [stable version][1]
*	Download [development version][2]

This add-on is used to add text to the clipboard, which can be useful when you want to join sections of text together ready for pasting.
The clipboard content can also be cleared.

## Keyboard commands ##
*	NVDA+windows+c: Add selected text, Unicode braille characters which represent MathML objects, or the string which has been marked with the review cursor, to the clipboard.
*	NVDA+windows+x: Clear clipboard contents.
*	NVDA+windows+f9: Mark the current position of the review cursor as the start of the text to be added to the clipboard. If you use nvda+F9, the text will not be added.
*	 Not assigned: Copies to the clipboard, with the possibility of being asked for a previous confirmation.

Note: The above commands can be changed from NVDA menu, Preferences submenu, Input gestures dialog, Text review category.

## Preferences Menu ##
*	Clip Contents Designer settings: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
It's also possible to choose if the added text will be appended or prepended, if available actions (add, clear clipboard and emulate copy) should be performed inmediately of after confirmation, and if confirmations will be requested just if text is contained in the clipboard.

Notes:

*	The above command can be changed from NVDA menu, Preferences submenu, Input gestures dialog, Configuration category.
*	Confirmations won't be requested when a message box of NVDA is still opened. In those cases, actions will be inmediately performed

## Changes for 6.0

*	 Added options to choose if available actions should be performed after confirmation.
*	Added an Emulate copy command, which could be assigned from the Input gestures dialog.
*	 Added a dialog to configure the Emulate copy functionality at installation. This allows to add the control+c command for copying to clipboard, and be asked if you want to replace the clipboard contents when pressing this keystroke.
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
