# Clip Contents Designer #
*   مطورو الإضافة: Noelia Ruiz Martínez.
*   تحميل [الإصدار النهائي] [1]
*   تحميل [الإصدار التجريبي] [2]

تستخدم هذه الإضافة لإلحاق نص بالحافظة, يفيد عندما تريد دمج أكثر من قطعة من
النصوص معا ولصقها. كما يمكن أيضا مسح محتوى الحافظة.

## مفاتيح الاختصار ##
*   NVDA+windows+c: Append selected text, Unicode braille characters which
    represent MathML objects, or the string which has been marked with the
    review cursor, to the clipboard.
*   NVDA+windows+x: لمسح محتوى الحافظة
*   NVDA+windows+f9: تحديد الموضع الحالي لمؤشر الاستعراض كبداية للنص الذي
    سيتم إلحاقه بالحافظة. إذا استخدمت NVDA+f9, فإن النص لم يلحق بالحافظة.

ملحوظة: يمكنك تغيير الاختصارات المذكورة أعلاه من خلال الذهاب إلى قائمة NVDA
الرئيسية, ثم قائمة التفضيلات, ثم تخصيص اختصارات NVDA, ثم فئة استعراض النص.

## قائمة التفضيلات ##
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

## مستجدات الإصدار 2.0 ##
*   يمكن استخدام الأحرف الهندية كفواصل بين قطع النصوص المختلفة الملحقة
    بالحافظة.

## مستجدات الإصدار 1.0 ##
*   إصدار أولي

[[!tag dev stable]]
[[!tag dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev
