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
tracker.bank.tail()
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
| 5   | nacion     | bank     | 3.710    | 0.000         | 3.770     | -0.010         |
| 6   | Yuan       | currency | 0.450    | -0.010        | 0.540     | 0.000          |
| 1   | canada     | currency | 2.650    | -0.040        | 2.795     | -0.005         |
| 4   | euro ocoña | currency | 4.185    | 0.015         | 4.205     | 0.015          |
| 0   | Libra      | currency | 4.850    | -0.010        | 4.990     | 0.000          |

</div>

4.  Check the data from exchange houses:

``` python
tracker.houses.tail()
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

|     | companny_name  | img                                               | companny_url                                      | banks                | days_open                                         | last_updated             | buy_cost | buy_variation | sale_cost | sale_variation |
|-----|----------------|---------------------------------------------------|---------------------------------------------------|----------------------|---------------------------------------------------|--------------------------|----------|---------------|-----------|----------------|
| 21  | Rissan         | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://rissanpe.com/?utm_source=ced&utm_mediu... | BCP                  | {'M_F': '9 am - 6pm', 'Saturdays': '9 am - 1pm... | 2024-01-28T03:06:47.540Z | 3.725    | 0.005         | 3.743     | -0.007         |
| 22  | vip capital    | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://vipcapital.com.pe/?utm_source=ced         | BCP, Scotiabank      | {'M_F': '9 am - 6pm', 'Saturdays': '9 am - 1pm... | 2024-03-01T14:20:50.970Z | 3.730    | 0.000         | 3.755     | 0.000          |
| 23  | Cambio Mas     | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://cambiomas.com.pe/?utm_source=ced          | BCP, BBVA, Interbank | {'M_F': '8 am - 6 pm', 'Saturdays': '8 am - 6 ... | 2024-05-13T19:06:30.179Z | 3.73     | 0.010         | 3.753     | 0.006          |
| 24  | Soluciones CR  | https://s3-ced-uploads-01.s3.amazonaws.com/171... | https://solucionescr.pe/                          | BCP                  | {'M_F': '8:00 am - 8:00 pm', 'Saturdays': '8:0... | 2024-06-06T22:45:57.628Z | 3.733    | 0.000         | 3.741     | 0.001          |
| 25  | Cambio Digital | https://s3-ced-uploads-01.s3.amazonaws.com/172... | https://cambiodigitalperu.com/                    | BCP                  | {'M_F': '9am - 7pm', 'Saturdays': '9am - 2pm',... | 2024-08-02T20:01:58.289Z | 3.73     | -0.002        | 3.743     | 0.003          |

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

|     | time     | name       | type     | buy_cost | buy_variation | sale_cost | sale_variation | day        |
|-----|----------|------------|----------|----------|---------------|-----------|----------------|------------|
| 715 | 14:02:22 | nacion     | bank     | 3.710    | 0.000         | 3.770     | -0.010         | 19-08-2024 |
| 716 | 14:02:22 | Yuan       | currency | 0.450    | -0.010        | 0.540     | 0.000          | 19-08-2024 |
| 717 | 14:02:22 | canada     | currency | 2.650    | -0.040        | 2.795     | -0.005         | 19-08-2024 |
| 718 | 14:02:22 | euro ocoña | currency | 4.185    | 0.015         | 4.205     | 0.015          | 19-08-2024 |
| 719 | 14:02:22 | Libra      | currency | 4.850    | -0.010        | 4.990     | 0.000          | 19-08-2024 |

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

|      | companny_url                                      | time     | img                                               | banks                | days_open                                         | last_updated             | buy_cost | buy_variation | sale_cost | sale_variation | day        |
|------|---------------------------------------------------|----------|---------------------------------------------------|----------------------|---------------------------------------------------|--------------------------|----------|---------------|-----------|----------------|------------|
| 2491 | https://rissanpe.com/?utm_source=ced&utm_mediu... | 14:02:22 | https://s3-ced-uploads-01.s3.amazonaws.com/170... | BCP                  | {'M_F': '9 am - 6pm', 'Saturdays': '9 am - 1pm... | 2024-01-28T03:06:47.540Z | 3.725    | 0.005         | 3.743     | -0.007         | 19-08-2024 |
| 2492 | https://vipcapital.com.pe/?utm_source=ced         | 14:02:22 | https://s3-ced-uploads-01.s3.amazonaws.com/170... | BCP, Scotiabank      | {'M_F': '9 am - 6pm', 'Saturdays': '9 am - 1pm... | 2024-03-01T14:20:50.970Z | 3.730    | 0.000         | 3.755     | 0.000          | 19-08-2024 |
| 2493 | https://cambiomas.com.pe/?utm_source=ced          | 14:02:22 | https://s3-ced-uploads-01.s3.amazonaws.com/170... | BCP, BBVA, Interbank | {'M_F': '8 am - 6 pm', 'Saturdays': '8 am - 6 ... | 2024-05-13T19:06:30.179Z | 3.730    | 0.010         | 3.753     | 0.006          | 19-08-2024 |
| 2494 | https://solucionescr.pe/                          | 14:02:22 | https://s3-ced-uploads-01.s3.amazonaws.com/171... | BCP                  | {'M_F': '8:00 am - 8:00 pm', 'Saturdays': '8:0... | 2024-06-06T22:45:57.628Z | 3.733    | 0.000         | 3.741     | 0.001          | 19-08-2024 |
| 2495 | https://cambiodigitalperu.com/                    | 14:02:22 | https://s3-ced-uploads-01.s3.amazonaws.com/172... | BCP                  | {'M_F': '9am - 7pm', 'Saturdays': '9am - 2pm',... | 2024-08-02T20:01:58.289Z | 3.730    | -0.002        | 3.743     | 0.003          | 19-08-2024 |

</div>

#### Last Data

Retrieve data for the last days number of days.

``` python
data_last = last_days_data(days=2)
data_last["he"].tail()
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

|      | companny_url                                      | time     | img                                               | banks                | days_open                                         | last_updated             | buy_cost | buy_variation | sale_cost | sale_variation | day        |
|------|---------------------------------------------------|----------|---------------------------------------------------|----------------------|---------------------------------------------------|--------------------------|----------|---------------|-----------|----------------|------------|
| 1607 | https://rissanpe.com/?utm_source=ced&utm_mediu... | 14:02:22 | https://s3-ced-uploads-01.s3.amazonaws.com/170... | BCP                  | {'M_F': '9 am - 6pm', 'Saturdays': '9 am - 1pm... | 2024-01-28T03:06:47.540Z | 3.725    | 0.005         | 3.743     | -0.007         | 19-08-2024 |
| 1608 | https://vipcapital.com.pe/?utm_source=ced         | 14:02:22 | https://s3-ced-uploads-01.s3.amazonaws.com/170... | BCP, Scotiabank      | {'M_F': '9 am - 6pm', 'Saturdays': '9 am - 1pm... | 2024-03-01T14:20:50.970Z | 3.730    | 0.000         | 3.755     | 0.000          | 19-08-2024 |
| 1609 | https://cambiomas.com.pe/?utm_source=ced          | 14:02:22 | https://s3-ced-uploads-01.s3.amazonaws.com/170... | BCP, BBVA, Interbank | {'M_F': '8 am - 6 pm', 'Saturdays': '8 am - 6 ... | 2024-05-13T19:06:30.179Z | 3.730    | 0.010         | 3.753     | 0.006          | 19-08-2024 |
| 1610 | https://solucionescr.pe/                          | 14:02:22 | https://s3-ced-uploads-01.s3.amazonaws.com/171... | BCP                  | {'M_F': '8:00 am - 8:00 pm', 'Saturdays': '8:0... | 2024-06-06T22:45:57.628Z | 3.733    | 0.000         | 3.741     | 0.001          | 19-08-2024 |
| 1611 | https://cambiodigitalperu.com/                    | 14:02:22 | https://s3-ced-uploads-01.s3.amazonaws.com/172... | BCP                  | {'M_F': '9am - 7pm', 'Saturdays': '9am - 2pm',... | 2024-08-02T20:01:58.289Z | 3.730    | -0.002        | 3.743     | 0.003          | 19-08-2024 |

</div>

``` python
data_last["bank"].tail()
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

|     | time     | name       | type     | buy_cost | buy_variation | sale_cost | sale_variation | day        |
|-----|----------|------------|----------|----------|---------------|-----------|----------------|------------|
| 481 | 14:02:22 | nacion     | bank     | 3.710    | 0.000         | 3.770     | -0.010         | 19-08-2024 |
| 482 | 14:02:22 | Yuan       | currency | 0.450    | -0.010        | 0.540     | 0.000          | 19-08-2024 |
| 483 | 14:02:22 | canada     | currency | 2.650    | -0.040        | 2.795     | -0.005         | 19-08-2024 |
| 484 | 14:02:22 | euro ocoña | currency | 4.185    | 0.015         | 4.205     | 0.015          | 19-08-2024 |
| 485 | 14:02:22 | Libra      | currency | 4.850    | -0.010        | 4.990     | 0.000          | 19-08-2024 |

</div>

#### Especific Date

Get data for a specific date.

``` python
data_day = load_day_data(today - timedelta(1))
data_day["he"].tail()
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

|     | img                                               | companny_url                                      | banks                | days_open                                         | last_updated             | buy_cost | buy_variation | sale_cost | sale_variation | time     | day        |
|-----|---------------------------------------------------|---------------------------------------------------|----------------------|---------------------------------------------------|--------------------------|----------|---------------|-----------|----------------|----------|------------|
| 229 | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://rissanpe.com/?utm_source=ced&utm_mediu... | BCP                  | {'M_F': '9 am - 6pm', 'Saturdays': '9 am - 1pm... | 2024-01-28T03:06:47.540Z | 3.72     | 0.0           | 3.750     | 0.000          | 18:53:24 | 18-08-2024 |
| 230 | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://vipcapital.com.pe/?utm_source=ced         | BCP, Scotiabank      | {'M_F': '9 am - 6pm', 'Saturdays': '9 am - 1pm... | 2024-03-01T14:20:50.970Z | 0.00     | 0.0           | 0.000     | 0.000          | 18:53:24 | 18-08-2024 |
| 231 | https://s3-ced-uploads-01.s3.amazonaws.com/170... | https://cambiomas.com.pe/?utm_source=ced          | BCP, BBVA, Interbank | {'M_F': '8 am - 6 pm', 'Saturdays': '8 am - 6 ... | 2024-05-13T19:06:30.179Z | 0.00     | -3.7          | 0.000     | -3.760         | 18:53:24 | 18-08-2024 |
| 232 | https://s3-ced-uploads-01.s3.amazonaws.com/171... | https://solucionescr.pe/                          | BCP                  | {'M_F': '8:00 am - 8:00 pm', 'Saturdays': '8:0... | 2024-06-06T22:45:57.628Z | 3.73     | 0.0           | 3.750     | 0.006          | 18:53:24 | 18-08-2024 |
| 233 | https://s3-ced-uploads-01.s3.amazonaws.com/172... | https://cambiodigitalperu.com/                    | BCP                  | {'M_F': '9am - 7pm', 'Saturdays': '9am - 2pm',... | 2024-08-02T20:01:58.289Z | 3.72     | 0.0           | 3.755     | 0.000          | 18:53:24 | 18-08-2024 |

</div>

``` python
data_day["bank"].tail()
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

|     | name       | type     | buy_cost | buy_variation | sale_cost | sale_variation | time     | day        |
|-----|------------|----------|----------|---------------|-----------|----------------|----------|------------|
| 76  | nacion     | bank     | 3.71     | 0.000         | 3.780     | 0.000          | 18:53:24 | 18-08-2024 |
| 77  | Yuan       | currency | 0.45     | -0.010        | 0.540     | 0.000          | 18:53:24 | 18-08-2024 |
| 78  | canada     | currency | 2.65     | -0.040        | 2.795     | -0.005         | 18:53:24 | 18-08-2024 |
| 79  | euro ocoña | currency | 4.17     | -0.001        | 4.190     | 0.000          | 18:53:24 | 18-08-2024 |
| 80  | Libra      | currency | 4.85     | -0.010        | 4.990     | 0.000          | 18:53:24 | 18-08-2024 |

</div>

## Contributing

If you wish to contribute to this project, please fork the repository
and submit a pull request with your improvements.
