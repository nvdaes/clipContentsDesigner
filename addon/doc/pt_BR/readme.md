# Gestor do conteúdo de transferência #
*   Autores: Noelia Ruiz Martínez.
*   Baixe a [versão estável][1]
*   Baixe a [versão de desenvolvimento][2]

This add-on is used to add text to the clipboard, which can be useful when
you want to join sections of text together ready for pasting.  The clipboard
content can also be cleared.

## Comandos de tecla ##
*   NVDA+windows+c: Add selected text, Unicode braille characters which
    represent MathML objects, or the string which has been marked with the
    review cursor, to the clipboard.
*   NVDA+windows+x: Apaga o conteúdo da área de transferência.
*   NVDA+windows+f9: Mark the current position of the review cursor as the
    start of the text to be added to the clipboard.  If you use nvda+F9, the
    text will not be added.

Nota: Os comandos acima podem ser alterados a partir do menu do NVDA,
submenu Preferências, diálogo de Gestos para Entrada, categoria Exploração
de texto.

## Menu Preferências ##
*   Clip Contents Designer settings: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
It's also possible to choose if the added text will be appended or prepended.

Nota: Os comandos acima podem ser alterados a partir do menu do NVDA,
submenu Preferências, diálogo de Gestos para Entrada, categoria
configuração.

## Changes for 4.0 ##
*   Add-on settings are managed from NVDA configuration, so that standard
    profiles can be used to save different separators, and it's not needed
    to copy the settings for importing at reinstallation.
*   Now it's possible to choose if the added text will be appended or
    prepended, using the Add text before clip data check box from the Clip
    Contents Designer settings dialog.

## Mudanças na 3.0 ##
*   Braille representation of MathML objects can be added to the clipboard
    if MathPlayer is installed.
*   If no separator is set, just a single line will be placed between the
    added text segments.
*   Uma tecla de atalho pode ser atribuída para abrir o diálogo de opções do
    gestor do conteúdo de transferência.
*   Adicionada uma caixa de seleção ao diálogo de opções, para escolher se o
    separador deve ser copiado para ser importado ao reinstalar o
    complemento.

## Mudanças na 2.0 ##
*   Hindi characters can be used as the separator between added contents.

## Mudanças na 1.0 ##
*   Versão inicial.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev
