my_list = [1,9,3,8,5,7]

for number in my_list:
  print(number * 2)

#NEXT

start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for number in start_list:
  square_list.append(number ** 2)
square_list.sort()

print (square_list)

#NEXT

# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print (residents['Puffin']) # Prints Puffin's room number

# Your code here!
print (residents['Sloth'])
print (residents['Burmese Python'])

#NEXT

menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print (menu['Chicken Alfredo'])

# Your code here: Add some dish-price pairs to menu!
menu['Chicken Ronaldo'] = 14.51
menu['Chicken Pele'] = 14.52
menu['Chicken Ozil'] = 14.53

print ("There are " + str(len(menu)) + " items on the menu.")
print (menu)

#NEXT

# key - animal_name : value - location 
zoo_animals = {
  'Unicorn' : 'Cotton Candy House',
  'Sloth' : 'Rainforest Exhibit',
  'Bengal Tiger' : 'Jungle House',
  'Atlantic Puffin' : 'Arctic Exhibit',
  'Rockhopper Penguin' : 'Arctic Exhibit'
}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin'] = 'Arctic Exhibit 2'

print (zoo_animals)

#NEXT

backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove('dagger')
print(backpack)