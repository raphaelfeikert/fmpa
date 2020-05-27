# fmpa is a Python wrapper for the [Financial Modelling Prep API](https://financialmodelingprep.com/)

## Basic usage:

```python
api_key = "your api-key"

api = FMPA(api_key)

apple = api.company("AAPL")

apple.inc_stmt()
```
