nestle_products={"KitKat" : 34456432 ,"Nescafe" : 14106132,"Maggi ": 9960312 ,"Nido" : 44506003 }

unilever_products={"Lipton" :23456000 ,"Breyers": 1235891 ,"HellManns":17241412 ,"Marmite":11715324 }

print("-"*25)
print ("products and sales of unilever :")
for key ,value in unilever_products.items():
    print(f"{key},{value} US Dollars")


print("-"*25)
print ("products and sales of nestle :")

for key ,value in nestle_products.items():
    print(f"{key},{value} US Dollars")

print("-"*25)

if len(nestle_products ) > len(unilever_products) :
    print("The nestle company has more products that the other company")

elif  len(nestle_products ) < len(unilever_products) :
    print("The unilever company has more products that the other company")

else:
    print("They have the same number of products")








print("the top selling product from Nestle is: ",max(nestle_products) )

print("the top selling product from Unilever is: ",max(unilever_products))

nestle={"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever={"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}


'''Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
- Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
- Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
'''

unilever_nestle_union=   Unilever | nestle
print(unilever_nestle_union)
for i in unilever_nestle_union:print(i)


unilever_nestle_Intersection=   nestle & Unilever
print(unilever_nestle_Intersection)
for i in unilever_nestle_Intersection:print(i)

unilever_nestle_difference=   nestle - Unilever
print(unilever_nestle_difference)
for i in unilever_nestle_difference:print(i)

