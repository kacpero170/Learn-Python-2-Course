my_list = [i ** 2 for i in range(1, 11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
  f.write(str(item) + "\n")

f.close()

#NEXT

my_file = open("output.txt", "r+")

#NEXT

my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")

# Add your code below!
for item in my_list:
  my_file.write(str(item) + "\n")
my_file.close()

#NEXT

my_file = open("output.txt", "r")
print(my_file.read())
my_file.close()

#NEXT

my_file = open("text.txt", "r")
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
my_file.close()

#NEXT

# Use a file handler to open a file for writing
write_file = open("text.txt", "w")

# Open the file for reading
read_file = open("text.txt", "r")

# Write to the file
write_file.write("Not closing files is VERY BAD.")
write_file.close()

# Try to read from the file
print(read_file.read())
read_file.close()

#NEXT

with open("text.txt", "w") as textfile:
  textfile.write("Success!")

#NEXT

with open("text.txt", "w") as my_file:
  my_file.write("Koniec.")

#NEXT

with open("text.txt", "w") as my_file:
  my_file.write("Koniec.")
  if my_file.closed == False:
    my_file.close()
  print(my_file.closed)