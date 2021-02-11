# Clip Contents Designer #

*	Autori: Noelia, Abdel.
*	Compatibilità con NVDA: versione 2019.3 o successive
*	Scarica la [versione stabile][1]
*	Scarica la [versione in sviluppo][2]

Questo componente aggiuntivo viene utilizzato per aggiungere testo negli
appunti, operazione utile quando si desidera unire sezioni di testo insieme
per poi incollarle in un'unica soluzione. Il contenuto degli appunti può
anche essere cancellato e visualizzato  in Modalità Navigazione.

## Comandi da tastiera ##
*	NVDA + Windows + C: Aggiunge agli appunti il testo selezionato, o i
  caratteri braille unicode che rappresentano oggetti MathMl, o la stringa
  che è stata contrassegnata con il cursore di controllo (comandi NVDA+f9 ed
  NVDA+f10).
*	NVDA + Windows + x: Cancella il contenuto degli appunti.
*	Non assegnato: copia o taglia, con possibilità di richiesta di conferma.
*	Not assigned: Shows the clipboard text as HTML in browse mode, or
  announces if clipboard is empty or has contents which can't be presented
  in a browseable message, for instance if files or folders are been copied
  from Windows Explorer.
*	Not assigned: Shows the textual clipboard contents as plain text in browse
  mode, or announces if clipboard is empty or has contents which can't be
  presented in a browseable message, for instance if files or folders are
  been copied from Windows Explorer.


## Clip Contents Designer settings ##

This panel is available from NVDA's menu, Preferences submenu, Settings
dialog.

It contains the following controls:

* Type the string to be used as a separator between contents added to the
  clipboard: Allows to set a separator which can be used to find the text
  segments once the entire added text is pasted.
* Add text before clip data: It's also possible to choose if the added text
  will be appended or prepended.
* Select the actions which require previous confirmation: You can choose,
  for each action available, if it should be performed inmediately or after
  confirmation. Available actions are: add text, clear clipboard, emulate
  copy and emulate cut.
* Request confirmation before performing the selected actions when: You can
  select if confirmations will be requested always, just if text is
  contained in the clipboard, or if clipboard is not empty (for example if
  you've copied a file, not text).
* Format to show the clipboard text as HTML in browse mode: If you're
  learning HTML markup language, you may choose Preformatted text in HTML or
  HTML as shown in a web browser, to have an idea of how your HTML code will
  be rendered by NVDA in a browser. The difference between preformatted and
  conventional HTML is that the first option will preserve consecutive
  spaces and line breaks, and the second one will compact them.  For
  example, write some HTML tags like h1, h2, li, pre, etc., select and copy
  the text to clipboard, and use clipContentsDesigner add-on to show the
  text in a browseable message.
* Maximum number of characters when showing clipboard text in browse mode:
  Please, be aware that increasing this limit may produce issues if the
  clipboard contains large strings of text. The default limit is 100000
  characters.

Note:

*	Quando è aperta una finestra di NVDA non verrà richiesta alcuna
  conferma. In questi casi le azioni verranno eseguite immediatamente.
*	Emulate copy and emulate cut commands mean that, when these features are
  enabled, the add-on will take control of control+c and control+x. This
  will allow to select if a confirmation should be requested before
  performing the actions corresponding to these keystrokes.

## Changes for 13.0 
* Fixed an issue in visual layout of the settings panel, thanks to Cyrille
  Bougot.
* Improved documentation.
* Added a Clip Contents Designer category to assign input gestures to all
  commands available for this add-on.
* Fixed bugs when using emulate copy in browsers if focus mode is active.
* You can assign different gestures to show the clipboard textual contents
  as raw text or formatted in HTML. The Format to show the clipboard text in
  the settings panel has being modified accordingly, to select the two
  options available for HTML format.

## Novità nella versione 12.0
* Risolti problemi che si riscontravano quando si utilizzava la simulazione
  copia in applicazioni come LibreOffice Writer.

## Novità nella versione 11.0
* E' ora possibile agiungere testo selezionato con il cursore di controllo
  utilizzando comandi standard di NVDA (NVDA+f9 e NVDA+f10). NVDA+windows+f9
  non è più utilizzato, per una migliore integrazione con il nuovo comando
  NVDA+shift+f9.
* Richiede NVDA 2019.3 o versioni successive.

## Novità nella versione 10.0
* Risolto un bug nella finestra di dialogo utilizzata per mostrare il testo
  degli appunti, quando il titolo contiene caratteri non latini.
* Risolto un bug che si verificava quando si utilizzavano le funzioni di
  simulazione taglia e copia con un layout di tastiera arabo. Questo
  problema è stato risolto da Abdel, aggiunto come autore.

## Novità nella versione 9.0

* Aggiunta la possibilità  di visualizzare il testo negli appunti in
  Modalità Navigazione.
* Aggiunta l'opzione per la richiesta di conferma quando negli appunti è
  presente contenuto vario, per esempio, se sono presenti file o cartelle.
* Richiede NVDA 2018.4 o versioni successive.

## Novità nella versione 8.0 ##

* Le impostazioni del componente aggiuntivo vengono mostrate nella
  corrispondente categoria della finestra  impostazioni di NVDA.
* Richiede NVDA 2018.2 o versioni successive.
* Se necessario, è possibile scaricare [l'ultima versione compatibile con
  NVDA 2017.3][3].

## Novità nella versione 7.0

* Nella finestra per configurare le operazioni di simulazione taglia e
  simulazione copia durante l'installazione,    se si sceglie di no, i
  comandi per queste operazioni verranno rimossi. In questo modo si possono
  utilizare control+C e control+x normalmente.

## Novità nella versione 6.0

*	 Aggiunte opzioni per stabilire se le azioni disponibili debbano essere eseguite dopo un messaggio di conferma.
*	 Aggiunti i comandi di simulazione copia e simulazione taglia, ai quali possono essere assegnati tasti dalla finestra di dialogo Gesti e Tasti di immissione.
*	 Aggiunta una finestra di dialogo che permette di configurare il comportamento della simulazione copia e simulazione taglia durante l'installazione. Ciò consente di controllare i comandi ctrl+c e ctrl+x per copia e taglia, in modo che venga richiesto all'utente se desidera sovrascrivere il contenuto attuale degli appunti quando preme questi tasti.
*	Risolto un bug nella documentazione per lo script_add (Windows+NVDA+c).

## Novità nella versione 5.0 ##

*	Migliorata la presentazione visiva della finestra di dialogo, in
  conformità con l'aspetto standard di NVDA.
*	Richiede NVDA 2016.4 o superiore.

## Novità nella versione 4.0 ##
*	Le impostazioni del componente aggiuntivo sono gestite dalla
  configurazione di NVDA. In questo modo si possono utilizzare i profili di
  configurazione di NVDA per salvare separatori differenti e non c'è bisogno
  di copiare le impostazioni ed importarle in caso di reinstallazione.
*	Ora è possibile stabilire se il testo aggiunto debba essere accodato o
  anteposto, attraverso la casella di controllo aggiungi testo prima degli
  appunti, dalla finestra di dialogo impostazioni ClipContents Designer.

## Novità nella versione 3.0 ##
*	Se MathPlayer è installato, può essere aggiunta agli appunti una
  rappresentazione Braille di oggetti MathMl.
*	Se non è stato impostato alcun separatore, verrà inserita soltanto una
  riga vuota tra i segmenti di testo aggiunti agli appunti.
*	Può essere assegnato un tasto caldo per aprire la finestra impostazioni di
  Clip Contents Designer.
*	Aggiunta una casella di controllo nella finestra di dialogo, per
  selezionare se il separatore debba essere copiato per poi essere importato
  in caso di nuova installazione del componente aggiuntivo.

## Novità nella versione 2.0 ##
*	Possono essere usati caratteri Hindi come separatori per il testo aggiunto
  aglu appunti.

## Novità nella versione 1.0 ##
*	Versione iniziale.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ccd

[2]: https://addons.nvda-project.org/files/get.php?file=ccd-dev

[3]: https://addons.nvda-project.org/files/get.php?file=ccd-o
