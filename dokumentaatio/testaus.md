# Testausdokumentti
## Yksikkötestit
Ohjelmalle toteutetaan yksikkötestaus. Se ajetaan komennolla

```bash
poetry run invoke test
```
Tämän hetkinen testikattavuus:
![](https://github.com/nikolaipaukkonen/tiralabra2022/blob/main/dokumentaatio/2022_04_23_coverage.png)

## Suorituskykytestit

Ohjelman osille on suoritettu manuaalisia suorituskykytestejä. Operaatio on toteutettu 10 kertaa eri kokoisilla avaimilla ja niiden kestosta on laskettu keskiarvo.

Viikon 5 tilanne avainten luonnissa oli seuraava:

Avaimen pituus bitteinä | Keskiarvo 10:llä kerralla |
512     | 1.503     |
1024    | 13.970    |
2048    | 114.510   |

Kuten näkyy, avainten luonti kestää tällaisenaan aivan liian pitkään. Sovelluslogiikkaa on paranneltava monilta osin tehokkuuden lisäämiseksi. 2048 bitin pituisen avaimen generointiin menee helposti toista minuuttia, mikä ei nykystandardeilla riitä lainkaan.