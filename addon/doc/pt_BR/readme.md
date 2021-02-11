# Gestor do Conteúdo de Transferência (Clip Contents Designer) #

*	Autores: Noelia, Abdel.
*	Compatibilidade com NVDA: 2019.3 ou posterior
*	Baixe a [versão estável][1]
*	Baixe a [versão em desenvolvimento][2]

Este complemento é usado para adicionar texto à área de transferência, o que
pode ser útil quando você deseja unir seções de texto prontas para colar. O
conteúdo da área de transferência também pode ser limpo e mostrado no modo
de navegação.

## Comandos de teclado ##
*	NVDA+windows+c: Acrescenta o texto selecionado, os caracteres braille
  Unicode que representem objetos MathML, ou a sequência (string) que foi
  marcada com o cursor de exploração, à área de transferência.
*	NVDA+windows+x: Apaga o conteúdo da área de transferência.
*	Não atribuído: copia (ou corta) a área de transferência, com a
  possibilidade de ser solicitada uma confirmação prévia.
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

Notas:

*	Confirmações não serão solicitadas quando uma caixa de mensagem do NVDA
  ainda estiver aberta. Nesses casos, as ações serão executadas
  imediatamente.
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

## Changes for 12.0
* Fixed bugs when using emulate copy in applications like LibreOffice
  Writer.

## Mudanças na 11.0
* Agora é possível adicionar texto marcado com o cursor de exploração usando
  comandos padrão do NVDA (NVDA+f9 e NVDA+f10). NVDA+windows+f9 não é mais
  usado, por uma melhor integração com o novo comando NVDA+shift+f9.
* Requer NVDA 2019.3 ou posterior.

## Mudanças na 10.0
* Corrigida uma falha no diálogo usado para mostrar o texto da área de
  transferência, quando o título continha caracteres não latinos.
* Corrigido uma falha ao usar os recursos de emulação de corte e cópia com
  um layout de teclado árabe. Isso foi corrigido por Abdel, adicionado como
  um autor do complemento.

## Mudanças na 9.0

* Adicionada a possibilidade de mostrar o texto da área de transferência no
  modo de navegação.
* Foi adicionada uma opção para escolher se as confirmações serão
  necessárias se a área de transferência não estiver vazia, por exemplo,
  caso arquivos ou pastas foram copiados.
* Requer NVDA 2018.4 ou posterior.

## Mudanças na 8.0 ##

* As configurações do complemento são mostradas na categoria correspondente
  da caixa de diálogo Configurações do NVDA.
* Requer NVDA 2018.2 ou posterior.
* Se necessário, você pode fazer o download da [última versão compatível com
  o NVDA 2017.3][3].

## Mudanças na 7.0

* Na caixa de diálogo da instalação para configurar as funcionalidades
  Emular cópia e Emular corte, se você escolher não, os comandos para esses
  recursos serão removidos, para que você possa restaurar o comportamento
  normal para control+c e control+x.

## Mudanças na 6.0

*	 Adicionadas opções para escolher se as ações disponíveis devem ser executadas após confirmação.
*	Adicionados comandos emulação de copiar e emulação de cortar, que podem ser atribuídos no diálogo de Gestos para entrada.
*	 Adicionado um diálogo para configurar as funções emulação de copiar e de cortar na instalação. Isso possibilita adicionar os comandos control+c e control+x para copiar e cortar e ser indagado se deseja substituir o conteúdo da área de transferência ao pressionar essas teclas.
*	Corrigida documentação para script_add (Windows+NVDA+c).

## Mudanças na 5.0 ##

*	A apresentação visual do diálogo foi aprimorada, aderindo à aparência dos
  diálogos mostrados no NVDA.
*	Requer NVDA 2016.4 ou posterior.

## Mudanças na 4.0 ##
*	As opções do complemento são agora geridas pela configuração do NVDA, de
  modo que se pode usar perfis para salvar diferentes separadores e não é
  necessário copiar as opções para importá-las quando duma reinstalação.
*	Agora é possível escolher se o texto será acrescentado depois ou antes do
  que já está lá, usando a caixa de seleção acrescentar texto antes dos
  dados, no diálogo de opções do gestor de conteúdo da área de
  transferência.

## Mudanças na 3.0 ##
*	Representações braille de objetos MathML podem ser acrescentadas à área de
  transferência se o MathPlayer estiver instalado.
*	Caso nenhum separador seja configurado, apenas uma linha será colocada
  entre os segmentos de texto acrescentados.
*	Uma tecla de atalho pode ser atribuída para abrir o diálogo de opções do
  gestor do conteúdo de transferência.
*	Adicionada uma caixa de seleção ao diálogo de opções, para escolher se o
  separador deve ser copiado para ser importado ao reinstalar o complemento.

## Mudanças na 2.0 ##
*	Caracteres hindi podem ser usados como o separador entre conteúdos
  acrescentados.

## Mudanças na 1.0 ##
*	Versão inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ccd

[2]: https://addons.nvda-project.org/files/get.php?file=ccd-dev

[3]: https://addons.nvda-project.org/files/get.php?file=ccd-o
