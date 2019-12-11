import re
#using functions for valid phone no and email
def is_valid_phone(input):#in a given string it print
    pattern=re.compile(r'\d{3} \d{3}-\d{4}')
    return pattern.search(input).group()

print(is_valid_phone("call me on 454 235-4561"))    


#---------------------------------------------------------------------

def is_valid(input):
    pattern=re.compile(r'^\d{3} \d{3}-\d{4}$')#---(^)means the input starts from here ---($)means it ends with this!!
    if pattern.search(input):
        return True
    else:
        return False    

print(is_valid("123 456-78947"))
print(is_valid("455 455-1234"))


#-------------------------------------------------------------------------------

def is_valid_email(input):
    pattern=re.compile(r'^([A-Za-z0-9\.]+)@([a-zA-Z]+)\.\w{2,5}$')
    if pattern.search(input):
        return True
    else:
        return None 


print(is_valid_email("1421najjsn@gmail.com145"))
print(is_valid_email("ansh.kvds0911@gmail.com"))







