webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}

# Add your code below!
for definition in webster:
  print(webster[definition])

#NEXT

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for number in a:
  if number % 2 == 0:
    print (number)

#NEXT

# Write your function below!
def fizz_count(x):
  count = 0
  for item in x:
    if item == "fizz":
      count += 1
  return count

#NEXT

for letter in "Codecademy":
  print (letter)
    
# Empty lines to make the output pretty
print
print

word = "Programming is fun!"

for letter in word:
  # Only print out the letter i
  if letter == "i":
    print (letter)