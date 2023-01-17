Nestle_products = {"KitKat" : 34_456_432,
 "Nescafe" : 14_106_132,
 "Maggi" : 9_960_312}
Unilever_products = {"Lipton" : 23_456_000 ,
 "Breyers" : 1_235_891 }

for product, sale in Nestle_products.items():
    print(product, ":", sale)

for product, sale in Unilever_products.items():
    print(product, ":", sale)

if len (Nestle_products) > len (Unilever_products):
    print("Nestle companies has more products")
else: 
    print("unilever companies has more products")


top_selling_product_Unilever = max(Unilever_products , key=Unilever_products.get)
print("top selling product in Unilever " , top_selling_product_Unilever)

top_selling_product_Nestle = max(Nestle_products , key=Nestle_products.get)
print("top selling product Nestle " , top_selling_product_Nestle)



Nestle_cities = {"Saudi Arabia", "Oman", "Kuwait",
 "Egypt", "Jordan", "Sudan"}

Unilever_cities = {"Saudi Arabia", "Kuwait",
  "Iraq", "Morocco", "Yemen", "United Emirates"}

all_Unilever_Nestle_list = Nestle_cities | Unilever_cities
for element in all_Unilever_Nestle_list:
    print("all the countries that has Nestle_product or Unilever_product" , element)

same_Nestle_Unilver_list = Nestle_cities & Unilever_cities
for element in same_Nestle_Unilver_list:
    print("both unilever & nestle are in " , element)    



Nestle_sells_no_Unilver  = Nestle_cities - Unilever_cities
for element in Nestle_sells_no_Unilver:
    print(" Unilver doens't sell in" , element) 
