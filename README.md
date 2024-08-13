

# Tracking price dolar

Scrapea los precios del dolar respecto al nuevo sol (Peru), de bancos y
diferentes casas de cambio

## Instalacion

``` sh
# Stable
pip install git+https://github.com/TJhon/tesis_peru@api
```

## Usage

``` python
from PDolar.api import PeruDolar
tracker = PeruDolar()
```

``` python
tracker.bank
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead th {
        text-align: right;
    }
</style>

|     | name       | type     | buy_cost | buy_variation | sale_cost | sale_variation |
|-----|------------|----------|----------|---------------|-----------|----------------|
| 2   | bbva       | bank     | 3.655    | -0.017        | 3.826     | 0.008          |
| 7   | scotiabank | bank     | 3.655    | -0.003        | 3.830     | -0.001         |
| 3   | Interbank  | bank     | 3.680    | -0.020        | 3.795     | -0.024         |
| 5   | nacion     | bank     | 3.690    | 0.000         | 3.760     | 0.000          |
| 8   | bcp        | bank     | 3.700    | 0.007         | 3.786     | 0.085          |
| 6   | Yuan       | currency | 0.450    | -0.010        | 0.540     | 0.000          |
| 1   | canada     | currency | 2.690    | 0.050         | 2.800     | 0.000          |
| 4   | euro ocoña | currency | 4.145    | 0.005         | 4.165     | 0.005          |
| 0   | Libra      | currency | 4.880    | -0.040        | 5.010     | 0.020          |

</div>

``` python
tracker.houses
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead th {
        text-align: right;
    }
</style>

|  | companny_name | img | companny_url | banks | days_open | last_updated | buy_cost | buy_variation | sale_cost | sale_variation |
|----|----|----|----|----|----|----|----|----|----|----|
| 0 | Dollar House | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://dollarhouse.pe/?utm_source=ced | BCP, Interbak | {'M_F': '9 am - 7 pm.', 'Saturdays': '10 am - ... | 2024-08-12T22:57:19.505Z | 3.740 | 0.000 | 3.748 | 0.000 |
| 1 | Rextie | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://web.rextie.com/registrate?utm_source=c... | BCP, Interbank, Pichincha, BANBIF | {'M_F': '8 am - 8 pm', 'Saturdays': '9 am - 3 ... | 2024-06-14T18:13:16.487Z | 3.7285 | 0.000 | 3.7615 | 0.000 |
| 2 | CambiaFX | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://cambiafx.pe/?utm_source=display&utm_me... | BCP, Interbank | {'M_F': '9 am - 7pm', 'Saturdays': '10 am - 1 ... | 2024-08-12T22:57:19.649Z | 3.731 | 0.000 | 3.755 | 0.000 |
| 3 | Cambio Mundial | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://www.cambiomundial.com/?utm_source=ced | BCP - Cambio mínimo \$500 | {'M_F': '9 am - 6 pm', 'Saturdays': '9 am - 1:... | 2024-08-01T19:25:54.028Z | 3.740 | -0.004 | 3.754 | 0.006 |
| 4 | mpodera | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://mpodera.pe/?utm_source=ced | BCP, Interbank. | {'M_F': '8 am - 7 pm', 'Saturdays': '8 am- 7 p... | 2024-07-26T00:57:20.359Z | 3.736 | -0.004 | 3.753 | 0.003 |
| 5 | Okane | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://www.okanecambiodigital.com/?utm_source... | BCP | {'M_F': '9 am - 6pm', 'Saturdays': '9 am - 2 p... | 2024-03-12T17:40:02.715Z | 3.72 | -0.018 | 3.77 | 0.018 |
| 6 | Dichikash | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://dichikash.com/?utm_source=ced | BCP, Interbank, BBVA | {'M_F': '9 am - 7 pm', 'Saturdays': '9 am - 7 ... | 2024-08-10T13:55:08.036Z | 3.740 | 0.001 | 3.755 | 0.000 |
| 7 | chapacambio | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://chapacambio.com/?c=CHAPACUANTO | BCP, BanBif, Interbank, BBVA, Scotiabank | {'M_F': '8:30 am - 6 pm', 'Saturdays': '8:30 a... | 2024-07-03T22:22:16.597Z | 3.73000 | -0.002 | 3.75800 | 0.002 |
| 8 | Western Union | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://westernunionperu.pe/cambiodemoneda?utm... | BCP, BANBIF, Pichincha, Scotiabank | {'M_F': '9 am - 5:00 pm', 'Saturdays': '', 'Su... | 2024-08-12T22:57:19.915Z | 3.730 | 0.000 | 3.752 | 0.000 |
| 9 | Dolarex | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://dolarex.pe/?utm_source=ced | BCP, BBVA, Interbank | {'M_F': '8 am - 6 pm', 'Saturdays': '8 am - 2 ... | 2024-01-28T02:07:40.417Z | 3.739 | 0.000 | 3.75 | -0.001 |
| 10 | sr Cambio | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://srcambio.pe/?utm_source=ced&utm_medium... | BCP | {'M_F': '9 am - 6pm', 'Saturdays': '9 am - 1pm... | 2024-05-13T19:03:22.616Z | 3.735 | 0.000 | 3.75 | 0.004 |
| 11 | Money House | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://www.moneyhouse.pe/?utm_source=ced | BCP e INTERBAK | {'M_F': '8:30 am - 6 pm ', 'Saturdays': '9 am ... | 2024-08-12T23:36:42.657Z | 3.741 | 0.000 | 3.747 | 0.001 |
| 12 | cambiosol | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://cambiosol.pe/?utm_source=ced | BCP | {'M_F': '9 am - 6 pm', 'Saturdays': '9 am a 1 ... | 2024-08-12T22:57:21.889Z | 3.735 | 0.000 | 3.760 | 0.000 |
| 13 | DLS Money | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://dlsmoney.com/?utm_source=ced&utm\r\n_m... | BCP, Interbank | {'M_F': '9 am - 7 pm', 'Saturdays': '9 AM - 1p... | 2023-12-29T22:23:55.146Z | 3.735 | 0.000 | 3.755 | 0.000 |
| 14 | Yanki | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://yanki.pe?utm_source=CED&utm_medium=pai... | BCP | {'M_F': '9 am - 7 pm', 'Saturdays': '9 am - 2 ... | 2024-05-13T19:04:16.498Z | 3.7330 | 0.000 | 3.7600 | 0.000 |
| 15 | Instakash | https://s3-ced-uploads-01.s3.amazonaws.com/172... | https://instakash.net/?utm_source=ced | BCP, Interbank | {'M_F': '9 am - 7 pm', 'Saturdays': '9 am - 2 ... | 2024-07-09T14:49:39.521Z | 3.7330 | 0.000 | 3.7610 | -0.003 |
| 16 | Perú dolar | https://s3-ced-uploads-01.s3.amazonaws.com/171... | https://perudolar.pe/?utm_source=ced&utm_mediu... | BCP | {'M_F': '9 am - 4 pm', 'Saturdays': '-', 'Sund... | 2024-08-12T21:35:15.870Z | 3.73 | 0.000 | 3.76 | 0.000 |
| 17 | Tu Cambista | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://tucambista.pe/ced?utm_source=ced&utm_m... | BCP, Interbank, Banbif | {'M_F': '8 am - 8 pm', 'Saturdays': '9 am - 3 ... | 2024-05-13T19:04:47.318Z | 3.7345 | 0.000 | 3.7535 | 0.002 |
| 18 | inka money | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://inkamoney.com/?utm_source=ced&utm_medi... | BCP, Interbank | {'M_F': '9 am - 6:30 pm', 'Saturdays': '9 am -... | 2024-06-03T15:18:49.370Z | 3.74 | 0.000 | 3.756 | 0.004 |
| 19 | Hir Power | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://hirpower.com/?utm_source=ced&utm_mediu... | BCP | {'M_F': '8 am - 8 pm', 'Saturdays': '8 am - 2 ... | 2024-07-17T06:35:13.910Z | 3.73 | -0.005 | 3.75 | 0.000 |
| 20 | Roblex | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://roblex.pe/?utm_source=ced&utm_medium=l... | BCP | {'M_F': '9 am - 6:30 pm', 'Saturdays': '9 am -... | 2024-06-11T17:13:07.197Z | 3.7350 | -0.001 | 3.7520 | -0.001 |
| 21 | Rissan | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://rissanpe.com/?utm_source=ced&utm_mediu... | BCP | {'M_F': '9 am - 6pm', 'Saturdays': '9 am - 1pm... | 2024-01-28T03:06:47.540Z | 3.73 | 0.000 | 3.76 | 0.000 |
| 22 | vip capital | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://vipcapital.com.pe/?utm_source=ced | BCP, Scotiabank | {'M_F': '9 am - 6pm', 'Saturdays': '9 am - 1pm... | 2024-03-01T14:20:50.970Z | 3.735 | 0.000 | 3.755 | 0.000 |
| 23 | Cambio Mas | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://cambiomas.com.pe/?utm_source=ced | BCP, BBVA, Interbank | {'M_F': '8 am - 6 pm', 'Saturdays': '8 am - 6 ... | 2024-05-13T19:06:30.179Z | 0 | -3.730 | 0 | -3.755 |
| 24 | Soluciones CR | https://s3-ced-uploads-01.s3.amazonaws.com/171... | https://solucionescr.pe/ | BCP | {'M_F': '8:00 am - 8:00 pm', 'Saturdays': '8:0... | 2024-06-06T22:45:57.628Z | 3.735 | -0.005 | 3.755 | 0.005 |
| 25 | Cambio Digital | https://s3-ced-uploads-01.s3.amazonaws.com/172... | https://cambiodigitalperu.com/ | BCP | {'M_F': '9am - 7pm', 'Saturdays': '9am - 2pm',... | 2024-08-02T20:01:58.289Z | 3.735 | -0.003 | 3.755 | 0.000 |

</div>

``` python
tracker.sunat
```

    0    3.725
    1    0.000
    2    3.731
    3    0.000
    dtype: float64
