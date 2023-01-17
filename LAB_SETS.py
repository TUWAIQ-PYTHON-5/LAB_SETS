

# - Create a variable to hold the values of Nestle products (use a dicitionary)
nestleProducts = { "KitKat" : "34456432", "Nescafe" : "14106132",
"Maggi" : "9960312", "Nido" : "44506003"}

# - Print each product sold by Nestle and the sales figures / numbers  for that product.
print("product sold by Nestle and the sales: ")
for product, sales in nestleProducts.items() :
    print(product, sales+" US Dollars")

print("*"*10)

# - Create a variable to hold the values of Unilever products (Use a dictionary)
unileverProducts = { "Lipton" : "23456000", "Breyers" : "1235891", 
"HellManns" : "17241412", "Marmite" : "11715324"}

# - Print each product sold by Unilever and the sales figures / numbers  for that product.
print("product sold by Unilever and the sales: ")
for product, sales in unileverProducts.items() :
    print(product, sales+" US Dollars")

# - Print which of the companies has more products that the other company.
numberOfNestleProducts = len(nestleProducts)
numberOfUnileverProducts = len(unileverProducts)

if numberOfNestleProducts > numberOfUnileverProducts :
    print("Nestle has more products than Unilever")
elif numberOfNestleProducts < numberOfUnileverProducts :
     print("Unilever has more products than Nestle")
else :
    print("Nestle amd Unilever has same number of products")

# - Print the top selling product from Nestle with sales figures.
highestSales = 0
for product in nestleProducts :
    if int(nestleProducts[product]) > int(highestSales) :
        highestSales = nestleProducts[product]
        topSalesProduct = product
    
print("highest sales product is "+topSalesProduct+" :" + highestSales+"US Dollars")

# - Print the top selling product from Unilever with sales figures.
highestSales2 = 0
for product in unileverProducts :
    if int(unileverProducts[product]) > int(highestSales2) :
        highestSales2 = unileverProducts[product]
        topSalesProduct = product
   
print("highest sales product is "+topSalesProduct+" :" + highestSales2+"US Dollars")




nestleCountries = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unileverCountries = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

# - Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
print("the cities Unilever & Nestle sell their products in: ")
for city in nestleCountries | unileverCountries :
    print(city)
    
# - Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
print("the cities that both Nestle & Unilver sell in common: ")
for city in nestleCountries & unileverCountries :
    print(city)

# - Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
print("the cities Nestle sells in , but Unilver doens't sell in: ")
for city in nestleCountries - unileverCountries :
    print(city)








 