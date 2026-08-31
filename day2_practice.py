cities = ["New York", "Trenton", "Newark", "Newark", "Trenton"]
city_counts = {}
for city in cities: 
    if city in city_counts:
        city_counts[city] = city_counts[city]+1
    else:
        city_counts[city] = 1
print(city_counts)


#---------------
cities = ["New York", "Trenton", "Newark", "Newark", "Trenton"]
city_counts = {}
for city in cities: 
    if city in city_counts:
        city_counts[city] = city_counts[city]+1
    else:
        city_counts[city] = 1
best_city = None
best_count = 0
for city, count in city_counts.items():
    if count > best_count:
        best_city = city
        best_count = count
print(best_city, best_count)
