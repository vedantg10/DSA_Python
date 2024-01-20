# Dictionary Comprehension

# new_dict = {new_key:new_value for item in list}

import random
city_names = ['Paris', 'London', 'Rome', 'Berlin', 'Madrid']

new_dict = {city:random.randint(20,30) for city in city_names}

print(new_dict)

city_temps = { city: temp for (city,temp) in new_dict.items() if temp>20}
print(city_temps)