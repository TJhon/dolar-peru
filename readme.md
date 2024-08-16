# Dolar Peru

- Scrapea el precio del dolar de diferentes casas de cambio
- Los datos son recoolectados cada 45 minutos.


## Instalacion

```sh
# Stable
pip install git+https://github.com/TJhon/dolar-peru@api
```

## Usage

```{python}
from PDolar.api import PeruDolar
tracker = PeruDolar()
```

```{python}
tracker.bank
```

```{python}
tracker.houses
```

```{python}
tracker.sunat
```
