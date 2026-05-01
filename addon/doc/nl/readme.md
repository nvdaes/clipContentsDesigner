# Samensteller voor klembordinhoud #

*	Auteurs: Noelia Ruiz Martínez.
*	Download [stabiele versie][1]
*	Download [ontwikkelversie][2]

This add-on is used to add text to the clipboard, which can be useful when
you want to join sections of text together ready for pasting.  The clipboard
content can also be cleared.

## Toetsenbordsneltoetsen ##
*	NVDA+windows+c: Add selected text, Unicode braille characters which
  represent MathML objects, or the string which has been marked with the
  review cursor, to the clipboard.
*	NVDA+windows+x: Inhoud van klembord wissen.
*	NVDA+windows+f9: Mark the current position of the review cursor as the start of the text to be added to the clipboard.
    If you use nvda+F9, the text will not be added.

Opmerking: De bovenstaande commando's kunnen worden gewijzigd via het
NVDA-menu, Opties submenu, Invoerhandelingen koppelen dialoogvenster,
Leesoverzicht categorie.

## Menu opties ##
*	Clip Contents Designer settings: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
It's also possible to choose if the added text will be appended or prepended.

Note: The above command can be changed from NVDA menu, Preferences submenu,
Input gestures dialog, Configuration category.

## Changes for 5.0 ##

*	The visual presentation of the dialog has been enhanced, adhering to the
  appearance of the dialogs shown in NVDA.
*	Requires NVDA 2016.4 or later.

## Changes for 4.0 ##
*	Add-on settings are managed from NVDA configuration, so that standard
  profiles can be used to save different separators, and it's not needed to
  copy the settings for importing at reinstallation.
*	Now it's possible to choose if the added text will be appended or
  prepended, using the Add text before clip data check box from the Clip
  Contents Designer settings dialog.

## Changes for 3.0 ##
*	Braille representation of MathML objects can be added to the clipboard if
  MathPlayer is installed.
*	If no separator is set, just a single line will be placed between the
  added text segments.
*	A shortcut can be assigned to open the Clip Contents Designer settings
  dialog.
*	Added a check box in the settings dialog, for choosing if the separator
  should be copied to be imported when reinstalling the add-on.

## Veranderingen in 2.0 ##
*	Hindi characters can be used as the separator between added contents.

## Veranderingen in 1.0 ##
*	Eerste versie.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev
