Nestle_product = {"KitKat" : "23,456,000" 
, "Breyers" : "1,235,891" 
, "HellManns" : "17,241,412" 
, "Marmite" :"11,715,324" ,
"Nido":"44,506,003" 
}

Unilever_product = { "Lipton" : "23,456,000" 
, "Breyers" : "1,235,891" 
, "HellManns" : "17,241,412 "
 , "Marmite" :"11,715,324"}

Nestle_set = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever_set = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}




print( Unilever_product.items())
print(Nestle_product.items())


top_selling_product_Unilever = max(Unilever_product , key=Unilever_product.get)
print("top selling product in Unilever " , top_selling_product_Unilever)

top_selling_product_Nestle = max(Nestle_product , key=Nestle_product.get)
print("top selling product Nestle " , top_selling_product_Nestle)

if len(Nestle_product) > len(Unilever_product):
    print ("Nestle has more products")
elif len(Nestle_product) == len(Unilever_product):
    print("both has a same number pf products")
else:
    print("unileaver has more products")  





    



all_Unilever_Nestle_list = Nestle_set | Unilever_set
for element in all_Unilever_Nestle_list:
    print("all the countries that has Nestle_product or Unilever_product" , element)

same_Nestle_Unilver_list = Nestle_set & Unilever_set
for element in same_Nestle_Unilver_list:
    print("both unilever & nestle are in " , element)    



Nestle_sells_no_Unilver  = Nestle_set - Unilever_set
for element in Nestle_sells_no_Unilver:
    print(" Unilver doens't sell in" , element)  

    







