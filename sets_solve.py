
# - Create a variable to hold the values of Nestle products (use a dicitionary)
kate_products_nestle = { 
    "KitKat" : "34456432", "Nescafe" : "14106132",
"Maggi" : "9960312", "Nido" : "44506003"}

dalia_products_unilever = { "Lipton" : "23456000", "Breyers" : "1235891", 
"HellManns" : "17241412", "Marmite" : "11715324"}

#___________________________________________#

print("product sold by Nestle and the sales: ")
for product, sales in kate_products_nestle.items() :
    print(product, sales+" US Dollars")
print("*"*10)

print("product sold by Unilever and the sales: ")
for product, sales in dalia_products_unilever.items() :
    print(product, sales+" US Dollars")

# - Print which of the companies has more products that the other company.
number_Nestle_Products = len(kate_products_nestle)
number_Unilever_Products = len(dalia_products_unilever)

if number_Nestle_Products > number_Unilever_Products :
    print("Nestle has more products than Unilever")
elif number_Nestle_Products < number_Unilever_Products :
     print("Unilever has more products than Nestle")
else :
    print("Nestle amd Unilever has same number of products")
#____________________________________________________________

# - Print the top selling product from Nestle with sales figures.
top_selling_nestle = 0
for product in kate_products_nestle :
    if int(kate_products_nestle[product]) > int(top_selling_nestle) :
        top_selling_nestle = kate_products_nestle[product]
        top_Product = product
    
print("highest sales product is "+top_Product+" :" + top_selling_nestle +"US Dollars")

# - Print the top selling product from Unilever with sales figures.
top_selling_unilever = 0
for product in dalia_products_unilever :
    if int(dalia_products_unilever[product]) > int(top_selling_unilever) :
        top_selling_unilever = dalia_products_unilever[product]
        top_Product = product
   
print("highest sales product is "+top_Product+" :" + top_selling_unilever+"US Dollars")

#____________________________________________________________


nestle_cityes = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unilever_cityes = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

print("the cities Unilever & Nestle sell their products in: ")
for city in nestle_cityes | unilever_cityes :
    print(city)
    
print("the cities that both Nestle & Unilver sell in common: ")
for city in nestle_cityes & unilever_cityes :
    print(city)

print("the cities Nestle sells in , but Unilver doens't sell in: ")
for city in nestle_cityes - unilever_cityes :
    print(city)





