my_dict = {
  'Name': 'Zbyszek',
  'Codename': 'Flapjack',
  'Grupa': '3C'
}
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

#NEXT

my_dict = {
  'Name': 'Zbyszek',
  'Codename': 'Flapjack',
  'Grupa': '3C'
}
print(my_dict.keys())
print(my_dict.values())

for key in my_dict:
  print(key, my_dict[key])

#NEXT

evens_to_50 = [i for i in range(51) if i % 2 == 0]
print(evens_to_50)

#NEXT

doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares = [x ** 2 for x in range(1, 12) if x % 2 ==0]
print(even_squares)

#NEXT

cubes_by_four = [x ** 3 for x in range(1, 11) if (x ** 3) % 4 == 0]
print(cubes_by_four)

#NEXT

l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print (l)
print (l[2:9:2])

#NEXT

my_list = range(1, 11) # List of numbers 1 - 10

# Add your code below!
print(my_list[::2])

#NEXT

my_list = range(1, 11)

# Add your code below!
backwards = my_list[::-1]
print(backwards)

#NEXT

to_one_hundred = range(101)
# Add your code below!
backwards_by_tens = to_one_hundred[::-10]
print(backwards_by_tens)

#NEXT

to_21 = range(1,22)
odds = to_21[::2]
middle_third = to_21[7:14:1]
print(to_21)
print(odds)
print(middle_third)

#NEXT

my_list = range(16)
print (filter(lambda x: x % 3 == 0, my_list))

#NEXT

languages = ["HTML", "JavaScript", "Python", "Ruby"]
# Add arguments to the filter()
print (filter(lambda x: x == "Python", languages))

#NEXT

squares = [x ** 2 for x in range(1, 11)]
print (filter(lambda x: x >= 30 and x <= 70, squares))

#NEXT

movies = {
  "Monty Python and the Holy Grail": "Great",
  "Monty Python's Life of Brian": "Good",
  "Monty Python's Meaning of Life": "Okay"
}

print(movies.items())

#NEXT

threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]

#NEXT

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
op1 = garbled[::-1]
op2 = op1[::2]
message = op2
print(message)

#NEXT

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x != "X", garbled)
print(message)