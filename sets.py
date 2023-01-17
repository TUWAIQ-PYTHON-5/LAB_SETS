Nestle_list = {
"KitKat" :  34456432,
"Nescafe" :  14106132,
"Maggi" : 9960312,
"Nido" : 44506003 }

Unilever_list = {
"Lipton":23456000,
"Breyers":1235891,
"HellManns":17241412,
"Marmite":11715324}


print(Unilever_list.items())
print(Nestle_list.items())


if len(Nestle_list)>len(Unilever_list):
    print("Nettl prodect more than Unilever")
elif len(Nestle_list)<len(Unilever_list):
    print("Unilever prodect more than Nestle")
else:print("is Ecuale")


top_selling_Nestl = max(Nestle_list, key = Nestle_list.get)
print("top_selling_Nestl:",top_selling_Nestl,"us Dollars")


top_selling_Unilever = max(Unilever_list, key = Unilever_list.get)
print("top selling Unilever:",top_selling_Unilever,"us Dollars")


Nestle_Cities : set = { "Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever_cities : set = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

all_cities_sell_their_sell = Nestle_Cities | Unilever_cities
for element in  all_cities_sell_their_sell :
    print("all the cities sell their products in ",element)

cities_both_Nestle_Unilver_sell = Nestle_Cities & Unilever_cities
for sell in  cities_both_Nestle_Unilver_sell :
    print("cities_both_Nestle_Unilver_sell",sell)


the_cities_Nestle_sells_in = Nestle_Cities-Unilever_cities 
for x in  the_cities_Nestle_sells_in :
    if x in Unilever_cities:None
else:
    print("the_cities_Nestle_sells_in",the_cities_Nestle_sells_in)
