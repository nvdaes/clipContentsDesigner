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
*	Não atribuído: Mostra o texto da área de transferência como HTML no modo
  de navegação ou anuncia se a área de transferência está vazia ou possui
  conteúdos que não podem ser apresentados em uma mensagem navegável, por
  exemplo, se arquivos ou pastas foram copiados do Windows Explorer.
*	Não atribuído: Mostra o conteúdo textual da área de transferência como
  texto simples no modo de navegação ou anuncia se a área de transferência
  está vazia ou tem conteúdos que não podem ser apresentados em uma mensagem
  navegável, por exemplo, se arquivos ou pastas foram copiados do Windows
  Explorer.


## Configurações do Gestor do Conteúdo de Transferência ##

Este painel está disponível no menu do NVDA, submenu Preferências, diálogo
de Configurações.

Contém os seguintes controles:

* Digite a sequência de caracteres a ser usada como separador entre os
  conteúdos adicionados à área de transferência: Permite definir um
  separador que pode ser usado para localizar os segmentos de texto, uma vez
  que todo o texto adicionado é colado.
* Adicionar texto antes dos dados da transferência: Também é possível
  escolher se o texto adicionado será anexado ou prefixado.
* Selecione as ações que requerem confirmação prévia: Você pode escolher,
  para cada ação disponível, se ela deve ser realizada imediatamente ou após
  a confirmação. As ações disponíveis são: adicionar texto, limpar área de
  transferência, emular copiar e emular cortar.
* Solicitar confirmação antes de executar as ações selecionadas quando: Você
  pode selecionar se as confirmações serão solicitadas sempre, apenas se
  houver texto na área de transferência ou se a área de transferência não
  estiver vazia (por exemplo, se você copiou um arquivo, não um texto).
* Formato para mostrar o texto da área de transferência como HTML no modo de
  navegação: se você está aprendendo a linguagem de marcação HTML, pode
  escolher Texto pré-formatado em HTML ou HTML como mostrado em um navegador
  da web, para ter uma ideia de como seu código HTML será processado pelo
  NVDA em um navegador. A diferença entre o HTML pré-formatado e o
  convencional é que a primeira opção preservará espaços consecutivos e
  quebras de linha, e a segunda os compactará. Por exemplo, escreva algumas
  marcações — tags — HTML como h1, h2, li, pre, etc., selecione e copie o
  texto para a área de transferência e use o complemento Gestor do Conteúdo
  de Transferência — clipContentsDesigner — para mostrar o texto em uma
  mensagem navegável.
* Número máximo de caracteres ao mostrar o texto da área de transferência no
  modo de navegação: Lembre-se de que aumentar este limite pode causar
  problemas se a área de transferência contiver grandes cadeias de texto. O
  limite padrão é 100000 caracteres.

Notas:

*	Confirmações não serão solicitadas quando uma caixa de mensagem do NVDA
  ainda estiver aberta. Nesses casos, as ações serão executadas
  imediatamente.
*	Os comandos emular cópia e emular corte significam que, quando esses
  recursos estão ativados, o complemento assumirá o controle de control+c e
  control+x. Isso permitirá selecionar se uma confirmação deve ser
  solicitada antes de realizar as ações correspondentes a essas teclas.

## Mudanças na 13.0
* Corrigido um problema no leiaute visual do painel de configurações, graças
  a Cyrille Bougot.
* Documentação melhorada.
* Adicionada uma categoria Gestor do Conteúdo de Transferência para atribuir
  comandos — gestos — de entrada a todos os comandos disponíveis para este
  complemento.
* Falhas corrigidas ao usar emular cópia em navegadores se o modo de foco
  estiver ativo.
* Você pode atribuir diferentes gestos para mostrar o conteúdo textual da
  área de transferência como texto bruto ou formatado em HTML. O formato
  para mostrar o texto da área de transferência no painel de configurações
  foi modificado conformemente, para selecionar as duas opções disponíveis
  para o formato HTML.

## Mudanças na 12.0
* Falhas corrigidas ao usar emular cópia em aplicativos como o LibreOffice
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
