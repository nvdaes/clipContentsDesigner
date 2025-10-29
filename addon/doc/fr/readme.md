# Clip Contents Designer #

*	Auteurs : Noelia, Abdel.

Cette extension permet d'ajouter du texte dans le presse-papiers, ce qui
peut être utile lorsque vous souhaitez joindre des portions de texte prêt
pour le collage. Le contenu du presse-papiers peut aussi être vidé.

## Commandes clavier ##

  avec le curseur de revue, dans le presse-papiers.

  texte brut en mode navigation, ou annonce si le presse-papiers est vide ou

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

*	Les confirmations ne seront pas demandées lorsqu'une boîte de message de
  NVDA est toujours ouverte. Dans ce cas, les actions seront effectuées
  immédiatement.
*	Emuler les commandes copier et couper signifie que, lorsque ces
  fonctionnalités sont activées, l'extension prendra le contrôle de
  contrôle+c et contrôle+x. Cela permettra de sélectionner si une
  confirmation doit être demandée avant d'effectuer les actions
  correspondant à ces frappes.

## Changements pour la version 46.0.0

  touche Échap.

## Changements pour la version 40.0.0

  présentée dans la boîte de dialogue des gestes de commande.

* Correction des gestes pour copier et couper avec le clavier persan, grâce
  à Mohammadhosein Ghezelsofla.

* Nécessite NVDA 2018.2 ou ultérieur.

## Changements pour la version 7.0

*	Ajout d'options pour choisir si les actions disponibles doivent être
  effectuées après confirmation.
  combinaisons de touches.

*	Correction de la documentation pour le script_add (Windows+NVDA+c).

## Changements pour la version 4.0 ##

  fin ou ajouté au début, en utilisant la case à cocher Ajouter du texte
  de Clip Contents Designer.

## Changements pour la version 3.0 ##

*	La représentation en braille des objets MathML peut être ajoutée dans le
  presse-papiers si MathPlayer est installé.

  les segments du texte ajouté.

*	Un raccourci peut être assigné pour ouvrir le dialogue paramètres Clip
*	Ajouté une case à cocher dans la boîte de dialogue paramètres, afin de
  choisir si le séparateur doit être copié pour être importé lors de la
  contenus concaténés.

## Changements pour la version 1.0 ##

*	Première version.
