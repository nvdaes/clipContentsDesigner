# Leikepöydän sisällön käsittelijä #

*	Tekijät: Noelia, Abdel.

Tätä lisäosaa käytetään tekstin lisäämiseen leikepöydälle, mistä voi olla
hyötyä, jos haluat yhdistää tekstin eri osia yhdeksi kokonaisuudeksi
liittääksesi sen jonnekin.  Leikepöydän sisällön voi myös tyhjentää ja
näyttää selaustilassa.

## Näppäinkomennot ##

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
* Palauta oletukset.

Huomautuksia:

*	Vahvistusta ei pyydetä NVDA:n ilmoitusruudun ollessa avoimena, vaan
  toiminnot suoritetaan heti.
*	Kun kopioinnin ja leikkaamisen emulointi on otettu käyttöön, tämä lisäosa
  ottaa hallintaansa Ctrl+C- ja Ctrl+X-komennot. Se mahdollistaa valinnaisen
  vahvistuksen pyytämisen ennen näiden komentojen suorittamista.

## Muutokset versiossa 46.0.0

  varten.

## Muutokset versiossa 40.0.0

* Lisäosan asetuspaneeliin lisätty painike oletusarvojen palauttamista
* Lisäosaa ei voi käyttää suojatussa tilassa.

* Voit määrittää eri näppäinkomennot näyttämään leikepöydän tekstisisällön





* Korjattu bugeja käytettäessä kopioinnin emulointia sellaisissa


## Muutokset versiossa 11.0
* Nyt on mahdollista lisätä tarkastelukohdistimella merkittyä tekstiä
  tavallisia NVDA-komentoja(NVDA+F9 ja NVDA+F10) käyttäen. Komentoa
  NVDA+Win+F9 ei enää käytetä paremman uuteen NVDA+Vaihto+F9-komentoon
  integroinnin takia.

## Muutokset versiossa 10.0

* Korjattu ohjelmavirhe leikepöydän sisältämän tekstin näyttämiseen
  käytettävässä valintaikkunassa, kun sen nimi sisälsi ei-latinalaisia
  merkkejä.
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

## Muutokset versiossa 7.0

* Jos valitset Ei Määritä kopioinnin ja leikkaamisen emuloinnin
  märitysvalintaikkunassa, joka tulee näkyviin lisäosaa asennettaessa,
  näiden ominaisuuksien komennot poistetaan käytöstä, mikä palauttaa
  normaalin Ctrl+C- ja Ctrl+X-toiminnallisuuden.

## Muutokset versiossa 6.0

*	Lisätty vaihtoehdot, joilla voidaan valita, pyydetäänkö käytettävissä
  olevien toimintojen suorittamiseen vahvistus.
*	Lisätty Vahvista kopioinnin emulointi- ja Vahvista leikkaamisen emulointi
  -asetukset, joille voidaan määrittää näppäinkomennot
  Näppäinkomennot-valintaikkunasta.
*	Lisätty valintaikkuna "Vahvista kopioinnin emulointi"- ja "Vahvista
  leikkaamisen emulointi" -toiminnallisuuksien  määrittämistä varten
  lisäosan asennuksen aikana. Kun nämä asetukset ovat käytössä, kopioinnin
  (Ctrl+C) ja leikkaamisen (Ctrl+X) suorittamiselle ja leikepöydän sisällön

  korvaamiselle pyydetään vahvistus.

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
  lisätty teksti leikepöydällä jo olevan tekstin loppuun vai alkuun.

## Muutokset versiossa 3.0 ##

  tyhjä rivi.

*	Leikepöydän sisällön käsittelijän asetusvalintaikkunan avaamista varten
*	Asetusvalintaikkunaan lisätty valintaruutu, jolla voidaan määrittää,
  kopioidaanko erotin käyttäjän NVDA-asetusten kansioon, josta se voidaan

*	Ensimmäinen versio.

[[!tag dev stable]]
