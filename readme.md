# Dolar Peru


# Dolar Perú Tracker

This tool allows you to scrape the price of the dollar from various
exchange houses in Peru. Data is collected every 45 minutes to ensure
up-to-date information.

## Installation

To install the latest stable version of the package, use the following
command:

``` sh
# Stable
pip install git+https://github.com/TJhon/dolar-peru
```

## Usage

### Last Track

To use the tool and access the most recent information, follow these
steps:

1.  Import the `PeruDolar` class from the `PDolar.api` module:

``` python
from PDolar.api import PeruDolar
```

2.  Create an instance of the tracker. You can pass a specific ID if
    needed, or `None` to use the default configuration:

``` python
tracker = PeruDolar(id = None)
```

3.  Access the information from banks:

``` python
tracker.bank.head()
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

|     | name       | type | buy_cost | buy_variation | sale_cost | sale_variation |
|-----|------------|------|----------|---------------|-----------|----------------|
| 7   | scotiabank | bank | 3.647    | 0.001         | 3.817     | 0.000          |
| 2   | bbva       | bank | 3.660    | -0.010        | 3.804     | -0.013         |
| 3   | Interbank  | bank | 3.677    | 0.011         | 3.778     | 0.000          |
| 8   | bcp        | bank | 3.690    | 0.001         | 3.775     | 0.000          |
| 5   | nacion     | bank | 3.710    | 0.000         | 3.770     | -0.010         |

</div>

4.  Check the data from exchange houses:

``` python
tracker.houses.head()
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

|     | companny_name  | img                                               | companny_url                                      | banks                             | days_open                                         | last_updated             | buy_cost | buy_variation | sale_cost | sale_variation |
|-----|----------------|---------------------------------------------------|---------------------------------------------------|-----------------------------------|---------------------------------------------------|--------------------------|----------|---------------|-----------|----------------|
| 0   | Dollar House   | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://dollarhouse.pe/?utm_source=ced            | BCP, Interbak                     | {'M_F': '9 am - 7 pm.', 'Saturdays': '10 am - ... | 2024-08-19T18:57:19.553Z | 3.734    | 0.000         | 3.743     | 0.000          |
| 1   | Rextie         | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://web.rextie.com/registrate?utm_source=c... | BCP, Interbank, Pichincha, BANBIF | {'M_F': '8 am - 8 pm', 'Saturdays': '9 am - 3 ... | 2024-06-14T18:13:16.487Z | 3.7240   | 0.000         | 3.7540    | 0.000          |
| 2   | CambiaFX       | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://cambiafx.pe/?utm_source=display&utm_me... | BCP, Interbank                    | {'M_F': '9 am - 7pm', 'Saturdays': '10 am - 1 ... | 2024-08-19T18:57:19.586Z | 3.730    | 0.000         | 3.754     | 0.000          |
| 3   | Cambio Mundial | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://www.cambiomundial.com/?utm_source=ced     | BCP - Cambio mínimo \$500         | {'M_F': '9 am - 6 pm', 'Saturdays': '9 am - 1:... | 2024-08-01T19:25:54.028Z | 3.735    | 0.005         | 3.740     | 0.000          |
| 4   | mpodera        | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://mpodera.pe/?utm_source=ced                | BCP, Interbank.                   | {'M_F': '8 am - 7 pm', 'Saturdays': '8 am- 7 p... | 2024-08-17T13:51:54.028Z | 3.734    | 0.002         | 3.74      | 0.002          |

</div>

5.  Retrieve data from SUNAT:

``` python
tracker.sunat
```

    0    3.738
    1    0.000
    2    3.748
    3    0.000
    dtype: float64

### Dates

The `PDolar` module provides functions to load and retrieve data related
to currency exchange rates from different sources, such as exchange
houses (`he`) and banks (`bank`). The functions return dictionaries
containing the required data, with default keys for exchange houses and
banks.

``` python
from PDolar.load_data.get_data import load_data, last_days_data, load_day_data

from datetime import datetime as dt, timedelta
```

#### Between dates

Load data for a range of dates between

``` python
today = dt(2024, 8, 19)
day_n = dt(2024, 8, 16)

range_data = load_data(day_n, today)
range_data['bank'].tail()
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

|     | compra | venta | img_url | companny_name | time     | name       | type     | buy_cost | buy_variation | sale_cost | sale_variation | day        |
|-----|--------|-------|---------|---------------|----------|------------|----------|----------|---------------|-----------|----------------|------------|
| 706 | NaN    | NaN   | NaN     | NaN           | 13:42:37 | nacion     | bank     | 3.710    | 0.000         | 3.770     | -0.010         | 19-08-2024 |
| 707 | NaN    | NaN   | NaN     | NaN           | 13:42:37 | Yuan       | currency | 0.450    | -0.010        | 0.540     | 0.000          | 19-08-2024 |
| 708 | NaN    | NaN   | NaN     | NaN           | 13:42:37 | canada     | currency | 2.650    | -0.040        | 2.795     | -0.005         | 19-08-2024 |
| 709 | NaN    | NaN   | NaN     | NaN           | 13:42:37 | euro ocoña | currency | 4.185    | 0.015         | 4.205     | 0.015          | 19-08-2024 |
| 710 | NaN    | NaN   | NaN     | NaN           | 13:42:37 | Libra      | currency | 4.850    | -0.010        | 4.990     | 0.000          | 19-08-2024 |

</div>

``` python
range_data['he'].tail() # house exchanges
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

|      | actualizacion | trash1 | compra | variacion_compra | venta | variacion_venta | img_url | companny_url                                      | companny_name  | time     | img                                               | banks                | days_open                                         | last_updated             | buy_cost | buy_variation | sale_cost | sale_variation | day        |
|------|---------------|--------|--------|------------------|-------|-----------------|---------|---------------------------------------------------|----------------|----------|---------------------------------------------------|----------------------|---------------------------------------------------|--------------------------|----------|---------------|-----------|----------------|------------|
| 2465 | NaN           | NaN    | NaN    | NaN              | NaN   | NaN             | NaN     | https://rissanpe.com/?utm_source=ced&utm_mediu... | Rissan         | 13:42:37 | https://s3-ced-uploads-01.s3.amazonaws.com/170... | BCP                  | {'M_F': '9 am - 6pm', 'Saturdays': '9 am - 1pm... | 2024-01-28T03:06:47.540Z | 3.725    | 0.005         | 3.743     | -0.007         | 19-08-2024 |
| 2466 | NaN           | NaN    | NaN    | NaN              | NaN   | NaN             | NaN     | https://vipcapital.com.pe/?utm_source=ced         | vip capital    | 13:42:37 | https://s3-ced-uploads-01.s3.amazonaws.com/170... | BCP, Scotiabank      | {'M_F': '9 am - 6pm', 'Saturdays': '9 am - 1pm... | 2024-03-01T14:20:50.970Z | 3.730    | 0.000         | 3.750     | 0.000          | 19-08-2024 |
| 2467 | NaN           | NaN    | NaN    | NaN              | NaN   | NaN             | NaN     | https://cambiomas.com.pe/?utm_source=ced          | Cambio Mas     | 13:42:37 | https://s3-ced-uploads-01.s3.amazonaws.com/170... | BCP, BBVA, Interbank | {'M_F': '8 am - 6 pm', 'Saturdays': '8 am - 6 ... | 2024-05-13T19:06:30.179Z | 3.730    | 0.010         | 3.753     | 0.006          | 19-08-2024 |
| 2468 | NaN           | NaN    | NaN    | NaN              | NaN   | NaN             | NaN     | https://solucionescr.pe/                          | Soluciones CR  | 13:42:37 | https://s3-ced-uploads-01.s3.amazonaws.com/171... | BCP                  | {'M_F': '8:00 am - 8:00 pm', 'Saturdays': '8:0... | 2024-06-06T22:45:57.628Z | 3.733    | 0.000         | 3.741     | 0.001          | 19-08-2024 |
| 2469 | NaN           | NaN    | NaN    | NaN              | NaN   | NaN             | NaN     | https://cambiodigitalperu.com/                    | Cambio Digital | 13:42:37 | https://s3-ced-uploads-01.s3.amazonaws.com/172... | BCP                  | {'M_F': '9am - 7pm', 'Saturdays': '9am - 2pm',... | 2024-08-02T20:01:58.289Z | 3.730    | -0.002        | 3.743     | 0.003          | 19-08-2024 |

</div>

#### Last Data

Retrieve data for the last days number of days.

``` python
data_last = last_days_data(days=2)
data_last["he"].head()
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

|     | actualizacion | trash1  | compra | variacion_compra | venta | variacion_venta | img_url                                            | companny_url                                      | companny_name      | time     | img | banks | days_open | last_updated | buy_cost | buy_variation | sale_cost | sale_variation | day        |
|-----|---------------|---------|--------|------------------|-------|-----------------|----------------------------------------------------|---------------------------------------------------|--------------------|----------|-----|-------|-----------|--------------|----------|---------------|-----------|----------------|------------|
| 0   | 14 horas      | Cambiar | 3.725  | 0.000            | 3.745 | 0.000           | https://s3-ced-uploads-01.s3.amazonaws.com/170...  | https://cambiafx.pe/?utm_source=display&utm_me... | cambiafx           | 08:19:56 | NaN | NaN   | NaN       | NaN          | NaN      | NaN           | NaN       | NaN            | 17-08-2024 |
| 1   | 1 horas       | Cambiar | 3.715  | 0.000            | 3.753 | 0.000           | https://cuantoestaeldolar.pe/\_next/image?url=h... | https://web.rextie.com/registrate?utm_source=c... | rextie             | 08:19:56 | NaN | NaN   | NaN       | NaN          | NaN      | NaN           | NaN       | NaN            | 17-08-2024 |
| 2   | 14 horas      | Cambiar | 3.720  | -0.006           | 3.750 | 0.010           | https://s3-ced-uploads-01.s3.amazonaws.com/170...  | https://www.okanecambiodigital.com/?utm_source... | okanecambiodigital | 08:19:56 | NaN | NaN   | NaN       | NaN          | NaN      | NaN           | NaN       | NaN            | 17-08-2024 |
| 3   | 14 horas      | Cambiar | 3.732  | 0.002            | 3.738 | -0.002          | https://s3-ced-uploads-01.s3.amazonaws.com/170...  | https://www.cambiomundial.com/?utm_source=ced     | cambiomundial      | 08:19:56 | NaN | NaN   | NaN       | NaN          | NaN      | NaN           | NaN       | NaN            | 17-08-2024 |
| 4   | 10 horas      | Cambiar | 3.720  | -0.002           | 3.744 | 0.000           | https://s3-ced-uploads-01.s3.amazonaws.com/170...  | https://chapacambio.com/?c=CHAPACUANTO            | chapacambio        | 08:19:56 | NaN | NaN   | NaN       | NaN          | NaN      | NaN           | NaN       | NaN            | 17-08-2024 |

</div>

``` python
data_last["bank"].head()
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

|     | compra | venta | img_url                                           | companny_name                   | time     | name | type | buy_cost | buy_variation | sale_cost | sale_variation | day        |
|-----|--------|-------|---------------------------------------------------|---------------------------------|----------|------|------|----------|---------------|-----------|----------------|------------|
| 0   | 3.658  | 3.829 | data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP//... | yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 | 08:19:56 | NaN  | NaN  | NaN      | NaN           | NaN       | NaN            | 17-08-2024 |
| 1   | 3.700  | 3.787 | data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP//... | yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 | 08:19:56 | NaN  | NaN  | NaN      | NaN           | NaN       | NaN            | 17-08-2024 |
| 2   | 3.678  | 3.789 | data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP//... | yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 | 08:19:56 | NaN  | NaN  | NaN      | NaN           | NaN       | NaN            | 17-08-2024 |
| 3   | 3.710  | 3.780 | data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP//... | yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 | 08:19:56 | NaN  | NaN  | NaN      | NaN           | NaN       | NaN            | 17-08-2024 |
| 4   | 3.670  | 3.817 | data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP//... | yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 | 08:19:56 | NaN  | NaN  | NaN      | NaN           | NaN       | NaN            | 17-08-2024 |

</div>

#### Especific Date

Get data for a specific date.

``` python
data_day = load_day_data(today - timedelta(1))
data_day["he"].head()
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

|     | companny_name  | img                                               | companny_url                                      | banks                             | days_open                                         | last_updated             | buy_cost | buy_variation | sale_cost | sale_variation | time     | day        |
|-----|----------------|---------------------------------------------------|---------------------------------------------------|-----------------------------------|---------------------------------------------------|--------------------------|----------|---------------|-----------|----------------|----------|------------|
| 0   | Dollar House   | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://dollarhouse.pe/?utm_source=ced            | BCP, Interbak                     | {'M_F': '9 am - 7 pm.', 'Saturdays': '10 am - ... | 2024-08-17T18:57:38.780Z | 3.732    | 0.000         | 3.742     | 0.000          | 15:01:32 | 18-08-2024 |
| 1   | Rextie         | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://web.rextie.com/registrate?utm_source=c... | BCP, Interbank, Pichincha, BANBIF | {'M_F': '8 am - 8 pm', 'Saturdays': '9 am - 3 ... | 2024-06-14T18:13:16.487Z | 3.719    | 0.000         | 3.755     | 0.000          | 15:01:32 | 18-08-2024 |
| 2   | CambiaFX       | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://cambiafx.pe/?utm_source=display&utm_me... | BCP, Interbank                    | {'M_F': '9 am - 7pm', 'Saturdays': '10 am - 1 ... | 2024-08-17T18:57:38.881Z | 3.725    | 0.000         | 3.745     | 0.000          | 15:01:32 | 18-08-2024 |
| 3   | Cambio Mundial | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://www.cambiomundial.com/?utm_source=ced     | BCP - Cambio mínimo \$500         | {'M_F': '9 am - 6 pm', 'Saturdays': '9 am - 1:... | 2024-08-01T19:25:54.028Z | 3.725    | 0.000         | 3.745     | 0.000          | 15:01:32 | 18-08-2024 |
| 4   | mpodera        | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://mpodera.pe/?utm_source=ced                | BCP, Interbank.                   | {'M_F': '8 am - 7 pm', 'Saturdays': '8 am- 7 p... | 2024-08-17T13:51:54.028Z | 3.732    | 0.002         | 3.749     | 0.003          | 15:01:32 | 18-08-2024 |

</div>

``` python
data_day["bank"].head()
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

|     | name       | type | buy_cost | buy_variation | sale_cost | sale_variation | time     | day        |
|-----|------------|------|----------|---------------|-----------|----------------|----------|------------|
| 0   | scotiabank | bank | 3.658    | 0.010         | 3.829     | 0.000          | 15:01:32 | 18-08-2024 |
| 1   | bbva       | bank | 3.670    | 0.004         | 3.817     | 0.002          | 15:01:32 | 18-08-2024 |
| 2   | Interbank  | bank | 3.678    | 0.005         | 3.789     | 0.001          | 15:01:32 | 18-08-2024 |
| 3   | bcp        | bank | 3.700    | 0.004         | 3.787     | 0.002          | 15:01:32 | 18-08-2024 |
| 4   | nacion     | bank | 3.710    | 0.000         | 3.780     | 0.000          | 15:01:32 | 18-08-2024 |

</div>

## Contributing

If you wish to contribute to this project, please fork the repository
and submit a pull request with your improvements.
