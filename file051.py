one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six = 0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100

#NEXT

print (bin(1))
print (bin(2))
print (bin(3))
print (bin(4))
print (bin(5))

#NEXT

print (int("1",2))
print (int("10",2))
print (int("111",2))
print (int("0b100",2))
print (int(bin(5),2))
# Print out the decimal equivalent of the binary 11001001.
print (int("0b11001001", 2))

#NEXT

shift_right = 0b1100
shift_left = 0b1

# Your code here!
shift_right = shift_right >> 2
shift_left = shift_left << 2

print (bin(shift_right))
print (bin(shift_left))

#NEXT

# AND Operator
print(bin(0b1110 & 0b101)) 

#NEXT

# OR Operator
print(bin(0b1110 | 0b101))

#NEXT

# XOR Operator
print(bin(0b1110 ^ 0b101))

#NEXT

# NOT Operator
print (~1)
print (~2)
print (~3)
print (~42)
print (~123)

#NEXT

def check_bit4(input):
  mask = 0b1000
  desired = input & mask
  if desired > 0:
    return "on"
  else:
    return "off"

#NEXT

a = 0b10111011
mask = 0b100
total = a | mask
print(bin(total))

#NEXT

# Do a flip!
a = 0b11101110
mask = 0b11111111
total = a ^ mask
print(bin(total))

#NEXT

def flip_bit(number, n):
  bit_to_flip = 0b1 << (n -1)
  result = number ^ bit_to_flip
  return bin(result)