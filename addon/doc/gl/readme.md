# Clip Contents Designer #

*	Autores: Noelia, Abdel.
*	Compatibilidade con NVDA: 2019.3 ou posterior
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
*	Sen asignar: Copia a (ou corta dende) o portapapeis, coa posibilidade de
  que se che pregunte por unha confirmación previa.
*	Sen asignar: amosa o texto do portapapeis como HTML en modo exploración,
  ou anuncia se o portapapeis está vacío ou ten contido que non se pode
  amosar nunha mensaxe navegable, se se están a copiar arquivos ou carpetas
  do Explorador de Windows, por exemplo.
*	Sen asignar: Amosa os contidos textuais do portapapeis como texto plano en
  modo exploración, ou anuncia se o portapapeis está vacío ou ten contido
  que non se pode amosar nunha mensaxe navegable, se se están a copiar
  arquivos ou carpetas do Explorador de Windows, por exemplo.


## Opcións de Clip Contents Designer ##

Este panel está dispoñible dende o menú de NVDA, submenú Preferencias,
diálogo Opcións.

contén os seguintes controis:

* Escribe a cadea de texto que se utilizará como separador entre contido
  engadido ao portapapeis: Permite establecer un separador que se pode
  utilizar para buscar os segmentos de texto unha vez se pegue todo o texto
  engadido.
* Engadir texto tralos datos do portapapeis: Tamén é posible escoller se o
  texto engadido se engadirá ó final ou ó principio.
* Seleccionar as accións que requiren confirmación previa: Podes escoller,
  para cada acción dispoñible, se se debe realizar inmediatamente ou previa
  confirmación. As accións dispoñibles son: engadir texto, limpar
  portapapeis, emular copiar e emular curtar.
* Pedir confirmación antes das accións seleccionadas cando: Podes
  seleccionar se as confirmacións se solicitarán sempre, só se o portapapeis
  contén texto, ou se o portapapeis non está baleiro (por exemplo se
  copiaches un arquivo, non texto).
* Formato no que amosar o texto do portapapeis como HTML en modo
  exploración: Se estás aprendendo a linguaxe de marcas HTML, podes escoller
  Texto Preformateado en HTML ou HTML como se amosaría nun navegador web,
  para ter unha idea de cómo o teu código HTML se tratará dende NVDA nun
  navegador. A diferencia entre HTML preformateado e convencional é que a
  primeira opción preservará os espazos e saltos de liña consecutivos, e o
  segundo compactaraos.  Por exemplo, escribe algunhas etiquetas HTML como
  h1, h2, li, pre, etc., selecciona e copia o texto ao portapapeis, e
  utiliza o complemento ClipContentsDesigner para amosar o texto nunha
  mensaxe navegable.
* Número máximo de caracteres ao amosar texto do portapapeis en modo
  exploración: Por favor, ten en conta que incrementar este límite podería
  producir problemas se o portapapeis contén largas cadeas de texto. O
  límite por defecto é de 100000 caracteres.

Notas:

*	Non se solicitarán confirmacións cando estea aberta unha Caixa de mensaxe
  do NVDA. Neses casos, as accións realizaranse inmediatamente.
*	As ordes emular copiar e emular curtar significan que, cando estas
  características estean habilitadas, o complemento controlará control+c e
  control+x. Isto permitirá seleccionar se se debería pedir unha
  confirmación antes de realizar as accións de ditos atallos.

## Cambios para 13.0 
* Arranxado un problema no deseño visual do panel de opcións, grazas a
  Cyrille Bougot.
* Mellorada a documentación.
* Engadida unha categoría Clip contents Designer para asignar xestos de
  entrada a tódolas ordes dispoñibles neste complemento.
* Arranxados erros ao usar emular copiar en en navegadores cando o modo foco
  estaba activo.
* Podes asignar diferentes xestos para amosar o contido textual do
  portapapeis como texto plano ou formateado en HTML. O Formato no que
  amosar o texto do portapapeis no panel de opcións modificouse en
  consecuencia, para seleccionar as dúas opcións dispoñibles para o formato
  HTML.

## Cambios para 12.0
* Arranxados erros ao usar emular copiar en aplicacións como LIbreOffice
  Writer.

## Cambios para 11.0
* Agora é posible engadir texto marcado co cursor de revisión utilizando
  ordes estándar do NVDA (NVDA+F9 e NVDA+F10). NVDA+Windows+F9 xa non se
  usa, para unha mellor integración co novo atallo NVDA+Shift+F9.
* Require NVDA 2019.3 ou posterior.

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
