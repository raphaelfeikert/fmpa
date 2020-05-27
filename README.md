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

#get all tradable tickersymbols
universe = api.universe() 

apple = api.company("AAPL")

#get apples discounted cashflow value
apple.dcf_val()
```
