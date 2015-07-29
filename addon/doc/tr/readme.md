# Pano içerik düzenleyicisi #
*   Yazarlar: Noelia Ruiz Martínez.
*   İndir [Kararlı Sürüm][1]
*   İndir [Geliştirme sürümü][2]

Bu eklenti panoya metinlerin arka arkaya eklenmesini mümkün kılar. Aynı
zamanda pano  içeriği tamamen de silinebilir.

## Klavye komutları ##
*   NVDA+windows+c: Append selected text, Unicode braille characters which
    represent MathML objects, or the string which has been marked with the
    review cursor, to the clipboard.
*   NVDA+windows+x: Pano içeriğini siler.
*   NVDA+windows+f9: İnceleme imlecinin mevcut konumunu panoya eklenecek
    metnin başlangıcı olarak işaretler. nvda+F9 tuşlarını kullanırsanız,
    metin panoya eklenmez.

Not: Yukarıdaki komutlar NVDA menüsünden, Tercihler altmenüsünden, girdi
hareketleri iletişim kutusu içerisindeki Metin incelemesi kategorisi
altından değiştirilebilir .

## Tercihler Menüsü ##
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

## 1.0 için Değişiklikler ##
*   İlk versiyon.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev
