from math import prod
from xml.etree.ElementTree import tostring
from numpy import product

from product import Product


class Store:
    def __init__(self,name):
        self.name=name
        self.products={}
    
    def add_product(self,new_product):
        product_key=str(new_product.id)
        self.products[product_key]=new_product

    def sell_product(self, id):
        str_id=str(id)
        product_To_Sell=self.products[str_id]
        print("the product:",product_To_Sell.name,"with the id:",product_To_Sell.id,"from the category:",product_To_Sell.category,"with the price",product_To_Sell.price,"is sold")
        del self.products[str_id]
    
    def inflation(self, percent_increase):
        for i in self.products:
            self.products[i].update_price(percent_increase)
    
    def set_clearance(self, category,percent_discount):
        for i in self.products:
            if self.products[i].category==category:
                self.products[i].update_price(percent_discount,False)

    def show_products(self):
        for i in self.products:
            self.products[i].print_info()



    