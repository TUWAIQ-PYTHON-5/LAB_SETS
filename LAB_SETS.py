
Nestle_product={"KitKat":34_456_43,"Nescafe":14_106_132,"Maggi":9_960_312,"Nido":44_506_003}
# Create a variable to hold the values of Nestle products (use a dicitionary)

Unilever_product={"Lipton ": "23,456,000","Breyers" :" 1,235,891", "HellManns" : "17,241,412"  ,"Marmite":"11,715,324" }
#  Create a variable to hold the values of Unilever products (Use a dictionary)


 # Print each product sold by Unilever and the sales figures / numbers  for that product.
  # Print the top selling product from Unilever with sales figures.

for key, value in Unilever_product.items():
    print(f"{key}:{value} US Dollars") 
    my_val2=Unilever_product.values()
    y:int=max(my_val2)
print( "Max value of Unilever:",y)

# Print each product sold by Nestle and the sales figures / numbers  for that product.
# Print the top selling product from Nestle with sales figures.
for key, value in Nestle_product.items():
    print(f"{key}:{value}")
    my_val=Nestle_product.values()
    x=max(my_val)
print(" Max value of Nestle",x)
#  Print which of the companies has more products that the other company
if len(Nestle_product)>len(Unilever_product):
    print("Nestle has more products")
elif len(Nestle_product)<len(Unilever_product):
    print("Unilever has more products")
else:
    print("both Nestle and unilever has the same products")
Nestle:set={"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever:set={"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
# Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
for element in Nestle:
    all= Unilever.union(Nestle)
print(all)
# Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
for z in Unilever:
    all2= Unilever.intersection(Nestle)
print(all2)
# Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
all3 = Nestle- Unilever
print(all3)