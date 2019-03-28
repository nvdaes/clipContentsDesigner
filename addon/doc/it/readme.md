# Clip Contents Designer #

*	Autori: Noelia Ruiz Martínez.
*	Compatibile con NVDA  2018.2 a 2019.1.
*	Scarica la [versione stabile][1]
*	Scarica la [versione in sviluppo][2]

This add-on is used to add text to the clipboard, which can be useful when
you want to join sections of text together ready for pasting.  The clipboard
content can also be cleared an shown in browse mode.

## Comandi rapidi ##
*	NVDA + Windows + C: Aggiunge e copia negli appunti il testo selezionato, o
  i caratteri braille unicode che rappresentano oggetti MathMl, o la stringa
  che è stata contrassegnata con il cursore di controllo.
*	NVDA + Windows + x: Cancella contenuto degli appunti.
*	NVDA+windows+f9: Mark the current position of the review cursor as the start of the text to be added to the clipboard. If you use nvda+F9, the text will not be added.
*	 Not assigned: Copies to (or cuts from) the clipboard, with the possibility of being asked for a previous confirmation.
*	 Not assigned: Shows the clipboard text in browse mode, or announces if clipboard is empty or has contents which can't be presented in a browseable message, for instance if files or folders are been copied from Windows Explorer..

Nota: I comandi di cui sopra possono essere modificati dal menu di NVDA,
sottomenu Preferenze, gesti di immissione, categoria revisione del testo.

## Menu preferenze ##
*	Clip Contents Designer settings: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
It's also possible to choose if the added text will be appended or prepended, if available actions (add, clear clipboard, emulate copy and emulate cut) should be performed inmediately or after confirmation, and if confirmations will be requested always, just if text is contained in the clipboard, or if clipboard is not empty.
Furthermore, it's possible to change the format and maximum number of characters of the clipboard text which will be shown in browse mode. Please, be aware that increasing this limit may produce issues if the clipboard contains large strings of text. The default limit is 100000 characters.

Nota:

*	Il comando sopra citato può essere modificato dal menu di NVDA, sottomenu
  Preferenze, gesti di immissione, categoria Configurazione
*	Quando è aperta una finestra di NVDA non verrà visualizzato il messaggio
  di conferma. In questa situazione lazione verrà eseguita direttamente.

## Changes for 9.0

* Added the possibility of showing the clipboard text in browse mode.
* Added an option to choose if confirmations will be required if clipboard
  is not empty, for instance, if files or folders are been copied.
* Requires NVDA 2018.4 or later.

## Cambiamenti per 8.0 ##

* Le impostazioni del componente aggiuntivo verranno visualizzate sulla
  corrispondente categoria della finestra  impostazioni di NVDA.
* Richiede NVDA 2018.2 o successive.
* E' possibile scaricare [l'ultima versione compatibile con NVDA 2017.3][3].

## Cambiamenti per 7.0

* Se durante l'installazione si sceglie di non usare  la simulazione copia e
  la simulazione taglia, questi comandi verranno rimossi, in questo modo si
  possono  utilizare control+C e control+x normalmente.

## Cambiamenti per 6.0

*	 Aggiunte opzioni per stabilire se le azioni disponibili debbano essere eseguite dopo un messaggio di conferma.
*	 Aggiunti i comandi di simulazione copia e simulazione taglia, che possono essere assegnati dalla finestra di dialogo tasti e gesti di immissione.
*	 Aggiunta una finestra di dialogo che permette di configurare il comportamento della simulazione copia e simulazione taglia durante l'installazione. Ciò consente di controllare i comandi ctrl+c e ctrl+v per copia e taglia, in modo che venga richiesto all'utente se desidera sovrascrivere il contenuto attuale degli appunti prima di effettuare una copia del contenuto selezionato.
*	Risolto un bug nella documentazione per lo script_add (Windows+NVDA+c).

## Cambiamenti per 5.0 ##

*	Migliorata la presentazione visiva della finestra di dialogo,
  conformandosi all'aspetto standard di NVDA.
*	Richiede NVDA 2016.4 o successive.

## Cambiamenti per 4.0 ##
*	Le impostazioni del componente aggiuntivo sono gestite dalla
  configurazione di NVDA, cosicché ci si possa servire dei profili standard
  per salvare separatori differenti; non ci sarà bisogno quindi di copiare
  le impostazioni ed importarle in caso di reinstallazione.-
*	Ora è possibile stabilire se il testo aggiunto debba essere accodato o
  preposto, attraverso la casella di controllo aggiungi testo prima degli
  appunti, dalla finestra di dialogo impostazioni ClipContents Designer.

## Cambiamenti per 3.0 ##
*	Una rappresentazione Braille di oggetti MathMl può essere accodata agli
  appunti se MathPlayer è installato
*	Se non è stato impostato alcun separatore, verrà inserita soltanto una
  riga vuota tra i segmenti di testo accodato.
*	Può essere assegnato un tasto caldo per aprire la finestra impostazioni di
  Clip Contents Designer 
*	Aggiunta una casella di controllo nella finestra di dialogo, per
  selezionare se il separatore debba essere copiato per poi essere importato
  in caso di nuova installazione del componente aggiuntivo.

## Cambiamenti per 2.0 ##
*	Possono essere usati caratteri Hindi come separatori per il testo aggiunto
  .

## Cambiamenti per 1.0 ##
*	Versione iniziale



[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ccd

[2]: https://addons.nvda-project.org/files/get.php?file=ccd-dev

[3]: https://addons.nvda-project.org/files/get.php?file=ccd-o
