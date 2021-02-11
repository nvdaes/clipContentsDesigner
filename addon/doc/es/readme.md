# Clip Contents Designer #

*	Autores: Noelia, Abdel.
*	Compatibilidad con NVDA: 2019.3 y versiones posteriores
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
*	Sin asignar: copia hacia (o desde) el portapapeles, con la posibilidad de
  solicitar una confirmación previa.
*	Sin asignar: Muestra el texto del portapapeles como HTML en modo
  exploración, o lo anuncia si el portapapeles está vacío o si tiene
  contenidos que no se pueden presentar en un mensaje navegable, por ejemplo
  si se están copiando archivos o carpetas desde el Explorador de Windows.
*	Sin asignar: Muestra el texto del portapapeles como texto sin formato en
  modo exploración, o lo anuncia si el portapapeles está vacío o si tiene
  contenidos que no se pueden presentar en un mensaje navegable, por ejemplo
  si se están copiando archivos o carpetas desde el Explorador de Windows.


## Opciones de Clip Contents Designer ##

Este panel se encuentra disponible en el menú NVDA, submenú Preferencias,
diálogo Opciones.

Contiene los siguientes controles:

* Teclea la cadena que se usará como separador entre contenidos añadidos al
  portapapeles: permite configurar un separador que puede usarse para buscar
  los segmentos de texto una vez que se pega el texto completo.
* Añadir texto antes de los datos del portapapeles: también es posible
  elegir si el texto añadido irá antes o después.
* Elige las acciones que requieren confirmación previa: puedes elegir, en
  cada acción disponible, si se debe realizar inmediatamente o tras una
  confirmación. Las acciones disponibles son: añadir texto, limpiar
  portapapeles, emular copia y emular cortar.
* Cuándo solicitar confirmación antes de realizar las acciones
  seleccionadas: puedes elegir si se solicitarán confirmaciones siempre,
  sólo si el portapapeles contiene texto, o si el portapapeles no está vacío
  (por ejemplo si has copiado un archivo, y no texto).
* Formatear para mostrar el texto del portapapeles como HTML en modo
  exploración: si estás aprendiendo el lenguaje de marcado HTML, puedes
  elegir texto preformateado en HTML o HTML como se muestra en un navegador
  web, para hacerte una idea de cómo renderizará NVDA tu código HTML en un
  navegador web. La diferencia entre HTML preformateado y convencional es
  que la primera opción preservará espacios consecutivos y saltos de línea,
  mientras que la segunda los compactará. Por ejemplo, escribe algunas
  etiquetas HTML como h1, h2, li, pre, etc., selecciona y copia el texto al
  portapapeles, y usa el complemento ClipContentsDesigner para mostrar el
  texto en un mensaje explorable.
* Máximo de caracteres cuando se muestra el texto del portapapeles en modo
  exploración: por favor, ten en cuenta que aumentar este límite puede
  producir problemas si el portapapeles contiene grandes cadenas de
  texto. El límite predeterminado es de 100000 caracteres.

Notas:

*	No se solicitarán confirmaciones cuando siga abierto un cuadro de mensaje
  de NVDA. En esos casos, las acciones se realizarán inmediatamente.
*	Las órdenes Emular copiar y Emular cortar significan que, cuando estas
  funciones están activadas, el complemento tomará el control de control+c y
  control+x. Esto permitirá elegir si se debería solicitar una confirmación
  antes de realizar las acciones correspondientes a estos atajos de teclado.

## Cambios para 13.0 
* Se ha corregido un problema en la disposición visual del panel de
  opciones, gracias a Cyrille Bougot.
* Se ha mejorado la documentación.
* Se ha añadido una categoría Clip Contents Designer para asignar gestos de
  entrada a todas las órdenes disponibles para este complemento.
* Se han corregido fallos al usar Emular copia en navegadores si el modo
  foco está activo.
* Puedes asignar diferentes gestos para mostrar el contenido textual del
  portapapeles como texto sin formato o formateado en HTML. Se ha modificado
  apropiadamente el formato en el que se muestra el texto del portapapeles
  en el panel de opciones para seleccionar las dos opciones disponibles para
  el formato HTML.

## Cambios para 12.0
* Se han corregido fallos al usar Emular copia en aplicaciones como Libre
  Office Writer.

## Cambios para 11.0
* Ahora es posible añadir texto marcado con el cursor de revisión usando
  órdenes estándar de NVDA (NVDA+f9 y NVDA+f10). Ya no se usa
  NVDA+windows+f9, para mejorar la integración con la nueva orden
  NVDA+shift+f9.
* Se requiere NVDA 2019.3 o posterior.

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
