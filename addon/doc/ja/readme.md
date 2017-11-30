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
*	NVDA+windows+f9: Mark the current position of the review cursor as the start of the text to be added to the clipboard. If you use nvda+F9, the text will not be added.
*	 Not assigned: Copies to (or cuts from) the clipboard, with the possibility of being asked for a previous confirmation.

注: 上記のコマンドは、NVDAメニュー、設定サブメニュー、入力ジェスチャーダイアログ、テキストレビューカテゴリから変更できます。

## 設定サブメニュー ##
*	Clip Contents Designer settings: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
It's also possible to choose if the added text will be appended or prepended, if available actions (add, clear clipboard, emulate copy and emulate cut) should be performed inmediately or after confirmation, and if confirmations will be requested just if text is contained in the clipboard.

Notes:

*	The above command can be changed from NVDA menu, Preferences submenu,
  Input gestures dialog, Configuration category.
*	Confirmations won't be requested when a message box of NVDA is still
  opened. In those cases, actions will be inmediately performed

## Changes for 6.0

*	 Added options to choose if available actions should be performed after confirmation.
*	Added Emulate copy and Emulate cut commands, which could be assigned from the Input gestures dialog.
*	 Added a dialog to configure the Emulate copy and Emulate cut functionalities at installation. This allows to add the control+c and control+x commands to copy and cut, and be asked if you want to replace the clipboard contents when pressing these keystrokes.
*	Fixed documentation for script_add (Windows+NVDA+c).

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

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev
