# RSA-salaus
## Aihe
Toteutan RSA-salausavainten luomisen ja käytön mahdollistavan ohjelman. Osa Tiralabra-kurssia Helsingin yliopistossa periodissa 4 2022.


## Linkit dokumentaatioon
* [Määrittelydokumentti](https://github.com/nikolaipaukkonen/tiralabra2022/blob/main/dokumentaatio/maarittely.md)
* [Käyttöohje](https://github.com/nikolaipaukkonen/tiralabra2022/blob/main/dokumentaatio/kaytto-ohje.md)
* [Testausdokumentti](https://github.com/nikolaipaukkonen/tiralabra2022/blob/main/dokumentaatio/testaus.md)
* [Toteutusdokumentti](https://github.com/nikolaipaukkonen/tiralabra2022/blob/main/dokumentaatio/toteutus.md)
* [Tuntikirjanpito](https://github.com/nikolaipaukkonen/tiralabra2022/blob/main/dokumentaatio/tuntikirjanpito.md)

## Viikkoraportit
* [Viikko 1](https://github.com/nikolaipaukkonen/tiralabra2022/blob/main/dokumentaatio/viikkoraportti_1.md)
* [Viikko 2](https://github.com/nikolaipaukkonen/tiralabra2022/blob/main/dokumentaatio/viikkoraportti_2.md)
* [Viikko 3](https://github.com/nikolaipaukkonen/tiralabra2022/blob/main/dokumentaatio/viikkoraportti_3.md)
* [Viikko 4](https://github.com/nikolaipaukkonen/tiralabra2022/blob/main/dokumentaatio/viikkoraportti_4.md)
* [Viikko 5](https://github.com/nikolaipaukkonen/tiralabra2022/blob/main/dokumentaatio/viikkoraportti_5.md)

## Asennus
1. Asenna ensin riippuvuudet:
```bash
ṕoetry install
```

2. Käynnistä sovelluksen komentorivikäyttöliittymä:
```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Pylint-tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
``` 

