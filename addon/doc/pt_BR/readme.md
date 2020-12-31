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

* NVDA+windows+c: Acrescenta o texto selecionado, os caracteres braille
  Unicode que representem objetos MathML, ou a sequência (string) que foi
  marcada com o cursor de exploração, à área de transferência.
* NVDA+windows+x: Apaga o conteúdo da área de transferência.
* Não atribuído: copia (ou corta) a área de transferência, com a
  possibilidade de ser solicitada uma confirmação prévia.
* Not assigned: Shows the clipboard text in browse mode, or announces if
  clipboard is empty or has contents which can't be presented in a
  browseable message, for instance if files or folders are been copied from
  Windows Explorer.

Nota: Os comandos acima podem ser alterados a partir do menu do NVDA,
submenu Preferências, diálogo Definir comandos (Gestos para entrada),
categoria Exploração de texto.

## Menu Preferências ##
*	Configurações do Gestor do Conteúdo de Transferência: Permite definir um separador que pode ser usado para localizar os segmentos de texto depois que todo o texto adicionado for colado.
Também é possível escolher se o texto adicionado será anexado ou prefixado, se as ações disponíveis (adicionar, limpar a área de transferência, emular cópia e emular corte) devem ser executadas imediatamente ou após a confirmação, e se as confirmações serão solicitadas sempre, apenas se o texto estiver contido na área de transferência, ou se a área de transferência não estiver vazia.
Além disso, é possível alterar o formato e o número máximo de caracteres do texto da área de transferência, que serão mostrados no modo de navegação. Por favor, esteja ciente de que aumentar esse limite pode causar problemas se a área de transferência contiver grandes seqüências de texto. O limite padrão é 100000 caracteres.

Notas:

*	Os comandos acima podem ser alterados a partir do menu do NVDA, submenu
  Preferências, diálogo Definir comandos (Gestos para entrada), categoria
  Configuração.
*	Confirmações não serão solicitadas quando uma caixa de mensagem do NVDA
  ainda estiver aberta. Nesses casos, as ações serão executadas
  imediatamente.

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
