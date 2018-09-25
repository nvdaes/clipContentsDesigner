# Gestor do conteúdo de transferência #

*	Autores: Noelia Ruiz Martínez.
*	Baixe a [versão estável][1]
*	Baixe a [versão de desenvolvimento][2]

Este complemento é usado para acrescentar texto à área de transferência, o
que pode ser útil quando você quiser juntar seções de texto num só, pronto
para colar. O conteúdo da área de transferência pode também ser apagado.

## Comandos de tecla ##
*	NVDA+windows+c: Acrescenta o texto selecionado, os caracteres unicode em
  braile que representem objetos MathML, ou a cadeia que foi marcada com o
  cursor de exploração, à área de transferência.
*	NVDA+windows+x: Apaga o conteúdo da área de transferência.
*	NVDA+windows+f9: Marca a posição atual do cursor de exploração como o início do texto a ser acrescentado à área de transferência. Se você usar nvda+F9, o texto não será acrescentado.
*	 Não atribuído: Copia para (ou corta) a área de transferência com possibilidade de ser previamente consultado para confirmar.

Nota: Os comandos acima podem ser alterados a partir do menu do NVDA,
submenu Preferências, diálogo de Gestos para Entrada, categoria Exploração
de texto.

## Menu Preferências ##
*	Opções do Gestor do conteúdo de transferência: Possibilita definir um separador que se pode usar para localizar os segmentos de texto uma vez que o texto inteiro seja colado.
Pode-se também escolher se o texto acrescentado virá por último ou primeiro, se as ações disponíveis (acrescentar, limpar área de transferência, emulação de copiar e emulação de cortar) devem ser executadas de imediato ou após confirmação e se a confirmação será solicitada apenas se a área de transferência já contiver texto.

Notas:

*	Os comandos acima podem ser alterados a partir do menu do NVDA, submenu
  Preferências, diálogo de Gestos para Entrada, categoria configuração.
*	Confirmação não será solicitada quando um diálogo do NVDA ainda estiver
  aberto. Nesses casos, as ações serão executadas de imediato

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
*	Adicionados comandos emulação de copiar e emulação de cortar, que podem ser atribuídos no diálogo de gestos para entrada.
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
*	Representações braile de objetos MathML podem ser acrescentadas à área de
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
