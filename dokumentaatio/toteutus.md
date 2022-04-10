# Toteutusdokumentti
Kurssityönä kirjoittamani ohjelma toteuttaa RSA-salausavainten luomisen sekä niiden käytön purkamisessa ja salauksessa. Ohjelma on toteutettu Pythonin versiolla 3.8. 

## Ohjelman rakenne
Tällaisenaan ohjelma on jaettu kolmeen pääosaan: käyttöliittymä (ui.py), alkulukuihin ja avainten generointiin keskittyvään luokkaan (prime_tools.py) sekä muihin laskutoimituksiin keskittyvään luokkaan (math_tools.py). Rakennetta tullaan refaktoroimaan rajusti ymmärrettävyyden lisäämiseksi. 

## Aika- ja tilavaativuudet

## Suorituskykytestit

## Puutteet ja jatkokehitys
Ohjelma on tällaisenaan ns. "textbook-RSA", eikä sovellu sellaisenaan turvalliseen salaamiseen. Erilaiset salaukseen liittyvät padding-menetelmät (esimerkiksi PKCS#1) kuuluvat myös käyttöön tarkoitettuihin RSA-sovelluksiin.

## Lähteet

https://en.wikipedia.org/wiki/RSA_(cryptosystem)
https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
https://en.wikipedia.org/wiki/Exponentiation_by_squaring
https://en.wikipedia.org/wiki/Euler%27s_totient_function
https://www.packetmania.net/en/2022/01/22/Python-Textbook-RSA/
https://link.springer.com/chapter/10.1007/978-981-10-3433-6_90

Cormen, T.; Leiserson, C.; Rivest, R. & Stein, C. Introduction to Algorithms (Third edition). The MIT Press, Cambridge, Massachusetts (2009), 958 - 984.