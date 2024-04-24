import random

print ("Lucky Numbers! 3 numbers will be generated.")
print ("If one of them is a '5', you lose!")

count = 0
while count < 3:
  num = random.randint(1, 6)
  print (num)
  if num == 5:
    print ("Sorry, you lose!")
    break
  count += 1
else:
  print ("You win!")

#NEXT

from random import randint
guesses_left = 3
while guesses_left > 0:
  random_number = randint(1, 10)
  guess = input("Your number: ")
  if random_number == guess:
    print("You win!")
    break
  guesses_left -= 1
else:
  print("You lose.")

#NEXT

print("Counting...")

for i in range(20):
  print (i)

#NEXT

hobbies = []

# Add your code below!
for i in range(3):
  hobby = input("Hobby: ")
  hobbies.append(hobby)
print (hobbies)

#NEXT

thing = "spam!"

for c in thing:
  print (c)

word = "eggs!"

# Your code here!
for letter in word:
  print (letter)

#NEXT

phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
  if char == "A" or char == "a":
    print ("X"),
  else:
    print (char),





#Don't delete this print statement!
print

#NEXT

numbers  = [7, 9, 12, 54, 99]

print ("This list contains: ")

for num in numbers:
  print (num)

# Add your loop below!
for number in numbers:
  print (number ** 2)


#NEXT

