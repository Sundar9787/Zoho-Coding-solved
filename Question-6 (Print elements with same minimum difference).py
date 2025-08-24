'''Write a program that takes an integer M and M integer array elements as input. The program needs to find the minimum
difference between two elements in the integer array. The program then needs to print all those pairs of elements that have
the minimum difference. If more than one pair has the minimum difference, then the program should print the output in the ascending
order, if an element exists in two or more pairs, then it should be printed two times or more.'''

M = int(input('Enter no of elements: '))
M_elements= list(map(int,input('Enter the elements: ').split()))
M_elements.sort()
minimum_difference=100000
for i in range(len(M_elements)-1):
    difference = M_elements[i+1]- M_elements[i]
    if difference < minimum_difference:
        minimum_difference = difference
 
ans=[]       
for i in range(len(M_elements)-1):
    if M_elements[i+1] - M_elements[i] == minimum_difference:
        ans.append(M_elements[i])
        ans.append(M_elements[i+1])
        
print('Final output: ',*ans)
        
