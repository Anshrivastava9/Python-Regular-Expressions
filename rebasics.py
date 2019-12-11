#Regular Expressions basics
import re
#method 1{1 time regex compile takes place}
#Defines the pattern for our regex
pattern=re.compile(r'\d{3} \d{3}-\d{4}')

#search for regex in given string
res=pattern.search('call me at 415 555-4242!')

print(res)#prints the object 
print(res.group())#specific first match is get printed

#Method 2
print(re.search(r'\d{3} \d{3}-\d{4}',"call me at 415 555-4242!"))
print(re.search(r'\d{3} \d{3}-\d{4}',"call me at 415 555-4242!").group())


#--------------------------------------------------------------------------------------------------

print(re.search(r'\d{3} \d{3}-\d{4}',"call me at 415 555-4242 or 123 789-1234").group())
print(re.findall(r'\d{3} \d{3}-\d{4}',"call me at 415 555-4242 or 123 789-1234"))


