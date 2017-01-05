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
*	NVDA+windows+f9: Mark the current position of the review cursor as the start of the text to be added to the clipboard.
    If you use nvda+F9, the text will not be added.

Nota: I comandi di cui sopra possono essere modificati dal menu di NVDA,
sottomenu Preferenze, gesti di immissione, categoria revisione del testo.

## Menu preferenze ##
*	Clip Contents Designer settings: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
It's also possible to choose if the added text will be appended or prepended.

Nota: Il comando di cui sopra può essere modificato dal menu di NVDA,
sottomenu Preferenze, gesti di immissione, categoria Configurazione

## Changes for 5.0 ##

*	The visual presentation of the dialog has been enhanced, adhering to the
  appearance of the dialogs shown in NVDA.
*	Requires NVDA 2016.4 or later.

## Cambiamenti per 4.0 ##
*	Add-on settings are managed from NVDA configuration, so that standard
  profiles can be used to save different separators, and it's not needed to
  copy the settings for importing at reinstallation.
*	Now it's possible to choose if the added text will be appended or
  prepended, using the Add text before clip data check box from the Clip
  Contents Designer settings dialog.

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
