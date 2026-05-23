# Clip Contents Designer #

*	Autores: Noelia, Abdel.

Este extra é usado para adicionar texto à área de transferência, o que lhe
pode ser útil quando quiser juntar várias partes de textos num só, pronto
para colar.  O conteúdo da área de transferência também pode ser visto no
modo de navegação.

## Comandos de teclado ##
*	NVDA+windows+c: adiciona o texto seleccionado, os caracteres unicode em
  Braille que representem objetos MathML, ou a cadeia que foi marcada com o
  cursor de exploração, à área de transferência.
*	NVDA+windows+x: limpa o conteúdo da área de transferência.
*	Não atribuído: Cópias para (ou cortes de) a área de transferência, com a
  possibilidade de ser solicitada uma confirmação prévia.
*	Não atribuído: Mostra o texto da área de transferência como HTML no modo
  de navegação, ou anuncia se a área de transferência está vazia ou tem
  conteúdos que não podem ser apresentados numa mensagem navegável, por
  exemplo, se ficheiros ou pastas foram copiados do Explorador do Windows.
*	Não atribuído: Mostra o conteúdo da área de transferência textual como
  texto simples no modo de navegação, ou anuncia se a área de transferência
  está vazia ou tem conteúdo que não pode ser apresentado numa mensagem
  navegável, por exemplo, se os ficheiros ou pastas foram copiados do
  Explorador do Windows.


## Configurações do gestor da área de transferência. ##

Este painel está disponível a partir do menu do NVDA, submenu Preferências,
diálogo configurações.

Contém os seguintes controlos:

* Digite a cadeia a ser utilizada como separador entre os conteúdos
  adicionados à área de transferência: Permite definir um separador que pode
  ser utilizado para encontrar os segmentos de texto uma vez colado todo o
  texto adicionado.
* Acrescentar texto antes dos dados do clip: Também é possível escolher se o
  texto adicionado será anexado ou pré-preenchido.
* Seleccionar as acções que requerem confirmação prévia: Pode escolher, para
  cada acção disponível, se esta deve ser realizada imediatamente ou após
  confirmação. As acções disponíveis são: adicionar texto, limpar a área de
  transferência, emular cópia e emular corte.
* Solicitar confirmação antes de executar as acções seleccionadas quando:
  Pode seleccionar se as confirmações serão sempre solicitadas, apenas se o
  texto estiver contido na área de transferência, ou se a área de
  transferência não estiver vazia (por exemplo, se copiou um ficheiro, não
  um texto).
* Formatação para mostrar o texto da área de transferência como HTML no modo
  de navegação: Se estiver a aprender a linguagem de marcação HTML, pode
  escolher texto pré-formatado em HTML ou HTML como mostrado num navegador
  web, para ter uma ideia de como o seu código HTML será apresentado pelo
  NVDA num navegador. A diferença entre HTML pré-formatado e convencional é
  que a primeira opção irá preservar espaços consecutivos e quebras de
  linha, e a segunda irá compactá-los.  Por exemplo, escreva algumas
  etiquetas HTML como h1, h2, li, pre, etc., seleccione e copie o texto para
  a área de transferência, e use o add-on clipContentsDesigner para mostrar
  o texto numa mensagem navegável.
* Número máximo de caracteres ao mostrar o texto da área de transferência no
  modo de navegação: Tenha em atenção que o aumento deste limite pode
  produzir problemas se a área de transferência contiver grandes cadeias de
  texto. O limite por defeito é de 100000 caracteres.
* Restore defaults.

Notas:

*	As confirmações não serão solicitadas quando uma caixa de mensagens do
  NVDA ainda estiver aberta. Nesses casos, as acções serão executadas de
  imediato.
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

## Changes for 16.0
* Reqires NVDA 2022.1 or later.

## Changes for 15.0
* The command to add text to clipboard is again presented in the input
  gestures dialog.
* Fixed gestures to copy and cut with Persian keyboard, thanks to
  Mohammadhosein Ghezelsofla.

## Changes for 14.0
* Compatible with NVDA 2021.1.

## Changes for 13.0
* Corrigido um problema na disposição visual do painel de configurações,
  graças a Cyrille Bougot.
* Documentação melhorada.
* Adicionada uma categoria Clip Content Designer para atribuir comandos de
  entrada a todos os comandos disponíveis para este add-on.
* Corrigidos bugs ao utilizar cópia emulada em navegadores se o modo de foco
  estiver activo.
* Pode atribuir diferentes comandos para mostrar o conteúdo textual da área
  de transferência como texto em bruto ou formatado em HTML. O Formato para
  mostrar o texto da área de transferência no painel de definições foi
  modificado em conformidade, para seleccionar as duas opções disponíveis
  para o formato HTML.

## Alterações para 12.0
* Corrigidos bugs ao utilizar cópia emulada em aplicações como o LibreOffice
  Writer.

## Alterações para 11.0
* Agora é possível adicionar texto marcado com o cursor de revisão usando
  comandos padrão do NVDA (NVDA+f9 e NVDA+f10). NVDA+windows+f9 já não é
  utilizado, para uma melhor integração com o novo comando NVDA+shift+f9.
* Requer NVDA 2019.3 ou posterior.

## Alterações para 10.0
* Corrigido um erro no diálogo utilizado para mostrar o texto da área de
  transferência, quando o seu título contém caracteres não latinos.
* Corrigido um erro ao utilizar as funções de corte e cópia emulada com um
  teclado árabe. Isto foi corrigido por Abdel, adicionado como um dos
  autores do extra.

## Alterações para a versão 9.0

* Adicionada a possibilidade de mostrar o texto da área de transferência no
  modo de navegação.
* Adicionada uma opção para escolher se as confirmações serão necessárias se
  a área de transferência não estiver vazia, por exemplo, se os arquivos ou
  pastas forem copiados.
* Requer o NVDA 2018.4 ou posterior.

## Alterações para a versão 8.0 ##

* As configurações adicionais são mostradas na categoria correspondente da
  caixa de diálogo Configurações do NVDA.
* Requer o NVDA 2018.2 ou posterior.

## Alterações para a versão 7.0

* Na caixa de diálogo da instalação para configurar as funcionalidades
  Emular cópia e Emular corte, se escolher não, os comandos para esses
  recursos serão removidos, para que possa restaurar o comportamento normal
  para controle + c e controle + x.

## Alterações para a versão 6.0

*	Added options to choose if available actions should be performed after
  confirmation.
*	Added Emulate copy and Emulate cut commands, which could be assigned from
  the Input gestures dialog.
*	Added a dialog to configure the Emulate copy and Emulate cut
  functionalities at installation. This allows to add the control+c and
  control+x commands to copy and cut, and be asked if you want to replace
  the clipboard contents when pressing these keystrokes.
*	Fixed documentation for script_add (Windows+NVDA+c).

## Alterações para a versão 5.0 ##

*	A apresentação visual do diálogo foi melhorada, coincidindo com a
  aparência dos diálogos mostrados no NVDA.
*	Requer o NVDA 2016.4 ou posterior.

## Alterações para a versão 4.0 ##
*	As opções do extra são agora geridas directamente pela configuração do
  NVDA, de modo que se pode usar perfis para salvar diferentes separadores e
  não é necessário copiar as opções para importá-las quando numa
  reinstalação.
*	Agora é possível escolher se o texto será colocado depois ou antes do que
  já lá está, usando a caixa de selecção  existente no diálogo de opções do
  gestor de conteúdos da área de transferência.

## Alterações para a versão 3.0 ##
*	As representações braile de objectos MathML podem ser acrescentadas à área
  de transferência, se o MathPlayer estiver instalado.
*	Se não for definido qualquer separador, apenas será colocada uma linha
  entre os vários fragmentos de texto adicionados.
*	Pode criar-se uma tecla de atalho para abrir o diálogo de opções do gestor
  do conteúdo de transferência.
*	Acrescentada uma caixa de selecção ao diálogo de opções, a qual permite
  escolher se o separador de fragmentos deve ser copiado para ser importado
  ao reinstalar o extra.

## Alterações para a versão 2.0 ##
*	Os caracteres hindi podem ser usados como separador entre conteúdos
  acrescentados.

## Alterações para a versão 1.0 ##
*	Versão inicial.

[[!tag dev stable]]

