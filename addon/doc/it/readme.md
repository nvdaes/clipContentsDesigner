# Clip Contents Designer #

*	Autori: Noelia, Abdel.
*	Compatibilità con NVDA: versione 2019.3 o successive
*	Scarica la [versione stabile][1]
*	Scarica la [versione in sviluppo][2]

Questo componente aggiuntivo viene utilizzato per aggiungere testo negli
appunti, operazione utile quando si desidera unire sezioni di testo insieme
per poi incollarlo. Il contenuto degli appunti può anche essere cancellato e
visualizzato  in Modalità Navigazione.

## Comandi da tastiera ##

* NVDA + Windows + C: Aggiunge e copia negli appunti il testo selezionato, o
  i caratteri braille unicode che rappresentano oggetti MathMl, o la stringa
  che è stata contrassegnata con il cursore di controllo.
* NVDA + Windows + x: Cancella contenuto degli appunti.
* Non assegnato: copia o taglia, con possibilità di richeista di conferma.
* Non assegnato: visualizza il testo presente negli appunti in un messaggio
  navigabile. Se negli appunti è presente contenuto diverso, come file o
  cartelle copiate precedentemente, NVDA informa che non è presente testo
  negli appunti.

Nota: I comandi di cui sopra possono essere modificati dal menu di NVDA,
sottomenu Preferenze, gesti di immissione, categoria revisione del testo.

## Menu preferenze ##
*	Impostazioni Clip Contents Designer: Permette di impostare un separatore che può essere utilizzato per trovare i segmenti di testo quando l'intero testo aggiunto viene incollato.
è anche possibile stabilire se il testo aggiunto debba essere accodato o anteposto, se le azioni disponibili (aggiungi, svuota appunti, simula copia e simula taglia) debbano essere eseguite immediatamente o previa conferma, e se tale conferma verrà richiesta sempre, solo se vi è testo contenuto negli appunti o solo se gli appunti non sono vuoti.
Inoltre, è possibile configurare il formato ed il numero massimo di carattere da visualizzare in Modalità Navigazione. Di default è impostato su 100.000; tenere presente che stringhe di testo troppo grandi possono comportare problemi.

Note:

*	Il comando sopra citato può essere modificato dal menu di NVDA, sottomenu
  Preferenze, gesti e tasti di immissione, categoria Configurazione.
*	Quando è aperta una finestra di NVDA non verrà visualizzato il messaggio
  di conferma. In questi casi le azioni verranno eseguite immediatamente.

## Novità nella versione 11.0
* E' ora possibile agiungere testo selezionato con il cursore di controllo
  utilizzando comandi standard di NVDA (NVDA+f9 e NVDA+f10). NVDA+windows+f9
  non è più utilizzato, per una migliore interazione con il nuovo comando
  NVDA+shift+f9.
* Richiede NVDA 2019.3 o superiore.

## Novità nella versione 10.0
* Risolto un bug nella finestra di dialogo utilizzata per mostrare il testo
  degli appunti, quando il titolo contiene caratteri non latini.
* Risolto un bug che si verificava quando si utilizzavano le funzioni di
  taglio e copia dell'emulazione con un layout di tastiera arabo. Questo
  problema è stato risolto da Abdel, aggiunto come autore.

## Novità nella versione 9.0

* Aggiunta la possibilità  di visualizzare il testo negli appunti in
  Modalità Navigazione.
* Aggiunta l'opzione per la richiesta di conferma quando negli appunti è
  presente contenuto vario, per esempio, se son presenti file o cartelle.
* Richiede NVDA 2018.4 o superiore.

## NOvità nella versione 8.0 ##

* Le impostazioni del componente aggiuntivo verranno visualizzate sulla
  corrispondente categoria della finestra  impostazioni di NVDA.
* Richiede NVDA 2018.2 o superiore.
* Se necessario, è possibile scaricare [l'ultima versione compatibile con
  NVDA 2017.3][3].

## Novità nella versione 7.0

* Se durante l'installazione si sceglie di non usare  la simulazione copia e
  la simulazione taglia, questi comandi verranno rimossi; in questo modo si
  possono  utilizare control+C e control+x normalmente.

## Novità nella versione 6.0

*	 Aggiunte opzioni per stabilire se le azioni disponibili debbano essere eseguite dopo un messaggio di conferma.
*	 Aggiunti i comandi di simulazione copia e simulazione taglia, che possono essere assegnati dalla finestra di dialogo tasti e gesti di immissione.
*	 Aggiunta una finestra di dialogo che permette di configurare il comportamento della simulazione copia e simulazione taglia durante l'installazione. Ciò consente di controllare i comandi ctrl+c e ctrl+v per copia e taglia, in modo che venga richiesto all'utente se desidera sovrascrivere il contenuto attuale degli appunti prima di effettuare una copia del contenuto selezionato.
*	Risolto un bug nella documentazione per lo script_add (Windows+NVDA+c).

## Novità nella versione 5.0 ##

*	Migliorata la presentazione visiva della finestra di dialogo,
  conformandosi all'aspetto standard di NVDA.
*	Richiede NVDA 2016.4 o superiore.

## Novità nella versione 4.0 ##
*	Le impostazioni del componente aggiuntivo sono gestite dalla
  configurazione di NVDA, cosicché ci si possa servire dei profili standard
  per salvare separatori differenti; non ci sarà bisogno quindi di copiare
  le impostazioni ed importarle in caso di reinstallazione.
*	Ora è possibile stabilire se il testo aggiunto debba essere accodato o
  anteposto, attraverso la casella di controllo aggiungi testo prima degli
  appunti, dalla finestra di dialogo impostazioni ClipContents Designer.

## Novità nella versione 3.0 ##
*	Una rappresentazione Braille di oggetti MathMl può essere accodata agli
  appunti se MathPlayer è installato.
*	Se non è stato impostato alcun separatore, verrà inserita soltanto una
  riga vuota tra i segmenti di testo accodato.
*	Può essere assegnato un tasto caldo per aprire la finestra impostazioni di
  Clip Contents Designer.
*	Aggiunta una casella di controllo nella finestra di dialogo, per
  selezionare se il separatore debba essere copiato per poi essere importato
  in caso di nuova installazione del componente aggiuntivo.

## Novità nella versione 2.0 ##
*	Possono essere usati caratteri Hindi come separatori per il testo aggiunto
  .

## Novità nella versione 1.0 ##
*	Versione iniziale.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ccd

[2]: https://addons.nvda-project.org/files/get.php?file=ccd-dev

[3]: https://addons.nvda-project.org/files/get.php?file=ccd-o
