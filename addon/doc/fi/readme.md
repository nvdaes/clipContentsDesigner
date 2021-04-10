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
*	Ei määritetty: Näyttää leikepöydällä olevan tekstin HTML-muodossa
  selaustilassa tai ilmoittaa, mikäli leikepöytä on tyhjä tai jos sillä on
  sisältöä, jota ei voida näyttää, esim. Resurssienhallinnasta kopioituja
  tiedostoja tai kansioita.
*	Ei määritetty: Näyttää leikepöydällä olevan tekstin pelkkänä tekstinä
  selaustilassa tai ilmoittaa, mikäli leikepöytä on tyhjä tai jos sillä on
  sisältöä, jota ei voida näyttää, esim. Resurssienhallinnasta kopioituja
  tiedostoja tai kansioita.


## Leikepöydän sisällön käsittelijän asetukset ##

Tämä paneeli löytyy kohdasta NVDA-valikko -> Asetukset -> Asetukset.

Se sisältää seuraavat säätimet:

* Kirjoita merkkijono, jota käytetään erottimena leikepöydälle lisättyjen
  tekstiosuuksien välissä: Mahdollistaa erottimen asettamisen, jota voidaan
  käyttää tekstiosioiden etsimiseen.
* Lisää teksti leikepöydällä olevan tekstin eteen: Voit myös valita,
  liitetäänkö lisätty teksti leikepöydällä jo olevan sisällön jälkeen vai
  eteen.
* Valitse vahvistusta edellyttävät toiminnot: Voit valita kullekin
  käytettävissä olevalle toiminnolle, suoritetaanko se heti vai vahvistuksen
  jälkeen. Käytettävissä ovat seuraavat toiminnot: lisää tekstiä, tyhjennä
  leikepöytä, kopioinnin emulointi sekä leikkaamisen emulointi.
* Pyydä vahvistus ennen valittujen toimintojen suorittamista: Voit valita,
  pyydetäänkö vahvistus aina, vain, jos leikepöydällä on tekstiä tai mikäli
  leikepöytä ei ole tyhjä (esim. jos olet kopioinut tiedoston tekstin
  asemesta).
* Näytä leikepöydän teksti selaustilassa HTML-muodossa: Jos opettelet
  HTML-kieltä, voit valita esimuotoillun tekstin HTML-muodossa tai HTML:n
  sellaisena, kuin se näytetään verkkoselaimessa saadaksesi käsityksen
  siitä, miten NVDA näyttää HTML-koodisi verkkoselaimessa. Ero esimuotoillun
  ja tavallisen HTML:n välillä on, että ensimmäinen vaihtoehto säilyttää
  peräkkäiset välilyönnit ja rivinvaihdot, kun jälkimmäinen tiivistää
  ne. Esimerkki: Kirjoita joitakin HTML-tägejä, kuten h1, h2, li, pre jne.,
  valitse ja kopioi teksti leikepöydälle ja käytä Leikepöydän sisällön
  käsittelijä -lisäosaa tekstin näyttämiseen selaustilassa.
* Merkkien enimmäismäärä selaustilassa leikepöydän tekstiä näytettäessä:
  Huomaa, että tämän rajan nostaminen saattaa aiheuttaa ongelmia, mikäli
  leikepöydällä on paljon tekstiä. Oletusraja on 100 000 merkkiä.

Huomautuksia:

*	Vahvistusta ei pyydetä NVDA:n ilmoitusruudun ollessa avoimena, vaan
  toiminnot suoritetaan heti.
*	Kun kopioinnin ja leikkaamisen emulointi on otettu käyttöön, tämä lisäosa
  ottaa hallintaansa Ctrl+C- ja Ctrl+X-komennot. Tämä mahdollistaa
  valinnaisen vahvistuksen pyytämisen ennen näiden komentojen suorittamista.

## Muutokset versiossa 13.0 
* Korjattu ongelma asetuspaneelin visuaalisessa ulkoasussa; kiitos Cyrille
  Bougotille.
* Dokumentaatiota paranneltu.
* Lisätty Leikepöydän sisällön käsittelijä -kategoria, josta voidaan
  määrittää syötekomennot kaikille tämän lisäosan komennoille.
* Korjattu bugeja käytettäessä kopioinnin emulointia selaimissa selaustilan
  ollessa käytössä.
* Voit määrittää eri syötekomennot näyttämään leikepöydän tekstisisällön
  joko raakatekstinä tai muotoiltuna HTML:nä.

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
