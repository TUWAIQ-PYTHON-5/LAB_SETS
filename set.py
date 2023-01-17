
Nestle_product = {

"KitKat"  : 34456432,
"Nescafe" : 14106132,
"Maggi"   : 9960312,
"Nido"    : 44506003
    
}

Unilever_products ={

"Lipton"    : 23456000,
"Breyers"   : 1235891,
"HellManns" : 17241412,
"Marmite"   : 11715324

}

for key , value in Unilever_products.items():
    print(value ," : ", key)
print("--------------------------")
for value , key in Nestle_product.items():
    print(value ," : ", key)

print("--------------------------")
count = 0
count2 = 0
for  i in  Nestle_product.items():
    count = count + 1
    for j in Unilever_products.items():
        count2 = count2 + 1
        break
if count > count2:
    print("Nestle products ")
elif count < count2:
    print("Unilever products ")
else: print("Nestle products Equal Unilever products")
print("--------------------------")

Nestle_product_ = Nestle_product.items()
max =0
for k ,top_selling in Nestle_product_:
    if top_selling > max:
        max = top_selling
print(k, max , "US Dollars")
print("----------------------------")

Unilever_product_ = Unilever_products.items()
max =0
for k ,top_selling in Unilever_product_:
    if top_selling > max:
        max = top_selling
print(k, max , "US Dollars")
print("----------------------------")

Nestle_cities_sales  = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever_cities_sales = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

for cities in Nestle_cities_sales.union(Unilever_cities_sales):
    print (cities)

print("----------------------------")
for cities in Nestle_cities_sales.intersection(Unilever_cities_sales):
    print (cities)
print("----------------------------")

Nestle_cities_sales.difference(Unilever_cities_sales)
Uniqe_sales_cities =Nestle_cities_sales - Unilever_cities_sales 
for cities in Uniqe_sales_cities:
    print(cities)

