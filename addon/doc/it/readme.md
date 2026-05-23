# Clip Contents Designer #

*	Autori: Noelia, Abdel.

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
*	Non assegnato: visualizza il testo presente negli appunti in modalità
  navigazione in formato html. In alternativa dice se negli appunti è
  presente contenuto che non è possibile mostrare in modalità navigazione,
  come file o cartelle copiati da Windows Explorer, o se non è presente
  testo negli appunti.
*	Non assegnato: visualizza il testo presente negli appunti in modalità
  navigazione come testo semplice. In alternativa dice se negli appunti è
  presente contenuto che non è possibile mostrare in modalità navigazione,
  come file o cartelle copiati da Windows Explorer, o se non è presente
  testo negli appunti.


## Impostazioni dell'add-on ##

Si accede a questa finestra dal menu di NVDA, scegliendo la voce Preferenze
e quindi Impostazioni.

Essa contiene i seguenti controlli:

* Digitare il testo da usare come separatore tra i contenuti aggiunti negli
  appunti: permette di definire un separatore da usare per individuare, nel
  momento in cui si effettua l'operazione di "incolla", i vari segmenti di
  testo aggiunti in sequenza agli appunti.
* Aggiungi testo prima degli appunti: è anche possibile scegliere se il
  testo tagliato o copiato deve essere aggiunto allin testa o in coda agli
  appunti.
* Seleziona le azioni che richiedono una conferma: si può scegliere, per
  ogni azione disponibile, se farla eseguire immediatamente o dopo una
  conferma da parte dell'utente. Le azioni disponibili sono: aggiungi testo,
  elimina gli appunti, emula copia ed emula taglia.
* Richiedi conferma prima di eseguire le azioni selezionate quando: si può
  scegliere se le conferme devono essere richieste sempre, solo se c'è del
  testo negli appunti o se gli appunti non sono vuoti (ossia, ad esempio, se
  avete copiato un file e non del testo).
* Formato di visualizzazione degli appunti in Modalità Navigazione, come
  html: se state imparando il linguaggio HTML, potete selezionare "HTML
  preformattato" oppure HTML semplice, per avere un'idea di come NVDA
  mostrerebbe il vostro codice HTML in un browser. La differenza tra l'HTML
  preformattato e quello semplice è che la prima opzione manterrà gli spazi
  consecutivi e le interruzioni di riga, mentre la seconda li eliminerà. Ad
  esempio, scrivete qualche tag HTML come h1, h2, li, pre, ecc., Selezionate
  e copiate quanto scritto negli appunti ed utilizzate clipContentsDesigner
  per visualizzare il testo in modalità navigazione.
* Numero massimo di caratteri quando il testo degli appunti è visualizzato
  in modalità navigazione: si noti che l'incremento di questo valore può
  causare problemi se gli appunti contengono grandi stringhe di testo. Il
  valore di default è 100000 caratteri.
* Restore defaults.

Note:

*	Quando è aperta una finestra di NVDA non verrà richiesta alcuna
  conferma. In questi casi le azioni verranno eseguite immediatamente.
*	Emulate copy and emulate cut commands mean that, when these features are
  enabled, the add-on will take control of control+c and control+x. This
  will allow to select if a confirmation should be requested before
  performing the actions corresponding to these keystrokes.

## Changes for 46.0.0
* NVDA will sanitize HTML in browseable messages.
* Added a button to close browseable messages, in addition to the Escape
  key.


## Changes for 40.0.0
* Added support for Hebrew keyboard.

## Changes for 22.0.0
* Added a button to restore defaults in the add-on settings panel.
* The add-on cannot be run in secure mode.

## Changes for 17.0
* Compatible with NVDA 2023.1.

## Novità nella versione 16.0
* Reqires NVDA 2022.1 or later.

## Novità nella versione 15.0
* Il comando per aggiungere testo agli appunti è nuovamente presente nella
  finestra di dialogo dei gesti di immissione.
* Risolti i gesti da copiare e tagliare con la tastiera persiana, grazie a
  Mohammadhosein Ghezelsofla.

## Novità nella versione 14.0
* Compatibile con NVDA 2021.1.

## Changes for 13.0
* Risolto un problema nella grafica della finestra Impostazioni. Grazie a
  Cyrille Bougot.
* Miglioramenti alla documentazione.
* Aggiunta la categoria Clip Contents Designer nella finestra Gesti e Tasti
  di Immissione di NVDA, per assegnare tasti personalizzati a tutti i
  comandi disponibili.
* Risolti problemi che si riscontravano quando si utilizzava l'emulazione
  copia nei browser con la modalità focus attiva.
* Potete assegnare tasti diversi per visualizzare il contenuto testuale
  degli appunti come testo puro o come HTML. Le scelte possibili nella
  finestra Impostazioni per il formato di visualizzazione degli appunti sono
  state modificate di conseguenza, per riflettere le due opzioni disponibili
  per l'HTML.

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

## Novità nella versione 7.0

* Nella finestra per configurare le operazioni di simulazione taglia e
  simulazione copia durante l'installazione,    se si sceglie di no, i
  comandi per queste operazioni verranno rimossi. In questo modo si possono
  utilizare control+C e control+x normalmente.

## Novità nella versione 6.0

*	Added options to choose if available actions should be performed after
  confirmation.
*	Added Emulate copy and Emulate cut commands, which could be assigned from
  the Input gestures dialog.
*	Added a dialog to configure the Emulate copy and Emulate cut
  functionalities at installation. This allows to add the control+c and
  control+x commands to copy and cut, and be asked if you want to replace
  the clipboard contents when pressing these keystrokes.
*	Fixed documentation for script_add (Windows+NVDA+c).

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

