# Clip Contents Designer #

*	Autores: Noelia, Abdel.
*	Compatibilidade con NVDA: da 2018.4 á 2019.2.
*	Descargar [versión estable][1]
*	Descargar [versión de desenvolvemento][2]

Este complemento úsase para engadir texto ó portapapeis, que pode ser útil
cando queras unir seccións de texto listas para pegarse xuntas.  O contido
do portapapeis tamén pode limparse e amosarse en modo exploración.

## Ordes de teclado ##
*	NVDA+windows+c: engade o texto seleccionado, os caracteres braille Unicode
  que representan obxectos MathML, ou a cadea que se marcou co cursor de
  revisión, ao portapapeis.
*	NVDA+windows+x: Limpa o contido do portapapeis.
*	NVDA+windows+f9: Marca a posición actual do cursor de revisión como o comezo do texto a engadir ó portapapeis. Se utilizas NVDA+F9, o texto non se engadirá.
*	 Non asignado: Copia (ou curta) ao/do portapapeis, coa posibilidade de seren preguntado por unha confirmación anterior.
*	 Non asignada: Amosa o texto do portapapeis en modo exploración, ou anuncia se o portapapeis está vacío ou se ten contidos que non se poden presentar nunha mensaxe de modo exploración, por exemplo, en caso de estarse copiando arquivos ou cartafoles dende o Explorador de Windows..

Nota: as ordes anteriores poden cambiarse dende o menú NVDA, submenú
Preferencias, diálogo Xestos de Entrada, categoría Revisión de Texto.

## Menú Preferencias ##
*	Opcións do Clip Contents Designer: permite poñer un separador que poda usarse para atopar os segmentos de texto una vez que todo o texto sexa pegado.
Tamén é posible escoller se o texto engadido se anexará ou se anteporá, se hai accións dispoñibles (engadir, valdeirar portapapeis, emular copiar e emular cortar) deberían realizarse inmediatamente ou despois dunha confirmación, e se se requerirá confirmanción sempre, só se o portapapeis contén texto, ou se o portapapeis non está baleiro.
Ademais, é posible cambiar o formato e o número máximo de caracteres do texto do portapapeis que se amosará en modo exploración. Por favor, ten en conta que incrementar este límite pode causar problemas se o portapapeis contén longas cadeas de texto. O límite por defecto é de 100000 caracteres.

Notas:

*	A orde anterior pódese cambiar dende o menú NVDA, submenú Preferencias,
  diálogo Xestos de Entrada, categoría Configuración.
*	Non se deberían de solicitar confirmacións cando siga aberto unha Caixa de
  mensaxe do NVDA. Nesos casos, as accións realizaranse inmediatamente

## Cambios para 10.0
* Arranxado un erro no diálogo utilizado para mostrar o texto do portapapeis
  cando o seu título contiña caracteres non latinos.
* Arranxado un erro ao utilizar as funcións emular curtar e copiar cunha
  distribución de teclado árabe. Isto foi solucionado por Abdel, engadido
  como un autor do complemento.

## Cambios para 9.0

* Engadida a posibilidade de amosar o texto do portapapeis en modo
  exploración.
* Engadida unha opción para elixir se se requerirán confirmacións se o
  portapapeis non está vacío; por xemplo, se se están a copiar arquivos ou
  cartafoles.
* Requírese do NVDA 2018.4 ou posterior.

## Cambios para 8.0 ##

* A configuración do complemento amósase na categoría correspondente do
  diálogo Opcións do NVDA.
* Requírese do NVDA 2018.2 ou posterior.
* Se fora necesario, podes descargar a [derradeira versión compatible co
  NVDA 2017.3][3].

## Cambios para 7.0

* No diálogo para configurar as funcionalidades de Emular copiar e Emular
  curtar na instalación, se elixes non, os comandos para estas
  características eliminaranse, de xeito que poidas restaurar o
  comportamento normal das teclas ctrl+c e ctrl+x.

## Cambios para 6.0

*	 Engadidas opcións para escoller se as accións dispoñibles se deberían realizar despois da confirmación.
*	Engadíronse ordes Emular copiar e Emular cortar, qué poderían asignarse dende o diálogo Xestos de Entrada.
*	 Engadido un diálogo para configurar as funcionalidades Emular copiar e Emular copiar na instalación. Esto permite engadir as ordes control+c e control+x para copiar e curtar, e ser preguntado se queres reemplazar os contidos do portapapeis ao premer estos atallos de teclado.
*	Arranxada a documentación para script_add (Windows+NVDA+c).

## Cambios para 5.0 ##

*	A presentación visual do diálogo mellorouse, engadíndose á aparenza dos
  diálogos amosados no NVDA.
*	Requírese do NVDA 2016.4 ou posterior.

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

[1]: https://addons.nvda-project.org/files/get.php?file=ccd

[2]: https://addons.nvda-project.org/files/get.php?file=ccd-dev

[3]: https://addons.nvda-project.org/files/get.php?file=ccd-o
