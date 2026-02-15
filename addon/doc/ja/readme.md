# Clip Contents Designer #

*	作者: Noelia, Abdel。

このアドオンは、クリップボードにテキストを追加するのに使用されます。テキストの切片を結合して一緒に貼り付けしたい時に便利です。クリップボードの内容は、ブラウズモードでの表示で消去も出来ます。

## キー操作 ##
*	NVDA+windows+c:
  選択したテキスト、MathMLオブジェクトを表すユニコード点字文字、またはレビューカーソルでマークされた文字列を、クリップボードに追加します。
*	NVDA+Windows+x: クリップボードの内容を消去します。
*	割り当てなし: クリップボードにコピー(または切り取り)、前回の確認を問い合わせるかどうかを切り替えます。
*	割り当てなし:
  クリップボードのテキストをブラウズモードでHTMLとして表示します。または、もしクリップボードが空、または、閲覧可能なメッセージの表示ではない、例えばファイルやフォルダがWindows
  Explorerからコピーされているなどの内容の場合に通知します。
*	割り当てなし:
  テキストのクリップボードの内容をブラウズモードで表示します。または、もしクリップボードが空、または、閲覧可能なメッセージの表示ではない、例えばファイルやフォルダがWindows
  Explorerからコピーされているなどの内容の場合に通知します。


## Clip Contents Designer設定 ##

このパネルはNVDAメニュー、設定(P)サブメニュー、設定(S)ダイアログから利用可能です。

次のコントロールを含みます:

* クリップボードに追加された内容の間のセパレータとして使用する文字列を入力します:
  追加されたテキスト全体がペーストされた時に、テキストの区切りを見つけるのに使用可能なセパレータを設定出来ます。
* クリップデータの前にテキストを追加: 追加されたテキストが後ろに追加されるか前に追加されるかを選択することも可能です。
* 前の確認を依頼する動作を選択します:
  それぞれの利用可能な動作について、それがすぐにまたは確認後に実行されるかどうか、選択することが出来ます。利用可能な動作:
  テキスト追加、クリップボード消去、コピーのエミュレートと切り取りのエミュレート。
* 選択された動作を実行する前に確認をいつ依頼するか:
  単にテキストがクリップボードに含まれている時、または、クリップボードが空でない時(例えばテキストでなくファイルをコピーした時)、確認を常に依頼するかどうか、選択出来ます。
* クリップボードのテキストを表示する書式をブラウズモードでHTMLに:
  もし、HTMLマークアップ言語を学んでいる場合、HTMLの整形済みテキストまたはHTMLをウェブブラウザに表示されるように、選択出来、HTMLコードがブラウザでどのようにNVDAにより表現されるかわかります。整形済みと従来のHTML違いは、最初の選択肢の場合は連続するスペースや改行を保持し、二番目の選択肢の場合は圧縮します。例えば、h1,
  h2, li,
  preなどのようなHTMLタグで書いて、テキストを選択してクリップボードにコピーし、clipContentsDesignerアドオンを使うと、閲覧可能なメッセージにテキストを表示します。
* クリップボードのテキストをブラウズモードで表示する時の最大文字数:
  この限界を増加することは、クリップボードが大きな文字列を含む場合に、問題となることに注意して下さい。初期の限界値は100000文字です。
* Restore defaults.

備考:

*	NVDAのメッセージボックスがまだ開いている時に、確認が依頼されません。これらの場合、動作がすぐに実行されます。
*	Emulate copy and emulate cut commands mean that, when these features are
  enabled, the add-on will take control of control+c and control+x. This
  will allow to select if a confirmation should be requested before
  performing the actions corresponding to these keystrokes.

## Changes for 46.0.0
* NVDA will sanitize HTML in browseable messages.
* Added a button to close browseable messages, in addition to the Escape
  key.


## Changes for 40.0.0
* Added support for Hebrew keyboard.

## Changes for 22.0.0
* Added a button to restore defaults in the add-on settings panel.
* The add-on cannot be run in secure mode.

## Changes for 17.0
* Compatible with NVDA 2023.1.

## 16.0の変更点
* Reqires NVDA 2022.1 or later.

## 15.0の変更点
* テキストをクリップボードに追加するコマンドが、再び入力ジェスチャーダイアログに現れるようになりました。
* ペルシア語キーボードでの、コピーと切り取りのジェスチャーを修正しました。Mohammadhosein Ghezelsoflaのおかげです。

## 14.0の変更点
* NVDA 2021.1に互換。

## Changes for 13.0
* 設定パネルの外観的なレイアウトの問題を修正しました。Cyrille Bougotのおかげです。
* ドキュメントの改善。
* このアドオンの利用可能な全てのコマンドに入力ジェスチャーを割り当てする、Clip Contents Designerカテゴリーを追加しました。
* もしフォーカスモードがアクティブな時に、ブラウザでコピーのエミュレートを使用している時の、バグを修正しました。
* クリップボードのテキストの内容を、テキストのまま、またはHTMLフォーマットで表示するのに、異なるジェスチャーを割り当てすることが出来ます。それに従って、設定パネルでの、クリップボードのテキストを表示するフォーマットは、HTMLフォーマットについて利用可能な2つの選択肢を選択するように、修正されています。

## 12.0の変更点
* LibreOffice Writerのようなアプリケーションで、コピーのエミュレートを使用する時の、バグを修正しました。

## 11.0の変更点
* NVDAの標準コマンド(NVDA+f9とNVDA+f10)を使用して、レビューカーソルでマークされたテキストを追加することが可能になりました。新しいNVDA+shift+f9コマンドとの統一性を良くするため、NVDA+windows+f9は使ええなくなりました。
* NVDA 2019.3以降が必要。

## 10.0の変更点
* クリップボードのテキストを表示するのに使用されるダイアログでの、タイトルが非ラテン文字を含む時のバグを修正しました。
* アラビア語キーボードレイアウトで、切り取りとコピー機能のエミュレートを使用する時のバグを修正しました。これはアドオンの作者として追加された、Abdelにより修正されました。

## 9.0の変更点

* ブラウズモードでクリップボードのテキストを表示出来る機能を追加しました。
* クリップボードが空でない時、例えば、ファイルまたはフォルダがコピーされている時に、確認が必要かどうかを選択するオプションを追加しました。
* NVDA 2018.4以降が必要。

## 8.0の変更点 ##

* アドオン設定は、NVDA設定ダイアログの、対応するカテゴリーに表示されます。
* NVDA 2018.2以降が必要。

## 7.0の変更点

* インストール時にコピーのエミュレートとカットのエミュレートの機能を設定するダイアログで、いいえを選ぶと、これらの機能のコマンドが除去され、control+cとcontrol+xの標準動作に戻すことが出来ます。

## 6.0の変更点

*	Added options to choose if available actions should be performed after
  confirmation.
*	Added Emulate copy and Emulate cut commands, which could be assigned from
  the Input gestures dialog.
*	Added a dialog to configure the Emulate copy and Emulate cut
  functionalities at installation. This allows to add the control+c and
  control+x commands to copy and cut, and be asked if you want to replace
  the clipboard contents when pressing these keystrokes.
*	Fixed documentation for script_add (Windows+NVDA+c).

## 5.0の変更点 ##

*	ダイアログの外観的表示が、NVDAで表示されるダイアログの外観と似るように、拡張されました。
*	NVDA 2016.4以降が必要。

## 4.0の変更点 ##
*	異なるセパレータを保存するのに、標準プロファイルが使用され、再インストール時にインポートする設定をコピーする必要がないように、アドオン設定をNVDA設定から管理。
*	Clip Contents
  Designer設定ダイアログから、テキストをクリップデータの前に追加チェックボックスを使用して、追加されたテキストが後ろに追加されるか前に追加されるかを選択可能。

## 3.0の変更点 ##
*	MathPlayerがインストールされている場合に、MathMLのオブジェクトの点字表記をクリップボードに追加可能。
*	セパレータの設定がされていない場合、テキストの切片の間には単線を配置。
*	Clip Contents Designer 設定ダイアログを開くショートカットを割り当て可能。
*	設定ダイアログに、このアドオンの再インストールの際にインポートされるように、このセパレータをコピーするかどうかを選択するチェックボックスを追加。

## 2.0の変更点 ##
*	追加されたテキストの間のセパレータとして、ヒンディー文字が使用可能。

## 1.0の変更点 ##
*	最初のバージョン。

[[!tag dev stable]]

