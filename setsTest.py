
#to create an empty set
empty_set = set()

#to create a set with initial values
fruit_set = {"Orange", "Apple"}
print(fruit_set)

#to add a new member
fruit_set.add("Plum")

print(fruit_set)


#to remove a member | if does not exsist gives error
fruit_set.remove("Orange")
print(fruit_set)

#to remove a member of a set using discard | does not give error
fruit_set.discard("Banana")
print(fruit_set)

is_apple_a_member = "Apple" in fruit_set
print(is_apple_a_member)

#to loop through a set
for fruit in fruit_set:
    print(fruit)


#Set operations


faiz_visited_cities : set = {"London", "Paris", "Abha"}
ahmed_visited_cities : set = {"Paris", "Dubai", "Mekkah", "Meddina"}


#Union
visited_cities_union = faiz_visited_cities.union(ahmed_visited_cities)

print(visited_cities_union)
#using the Union operator
print(faiz_visited_cities | ahmed_visited_cities)


#Intersection
visited_cities_intersection = faiz_visited_cities.intersection(ahmed_visited_cities)
print("visited cities by both Ahmed & Faiz: ", visited_cities_intersection)
#using the intersection operator
print(faiz_visited_cities & ahmed_visited_cities)


#Difference
faiz_recommended_cities = ahmed_visited_cities.difference(faiz_visited_cities)
print("Recommended to visit next for Faize :", faiz_recommended_cities)

#using the difference operator
print("Recommeded fro Ahmed",  faiz_visited_cities - ahmed_visited_cities)


#Symmetric difference
visited_cities_symmetric_difference = faiz_visited_cities.symmetric_difference(ahmed_visited_cities)

print(visited_cities_symmetric_difference)
#using the symmetric difference operator
print(faiz_visited_cities ^ ahmed_visited_cities)