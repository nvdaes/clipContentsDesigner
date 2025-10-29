# Clip Contents Designer #

*	مطورو الإضافة: Noelia Ruiz Martínez.
*	تحميل [الإصدار النهائي] [1]
*	تحميل [الإصدار التجريبي] [2]

This add-on is used to add text to the clipboard, which can be useful when
you want to join sections of text together ready for pasting.  The clipboard
content can also be cleared.

## مفاتيح الاختصار ##

* VDA+windows+f9: Mark the current position of the review cursor as the start of the text to be added to the clipboard. If you use nvda+F9, the text will not be added.
* Not assigned: Copies to (or cuts from) the clipboard, with the possibility of being asked for a previous confirmation.

ملحوظة: يمكنك تغيير الاختصارات المذكورة أعلاه من خلال الذهاب إلى قائمة NVDA
الرئيسية, ثم قائمة التفضيلات, ثم تخصيص اختصارات NVDA, ثم فئة استعراض النص.

## قائمة التفضيلات ##

* In the dialog to configure the Emulate copy and Emulate cut
  functionalities at installation, if you choose no, the commands for these
# Changes for 6.0

* dded options to choose if available actions should be performed after confirmation.
*	Added Emulate copy and Emulate cut commands, which could be assigned from the Input gestures dialog.
* Added a dialog to configure the Emulate copy and Emulate cut functionalities at installation. This allows to add the control+c and control+x commands to copy and cut, and be asked if you want to replace the clipboard contents when pressing these keystrokes.
*	Fixed documentation for script_add (Windows+NVDA+c).

## Changes for 5.0 ##

*	The visual presentation of the dialog has been enhanced, adhering to the
  appearance of the dialogs shown in NVDA.
*	Requires NVDA 2016.4 or later.

## Changes for 4.0 ##

  profiles can be used to save different separators, and it's not needed to

## مستجدات الإصدار 3.0 ##

*	Braille representation of MathML objects can be added to the clipboard if
  MathPlayer is installed.

*	If no separator is set, just a single line will be placed between the
  added text segments.
  بين القطع النصية لاستيراده عند إعادة تثبيت الإضافة


## مستجدات الإصدار 2.0 ##


[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev