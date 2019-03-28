# Clip Contents Designer #

*	Autores: Noelia Ruiz Martínez.
*	Compatibilidad con NVDA: de 2018.2 a 2019.1.
*	Descargar [versión estable][1]
*	Descargar [versión de desarrollo][2]

This add-on is used to add text to the clipboard, which can be useful when
you want to join sections of text together ready for pasting.  The clipboard
content can also be cleared an shown in browse mode.

## Órdenes de teclado ##
*	NVDA+windows+c: añade el texto seleccionado, los caracteres braille
  Unicode que representan objetos MathML, o la cadena que se haya marcado
  con el cursor de revisión, al portapapeles.
*	NVDA+windows+x: Limpia el contenido del portapapeles.
*	NVDA+windows+f9: Mark the current position of the review cursor as the start of the text to be added to the clipboard. If you use nvda+F9, the text will not be added.
*	 Not assigned: Copies to (or cuts from) the clipboard, with the possibility of being asked for a previous confirmation.
*	 Not assigned: Shows the clipboard text in browse mode, or announces if clipboard is empty or has contents which can't be presented in a browseable message, for instance if files or folders are been copied from Windows Explorer..

Nota: Las órdenes anteriores se pueden cambiar desde el menú NVDA, submenú
Preferencias, Diálogo Gestos de Entrada, Categoría Revisión de Texto.

## Menú Preferencias ##
*	Clip Contents Designer settings: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
It's also possible to choose if the added text will be appended or prepended, if available actions (add, clear clipboard, emulate copy and emulate cut) should be performed inmediately or after confirmation, and if confirmations will be requested always, just if text is contained in the clipboard, or if clipboard is not empty.
Furthermore, it's possible to change the format and maximum number of characters of the clipboard text which will be shown in browse mode. Please, be aware that increasing this limit may produce issues if the clipboard contains large strings of text. The default limit is 100000 characters.

Notas:

*	La orden anterior puede cambiarse desde el menú NVDA, submenú
  Preferencias, diálogo Gestos de Entrada, Categoría Configuración.
*	No se deberían solicitar confirmaciones cuando siga abierto un cuadro de
  mensaje de NVDA. En esos casos, las acciones se realizarán inmediatamente

## Changes for 9.0

* Added the possibility of showing the clipboard text in browse mode.
* Added an option to choose if confirmations will be required if clipboard
  is not empty, for instance, if files or folders are been copied.
* Requires NVDA 2018.4 or later.

## Cambios para 8.0 ##

* La configuración del complemento se muestra en la categoría
  correspondiente del diálogo Opciones de NVDA.
* Se requiere de NVDA 2018.2 o posterior.
* Si fuese necesario, puedes descargar la [última versión compatible con
  NVDA 2017.3][3].

## Cambios para 7.0

* En el diálogo para configurar las funciones Emular copiar y Emular cortar
  en la instalación, si eliges no, los comandos para estas características
  se eliminarán, de manera que puedas restaurar el comportamiento anterior
  de ctrl+c y ctrl+x.

## Cambios para 6.0

*	 Añadidas opciones para elegir si las acciones disponibles se deberían llevar a cabo después de la confirmación.
*	Se han añadido órdenes Emular copiar y Emular cortar, qué podrían asignarse desde el diálogo Gestos de Entrada.
*	 Añadido un diálogo para configurar las funcionalidades Emular copiar y Emular copiar en la instalación. Esto permite añadir las órdenes control+c y control+x para copiar y cortar, y ser preguntado si quieres reemplazar los contenidos del portapapeles al pulsar estos atajos de teclado.
*	Corregida la documentación para script_add (Windows+NVDA+c).

## Cambios para 5.0 ##

*	La presentación visual del diálogo se ha mejorado, adhiriéndose a la
  apariencia de los diálogos mostrados por NVDA.
*	Se requiere de NVDA 2016.4 o posterior.

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

[1]: https://addons.nvda-project.org/files/get.php?file=ccd

[2]: https://addons.nvda-project.org/files/get.php?file=ccd-dev

[3]: https://addons.nvda-project.org/files/get.php?file=ccd-o
