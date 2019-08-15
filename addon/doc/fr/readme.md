# Clip Contents Designer #

*	Authors: Noelia, Abdel.
*	NVDA compatibility: 2018.4 to 2019.2.
*	Télécharger [version stable][1]
*	Télécharger [version de développement][2]

Cette extension permet d'ajouter du texte dans le presse-papiers, ce qui
peut être utile lorsque vous souhaitez relier des portions de texte ensemble
prêt pour le collage. Le contenu du presse-papiers peut aussi être vidé.

## Commandes clavier ##
*	NVDA+windows+c : Ajoute le texte sélectionné, les caractères braille
  Unicode qui représentent les objets MathML ou la chaîne qui a été marquée
  avec le curseur de revue, dans le presse-papiers.
*	NVDA+windows+x : Vide le contenu du presse-papiers.
*	NVDA+windows+f9 : Marque la position courante du curseur de revue comme début du texte devant être ajouté au presse-papiers. Si vous utilisez nvda+F9, le texte ne sera pas ajouté.
*	 Non assigné : Copier (ou couper) vers le presse-papiers, avec la possibilité de demander une confirmation préalable.
*	 Non assigné : Afficher le contenu du presse-papiers en mode navigation, ou annoncer si le presse-papiers est vide ou si son contenu ne peut être présenté en mode navigation, par exemple si des fichiers ou dossiers ont été copiés depuis l'explorateur de fichiers..
*	NVDA+windows+f9 : Marque la position actuelle du curseur de revue comme le début du texte à ajouter au presse-papiers. Si vous utilisez nvda+F9, le texte ne sera pas ajouté.
*	 Non affecté : Copie dans (ou coupe depuis) le presse-papiers, avec la possibilité de demander une confirmation préalable.

Note : Les commandes ci-dessus peuvent être changés depuis le menu NVDA,
sous-menu Préférences, dans la boîte de dialogue Gestes de commandes, dans
la catégorie Revue de texte.

## Menu Préférences ##
*	Paramètres Clip Contents Designer : Permet de définir un séparateur qui peut être utilisé pour trouver les segments de texte une fois que tout le texte ajouté est collé.
Vous pouvez également choisir si le texte sera ajouté à la fin ou au début, si les actions disponibles (ajouter, vider le presse-papiers, émuler copier et émuler couper) doivent être effectuées immédiatement ou après confirmation, et si des confirmations seront demandées juste si le texte est contenu dans le presse-papiers.

Notes :

*	La commande ci-dessus peut être changé depuis le menu NVDA, sous-menu
  Préférences, dans la boîte de dialogue Gestes de commandes, dans la
  catégorie Configuration.
*	Les confirmations ne seront pas demandées lorsqu'une boîte de message de
  NVDA est toujours ouverte. Dans ces cas, les actions seront effectuées
  immédiatement

## Changes for 10.0
* Fixed a bug in the dialog used to show the clipboard text, when its title
  contains non latin characters.
* Fixed a bug when using the emulate cut and copy features with an Arabic
  keyboard layout. This has been fixed by Abdel, added as an add-on author.

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
* Si nécessaire, vous pouvez télécharger la [dernière version compatible
  avec NVDA 2017.3][3].

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
