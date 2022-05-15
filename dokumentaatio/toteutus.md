# Toteutusdokumentti
Kurssityönä kirjoittamani ohjelma toteuttaa RSA-salausavainten luomisen sekä niiden käytön purkamisessa ja salauksessa. Ohjelma on toteutettu Pythonin versiolla 3.8. Ohjelman toteuttama salaus on harjoitelma, eikä sellaisenaan sovellu todelliseen tietoturvakäyttöön.

## Ohjelman rakenne
Tällaisenaan ohjelma on jaettu kolmeen pääosaan: käyttöliittymä (ui.py), alkulukuihin ja avainten generointiin keskittyvään luokkaan (prime_tools.py) sekä muihin laskutoimituksiin keskittyvään luokkaan (math_tools.py). Rakennetta tulisi refaktoroida ymmärrettävyyden lisäämiseksi. 

## Aika- ja tilavaativuudet
En päässyt kovinkaan syvälle aika- ja tilavaatimusten tutkimiseen työni aikana. RSA Laboratoriesin mukaan salaamisen aikavaativuus on O(k^ 2) ja purkamisen O(k^3), kun k = modulus_n:n koko. Avainten generoinnin vaativuus olisi O(k^4).

## Suorituskykytestit
Suorituskykytesteistä kerrotaan tarkemmin testausdokumentissa. Yleisesti ottaen avainten luominen kestää melko pitkään -- 1024 bitin vaihtoehdolla tavallisella kannettavalla tietokoneella generoinnissa menee noin 10 sekuntia -- mutta purkaminen ja salaaminen ovat nopeita operaatioita.

## Puutteet ja jatkokehitys
Ohjelma on tällaisenaan ns. "textbook-RSA", eikä sovellu sellaisenaan turvalliseen salaamiseen. Erilaiset salaukseen liittyvät padding-menetelmät (esimerkiksi PKCS#1) kuuluvat myös käyttöön tarkoitettuihin RSA-sovelluksiin.

Yleisesti ottaen ohjelma kaipaisi enemmän refaktorointia ja laajempaa testausta. 

## Lähteet

https://en.wikipedia.org/wiki/RSA_(cryptosystem)
https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
https://en.wikipedia.org/wiki/Exponentiation_by_squaring
https://en.wikipedia.org/wiki/Euler%27s_totient_function
https://www.packetmania.net/en/2022/01/22/Python-Textbook-RSA/
https://link.springer.com/chapter/10.1007/978-981-10-3433-6_90
https://web.archive.org/web/20071112103441/http://www.rsa.com/rsalabs/node.asp?id=2215

Cormen, T.; Leiserson, C.; Rivest, R. & Stein, C. Introduction to Algorithms (Third edition). The MIT Press, Cambridge, Massachusetts (2009), 958 - 984.