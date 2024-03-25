response = "Y"
answer = "Left"
if answer == "Left":
    print ("This is the Verbal Abuse Room, you heap of parrot droppings!")

# No co tam studencie
def using_control_once():
    if True:
        return "Success #1"

def using_control_again():
    if True:
        return "Success #2"

print (using_control_once())
print (using_control_again())

# Skandalej
answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:             
        return False        # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:             
        return False       # Make sure this returns Falseprint
print(black_knight())
print(french_soldier())

#COOODE
def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print (greater_less_equal_5(4))
print (greater_less_equal_5(5))
print (greater_less_equal_5(6))
