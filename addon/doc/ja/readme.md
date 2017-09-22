# Clip Contents Designer #

*	作者: Noelia Ruiz Martínez
*	ダウンロード [安定版][1]
*	ダウンロード [開発版][2]

このアドオンは、クリップボードにテキストを追加するのに使用します。貼り付け前に複数のテキスト部分を結合したい時に便利です。クリップボードの内容を消去することもできます。

## キー操作: ##
*	NVDA+windows+c: Add selected text, Unicode braille characters which
  represent MathML objects, or the string which has been marked with the
  review cursor, to the clipboard.
*	NVDA+Windows+x: クリップボードの内容を消去します。
NVDA+Windows+F9: レビューカーソルの現在の位置を、クリップボードに追加するテキストの開始位置として記録します。NVDA+F9を使用すると、テキストは追加されません。

注: 上記のコマンドは、NVDAメニュー、設定サブメニュー、入力ジェスチャーダイアログ、テキストレビューカテゴリから変更できます。

## 設定サブメニュー ##
*	Clip Contents Designer settings: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
It's also possible to choose if the added text will be appended or prepended.

注: 上記のコマンドは、NVDAメニュー、設定サブメニュー、入力ジェスチャーダイアログ、設定カテゴリから変更できます。

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

## 3.0の変更点 ##
*	Braille representation of MathML objects can be added to the clipboard if
  MathPlayer is installed.
*	If no separator is set, just a single line will be placed between the
  added text segments.
*	Clip Contents Designer 設定ダイアログを開くショートカットを割り当て可能
*	設定ダイアログに、このアドオンの再インストールの際にインポートされるように、このセパレータをコピーするかどうかを選択するチェックボックスを追加

## 2.0の変更点 ##
*	Hindi characters can be used as the separator between added contents.

## バージョン1.0 ##
*	最初のバージョン

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ccd

[2]: https://addons.nvda-project.org/files/get.php?file=ccd-dev
