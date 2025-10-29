# Clip Contents Designer #

*	Autori: Noelia, Abdel.

Questo componente aggiuntivo viene utilizzato per aggiungere testo negli
appunti, operazione utile quando si desidera unire sezioni di testo insieme
per poi incollarle in un'unica soluzione. Il contenuto degli appunti può
anche essere cancellato e visualizzato  in Modalità Navigazione.

## Comandi da tastiera ##

  che è stata contrassegnata con il cursore di controllo (comandi NVDA+f9 ed
  NVDA+f10).

  testo negli appunti.
*	Non assegnato: visualizza il testo presente negli appunti in modalità
  navigazione come testo semplice. In alternativa dice se negli appunti è
  presente contenuto che non è possibile mostrare in modalità navigazione,
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

  key.

## Changes for 40.0.0

## Novità nella versione 16.0

  finestra di dialogo dei gesti di immissione.
  Mohammadhosein Ghezelsofla.

* Compatibile con NVDA 2021.1.
## Changes for 13.0

  copia nei browser con la modalità focus attiva.


  degli appunti come testo puro o come HTML. Le scelte possibili nella
  finestra Impostazioni per il formato di visualizzazione degli appunti sono

## Novità nella versione 12.0
## Novità nella versione 11.0

  utilizzando comandi standard di NVDA (NVDA+f9 e NVDA+f10). NVDA+windows+f9
  non è più utilizzato, per una migliore integrazione con il nuovo comando

* Risolto un bug nella finestra di dialogo utilizzata per mostrare il testo
  degli appunti, quando il titolo contiene caratteri non latini.
* Risolto un bug che si verificava quando si utilizzavano le funzioni di
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
  anteposto, attraverso la casella di controllo aggiungi testo prima degli
  appunti, dalla finestra di dialogo impostazioni ClipContents Designer.

## Novità nella versione 3.0 ##

*	Se MathPlayer è installato, può essere aggiunta agli appunti una
*	Se non è stato impostato alcun separatore, verrà inserita soltanto una

  riga vuota tra i segmenti di testo aggiunti agli appunti.

*	Può essere assegnato un tasto caldo per aprire la finestra impostazioni di
*	Aggiunta una casella di controllo nella finestra di dialogo, per
  selezionare se il separatore debba essere copiato per poi essere importato
  in caso di nuova installazione del componente aggiuntivo.

## Novità nella versione 2.0 ##

*	Versione iniziale.

[[!tag dev stable]]
