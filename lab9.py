
'''
kata_product_nestle={"34,456,432" : "KitKat" ,"14,106,132" : "Nescafe" , "9,960,312": "Maggi" ,
 "44,506,003": "Nido"}
dalia_products_unilever={"23,456,000" : "Lipton" ,"1,235,891": "Breyers" , "17,241,412" : "HellManns", "11,715,324": "Marmite"}
'''

kata_product_nestle={"KitKat" : "34,456,432" ,"Nescafe" : "14,106,132" ,"Maggi": "9,960,312" ,"Nido" :"44,506,003" }

dalia_products_unilever={"Lipton" : "23,456,000" ,"Breyers":"1,235,891"  ,"HellManns": "17,241,412", "Marmite":"11,715,324" }
for index,value in dalia_products_unilever.items():
 print(index,value)
print(" \n")
for index,value in kata_product_nestle.items():
 print(index,value)

print(" \n")

max_value_nestle=max(kata_product_nestle.values())
max_value_unilever=max(dalia_products_unilever.values())
if max_value_nestle > max_value_unilever:
 print("the largest number is: ",max_value_nestle)
else:
 print("the largest number is: ",max_value_unilever)

print("the top selling product from Nestle is: ",max_value_nestle)
print("the top selling product from Unilever is: ",max_value_unilever)
print("\n")

monica_nestle:set={"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
monica_unilever:set={"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

print(monica_nestle|monica_unilever)
print(monica_nestle&monica_unilever)
print(monica_nestle-monica_unilever)