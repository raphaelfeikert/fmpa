import json
from requests_toolbelt import sessions
 
class FMPA(object):

    def __init__(self, key):
        self.key = key

    def company(self, symb):
        return self.Company(self, symb)

    
    class Company(object):
        
        def __init__(self, outer, symb):
            self.outer = outer
            self.symb = symb
            
        @property
        def getkey(self):
            return self.outer.key

        #functions not depending on specific stock:
    
        def endpt(self, url):
            
            baseurl = "https://financialmodellingprep.com/api/v3/"
            http = sessions.BaseUrlSession(base_url = baseurl)        
            path = (url + "?apikey={}").format(self.symb, self.getkey)
            #print(path)
            result = http.get(path).text
            return json.loads(result)

        
        #functions depending on specific stock:

        def inc_stmt(self):
            path = "financials/income-statement/{}"
            result = self.endpt(path)
            return result

        def bal_stmt(self):
            path = "financials/balance-sheet-statement/{}"
            result = self.endpt(path)
            return result

        def cf_stmt(self):
            path = "financials/cash-flow-statement/{}"
            result = self.endpt(path)
            return result

        def fin_ratio(self):
            path = "financial-ratios/{}"
            result = self.endpt(path)
            return result

        def ent_val(self):
            path = "enterprise-value/{}"
            result = self.endpt(path)
            return result

        def ent_keymetr(self):
            path = "company-key-metrics/{}"
            result = self.endpt(path)
            return result

        def fin_grth(self):
            path = "financial-statement-growth/{}"
            result = self.endpt(path)
            return result

        def rating(self):
            path = "company/rating/{}"
            result = self.endpt(path)
            return result

        def dcf(self):
            path = "company/discounted-cash-flow/{}"
            result = self.endpt(path)
            return result

        def dcf_hist(self):
            path = "company/historical-discounted-cash-flow/{}"
            print(path)
            result = self.endpt(path)
            return result

        def rlt_price(self):
            path = "stock/real-time-price/{}"
            result = self.endpt(path)
            return result

