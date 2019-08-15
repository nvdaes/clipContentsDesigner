# Clip Contents Designer #

*	Authors: Noelia, Abdel.
*	NVDA compatibility: 2018.4 to 2019.2.
*	Baixar a [versão estável][1]
*	Baixar a [versão de desenvolvimento][2]

Este extra é usado para adicionar texto à área de transferência, o que lhe
pode ser útil quando quiser juntar várias partes de textos num só, pronto
para colar.  O conteúdo da área de transferência também pode ser visto no
modo de navegação.

## Comandos de teclado ##
*	NVDA+windows+c: adiciona o texto seleccionado, os caracteres unicode em
  Braille que representem objetos MathML, ou a cadeia que foi marcada com o
  cursor de exploração, à área de transferência.
*	NVDA+windows+x: limpa o conteúdo da área de transferência.
* NVDA+windows+f9: Marca a posição actual do cursor de revisão como o início do texto a ser adicionado à área de transferência. Se usar nvda+F9, o texto não será adicionado.
*	 Não atribuído: copia para (ou corta) a área de transferência, com a possibilidade de ser solicitada uma confirmação anterior.
*	 Não atribuído: mostra o texto da área de transferência no modo de navegação ou anuncia se a área de transferência está vazia ou tem conteúdo que não pode ser apresentado numa mensagem navegável, por exemplo, se arquivos ou pastas foram copiados do Windows Explorer.

Nota: Os comandos anteriores podem ser alterados a partir do menu do NVDA,
submenu Preferências, comandos, categoria Revisão de texto.

## Menu Preferências ##
*	 Configurações do conteúdo do extra: Permite definir um separador que pode ser usado para procurar os segmentos de texto logo que todo o texto adicionado seja colado.
Também é possível escolher se o texto adicionado será acrescentado ou prefixado, se as ações disponíveis (adicionar, limpar área de transferência, emular cópia e emular recortar) devem ser executadas imediatamente ou após a confirmação e se as confirmações serão solicitadas sempre, apenas se o texto estiver já contido na área de transferência ou se a área de transferência não estiver vazia.
Além disso, é possível alterar o formato e o número máximo de caracteres do texto da área de transferência, que será mostrado no modo de navegação. Por favor, esteja ciente de que aumentar este limite pode produzir problemas se a área de transferência contiver grandes cadeias de texto. O limite padrão é de 100.000 caracteres.

Notas:

*	Os comandos anteriores podem ser modificados a partir do menu do NVDA,
  submenu Preferências, comandos, configuração.
*	As confirmações não serão pedidas quando um diálogo do NVDA ainda estiver
  aberto. Nesses casos, as acções serão executadas de imediato

## Changes for 10.0
* Fixed a bug in the dialog used to show the clipboard text, when its title
  contains non latin characters.
* Fixed a bug when using the emulate cut and copy features with an Arabic
  keyboard layout. This has been fixed by Abdel, added as an add-on author.

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
* Se for necessário, pode fazer o download da [última versão compatível com
  o NVDA 2017.3] [3].

## Alterações para a versão 7.0

* Na caixa de diálogo da instalação para configurar as funcionalidades
  Emular cópia e Emular corte, se escolher não, os comandos para esses
  recursos serão removidos, para que possa restaurar o comportamento normal
  para controle + c e controle + x.

## Alterações para a versão 6.0

*	 Adicionadas opções para escolher se as acções disponíveis devem ser executadas após confirmação.
*	Adicionados os comandos emulação de copiar e emulação de cortar, que podem ser atribuídos no diálogo definir comandos.
*	 Adicionado um diálogo para configurar as funções emulação de copiar e de cortar na instalação. Isso permite acrescentar os comandos control+c e control+x para copiar e cortar e ser questionado sobre se deseja substituir o conteúdo da área de transferência ao pressionar essas teclas.
*	Corrigida a documentação para script_add (Windows+NVDA+c).

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

[1]: https://addons.nvda-project.org/files/get.php?file=ccd

[2]: https://addons.nvda-project.org/files/get.php?file=ccd-dev

[3]: https://addons.nvda-project.org/files/get.php?file=ccd-o
