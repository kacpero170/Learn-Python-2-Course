n = [3, 5, 7]

def print_list(x):
  for i in range(0, len(x)):
    print (x[i])
    
print_list(n)

#NEXT

n = [3, 5, 7]

def double_list(x):
  for i in range(0, len(x)):
    x[i] = x[i] * 2
  return x
# Don't forget to return your new list!

print (double_list(n))

#NEXT

def my_function(x):
  for i in range(0, len(x)):
    x[i] = x[i]
  return x

print (my_function(range(3))) # Add your range between the parentheses!

#NEXT

n = [3, 5, 7]

def total(numbers):
  result = 0
  for i in range(len(numbers)):
    result += numbers[i]
  return result

#NEXT

n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
  result = ""
  for i in range(0, len(words)):
    result += words[i]
  return result

print (join_strings(n))

#NEXT

m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!
def join_lists(x, y):
  return x + y

print (join_lists(m, n))
# You want this to print [1, 2, 3, 4, 5, 6]