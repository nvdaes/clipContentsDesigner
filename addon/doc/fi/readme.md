# Leikepöydän sisällön käsittelijä #

*	Tekijät: Noelia, Abdel.
*	Yhteensopivuus: NVDA 2019.3 tai uudempi
*	Lataa [vakaa versio][1]
*	Lataa [kehitysversio][2]

Tätä lisäosaa käytetään tekstin lisäämiseen leikepöydälle, mistä voi olla
hyötyä, jos haluat yhdistää tekstin eri osia yhdeksi kokonaisuudeksi
liittääksesi sen jonnekin.  Leikepöydän sisällön voi myös tyhjentää ja
näyttää selaustilassa.

## Näppäinkomennot ##
*	NVDA+Windows+C: Lisää valittu/tarkastelukohdistimella merkitty teksti tai
  MathML-objekteja kuvaavat Unicode-pistekirjoitusmerkit leikepöydälle.
*	NVDA+Windows+X: Tyhjennä leikepöydän sisältö.
*	Ei määritetty: Kopioi leikepöydälle tai leikkaa siltä ja pyytää
  vaihtoehtoisesti vahvistuksen.
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

Huomautuksia:

*	Vahvistusta ei pyydetä NVDA:n ilmoitusruudun ollessa avoimena, vaan
  toiminnot suoritetaan heti.
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

## Muutokset versiossa 12.0
* Korjattu bugeja käytettäessä kopioinnin emulointia sellaisissa
  sovelluksissa kuin LibreOffice Writer.

## Muutokset versiossa 11.0
* Nyt on mahdollista lisätä tarkastelukohdistimella merkittyä tekstiä
  tavallisia NVDA-komentoja(NVDA+F9 ja NVDA+F10) käyttäen. Komentoa
  NVDA+Win+F9 ei enää käytetä paremman uuteen NVDA+Vaihto+F9-komentoon
  integroinnin takia.
* Edellyttää NVDA 2019.3:a tai uudempaa.

## Muutokset versiossa 10.0
* Korjattu ohjelmavirhe leikepöydän sisältämän tekstin näyttämiseen
  käytettävässä valintaikkunassa, kun sen nimi sisälsi ei-latinalaisia
  merkkejä.
* Korjattu ohjelmavirhe leikkaamisen ja kopioinnin emulointitoiminnoissa
  arabialaista näppäimistöasettelua käytettäessä. Tämän korjasi Abdel, joka
  on lisätty lisäosan tekijäksi.

## Muutokset versiossa 9.0

* Lisätty mahdollisuus leikepöydän tekstin näyttämiseen selaustilassa.
* Lisätty asetus, jolla voidaan valita, kysytäänkö vahvistus, jos leikepöytä
  ei ole tyhjä esim. tiedostoja tai kansioita kopioitaessa.
* Edellyttää NVDA 2018.4:ää tai uudempaa.

## Muutokset versiossa 8.0 ##

* Lisäosan asetukset näkyvät omassa kategoriassaan NVDA:n
  Asetukset-valintaikkunassa.
* Edellyttää NVDA 2018.2:ta tai uudempaa.
* Tarvittaessa voit ladata [viimeisimmän version, joka on yhteensopiva NVDA
  2017.3:n kanssa.][3]

## Muutokset versiossa 7.0

* Jos valitset Ei Määritä kopioinnin ja leikkaamisen emuloinnin
  märitysvalintaikkunassa, joka tulee näkyviin lisäosaa asennettaessa,
  näiden ominaisuuksien komennot poistetaan käytöstä, mikä palauttaa
  normaalin Ctrl+C- ja Ctrl+X-toiminnallisuuden.

## Muutokset versiossa 6.0

*	 Lisätty vaihtoehdot, joilla voidaan valita, pyydetäänkö käytettävissä olevien toimintojen suorittamiseen vahvistus.
*	Lisätty Vahvista kopioinnin emulointi- ja Vahvista leikkaamisen emulointi -asetukset, joille voidaan määrittää syötekomennot Syötekomennot-valintaikkunasta.
*	Lisätty valintaikkuna Vahvista kopioinnin emulointi- ja Vahvista leikkaamisen emulointi -toiminnallisuuksien  määrittämiseen lisäosan asennuksen aikana. Kun nämä asetukset ovat käytössä, kopioinnin (Ctrl+C) ja leikkaamisen (Ctrl+X) suorittamiselle pyydetään vahvistus.
*	Korjattu tekstinlisäämiskomennon (Windows+NVDA+C) ohje.

## Muutokset versiossa 5.0 ##

*	Valintaikkunan visuaalista esitystä on parannettu noudattamaan NVDA:n
  ikkunoiden ulkoasua.
*	Edellyttää NVDA:n 2016.4-versiota tai uudempaa.

## Muutokset versiossa 4.0 ##
*	NVDA hallitsee nyt lisäosan asetuksia, jotta profiilien käyttäminen eri
  erottimien tallentamiseen olisi mahdollista, eikä asetusten kopiointia
  tarvita niiden tuomiseksi asennettaessa lisäosaa uudelleen.
*	Lisäosan asetusvalintaikkunan Lisää teksti leikepöydän nykyisen sisällön
  alkuun -valintaruutua käyttäen on nyt mahdollista valita, liitetäänkö
  lisätty teksti leikepöydällä jo olevan tekstin loppuun vai alkuun.

## Muutokset versiossa 3.0 ##
*	MathML-objekteja kuvaavat pistekirjoitusmerkit voidaan lisätä
  leikepöydälle, mikäli MathPlayer on asennettu.
*	Mikäli erotinta ei ole määritetty, tekstiosuuksien väliin lisätään yksi
  tyhjä rivi.
*	Leikepöydän sisällön käsittelijän asetusvalintaikkunan avaamista varten
  voidaan määrittää pikanäppäin.
*	Asetusvalintaikkunaan lisätty valintaruutu, jolla voidaan määrittää,
  kopioidaanko erotin käyttäjän NVDA-asetusten kansioon, josta se voidaan
  tuoda asennettaessa lisäosaa uudelleen.

## Muutokset versiossa 2.0 ##
*	Hindinkielisiä merkkejä voidaan käyttää tekstiosuuksien välisenä
  erottimena.

## Muutokset versiossa 1.0 ##
*	Ensimmäinen versio.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ccd

[2]: https://addons.nvda-project.org/files/get.php?file=ccd-dev

[3]: https://addons.nvda-project.org/files/get.php?file=ccd-o
