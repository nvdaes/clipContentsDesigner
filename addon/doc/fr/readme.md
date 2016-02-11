# Clip Contents Designer #
*   Auteurs : Noelia Ruiz Martínez.
*   Télécharger [version stable][1]
*   Télécharger [version de développement][2]

Ce module complémentaire est utilisé pour ajouter du texte dans le
presse-papiers, ce qui peut être utile lorsque vous souhaitez joindre des
portions de texte ensemble prêt pour le collage. Le contenu du
presse-papiers peut aussi être effacé.

## Commandes clavier ##
*   NVDA+windows+c : Ajoute le texte sélectionné, les caractères braille
    Unicode qui représentent les objets MathML ou la chaîne qui a été
    marquée avec le curseur de revue, dans le presse-papiers.
*   NVDA+windows+x : Efface le contenu du presse-papiers.
*   NVDA+windows+f9 : Marque la position actuelle du curseur de revue comme
    le début du texte à ajouter au presse-papiers. Si vous utilisez nvda+F9,
    le texte ne sera pas ajouté.

Note : Les commandes ci-dessus peuvent être changés depuis le menu NVDA,
sous-menu Préférences, dans la boîte de dialogue Gestes de commandes, dans
la catégorie Revue de texte.

## Menu Préférences ##
*   Paramètres Clip Contents Designer : Permet de définir un séparateur qui
    peut être utilisé pour trouver les segments de texte une fois que tout
    le texte ajouté est collé. Vous pouvez également choisir si le
    séparateur doit être copié dans votre dossier de configuration personnel
    de NVDA, afin qu'il puisse être importé lors de la réinstallation du
    module complémentaire.

Note : Les commandes ci-dessus peuvent être changés depuis le menu NVDA,
sous-menu Préférences, dans la boîte de dialogue Gestes de commandes, dans
la catégorie Configuration.

## Changements pour la version 3.0 ##
*   La représentation en braille des objets MathML peut être ajoutée dans le
    presse-papiers si MathPlayer est installé.
*   Si aucun séparateur n'est définie, juste une seule ligne sera placée
    entre les segments du texte ajouté.
*   Un raccourci peut être assigné pour ouvrir le dialogue paramètres Clip
    Contents Designer.
*   Ajouté une case à cocher dans la boîte de dialogue paramètres, afin de
    choisir si le séparateur doit être copié pour être importé lors de la
    réinstallation du module complémentaire.

## Changements pour la version 2.0 ##
*   Les caractères Hindous peuvent être utilisés comme séparateur entre les
    contenus concaténés.

## Changements pour la version 1.0 ##
*   Première version.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev
