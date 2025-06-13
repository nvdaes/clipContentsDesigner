# Clip Contents Designer #

*	Auteurs : Noelia, Abdel.

Cette extension permet d'ajouter du texte dans le presse-papiers, ce qui
peut être utile lorsque vous souhaitez joindre des portions de texte prêt
pour le collage. Le contenu du presse-papiers peut aussi être vidé.

## Commandes clavier ##
*	NVDA+windows+c : Ajoute le texte sélectionné, les caractères braille
  Unicode qui représentent les objets MathML ou la chaîne qui a été marquée
  avec le curseur de revue, dans le presse-papiers.
*	NVDA+windows+x: Clear clipboard contents.
*	 Not assigned: Copies to (or cuts from) the clipboard, with the possibility of being asked for a previous confirmation.
*	 Not assigned: Shows the clipboard text as HTML in browse mode, or announces if clipboard is empty or has contents which can't be presented in a browseable message, for instance if files or folders are been copied from Windows Explorer.
*	 Not assigned: Shows the textual clipboard contents as plain text in browse mode, or announces if clipboard is empty or has contents which can't be presented in a browseable message, for instance if files or folders are been copied from Windows Explorer.


## Paramètres de Clip Contents Designer ##

Ce panneau est disponible depuis le menu de NVDA, le sous-menu Préférences,
le dialogue Paramètres.

Il contient les contrôles suivants :

* Tapez la chaîne à utiliser comme séparateur entre les contenus ajoutés au
  presse-papiers : Permet de définir un séparateur qui peut être utilisé
  pour trouver les segments de texte une fois que tout le texte ajouté est
  collé.
* Ajouter du texte  au début du presse-papiers : il est également possible
  de choisir si le texte ajouté sera ajouté  à la fin ou ajouté au début.
* Sélectionnez les actions qui nécessitent une confirmation préalable : Vous
  pouvez choisir, pour chaque action disponible, si elle doit être effectuée
  immédiatement ou après confirmation. Les actions disponibles sont :
  ajouter du texte, effacer le presse-papiers, émuler la copie et émuler la
  coupe.
* Demander une confirmation avant d'effectuer les actions sélectionnées
  quand : Vous pouvez sélectionner si les confirmations seront toujours
  demandées, juste si du texte est contenu dans le presse-papiers, ou si le
  presse-papiers n'est pas vide (par exemple si vous avez copié un fichier,
  pas du texte).
* Format pour afficher le texte du presse-papiers au format HTML en mode
  navigation : si vous apprenez le langage de balisage HTML, vous pouvez
  choisir le texte préformaté en HTML ou HTML comme affiché dans un
  navigateur Web, pour avoir une idée de la façon dont votre code HTML sera
  rendu par NVDA dans un navigateur. La différence entre le HTML préformaté
  et le HTML conventionnel est que la première option conservera les espaces
  et les sauts de ligne consécutifs, et la seconde les compactera. Par
  exemple, écrivez des balises HTML telles que h1, h2, li, pre, etc.,
  sélectionnez et copiez le texte dans le presse-papiers et utilisez
  l'extension clipContentsDesigner pour afficher le texte dans un message
  consultable.
* Nombre maximal de caractères lors de l'affichage du texte du
  presse-papiers en mode navigation : veuillez noter que l'augmentation de
  cette limite peut entraîner des problèmes si le presse-papiers contient de
  grandes chaînes de texte. La limite par défaut est de 100 000 caractères.
* Restaurer les valeurs par défaut.

Notes :

*	Confirmations won't be requested when a message box of NVDA is still opened. In those cases, actions will be inmediately performed.
* Emulate copy and emulate cut commands mean that, when these features are enabled, the add-on will take control of control+c and control+x. This will allow to select if a confirmation should be requested before performing the actions corresponding to these keystrokes.

## Changes for 46.0.0
* NVDA will sanitize HTML in browseable messages.
* Added a button to close browseable messages, in addition to the Escape
  key.


## Changements pour la version 40.0.0
* Ajout de la prise en charge du clavier hébreu.

## Changements pour la version 22.0.0
* Ajout d'un bouton pour restaurer aux paramètres par défaut dans le panneau
  de paramètres de l'extension.
* L'extension ne peut pas être exécuté en mode sécurisé.

## Changements pour la version 17.0
* Compatible avec NVDA 2023.1.

## Changements pour la version 16.0
* Nécessite NVDA 2022.1 ou ultérieur.

## Changements pour la version 15.0
* La commande pour ajouter du texte au presse-papiers est à nouveau
  présentée dans la boîte de dialogue des gestes de commande.
* Correction des gestes pour copier et couper avec le clavier persan, grâce
  à Mohammadhosein Ghezelsofla.

## Changements pour la version 14.0
* Compatible avec NVDA 2021.1.

## Changes for 13.0
* Correction d'un problème dans la disposition visuelle du panneau des
  paramètres, grâce à Cyrille Bougot.
* Documentation améliorée.
* Ajout d'une catégorie Clip Contents Designer pour attribuer des gestes
  d'entrée à toutes les commandes disponibles pour cette extension.
* Correction de bugs lors de l'utilisation de la copie d'émulation dans les
  navigateurs si le mode focus est actif.
* Vous pouvez assigner différents gestes pour afficher le contenu textuel du
  presse-papiers sous forme de texte brut ou formaté en HTML. Le Format pour
  afficher le texte du presse-papiers dans le panneau des paramètres a été
  modifié en conséquence, pour sélectionner les deux options disponibles
  pour le format HTML.

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
  a été corrigé par Abdel, ajouté comme auteur de l'extension.

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

## Changements pour la version 7.0

* Dans le dialogue pour configurer les fonctionnalités Émuler copier et
  Émuler couper à l'installation, si vous choisissez non, les commandes pour
  ces fonctionnalités seront supprimées, de sorte que vous pouvez restaurer
  le comportement normal pour contrôle+c et contrôle+x.

## Changements pour la version 6.0

*	 Added options to choose if available actions should be performed after confirmation.
*	Added Emulate copy and Emulate cut commands, which could be assigned from the Input gestures dialog.
*	 Added a dialog to configure the Emulate copy and Emulate cut functionalities at installation. This allows to add the control+c and control+x commands to copy and cut, and be asked if you want to replace the clipboard contents when pressing these keystrokes.
*	Fixed documentation for script_add (Windows+NVDA+c).

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
  réinstallation de l'extension.

## Changements pour la version 2.0 ##
*	Les caractères Hindous peuvent être utilisés comme séparateur entre les
  contenus concaténés.

## Changements pour la version 1.0 ##
*	Première version.

[[!tag dev stable]]

