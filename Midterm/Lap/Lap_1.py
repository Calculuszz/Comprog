def no_lowercase(t): # return True if no lowercase, otherwise return False 
    char = 'abcdefghijklmnopqrstuvwsyxz'
    for i in t:
        if i in char:
            return False
    return True
 
def no_uppercase(t): 
    CHAR = 'ABCDEFGHIJKLMNOPQRSTUVWSYXZ'
    for i in t :
        if i in CHAR:
            return False
    return True 
 
def no_number(t): 
    num = '0123456789'
    for i in t:
        if i in num:
            return False
    return True
 
def no_symbol(t): 
    symbol = '!@#$%^&*()_+-*/'
    for i in t:
        if i in symbol:
            return False
    return True
 
def character_repetition(t): 
    x = []
    for i in range(0, len(t), 4):
        for j in t[i:i+4]:
            if j in x:
                return True
        x = []
    return False
 
def number_sequence(t): 
    num1 = '0123456789'
    num2 = '9876543210'
    for i in range(0, len(t), 4):
        if t[i:i+4] in num1 and t[i:i+4] in num2:
            return False
    return True
 

def letter_sequence(t): 
    char_re = 'qwertyuiopasdfghjklzxcvbnm'
    for i in range(0, len(t), 4):
        if t[i:i+4] in char_re:
            return True
    return False 
 
def keyboard_pattern(t): 
    t = t.lower()
    p1 = '!@#$%^&*()_+qwertyuiopasdfghjklzxc'
    p2 = 'mnbvcxzlkjhgfdsapoiuytrewq+_)(*&^%$#@!'
    for i in range(0, len(t), 4):
        if t[i:i+4] in p1 and t[i:i+4] in p2:
            return False
    return True
 
#----------------------------- 
passw = input().strip() 
errors = [] 
if len(passw) < 8: 
    errors.append("Less than 8 characters") 
 
if no_lowercase(passw): 
    errors.append("No lowercase letters") 
 
if no_uppercase(passw): 
    errors.append("No uppercase letters")

if no_number(passw): 
    errors.append("No numbers")

if no_symbol(passw): 
    errors.append("No symbols")

if character_repetition(passw): 
    errors.append("Character repetition")

if number_sequence(passw): 
    errors.append("Number sequences")

if letter_sequence(passw): 
    errors.append("Letter sequence")

if keyboard_pattern(passw): 
    errors.append("Keyboard pattern")

if len(errors) == 0: 
    print('OK')
else: 
    for i in errors:
        print(i)