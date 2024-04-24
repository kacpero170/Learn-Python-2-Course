d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
  # Your code here!
  print (key, d[key])


#NEXT


choices = ['pizza', 'pasta', 'salad', 'nachos']

print ('Your choices are:')
for index, item in enumerate(choices):
  print (index + 1, item)


#NEXT


list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
  # Add your code here!
  if a > b:
    print (a)
  else:
    print (b)


#NEXT

fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print ('You have...')
for f in fruits:
  if f == 'tomato':
    print ('A tomato is not a fruit!') # (It actually is.)
    break
  print ('A', f)
else:
  print ('A fine selection of fruits!')


#NEXT


fruits = ['banana', 'apple', 'orange', 'pear', 'pear', 'grape']

print ('You have...')
for f in fruits:
  if f == 'tomato':
    print ('A tomato is not a fruit!') # (It actually is.)
    break
  print ('A', f)
else:
  print ('A fine selection of fruits!')


#NEXT


numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
  if number <= 3:
    print (number ** 2)
  else:
    print (number * 2)