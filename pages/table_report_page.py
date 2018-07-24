from selene.support.jquery_style_selectors import s, ss
from selene import bys
from selene.browser import *

class TableReport(object):

    # methods
    def check_total_amount_for_each_quarter(self):
        size = ss('tbody>tr').size()
        for item in range(1, size):  
            quantity = [ i.text[1:].replace(",", "") for i in ss(('tbody>tr:nth-child({})>td').format(item)) if "$" in i.text ]    
            if len(quantity) > 1:
                price_for_all_products = [ round(sum(float(i) for i in quantity[:-1] ), 1) ] 
                total_price = [ float(i) for i in quantity[-1:] ]
                assert price_for_all_products == total_price


    def check_total_amount_for_year(self):          
        size = ss('tbody>tr').size()
        total_for_year = []
        for item in range(1, size):
            item = [ i.text for i in ss(('tbody>tr:nth-child({})>td').format(item)) ] 
            total_for_year.append(item[-1:][0])
        new = []
        for i in total_for_year[1:]:
            if i == "":
                break
            else:     
                new.append(i[1:].replace(",", ""))
        price_for_all_products = [ round(sum(float(i) for i in new[:-1] ), 1) ]  
        total_price = [ float(i) for i in new[-1:] ]       
        assert price_for_all_products == total_price
      