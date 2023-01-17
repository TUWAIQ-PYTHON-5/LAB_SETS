
#1
nestleDict = {'KitKat':34456432,
              'Nescafe':14106132,
              'Maggi':9960312,
              'Nido':44506003}

#2
unileverDict = {'Lipton':23456000,
                'Breyers':1235891,
                'HallManns':17241412,
                'Marmite':11715324} 

#3
print()
print("Unilever sales Sheet:")
for uniLproduct, uniSales in unileverDict.items():
    print("The Producte [",uniLproduct,"  \t] Soled [",uniSales,"\t]")


#4
print()
print("Nestle sales Sheet:")
for nestleLproduct, nestleLSales in nestleDict.items():
    print("The Producte [",nestleLproduct,"    \t] Soled [",nestleLSales,"\t]")


#5
print()
uniTotal:int=0
nestleTotal:int=0
for uniLproduct, uniSales in unileverDict.items():
    uniTotal += uniSales
for nestleLproduct, nestleLSales in nestleDict.items():
    nestleTotal += nestleLSales

if (nestleTotal > uniTotal) : print("Nestle Sales are higher")
elif(uniTotal > nestleTotal): print("Unilever Sales are higher")
else: print("Bothe companies sales is equal")

#6
print()
nestleHighst:int=0
for nestleLproduct, nestleLSales in nestleDict.items():
    #print(nestleLSales)
    if (nestleHighst < nestleLSales): 
        nestleHighst = nestleLSales
#print(nestleHighst)
bestNesPro:str=""
for nestleLproduct, nestleLSales in nestleDict.items():
    if (nestleHighst == nestleLSales): bestNesPro = nestleLproduct

print("The highest sales in Nestle [", bestNesPro, "] with the sale of [",nestleHighst,"]")


#7
print()
uniHighst:int=0
for uniLproduct, uniLSales in unileverDict.items():
    #print(nestleLSales)
    if (uniHighst < uniLSales): 
        uniHighst = uniLSales
#print(nestleHighst)
bestUniPro:str=""
for uniLproduct, uniLSales in unileverDict.items():
    if (uniHighst == uniLSales): bestUniPro = uniLproduct

print("The highest sales in Nestle [", bestUniPro, "] with the sale of [",uniHighst,"]")


#8
print()
nestleSet = {"Saudi Arabia", 
             "Oman", "Kuwait", 
             "Egypt", "Jordan", 
             "Sudan"}

unileverSet = {"Saudi Arabia", 
               "Kuwait", "Iraq", 
               "Morocco", "Yemen", 
               "United Emirates"}
'''
largSet:int=0
tempSet: set = set()
tempTxt:str=""
if (len(nestleSet) > len(unileverSet)): largSet = len(nestleSet)
else: largSet = len(unileverSet)
for city in nestleSet, unileverSet:
    tempTxt = city
    #print(city)
    if (not city == tempSet): 
        tempSet.add(tempTxt)

'''
unionNesUni= (unileverSet | nestleSet)
#print(unionNesUni)
counter:int=1
print("Union:")
for value in unionNesUni:
    print(counter, "- ", value) 
    counter+=1
#print("Total Sales Countries: ", nestleSet | unileverSet)
#print("Total Sales Countries: ",tempSet)


#9
print()
interNesUni= (nestleSet - unileverSet)
#print(unionNesUni)
counter:int=1
print("Subtract:")
for value in interNesUni:
    print(counter, "- ", value) 
    counter+=1
#print("Total Sales Countries: ", nestleSet | unileverSet)
#print("Total Sales Countries: ",tempSet)
