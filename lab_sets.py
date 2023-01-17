nestle_products :dict = {"KitKat" : '34,456,432', 
                    "Nescafe" : '14,106,132' ,
                     "Maggi" : '9,960,312' , 
                     "Nido" : '44,506,003' }

unilever_products :dict = { "Lipton" : '23,456,000' ,
                       "Breyers" : '1,235,891', 
                       "HellManns" : '17,241,412' , 
                        "Marmite" : '11,715,324' }


print (unilever_products.items())
print (nestle_products.items())


if len(nestle_products) > len(unilever_products):
    print("the company has more products is : nestle_products")

elif len(nestle_products) < len(unilever_products):
     print("the company has more products is :unilever_products ")
else :
    print ("All of them are equal")




top_selling_of_nestle = max(nestle_products, key = nestle_products.get)
print("the top selling :" ,top_selling_of_nestle)
top_selling_of_unilever= max(unilever_products, key = unilever_products.get)
print( "the top selling :" ,top_selling_of_unilever)

cities_unilever={"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
cities_nestle ={"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}


cities_of_selling_both= cities_nestle | cities_unilever 
for element in  cities_of_selling_both :
    print ("cities_of_selling_both: " , cities_of_selling_both)
    break

intersection_cities = cities_nestle & cities_unilever 
for i in intersection_cities:
    print ("intersection_cities:", intersection_cities)
    break
deffrince_cities= cities_nestle - cities_unilever
for x in deffrince_cities:
    print( "deffrince_cities: ",deffrince_cities)
    break
