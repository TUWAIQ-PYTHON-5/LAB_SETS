#- Create a variable to hold the values of Nestle products (use a dicitionary)
nestleProduct:dict={
    'KitKat' : 34456432,
    'Nescafe' : 14106132,
    'Maggi' : 9960312,
    'Nido' : 44506003
    }
#- Create a variable to hold the values of Unilever products (Use a dictionary)
unileverProduct:dict={
    'Lipton' : 23456000,
    'Breyers' : 1235891,
    'HellManns' : 17241412,
    'Marmite' : 11715324
}

#- Print each product sold by Unilever and the sales figures / numbers  for that product.
for key in unileverProduct:
    print(key ,':', unileverProduct[key] ,'US Dollars')

print('\n')

# - Print each product sold by Nestle and the sales figures / numbers  for that product.
for key in nestleProduct:
    print(key ,':', nestleProduct[key] ,'US Dollars')

print('\n')

#- Print which of the companies has more products that the other company.###
lengthOfUnilever:int = len(unileverProduct)
lengthOfNestle:int = len(nestleProduct)
if(lengthOfUnilever > lengthOfNestle):
    print("The Product in Unilever is more than the Product in Nestle")
elif(lengthOfUnilever > lengthOfNestle):
    print("The Product in Nestle is more than the Product in Unilever")
else:
    print("They are Equal")

print('\n')

#- Print the top selling product from Nestle with sales figures.
for name , selling in nestleProduct.items():
    topSales:float=0
    if selling > topSales:
        topSales=selling
print('The Top sell in Nestle is : ',name ,' ', selling,' US Dollars')

print('\n')

#- Print the top selling product from Unilever with sales figures.
for name , selling in unileverProduct.items():
    topSales:float=0
    if selling > topSales:
        topSales=selling
print('The Top sell in Unilever is : ',name ,' ', selling,' US Dollars')

print('\n')

countriesNestle:set={"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
countriesUnilever:set={"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

#- Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
print("\nUnilever & Nestle sell their products in\n")
for Country in countriesNestle.union(countriesUnilever):
    print (Country)

print('\n')

#- Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
print("They both sell in")
for Country in countriesNestle.intersection(countriesUnilever):
    print (Country)

print('\n')

#- Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
print("cities Nestle sells in")
for Country in countriesNestle.difference(countriesUnilever):
    print (Country)

