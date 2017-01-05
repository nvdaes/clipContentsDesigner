# Leikepöydän sisällön käsittelijä #

*	Tekijä: Noelia Ruiz Martínez
*	Lataa [vakaa versio][1]
*	Lataa [kehitysversio][2]

Tätä lisäosaa käytetään tekstin lisäämiseen leikepöydälle, mistä voi olla
hyötyä, jos haluat yhdistää tekstin eri osia yhdeksi kokonaisuudeksi
liittääksesi sen jonnekin.  Leikepöydän sisällön voi myös tyhjentää.

## Näppäinkomennot ##
*	NVDA+Windows+C: Lisää valittu/tarkastelukohdistimella merkitty teksti tai
  MathML-objekteja kuvaavat Unicode-pistekirjoitusmerkit leikepöydälle.
*	NVDA+Windows+X: Tyhjennä leikepöydän sisältö.
*	NVDA+windows+f9: Mark the current position of the review cursor as the start of the text to be added to the clipboard.
    If you use nvda+F9, the text will not be added.

Huomaa, että edellä mainittuja komentoja on mahdollista muuttaa kohdasta
NVDA-valikko -> Asetukset -> Syöte-eleet ja valitsemalla Tekstin tarkastelu
-kategoria.

## Asetukset-valikko ##
*	Clip Contents Designer settings: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
It's also possible to choose if the added text will be appended or prepended.

Huomaa, että edellä mainittua komentoa on mahdollista muuttaa kohdasta
NVDA-valikko -> Asetukset -> Syöte-eleet ja valitsemalla
Asetukset-kategoria.

## Changes for 5.0 ##

*	The visual presentation of the dialog has been enhanced, adhering to the
  appearance of the dialogs shown in NVDA.
*	Requires NVDA 2016.4 or later.

## Muutokset versiossa 4.0 ##
*	NVDA hallitsee nyt lisäosan asetuksia, jotta profiilien käyttäminen eri
  erottimien tallentamiseen olisi mahdollista, eikä asetusten kopiointia
  tarvita niiden tuomiseksi asennettaessa lisäosaa uudelleen.
*	Nyt on mahdollista valita, liitetäänkö lisätty teksti leikepöydällä jo
  olevan tekstin loppuun vai ennen sitä Leikepöydän sisällön käsittelijän
  asetusvalintaikkunan Lisää teksti ennen leikepöydän nykyistä sisältöä
  -valintaruutua käyttäen.

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

[1]: http://addons.nvda-project.org/files/get.php?file=ccd

[2]: http://addons.nvda-project.org/files/get.php?file=ccd-dev
