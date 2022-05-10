# Käyttöohje
Tämän ohjelman tarkoituksena on toteuttaa RSA-salausavainten generointi ja lyhyiden viestien salaaminen. Ohjelma tarjoaa mahdollisuuden generoida käyttäjän haluaman kokoisen avainparin sekä viestien salaamisen ja purkamisen. Lisäksi ohjelmassa on toiminnallisuus avainparien tallentamiseen ja tuomiseen erillisistä tekstitiedostoista. 

## Asentaminen
Ohjelma vaatii toimiakseen Pythonin (versio 3.8 tai uudempi) ja paketinhallintajärjestelmä Poetryn, jonka asennusohjeet ovat [täällä](https://ohjelmistotekniikka-hy.github.io/python/viikko2#poetry-ja-riippuvuuksien-hallinta).

1. Asenna ensin riippuvuudet:
```bash
ṕoetry install
```

2. Käynnistä sovelluksen komentorivikäyttöliittymä:
```bash
poetry run invoke start

## Salausavainten generointi
Ohjelma kysyy käynnistyessään luotavan avaimen koon biteissä (suositus vähintään 1024 bittiä). Käyttöliittymässä valitsemalla vaihtoehdon "1" ohjelma generoi avaimet ja tulostaa sen jälkeen sen komponentit sekä niiden luomiseen kestäneen ajan. Tämän jälkeen avainpari on käynnissä olevan ohjelman muistissa, mutta ei tallennu sellaisenaan mihinkään, mikäli ohjelman suoritus keskeytetään.

## Avainten tuonti ja vienti
Ohjelma tarjoaa toiminnallisuuden myös avainten viemiseen tekstitiedostoiksi sekä aiemmin generoitujen avainparien tuomiseen. Valitsemalla vaihtoehdon "2" käyttäjä voi tallentaa avainparin tekstitiedostona projektin kansioon. Vaihtoehto "3" mahdollistaa avaimen tuomisen, kun käyttäjä syöttää avainparitiedoston nimen.

Nämä tekstitiedostot eivät sisällä muuta tietoa kuin omille riveilleen järjestyksessä tallennetut julkisen ja yksityisen eksponentin sekä moduluksen. 

## Salaaminen ja purkaminen
Valinnalla "4" ohjelma kysyy salattavaa viestiä käyttäjältä (tai ilmoittaa, että salausavainta ei ole vielä generoitu tai tuotu). Salattu viesti tulostetaan, minkä lisäksi se pysyy ohjelman muistissa. 

Valinnalla "5" käyttäjä voi purkaa viestin joko syöttämällä salatun viestin komentoriville tai vaihtoehtoisesti syöttämällä tyhjän rivin, jolloin ohjelma hakee viimeisen salatun viestin ja purkaa sen. Purettu viesti tulostetaan.

## Ohjelman lopettaminen
Valinta "6" lopettaa ohjelman suorittamisen. Mikäli luotua avainparia ei ole viety omaksi tekstitiedostokseen, se häviää. 