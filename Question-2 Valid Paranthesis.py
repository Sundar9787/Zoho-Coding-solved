# Write a program that will take a string as input. The program will then determine whether each left parenthesis ‘(’ has a matching 
#right parenthesis ‘)’ and also all the ‘)’ has a  consecutive ‘(‘. If so, the program will print 0 else the program will print 1.
input_val = input('Enter string: ')
def valid_paranthesis(input_val):
    stack=[]
    for char in input_val:
        if char =='(':
            stack.append(char)
        elif char == ')':
            if not stack :
                return 1 
            stack.pop()
            
    if not stack:
        return 0 
    return 1
    
print(valid_paranthesis(input_val))
