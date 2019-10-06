# Clip Contents Designer #

*	Autores: Noelia, Abdel.
*	Compatibilidad con NVDA: de 2018.4 a 2019.2.
*	Descargar [versión estable][1]
*	Descargar [versión de desarrollo][2]

Este complemento se utiliza para agregar texto al portapapeles, el cual
puede ser útil cuando quieras unir secciones de texto listas para pegar
juntas.  El contenido del portapapeles también puede limpiarse y mostrarse
en modo exploración.

## Órdenes de teclado ##
*	NVDA+windows+c: añade el texto seleccionado, los caracteres braille
  Unicode que representan objetos MathML, o la cadena que se haya marcado
  con el cursor de revisión, al portapapeles.
*	NVDA+windows+x: Limpia el contenido del portapapeles.
*	NVDA+windows+f9: Marca la posición actual del cursor de revisión como el comienzo del texto a añadir al portapapeles. Si utilizas NVDA+F9, el texto no se añadirá.
*	 No asignado: Copia (o corta) al/del portapapeles, con la posibilidad de ser preguntado por una confirmación previa.
*	 Sin asignar: Muesra el texto de portapapeles en modo exploración, o lo anuncia si el portapapeles está vacío o si tiene contenidos que no se pueden presentar en un mensaje navegable, por ejemplo si se están copiando archivos o carpetas desde el Explorador de Windows..

Nota: Las órdenes anteriores se pueden cambiar desde el menú NVDA, submenú
Preferencias, Diálogo Gestos de Entrada, Categoría Revisión de Texto.

## Menú Preferencias ##
*	Opciones de Clip Contents Designer: te permite poner un separador que se pueda  utilizar para encontrar los segmentos de texto una vez todo el texto añadido sea pegado.
También es posible elegir si el texto añadido se anexará o se antepondrá, si hay acciones disponibles (añadir, vaciar portapapeles, emular copiar y emular cortar) deberían realizarse inmediatamente o después de una confirmación, y de haber confirmaciones si se preguntará siempre, sólo si hay texto en el portapapeles o si el portapapeles no está vacío.
Adicionalmente, es posible cambiar el formato y el número máximo de caracteres del texto del portapapeles que se mostrará en modo exploración. Por favor, ten en cuenta que incrementar este límite podría causar problemas cuando el portapapeles contenga largas cadenas de texto. El límite por defecto es 100000 caracteres.

Notas:

*	La orden anterior puede cambiarse desde el menú NVDA, submenú
  Preferencias, diálogo Gestos de Entrada, Categoría Configuración.
*	No se deberían solicitar confirmaciones cuando siga abierto un cuadro de
  mensaje de NVDA. En esos casos, las acciones se realizarán inmediatamente

## Cambios para 10.0
* Corregido un problema en el diálogo usado para mostrar el texto del
  portapapeles, cuando su título contiene caracteres no latinos.
* Corregido un problema al usar las funciones de emular cortar y copiar con
  la distribución de teclado árabe. Esto ha sido corregido por Abdel, que se
  ha añadido como autor del complemento.

## Cambios para 9.0

* Añadida la posibilidad de mostrar el texto del portapapeles en modo
  exploración.
* Añadida una opción para elegir si se requerirá confirmación si el
  portapapeles no está vacío, por ejemplo, si se están copiando archivos o
  carpetas.
* Se requiere de NVDA 2018.4 o posterior.

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
