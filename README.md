# fmpa is a Python wrapper for the [Financial Modelling Prep API](https://financialmodelingprep.com/) (under construction)

## Installation
```console
> pip install fmpa
```
## Basic usage:

```python

from fmpa import FMPA

api_key = "your api-key"
api = FMPA(api_key)
apple = api.company("AAPL")

apple.inc_stmt()
```
