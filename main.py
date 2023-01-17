Nestle_product = {"KitKat" : 23456000 
, "Breyers" : 1235891 
, "HellManns" : 17241412 ,
"Nido":44506003
}

Unilever_product = { "Lipton" : 23456000 
, "Breyers" : 1235891 
, "HellManns" : 17241412 
 , "Marmite" :11715324}

Nestle_set = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever_set = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}




print( Unilever_product.items())
print(Nestle_product.items())

print("____"*10 )


top_selling_product_Unilever = max(Unilever_product , key=Unilever_product.get)
print("top selling product in Unilever " , top_selling_product_Unilever)

top_selling_product_Nestle = max(Nestle_product , key=Nestle_product.get)
print("top selling product Nestle " , top_selling_product_Nestle)
print("______" * 10)
if len(Nestle_product) > len(Unilever_product):
    print ("Nestle has more products")
elif len(Nestle_product) == len(Unilever_product):
    print("both has a same number pf products")
else:
    print("unileaver has more products")  
print("______" * 10)






    



all_Unilever_Nestle_list = Nestle_set | Unilever_set
for element in all_Unilever_Nestle_list:
    print("all the countries that has Nestle_product or Unilever_product" , element)

print("______" * 10)


same_Nestle_Unilver_list = Nestle_set & Unilever_set
for element in same_Nestle_Unilver_list:
    print("both unilever & nestle are in " , element)    

print("______" * 10)


Nestle_sells_no_Unilver  = Nestle_set - Unilever_set
for element in Nestle_sells_no_Unilver:
    print(" Unilver doens't sell in" , element)  

    
print("______" * 10)







