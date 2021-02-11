# Clip Contents Designer #

*	Auteurs : Noelia, Abdel
*	Compatibilité NVDA : 2019.3 ou ultérieure
*	Télécharger [version stable][1]
*	Télécharger [version de développement][2]

Cette extension permet d'ajouter du texte dans le presse-papiers, ce qui
peut être utile lorsque vous souhaitez joindre des portions de texte prêt
pour le collage. Le contenu du presse-papiers peut aussi être vidé.

## Commandes clavier ##
*	NVDA+windows+c : Ajoute le texte sélectionné, les caractères braille
  Unicode qui représentent les objets MathML ou la chaîne qui a été marquée
  avec le curseur de revue, dans le presse-papiers.
*	NVDA+windows+x : Vide le contenu du presse-papiers.
*	Non assigné : Copier vers (ou couper depuis) le presse-papiers, avec la
  possibilité d'une demande de confirmation préalable.
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

Notes :

*	Les confirmations ne seront pas demandées lorsqu'une boîte de message de
  NVDA est toujours ouverte. Dans ce cas, les actions seront effectuées
  immédiatement.
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

## Changements pour la version 12.0
* Correction de bogues lors de l'utilisation de l'émulation de copie dans
  les applications telles que LibreOffice Writer.

## Changements pour la version 11.0
* Il est maintenant possible d'ajouter du texte marqué avec le curseur de
  revue à l'aide de commandes standards de NVDA (NVDA+f9 et
  NVDA+f10). NVDA+Windows+f9 n'est plus utilisé pour une meilleure
  intégration avec na nouvelle commande de NVDA NVDA+maj+f9.
* Nécessite NVDA 2019.3 ou ultérieur.

## Changements pour la version 10.0
* Correction d'un bogue dans le dialogue présentant le texte du
  presse-papiers, quand son titre contient des caractères non latins.
* Correction d'un bogue lors de l'utilisation des fonctionnalités
  d'émulation de copier ou couper avec une configuration clavier Arabe. Ceci
  a été corrigé par Abdel, ajouté comme auteur de l'extention.

## Changements pour la version 9.0

* Ajout de la possibilité de voir le contenu du presse-papiers en mode
  navigation.
* Ajout d'une option pour définir si une confirmation sera requise quand le
  presse-papiers n'est pas vide, par exemple si des fichiers ou dossiers
  sont en cours de copie.
* Nécessite NVDA 2018.4 ou ultérieur.

## Changements pour la version 8.0 ##

* Les paramètres de l'extension sont affichés dans la catégorie
  correspondante au dialogue Paramètres NVDA.
* Nécessite NVDA 2018.2 ou ultérieur.
* Si besoin, vous pouvez télécharger la [dernière version compatible avec
  NVDA 2017.3][3].

## Changements pour la version 7.0

* Dans le dialogue pour configurer les fonctionnalités Émuler copier et
  Émuler couper à l'installation, si vous choisissez non, les commandes pour
  ces fonctionnalités seront supprimées, de sorte que vous pouvez restaurer
  le comportement normal pour contrôle+c et contrôle+x.

## Changements pour la version 6.0

*	 Ajout d'options pour choisir si les actions disponibles doivent être effectuées après confirmation.
*	Ajout des commandes Émuler copier et Émuler couper, qui peuvent être affectées  à partir de la boîte de dialogue Gestes de commandes.
*	 Ajout d'une boîte de dialogue pour configurer les fonctionnalités Émuler copier et Émuler couper lors de l'installation. Cela permet d'ajouter les commandes Contrôle+c et Contrôle+x pour copier et couper et de demander si vous voulez remplacer le contenu du presse-papiers en appuyant sur ces combinaisons de touches.
*	Correction de la documentation pour le script_add (Windows+NVDA+c).

## Changements pour la version 5.0 ##

*	La présentation visuelle de la boîte de dialogue a été améliorée, en
  respectant l'apparence des dialogues présentés dans NVDA.
*	Nécessite NVDA 2016.4 ou ultérieur.

## Changements pour la version 4.0 ##
*	Les paramètres de l'extension sont gérés à partir de la configuration
  NVDA, afin que les profils standard puisse être utilisés pour enregistrer
  des séparateurs différents, et les paramètres n'ont pas besoin d'être
  copiés lors de l'importation pendant la réinstallation.
*	Il est maintenant possible de choisir si l’ajout de texte sera ajouté à la
  fin ou ajouté au début, en utilisant la case à cocher Ajouter du texte
  avant l'insertion des données à partir de la boîte de dialogue Paramètres
  de Clip Contents Designer.

## Changements pour la version 3.0 ##
*	La représentation en braille des objets MathML peut être ajoutée dans le
  presse-papiers si MathPlayer est installé.
*	Si aucun séparateur n'est définie, juste une seule ligne sera placée entre
  les segments du texte ajouté.
*	Un raccourci peut être assigné pour ouvrir le dialogue paramètres Clip
  Contents Designer.
*	Ajouté une case à cocher dans la boîte de dialogue paramètres, afin de
  choisir si le séparateur doit être copié pour être importé lors de la
  réinstallation du module complémentaire.

## Changements pour la version 2.0 ##
*	Les caractères Hindous peuvent être utilisés comme séparateur entre les
  contenus concaténés.

## Changements pour la version 1.0 ##
*	Première version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ccd

[2]: https://addons.nvda-project.org/files/get.php?file=ccd-dev

[3]: https://addons.nvda-project.org/files/get.php?file=ccd-o
