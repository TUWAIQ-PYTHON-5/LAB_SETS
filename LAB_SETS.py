# Create a variable to hold the values of Nestle products (use a dicitionary)

nestle_products = { "KitKat" : 34_456_432  , "Nescafe" : 14_106_132 
, "Maggi" : 9_960_312  , "Nido" : 44_506_003  }

# Create a variable to hold the values of Unilever products (Use a dictionary)

unilever_products = {"Lipton" : 23_456_000  , "Breyers" : 1_235_891 
, "HellManns" : 17_241_412 , "Marmite" : 11_715_324 }

monica_nestle = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}

monica_unilever =  {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

# Print each product sold by Unilever and the sales figures / numbers for that product.

print(" Product sold by Unilever and the sales numbers for that product : ",unilever_products )

# Print each product sold by Nestle and the sales figures / numbers for that product.

print("Product sold by Nestle and the sales numbers for that product : ", nestle_products )

# Print which of the companies has more products that the other company.

print("Products sold by Nestle :")
for key, value in nestle_products.items():
    print(f"{key} : {value} US Dollars ")

print("*"*10)

print("Products sold by Unilever :")
for key, value in unilever_products.items():
    print(f"{key} : {value} US Dollars ")

if len(nestle_products) > len(unilever_products):
    print("Nestle has more products ")
elif len(unilever_products) > len(nestle_products):
    print("Unilever has more products ")
else:
    print("Unilever and Nestle has the same products count")


#Print the top selling product from Nestle with sales figures.

nestle_most_sold_product_figure = 0
nestle_most_sold_product = None

for key, value in nestle_products.items():
    if value > nestle_most_sold_product_figure :
        nestle_most_sold_product_figure = value
        nestle_most_sold_product = key 

print("The most sold product in Nestle :")
print(f"{nestle_most_sold_product} {nestle_most_sold_product_figure} US Dollars")

#Print the top selling product from Unilever with sales figures.

unilever_most_sold_product_figure = 0
unilever_most_sold_product = None

for key, value in unilever_products.items():
    if value > unilever_most_sold_product_figure :
        unilever_most_sold_product_figure = value
        unilever_most_sold_product = key 

print("The most sold product in Unilever :")
print(f"{unilever_most_sold_product} {unilever_most_sold_product_figure} US Dollars")

# Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.

sets_with_loop1 = monica_nestle.union(monica_unilever)

for element in monica_unilever:
    if element not in sets_with_loop1:
        sets_with_loop1.append(element)
print("The union sets : ", sets_with_loop1 | monica_unilever)


# Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.

sets_with_loop2 = monica_nestle.intersection(monica_unilever)

for element in monica_unilever:
    if element in sets_with_loop2:
        sets_with_loop2.__class_getitem__(element)
print("The intersection sets : ", sets_with_loop2 & monica_unilever)

# Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.

sets_with_loop3 = monica_nestle.difference(monica_unilever)

for element in monica_unilever:
    if element in sets_with_loop3:
        sets_with_loop3.__class_getitem__(element)
print("The  Difference sets : " , sets_with_loop3 - monica_unilever)