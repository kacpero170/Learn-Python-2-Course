def is_even(x):
  if x % 2 == 0:
    return True
  else:
    return False
  

#NEXT

def is_int(x):
  absolute = abs(x)
  rounded = round(absolute)
  return absolute - rounded == 0

print (is_int(10))
print (is_int(10.5))


#NEXT

def digit_sum(n):
  x = abs(n)
  l = str(x)
  s = 0
  for i in l:
    s += int(i)
  return s


#NEXT

def factorial(x):
    total = 1
    while x>0:
        total *= x
        x-=1
    return total
  
print (factorial(4))


#NEXT


def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

print (is_prime(13))
print (is_prime(10))


#NEXT


def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word
  
print (reverse("Hello World"))


#NEXT


def anti_vowel(text):
    result = ""
    vowels = "ieaouIEAOU"
    for char in text:
          if char not in vowels:
            result += char
    return result
print (anti_vowel("hello book"))


#NEXT


score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word):
  word = word.lower()
  total = 0
  for letter in word:
    for leter in score:
      if letter == leter:
        total = total + score[leter]
  return total

print (scrabble_score("pizza"))


#NEXT


def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result
  
print (censor("this hack is wack hack", "hack"))


#NEXT


def count(sequence, item):
  how_many = 0
  c = 0
  while c in range(len(sequence)):
    if item == sequence[c]:
      how_many += 1
      c += 1
    else:
      c += 1
  return how_many

print(count([1, 2, 1, 1], 1))


#NEXT


def purify(numbers):
  even = []
  i = 0
  while i in range(len(numbers)):
    if numbers[i] % 2 == 0:
      even.append(numbers[i])
      i += 1
    else:
      i += 1
  return even
print(purify([1,2,3]))


#NEXT


def product(ints):
  total = 1
  i = 0
  while i <= (len(ints) - 1):
    total *= ints[i]
    i += 1
  return total
print(product([4, 5, 5]))


#NEXT


def remove_duplicates(inputlist):
    if inputlist == []:
        return []
    
    # Sort the input list from low to high    
    inputlist = sorted(inputlist)
    # Initialize the output list, and give it the first value of the now-sorted input list
    outputlist = [inputlist[0]]

    # Go through the values of the sorted list and append to the output list
    # ...any values that are greater than the last value of the output list
    for i in inputlist:
        if i > outputlist[-1]:
            outputlist.append(i)
        
    return outputlist
  
print (remove_duplicates([1, 1, 2, 2]))


#NEXT


def median(lst):
    sorted_list = sorted(lst)
    if len(sorted_list) % 2 != 0:
        #odd number of elements
        index = len(sorted_list)//2 
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        #even no. of elements
        index_1 = len(sorted_list)/2 - 1
        index_2 = len(sorted_list)/2
        mean = (sorted_list[index_1] + sorted_list[index_2])/2.0
        return mean
   
print (median([2, 4, 5, 9]))