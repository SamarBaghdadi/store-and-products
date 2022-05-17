from datetime import datetime
from math import floor
from pickletools import long1
from random import random
from sqlite3 import Time
from time import time


class Product:
    def __init__(self,name,price,category):
        self.name=name
        self.price=price
        self.category=category
        self.id=datetime.now().toordinal()+floor(random()*100000)


    
    def update_price(self,percent_change,is_increased=True):
        if is_increased:
            self.price+=self.price*percent_change/100
        else:
            self.price-=self.price*percent_change/100
    
    def print_info(self):
        print("The product :",self.name,"with id",self.id,"from the category",self.category,"has the price of $",self.price)
        
    def return_id(self):
        return self.id

Fanta=Product("Fanta",2,"beverage")
Fanta.return_id()


    