# Clip Contents Designer #


* Type the string to be used as a separator between contents added to the clipboard: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
* Add text before clip data: It's also possible to choose if the added text will be appended or prepended.
* Request confirmation before performing the selected actions when: You can select if confirmations will be requested always, just if text is contained in the clipboard, or if clipboard is not empty (for example if you've copied a file, not text).
* Format to show the clipboard text as HTML in browse mode: If you're learning HTML markup language, you may choose Preformatted text in HTML or HTML as shown in a web browser, to have an idea of how your HTML code will be rendered by NVDA in a browser. The difference between preformatted and conventional HTML is that the first option will preserve consecutive spaces and line breaks, and the second one will compact them.  For example, write some HTML tags like h1, h2, li, pre, etc., select and copy the text to clipboard, and use clipContentsDesigner add-on to show the text in a browseable message.
* Maximum number of characters when showing clipboard text in browse mode: Please, be aware that increasing this limit may produce issues if the clipboard contains large strings of text. The default limit is 100000 characters.
* Restore defaults.

Notes:

*	Confirmations won't be requested when a message box of NVDA is still opened. In those cases, actions will be inmediately performed.
* Emulate copy and emulate cut commands mean that, when these features are enabled, the add-on will take control of control+c and control+x. This will allow to select if a confirmation should be requested before performing the actions corresponding to these keystrokes.

## Changes for 46.0.0

## Changes for 40.0.0

* Added support for Hebrew keyboard.


## Changes for 22.0.0

* Fixed gestures to copy and cut with Persian keyboard, thanks to Mohammadhosein Ghezelsofla.

* Fixed an issue in visual layout of the settings panel, thanks to Cyrille Bougot.
* Improved documentation.
* Fixed bugs when using emulate copy in browsers if focus mode is active.
* You can assign different gestures to show the clipboard textual contents as raw text or formatted in HTML. The Format to show the clipboard text in the settings panel has being modified accordingly, to select the two options available for HTML format.

## Changes for 12.0

* Fixed bugs when using emulate copy in applications like LibreOffice Writer.

* Now it's possible to add text marked with the review cursor using standard commands of NVDA (NVDA+f9 and NVDA+f10). NVDA+windows+f9 is no longer used, for a better integration with the new NVDA+shift+f9 command.
* Requires NVDA 2019.3 or later.

* Fixed a bug when using the emulate cut and copy features with an Arabic keyboard layout. This has been fixed by Abdel, added as an add-on author.
* Requires NVDA 2018.4 or later.

# Changes for 8.0 ##

* Requires NVDA 2018.2 or later.

* In the dialog to configure the Emulate copy and Emulate cut functionalities at installation, if you choose no, the commands for these features will be removed, so that you can restore the normal behavior for control+c and control+x.
*	Add-on settings are managed from NVDA configuration, so that standard profiles can be used to save different separators, and it's not needed to copy the settings for importing at reinstallation.
*	Now it's possible to choose if the added text will be appended or prepended, using the Add text before clip data check box from the Clip Contents Designer settings dialog.
*	A shortcut can be assigned to open the Clip Contents Designer settings dialog.
*	Added a check box in the settings dialog, for choosing if the separator should be copied to be imported when reinstalling the add-on.

*	Hindi characters can be used as the separator between added contents.

## Changes for 1.0 ##

