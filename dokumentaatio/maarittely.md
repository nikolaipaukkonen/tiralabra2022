# Määrittelydokumentti

## Taustatiedot
* Sovellus on osa kevään 2022 Tiralabra-kurssia
* Sovellus kirjoitetaan Python 3.8:lla. Dokumentaatio ja koodi tehdään suomeksi.
* Pystyn arvioimaan myös Javalla ja C++:lla kirjoitettuja projekteja.
* Suoritus on osa tietojenkäsittelytieteen kandidaatin opintoja.

## Sovelluksen tarkoitus
Kurssia varten toteutan RSA-salaamiseen kykenevän ohjelman, joka luo riittävän pitkiä (1024 bittiä) avaimia ja kykenee käyttämään niitä viestien salaamiseen ja purkamiseen. Tarkoituksena on ensisijaisesti perehtyä RSA-salausmenetelmään ja sen vaatimiin algoritmeihin, joten esimerkiksi avainten hallintaa ei toteuteta tietoturvan näkökulmasta.

## Algoritmit ja tietorakenteet
Työssä toteutetaan RSA-avaimia generoiva algoritmi siihen liittyvine lauseineen (Eukleideen algoritmi, Fermat'n pieni lause, jakoyhtälö). 

## Syötteet ja käyttöliittymä
Ohjelmalle toteutetaan suomenkielinen komentorivikäyttöliittymä. Ohjelma ottaa syötteeksi tarvittavat alkuluvut ym. käyttäjältä ja varmistaa niiden oikeellisuuden ja pituusvaatimuksen täyttymisen. 

## Tavoitteena olevat aika- ja tilavaativuudet
Toteutuksen tavoitteena on saada salaukselle ja purkamiselle tehokkuus O(1) ja O(k), avaimen koosta riippuen. Avainten luominen on oletettavasti hitaampi operaatio. 

## Lähteet

Cormen, T.; Leiserson, C.; Rivest, R. & Stein, C. Introduction to Algorithms (Third edition). The MIT Press, Cambridge, Massachusetts (2009), 958 - 984.

DI Management Services. RSA Algorithm. https://www.di-mgt.com.au/rsa_alg.html [käyty 13.3.2022]

Larja, P. RSA-salaus ja sen lukuteoreettinen pohja. Pro gradu -tutkielma, Tampereen yliopisto (2011). 

Palola, J. RSA-salausalgoritmi ja alkuluvut. Pro gradu -tutkielma, Tampereen yliopisto (2008). 

Wikipedia. RSA (cryptosystem). https://en.wikipedia.org/wiki/RSA_(cryptosystem) [käyty 18.3.2022]


