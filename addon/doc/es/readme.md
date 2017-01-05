# Clip Contents Designer #

*	Autores: Noelia Ruiz Martínez.
*	Descargar [versión estable][1]
*	Descargar [versión de desarrollo][2]

Este complemento se utiliza para agregar texto al portapapeles, el cual
puede ser útil cuando quieras unir secciones de texto listas para pegar
juntas.  El contenido del portapapeles también puede limpiarse.

## Órdenes de teclado ##
*	NVDA+windows+c: añade el texto seleccionado, los caracteres braille
  Unicode que representan objetos MathML, o la cadena que se haya marcado
  con el cursor de revisión, al portapapeles.
*	NVDA+windows+x: Limpia el contenido del portapapeles.
*	NVDA+windows+f9: Mark the current position of the review cursor as the start of the text to be added to the clipboard.
    If you use nvda+F9, the text will not be added.

Nota: Las órdenes anteriores se pueden cambiar desde el menú NVDA, submenú
Preferencias, Diálogo Gestos de Entrada, Categoría Revisión de Texto.

## Menú Preferencias ##
*	Clip Contents Designer settings: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
It's also possible to choose if the added text will be appended or prepended.

Nota: La orden anterior puede cambiarse desde el menú NVDA, submenú
Preferencias, diálogo Gestos de Entrada, Categoría Configuración.

## Changes for 5.0 ##

*	The visual presentation of the dialog has been enhanced, adhering to the
  appearance of the dialogs shown in NVDA.
*	Requires NVDA 2016.4 or later.

## Cambios para 4.0 ##
*	Ahora las opciones del complemento se gestionan desde la configuración de
  NVDA, así que pueden utilizarse perfiles estándar para guardar diferentes
  separadores, y no es necesario copiar las opciones para importarlas en la
  reinstalación.
*	Ahora es posible elegir si el texto añadido se anexará o se antepondrá,
  utilizando la casilla de verificacción Añadir texto antes de clip data
  desde el diálogo de opciones de Clip Contents Designer.

## Cambios para 3.0 ##
*	Se puede añadir al portapapeles la representación braille de objetos
  MathML si MathPlayer está instalado.
*	<Si no se a puesto un separador, se colocará una sola línea entre los
  segmentos de texto añadido.
*	Se puede asignar un atajo de teclado para abrir el diálogo de Opciones de
  Clip Contents Designer.
*	Añadida una casilla de verificación en el diálogho de opciones, para
  elegir si el separador debería copiarse para importarse cuando se
  reinstale el complemento.

## Cambios para 2.0 ##
*	Se pueden utilizar caracteres hindi como separador entre contenidos
  añadidos.

## Cambios para 1.0 ##
*	Versión inicial.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev
