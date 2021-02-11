# 剪辑内容设计器 #

*	作者: Noelia, Abdel。
*	NVDA兼容版本: 2019.3或更高
*	下载 [稳定版][1]
*	下载 [开发板][2]

此插件用于向剪贴板添加文本，当您希望将文本部分连接在一起以准备粘贴时，这可能很有用。剪贴板内容也可以清除或者用浏览模式逐字逐句查看。

## 键盘快捷键 ##
*	NVDA+windows+c: 将选定的文本，表示MathML对象的Unicode盲文字符或已使用浏览光标标记的字符串添加到剪贴板.
*	NVDA+windows+x: 清除剪贴板内容.
*	未分配：复制到剪贴板（或从剪贴板剪切），并跳出确认框。
*	Not assigned: Shows the clipboard text as HTML in browse mode, or
  announces if clipboard is empty or has contents which can't be presented
  in a browseable message, for instance if files or folders are been copied
  from Windows Explorer.
*	Not assigned: Shows the textual clipboard contents as plain text in browse
  mode, or announces if clipboard is empty or has contents which can't be
  presented in a browseable message, for instance if files or folders are
  been copied from Windows Explorer.


## Clip Contents Designer settings ##

This panel is available from NVDA's menu, Preferences submenu, Settings
dialog.

It contains the following controls:

* Type the string to be used as a separator between contents added to the
  clipboard: Allows to set a separator which can be used to find the text
  segments once the entire added text is pasted.
* Add text before clip data: It's also possible to choose if the added text
  will be appended or prepended.
* Select the actions which require previous confirmation: You can choose,
  for each action available, if it should be performed inmediately or after
  confirmation. Available actions are: add text, clear clipboard, emulate
  copy and emulate cut.
* Request confirmation before performing the selected actions when: You can
  select if confirmations will be requested always, just if text is
  contained in the clipboard, or if clipboard is not empty (for example if
  you've copied a file, not text).
* Format to show the clipboard text as HTML in browse mode: If you're
  learning HTML markup language, you may choose Preformatted text in HTML or
  HTML as shown in a web browser, to have an idea of how your HTML code will
  be rendered by NVDA in a browser. The difference between preformatted and
  conventional HTML is that the first option will preserve consecutive
  spaces and line breaks, and the second one will compact them.  For
  example, write some HTML tags like h1, h2, li, pre, etc., select and copy
  the text to clipboard, and use clipContentsDesigner add-on to show the
  text in a browseable message.
* Maximum number of characters when showing clipboard text in browse mode:
  Please, be aware that increasing this limit may produce issues if the
  clipboard contains large strings of text. The default limit is 100000
  characters.

注意:

*	当NVDA的消息框仍然打开时，将不会请求确认。在这些情况下，将立即执行操作。
*	Emulate copy and emulate cut commands mean that, when these features are
  enabled, the add-on will take control of control+c and control+x. This
  will allow to select if a confirmation should be requested before
  performing the actions corresponding to these keystrokes.

## Changes for 13.0 
* Fixed an issue in visual layout of the settings panel, thanks to Cyrille
  Bougot.
* Improved documentation.
* Added a Clip Contents Designer category to assign input gestures to all
  commands available for this add-on.
* Fixed bugs when using emulate copy in browsers if focus mode is active.
* You can assign different gestures to show the clipboard textual contents
  as raw text or formatted in HTML. The Format to show the clipboard text in
  the settings panel has being modified accordingly, to select the two
  options available for HTML format.

## 版本 12.0
* 修复了在 LibreOffice Writer 等应用程序中使用模拟复制时的错误。

## 版本11.0
* 现在可以使用 NVDA （NVDA_f9 和 NVDA_f10） 的标准命令添加带有浏览光标标记的文本。NVDA_windows_f9
  不再使用，以便更好地与新的 NVDA_shift_f9 命令集成。
* 需要NVDA 2019.3或更高版本。

## 版本10.0
* 修复了用于显示剪贴板文本的对话框中的错误，当其标题包含非拉丁字符时。
* 修复阿拉伯语键盘使用剪辑内容设计器的错误。已由Abdel修复，有插件作者添加。

## 版本9.0

* 新增了在浏览模式下显示剪贴板文本的功能。
* 添加了一个选项，用于选择在剪贴板不为空时追加内容时是否需要确认，例如，剪贴板里面已有复制的文件或文件夹。
* 需要NVDA 2018.4或更高版本。

## 版本8.0 ##

* 插件设置显示在NVDA设置对话框的相应类别中。
* 需要NVDA 2018.2或更高版本。
* 假如需要用旧版本，您可以下载[与NVDA 2017.3兼容的旧版本] [3]。

## 版本7.0

* 在安装时配置模拟复制和模拟剪切功能的对话框中，如果选择否，将删除这些功能的命令，以便您可以恢复control + c和control +
  x的正常行为。

## 版本6.0

*	 添加选项以选择是否应在确认后执行可用操作.
*	添加了“模拟复制”和“模拟剪切”快捷键，可以从“输入”手势对话框中指定.
*	 添加了一个对话框，用于在安装时配置模拟复制和模拟剪切功能。这允许添加control + c和control + x命令进行复制和剪切，并在按下这些按键时询问是否要替换剪贴板内容.
*	Fixed documentation for script_add (Windows+NVDA+c).

## 版本5.0 ##

*	对话框的视觉呈现得到了增强，并且遵循NVDA中显示的对话框的外观。
*	需要NVDA 2016.4或更高版本。

## 版本4.0 ##
*	插件设置由NVDA配置管理，因此标准配置文件可用于保存不同的分隔符，并且不需要在重新安装时复制导入设置。
*	现在，可以使用“剪辑内容设计器”设置对话框中的“添加剪辑前数据”复选框，选择是添加还是添加文本。

## 版本3.0 ##
*	如果安装了MathPlayer，则可以将MathML对象的盲文表示添加到剪贴板。
*	如果未设置分隔符，则只会在添加的文本段之间放置一行。
*	可以指定快捷键来打开“剪辑内容设计器”设置对话框。
*	在设置对话框中添加了一个复选框，用于选择是否应复制分隔符以在重新安装插件时导入。

## 版本2.0 ##
*	印地语字符可以用作添加内容之间的分隔符。

## 版本1.0 ##
*	发布初始版本。

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ccd

[2]: https://addons.nvda-project.org/files/get.php?file=ccd-dev

[3]: https://addons.nvda-project.org/files/get.php?file=ccd-o
