# LOOPS OR ARRAY
#            0         1       2       3
cities = ['Skidel','Grodno','minsk','Toronto']  # NEW LOOPS Skidel - 0 Grodno -1.....
print(cities)
print(len(cities))    # Quantity in loops
print(cities[2].title())  # Minsk)

cities[2] = 'Mosty'  # word replacement 2 - minsk ['Skidel', 'Grodno', 'Mosty', 'Toronto']
print(cities)

cities.append('Slonim') # ADD in end ['Skidel', 'Grodno', 'Mosty', 'Toronto']
print(cities)
cities.insert (3, 'Brest')  # Insert instead  before 3-toronto
print(cities)
del cities[-1]              # Delete from end first if -2 delete from second
print(cities)
cities.remove ('Mosty')      # Delete Mosty
cities.sort()                # Sort by alphabat
print(cities)