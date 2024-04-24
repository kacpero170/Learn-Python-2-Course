count = 0

if count < 5:
  print ("Hello, I am an if statement and count is", count)

while count in range(10):
  print ("Hello, I am a while and count is", count)
  count += 1

#NEXT

num = 1

while num <= 10:
  print(num ** 2)
  num += 1

#NEXT

choice = input('Enjoying the course? (y/n): ')

while choice != 'y' and choice != 'n':  # Fill in the condition (before the colon)
  choice = input("Sorry, I didn't catch that. Enter again: ")