# Clip Contents Designer #

*	Autores: Noelia Ruiz Martínez.
*	Descargar [versión estable][1]
*	Descargar [versión de desenvolvemento][2]

Este complemento úsase para engadir texto ó portapapeis, que pode ser útil
cando queras unir seccións de texto listas para pegarse xuntas.  O contido
do portapapeis tamén pode limparse.

## Ordes de teclado ##
*	NVDA+windows+c: engade o texto seleccionado, os caracteres braille Unicode
  que representan obxectos MathML, ou a cadea que se marcou co cursor de
  revisión, ao portapapeis.
*	NVDA+windows+x: Limpa o contido do portapapeis.
*	NVDA+windows+f9: Mark the current position of the review cursor as the start of the text to be added to the clipboard.
    If you use nvda+F9, the text will not be added.

Nota: as ordes anteriores poden cambiarse dende o menú NVDA, submenú
Preferencias, diálogo Xestos de Entrada, categoría Revisión de Texto.

## Menú Preferencias ##
*	Clip Contents Designer settings: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
It's also possible to choose if the added text will be appended or prepended.

Nota: A orde anterior pódese cambiar dende o menú NVDA, submenú
Preferencias, diálogo Xestos de Entrada, categoría Configuración.

## Changes for 5.0 ##

*	The visual presentation of the dialog has been enhanced, adhering to the
  appearance of the dialogs shown in NVDA.
*	Requires NVDA 2016.4 or later.

## Cambios para 4.0 ##
*	As opción do complemento adminístranse dende a configuración do NVDA, así
  que os perfís estándar pódense usar para gardar diferentes separadores, e
  non é necesario copiar as opcións para importalas na reinstalación.
*	Agora é posible escoller se o texto engadido se anexará ou se anteporá,
  usando a casilla de verificación Engadir texto antes de clip data dende o
  diálogo Opcións do Clip Contents Designer.

## Cambios para 3.0 ##
*	Pódese engadir a representación braille de obxectos MathML ó portapapeis
  se MathPlayer está instalado.
*	Se non se puxo un separador, porase una soa liña entre os segmentos de
  texto engadido.
*	Pódese asignar un atallo de teclado para abrir o diálogo de opcións do
  Clip Contents Designer .
*	Engadida unha caixa de verificación no diálogo de opcións, para escoller
  se o separador se debería copiar para seren importado cando se reinstale o
  complemento.

## Cambios para 2.0 ##
*	Pódense usar caracteres Hindi como o separador entre contidos engadidos.

## Cambios para 1.0 ##
*	Versión inicial.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev
