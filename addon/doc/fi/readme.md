# Leikepöydän sisällön käsittelijä #

*	Tekijät: Noelia, Abdel.
*	Yhteensopivuus: NVDA 2018.4-2019.2.
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
*	NVDA+Windows+F9: Merkitse tarkastelukohdistimen nykyinen sijainti leikepöydälle kopioitavan tekstin alkukohdaksi. Tekstiä ei lisätä, jos käytät näppäinkomentoa NVDA+F9.
*	Ei määritetty: Kopioi tai leikkaa leikepöydälle sekä pyytää vaihtoehtoisesti vahvistuksen toiminnon suorittamiselle.
*	Ei määritetty: Näyttää leikepöydällä olevan tekstin selaustilassa tai ilmoittaa, mikäli leikepöytä on tyhjä tai jos siinä on sisältöä, jota ei voida näyttää selaustilassa, esim. Resurssienhallinnasta kopioituja tiedostoja tai kansioita.

Huomaa, että edellä mainittuja komentoja on mahdollista muuttaa kohdasta
NVDA-valikko -> Asetukset -> Syötekomennot ja valitsemalla avautuvasta
valintaikkunasta Tekstin tarkastelu -kategoria.

## Asetukset-valikko ##
*	Leikepöydän sisällön käsittelijä: Mahdollistaa erottimen määrittämisen, jota voidaan käyttää tekstilohkojen etsimiseen, kun lisätty tekstikokonaisuus on ensin liitetty jonnekin.
On myös mahdollista valita, liitetäänkö lisätty teksti jo leikepöydällä olevan tekstin loppuun vai alkuun, suoritetaanko käytettävissä olevat toiminnot (lisää, tyhjennä leikepöytä, kopioinnin ja leikkaamisen emulointi) heti vai pyydetäänkö ensin vahvistus, ja pyydetäänkö aiemman sisällön korvaamiseen vahvistus, jos leikepöydällä on vain tekstiä tai jos se ei ole tyhjä.
Lisäksi on mahdollista muuttaa leikepöydällä olevan tekstin muotoa ja selaustilassa näytettävien merkkien enimmäismäärää. Huomaa, että tämän rajan nostaminen saattaa aiheuttaa ongelmia, jos leikepöydällä on paljon tekstiä. Oletusraja on 100 000 merkkiä.

Huomautuksia:

*	Edellä mainittua komentoa on mahdollista muuttaa kohdasta NVDA-valikko ->
  Asetukset -> Syötekomennot ja valitsemalla avautuvasta valintaikkunasta
  Asetukset-kategoria.
*	Vahvistusta ei pyydetä NVDA:n ilmoitusruudun ollessa avoimena, vaan
  toiminnot suoritetaan heti.

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
