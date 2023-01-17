

'''
## Using what you've learned during . Please do the following :
- Create a variable to hold the values of Nestle products (use a dicitionary)
- Create a variable to hold the values of Unilever products (Use a dictionary)
- Print each product sold by Unilever and the sales figures / numbers  for that product.
- Print each product sold by Nestle and the sales figures / numbers  for that product.
- Print which of the companies has more products that the other company.

'''

kate_sales_Nestle ={
    "KitKat" : 34_456_432 ,
    "Nescafe" : 14_106_132,
    "Maggi" : 9_960_312,
    "Nido" : 44_506_003 }

Dalia_sales_Unilever={
    "Lipton" : 23_456_000,
     "Breyers" : 1_235_891, 
     "HellManns" : 17_241_412,
     "Marmite" : 11_715_324
    }

Monica_Nestle ={"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}

Monica_Unilever ={"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

print("products that sold by Unilever and the sales figures : ",Dalia_sales_Unilever)
print("products that sold by Nestle and the sales figures :",kate_sales_Nestle)


def highest_products (first_company : dict, second_company : dict) :
    if len(first_company) > len(second_company) :
        return "The company has the highest products is : " ,first_company 
    elif len(second_company) > len(first_company) :
        return "The company has the highest products is : " ,second_company 
    else :
        return "The number of products is equal in both companies"

print(highest_products(kate_sales_Nestle ,Dalia_sales_Unilever))


#Print the top selling product from Nestle with sales figures.
# Print the top selling product from Unilever with sales figures.

top_prodect_price_N = 0
top_prodect_N = None

for key , value in kate_sales_Nestle.items():
    if value > top_prodect_price_N :
        top_prodect_price_N = value
        top_prodect_N = key


print("the top sold prodect in Nestle is : ")
print(f"{top_prodect_N} {top_prodect_price_N} ")

top_prodect_price_U = 0
top_prodect_U = None

for key , value in Dalia_sales_Unilever.items():
    if value > top_prodect_price_U :
        top_prodect_price_U = value 
        top_prodect_U = key
print("the top sold prodect in Unilever is : ")
print(f"{top_prodect_U} {top_prodect_price_U} ")

#Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.

cities_Unilever_Nestle_products = Monica_Nestle | Monica_Unilever
print(" all the cities Unilever & Nestle sell their products in :")

for cities in cities_Unilever_Nestle_products :
 print(cities) 

#Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.


cities_both_Nestle_Unilver_common = Monica_Nestle & Monica_Unilever
print("cities that both Nestle & Unilver sell in common :")
for common in cities_both_Nestle_Unilver_common:
 print(common) 

# Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
cities_Nestle_in_but_Unilver_not = Monica_Nestle - Monica_Unilever
print("cities Nestle sells in , but Unilver doens't sell in :")

for in_not in cities_Nestle_in_but_Unilver_not:
 print(in_not) 