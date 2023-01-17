nestleSales = {"KitKat" : "34456432" , "Nescafe" : "14106132" , "Maggi" : "9960312" , "Nido" : "44506003"}
unileverSales = {"Lipton" : "23456000" , "Breyers" : "1235891" , "HellManns" : "17241412" , "Marmite" : "11715324"}

nestlesCountries = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unileversCountries = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

nestleProductsValues=set()
unileverProductsValues=set()

for value in unileverSales:
    unileverProductsValues.add(unileverSales[value])
    print(f"{value}: {unileverSales[value]}$")
for value in nestleSales:
    nestleProductsValues.add(nestleSales[value])
    print(f"{value}: {nestleSales[value]}$")

if not len(nestleSales) == len(unileverSales):
    if len(nestleSales) > len(unileverSales):
        print("Nestle have more products")
    else:
        print("Unilever have more products")
else:
    print("they have equal products")

topSellingValue = 0
for value in nestleSales:
    if int(nestleSales[value]) > int(topSellingValue):
        topSellingValue = nestleSales[value]
        topSellingProduct = value
    else:
        continue
print(f"The top selling products in Nestle is: {topSellingProduct}")

topSellingValue = 0
for value in unileverSales:
    if int(unileverSales[value]) > int(topSellingValue):
        topSellingValue = unileverSales[value]
        topSellingProduct = value
    else:
        continue
print(f"The top selling products in Unilever is: {topSellingProduct}")

allCities = unileversCountries.union(nestlesCountries)
print("All the cities that sell the products:")
for city in allCities:
    print(f"    {city}")

commonCities = nestlesCountries&unileversCountries
print("All the common cities that sell the products:")
for city in commonCities:
    print(f"    {city}")

differentCities = nestlesCountries - unileversCountries
print("All the cities that Nestle sells in , but Unilver doens't sell in:")
for city in differentCities:
    print(f"    {city}")


