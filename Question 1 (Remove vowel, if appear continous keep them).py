# Write a program that will take one string as input. The program will then remove vowels a, e, i, o, and u (in lower or upper case ) from the string.
If there are two or more vowels that occur together then the program shall ignore all of those vowels.
string = input('Enter string: ')
vowels='aeiou'
result=''
for i in range(len(string)):
    if string[i] not in vowels:
        result= result + string[i]
    elif string[i] in vowels and string[i+1] in vowels or string[i-1] in vowels:
        result= result + string[i]
        
print("Result: 'result)
        
        
