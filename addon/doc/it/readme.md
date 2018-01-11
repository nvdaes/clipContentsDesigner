# Clip Contents Designer #

*	Autori: Noelia Ruiz Martínez.
*	Download [stable version][1]
*	Download [development version][2]

Questo componente aggiuntivo viene utilizzato per aggiungere il testo agli
appunti, il che può essere utile quando si desidera unire sezioni di testo
insieme per poi incollarlo. Il contenuto degli appunti può essere
cancellato.

## Comandi rapidi ##
*	NVDA + Windows + C: Aggiunge e copia negli appunti il testo selezionato, o
  i caratteri braille unicode che rappresentano oggetti MathMl, o la stringa
  che è stata contrassegnata con il cursore di controllo.
*	NVDA + Windows + x: Cancella contenuto degli appunti.
*	NVDA+windows+f9: Mark the current position of the review cursor as the start of the text to be added to the clipboard. If you use nvda+F9, the text will not be added.
*	 Not assigned: Copies to (or cuts from) the clipboard, with the possibility of being asked for a previous confirmation.

Nota: I comandi di cui sopra possono essere modificati dal menu di NVDA,
sottomenu Preferenze, gesti di immissione, categoria revisione del testo.

## Menu preferenze ##
*	Clip Contents Designer settings: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
It's also possible to choose if the added text will be appended or prepended, if available actions (add, clear clipboard, emulate copy and emulate cut) should be performed inmediately or after confirmation, and if confirmations will be requested just if text is contained in the clipboard.

Note:

*	Il comando di cui sopra può essere modificato dal menu di NVDA, sottomenu
  Preferenze, gesti di immissione, categoria Configurazione
*	Confirmations won't be requested when a message box of NVDA is still
  opened. In those cases, actions will be inmediately performed

## Cambiamenti per 6.0

*	 Added options to choose if available actions should be performed after confirmation.
*	Added Emulate copy and Emulate cut commands, which could be assigned from the Input gestures dialog.
*	 Added a dialog to configure the Emulate copy and Emulate cut functionalities at installation. This allows to add the control+c and control+x commands to copy and cut, and be asked if you want to replace the clipboard contents when pressing these keystrokes.
*	Fixed documentation for script_add (Windows+NVDA+c).

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

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev
