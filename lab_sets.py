nestle_products :dict = {"KitKat" : '34,456,432', 
                    "Nescafe" : '14,106,132' ,
                     "Maggi" : '9,960,312' , 
                     "Nido" : '44,506,003' }

unilever_products :dict = { "Lipton" : '23,456,000' ,
                       "Breyers" : '1,235,891', 
                       "HellManns" : '17,241,412' , 
                        "Marmite" : '11,715,324' }
print (dict(unilever_products))
print (dict(nestle_products))
if len(nestle_products) > len(unilever_products):
    print("the company has more products is : nestle_products")

elif len(nestle_products) < len(unilever_products):
     print("the company has more products is :unilever_products ")
else :
    print ("All of them are equal")

top_selling_of_nestle=max(nestle_products.values())
print("the top selling :" ,top_selling_of_nestle )
top_selling_of_unilever= max(unilever_products.items())
print( "the top selling :" ,top_selling_of_unilever)

cities_unilever={"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
cities_nestle ={"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
cities_of_selling_both= cities_nestle | cities_unilever
print (cities_of_selling_both)
intersection_cities = cities_nestle & cities_unilever 
print (intersection_cities)
deffrince_cities= cities_nestle - cities_unilever
print( deffrince_cities)