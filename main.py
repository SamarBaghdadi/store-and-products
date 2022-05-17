from product import Product
from store import Store


orange_juice=Product("orange_juice",2,"beverage")
cheddar =Product("Cheddar",5,"cheese")
prince= Product("Prince",8,"cake")
nescafe=Product("Nescafe",0.5,"beverage")
parmesan=Product("Parmesan",18,"cheese")
anchois=Product("Anchois",54,"fish")
Fanta=Product("Fanta",2,"beverage")
Fanta.print_info()
parmesan.print_info()
cheddar.print_info()

Aziza=Store("Aziza")
Aziza.add_product(cheddar)
Aziza.add_product(nescafe)
# Aziza.add_product(orange_juice)
# Aziza.add_product(parmesan)
Aziza.show_products()
Aziza.inflation(2)
Aziza.show_products()
Aziza.set_clearance("cheese",50)
Aziza.sell_product(cheddar.id)
Aziza.show_products()
Aziza.sell_product(nescafe.id)
Aziza.show_products()

