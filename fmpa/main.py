import requests
import pandas as pd
import numpy as np
https://financialmodelingprep.com/api/v3/profile/AAPL?apikey=3b4daf218714762f63ff568c86e2083c


def endpoint_handler(endpoint):
        base_url = "https://financialmodellingprep.com/api/v3/"
        response=requests.get(base_url+endpoint)
        results=json.loads(response.text)
        if response.status_code==200:
            return results
        elif response.status_code==404:
            print("Not found!")

def get_stocks():
    response=endpoint_handler("company/stock/list")
    symb_list=[{i["name"]:i["symbol"]} for i in response["symbolsList"]]
    return symb_list

def get_symbol(stock):
    response=endpoint_handler("company/stock/list")
    symbol=[i['symbol'] for i in response["symbolsList"] if i['name']==stock]
    return symbol[0]

def get_symbols():
    response=endpoint_handler("company/stock/list")
    symbols=[i['symbol'] for i in response["symbolsList"]]
    return symbols


class Company:

    def __init__(self,symb):
        self.symb=symb

    #financial statements:
    def inc_stmt(self):
        response = endpoint_handler("financials/income-statement/{}?apikey={}".format(self.symb, TOKEN))
        return response

    def bal_stmt(self, df=None):
        response = endpoint_handler("financials/balance-sheet-statement/{}?apikey={}".format(self.symb, TOKEN))
        if df==None:
            return response['financials']
        else:
            return make_df(response['financials'])

    def cf_stmt(self):
        response = endpoint_handler("financials/cash-flow-statement/{}?apikey={}".format(self.symb, TOKEN))
        return response

    #financial ratios:
    def fin_ratios(self):
        response = endpoint_handler("financial-ratios/{}?apikey={}".format(self.symb, TOKEN))
        return response

    #company-enterprise-value:
    def entpr_val(self):
        response = endpoint_handler("enterprise-value/{}?apikey={}".format(self.symb, TOKEN))
        return response

    #company key metrics:
    def entpr_keymetr(self):
        response = endpoint_handler("company-key-metrics/{}?apikey={}".format(self.symb, TOKEN)))
        return response

    #company financial growth:
    def fin_grth(self):
        response = endpoint_handler("financial-statement-growth/{}?apikey={}".format(self.symb, TOKEN))
        return response

    #company rating:
    def rating(self):
        response = endpoint_handler("company/rating/{}?apikey={}".format(self.symb, TOKEN))
        return response

    #discounted cash flow value:
    def dcf(self):
        response = endpoint_handler("company/discounted-cash-flow/{}?apikey={}".format(self.symb, TOKEN))
        return response

    #historical dcf:
    def hist_dcf(self):
        response = endpoint_handler("company/historical-discounted-cash-flow/{}?apikey={}".format(self.symb, TOKEN))
        return response

    #realtime stockprice:
    def rlt_price(self):
        response = endpoint_handler("stock/real-time-price/{}?apikey={}".format(self.symb, TOKEN))
        return response['price']


